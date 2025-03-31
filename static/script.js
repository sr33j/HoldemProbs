document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('pokerForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.textContent = `Error: ${data.error}`;
                resultDiv.style.color = 'red';
            } else {
                resultDiv.textContent = `Your probability of winning is ${data.probability * 100}%`;
                resultDiv.style.color = 'green';
            }
        })
        .catch(error => {
            resultDiv.textContent = `Error: ${error.message}`;
            resultDiv.style.color = 'red';
        });
    });
});