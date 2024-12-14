from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model
model = joblib.load('best_mlp_model.pkl')

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        data = request.form
        satisfaction_level = float(data['satisfaction_level'])
        last_evaluation = float(data['last_evaluation'])
        number_projects = int(data['number_projects'])
        daily_hours = int(data['daily_hours'])
        time_spend_company = int(data['time_spend_company'])
        Work_accident = int(data['Work_accident'])
        promotion_last_5years = int(data['promotion_last_5years'])
        Departments = int(data['Departments'])
        salary = int(data['salary'])

        # Prepare data for prediction
        input_data = np.array([[satisfaction_level, last_evaluation, number_projects,
                                daily_hours, time_spend_company,
                                Work_accident, promotion_last_5years, Departments, salary]])

        # Make prediction
        prediction = model.predict(input_data)
        result = "Leave" if prediction[0] == 1 else "Stay"

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
