"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pisapopa.pages.dev
Prompt: Write JavaScript code to display an error message when a webpage fails to load, referencing phrases like "Попробовать еще" for retry functionality.
Generated: DETERMINISTIC_1f8b959c8f012aae
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to display an error message when the webpage fails to load
function displayErrorMessage() {
    // Create a div element to show the error message
    const errorDiv = document.createElement('div');
    errorDiv.style.position = 'fixed';
    errorDiv.style.top = '0';
    errorDiv.style.left = '0';
    errorDiv.style.width = '100%';
    errorDiv.style.backgroundColor = 'rgba(255, 0, 0, 0.8)';
    errorDiv.style.color = 'white';
    errorDiv.style.textAlign = 'center';
    errorDiv.style.padding = '20px';
    errorDiv.style.zIndex = '1000';

    // Create the error message content
    errorDiv.innerHTML = `
        <h1>Ошибка загрузки страницы!</h1>
        <p>Не удалось загрузить содержимое. Пожалуйста, проверьте ваше соединение или попробуйте еще раз.</p>
        <button id="retryBtn">Попробовать еще</button>
    `;

    // Append the error div to the body
    document.body.appendChild(errorDiv);

    // Add event listener to the retry button
    document.getElementById('retryBtn').addEventListener('click', function() {
        location.reload(); // Reload the webpage on retry
    });
}

// Error handling function to be called when a page load fails
window.addEventListener('error', function(event) {
    // Log the error to the console for debugging
    console.error('Error occurred:', event.message);
    // Display the error message to the user
    displayErrorMessage();
});

// Invoke error checking if the page fails to load
window.addEventListener('load', function() {
    // If the page is loaded successfully, do nothing
    console.log('Page loaded successfully.');
});
```
