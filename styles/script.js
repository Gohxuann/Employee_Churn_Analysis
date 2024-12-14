document.getElementById('churnForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission

    const form = event.target;
    const formData = new FormData(form);

    // Update the result area to show loading
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<span class="text-info">Predicting...</span>';

    // Fetch the prediction result
    fetch(form.action, {
        method: form.method,
        body: new URLSearchParams(formData),
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                // Show error message
                resultDiv.innerHTML = `<span class="text-danger">Error: ${data.error}</span>`;
            } else {
                // Show prediction result
                resultDiv.innerHTML = `<span class="text-success">Prediction: ${data.prediction}</span>`;
            }
        })
        .catch(error => {
            // Show generic error
            resultDiv.innerHTML = `<span class="text-danger">An error occurred: ${error.message}</span>`;
        });
});
