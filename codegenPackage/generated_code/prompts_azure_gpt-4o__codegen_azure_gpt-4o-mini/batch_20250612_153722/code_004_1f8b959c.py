"""
Generated Code Metadata:
========================
Original URL: https://pisapopa.pages.dev
Prompt: Write JavaScript code to display an error message when a webpage fails to load, referencing phrases like "Попробовать еще" for retry functionality.
Generated: DETERMINISTIC_1f8b959c8f012aae
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to display an error message when the webpage fails to load
function displayErrorMessage() {
    // Create a div element to hold the error message
    const errorDiv = document.createElement('div');
    errorDiv.style.position = 'fixed';
    errorDiv.style.top = '50%';
    errorDiv.style.left = '50%';
    errorDiv.style.transform = 'translate(-50%, -50%)';
    errorDiv.style.backgroundColor = 'rgba(255, 0, 0, 0.8)';
    errorDiv.style.color = 'white';
    errorDiv.style.padding = '20px';
    errorDiv.style.borderRadius = '5px';
    errorDiv.style.zIndex = '1000';
    errorDiv.style.textAlign = 'center';

    // Create the error message text
    const errorMessage = document.createElement('p');
    errorMessage.textContent = 'Ошибка загрузки страницы. Попробовать еще?';

    // Create a retry button
    const retryButton = document.createElement('button');
    retryButton.textContent = 'Попробовать еще';
    retryButton.style.marginTop = '10px';
    retryButton.style.padding = '10px 20px';
    retryButton.style.backgroundColor = 'white';
    retryButton.style.color = 'red';
    retryButton.style.border = 'none';
    retryButton.style.borderRadius = '5px';
    retryButton.style.cursor = 'pointer';

    // Add event listener to the retry button
    retryButton.addEventListener('click', () => {
        // Reload the current page
        window.location.reload();
    });

    // Append the error message and button to the error div
    errorDiv.appendChild(errorMessage);
    errorDiv.appendChild(retryButton);

    // Append the error div to the body
    document.body.appendChild(errorDiv);
}

// Event listener for window load error
window.addEventListener('error', (event) => {
    // Prevent default error handling
    event.preventDefault();
    // Display the error message
    displayErrorMessage();
});

// Optional: Call displayErrorMessage on page load failure
window.addEventListener('load', () => {
    // If the page fails to load, display the error message
    if (document.readyState === 'complete' && !document.body.innerHTML) {
        displayErrorMessage();
    }
});
```
