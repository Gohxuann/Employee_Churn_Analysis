
# Employee Churn Prediction

This project predicts whether an employee will stay or leave an organization based on various factors, such as satisfaction level, last evaluation, number of projects, and more. The prediction is powered by a machine learning model deployed with Flask, offering a user-friendly web-based interface.

---

## Features
- **Interactive Input Form**: Users can input employee details via a clean and responsive form.
- **Machine Learning Prediction**: Uses a pre-trained model to predict employee churn.
- **Dynamic Result Display**: Prediction results are displayed below the form dynamically without page reloads.
- **Responsive Design**: Built using HTML, CSS, and Bootstrap for mobile and desktop compatibility.

---

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, NumPy
- **Model Serialization**: Joblib

---

## Getting Started

### Prerequisites
Ensure you have Python 3.8+ installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd employee-churn-prediction
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Access the application in your browser at:
   ```
   http://127.0.0.1:5000
   ```

---

## Project Structure
```
employee-churn-prediction/
├── app.py              # Flask backend for handling predictions
├── templates/
│   └── index.html      # Frontend HTML file
├── static/
│   ├── styles.css      # Styling for the frontend
│   └── script.js       # JavaScript for frontend behavior
├── best_mlp_model.pkl  # Pre-trained machine learning model
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## How It Works
1. **Input Data**: 
   - Users input values such as satisfaction level, last evaluation score, number of projects, daily hours, and other employee features in a form.
2. **Backend Processing**:
   - The input data is sent to the Flask backend, which uses a pre-trained machine learning model (`best_mlp_model.pkl`) to predict whether the employee will "Stay" or "Leave".
3. **Dynamic Result**:
   - The result is displayed below the "Predict" button dynamically without reloading the page.

---

## Example Input
| Feature                   | Description                      | Example Value |
|---------------------------|----------------------------------|---------------|
| Satisfaction Level         | Employee satisfaction (0-1)      | `0.7`         |
| Last Evaluation            | Last evaluation score (0-1)      | `0.8`         |
| Number of Projects         | Total projects handled           | `5`           |
| Daily Hours                | Average daily hours worked       | `7`           |
| Time Spent at Company      | Years in the company             | `3`           |
| Work Accident              | Had a workplace accident (0 or 1)| `0`           |
| Promotion in Last 5 Years  | Promoted in last 5 years (0 or 1)| `1`           |
| Departments                | Department ID (1-10)             | `3`           |
| Salary                     | Salary level (1-Low, 2-Med, 3-High) | `2`        |

---

## To-Do
- Add model explanation (e.g., feature importance).
- Extend with more advanced machine learning models.
- Save predictions and user inputs in a database for analytics.
- Improve UI/UX for enhanced user interaction.

---

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.

---

## Author
- **Your Name**
- Feel free to connect on [GitHub](https://github.com/yourusername) or contribute to the project.
