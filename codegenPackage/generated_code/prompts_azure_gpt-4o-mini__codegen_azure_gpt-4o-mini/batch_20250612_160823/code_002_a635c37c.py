"""
Generated Code Metadata:
========================
Original URL: https://ksaacademy-classera.classera.com
Prompt: Write a function in JavaScript that simulates a loading state for a web page, inspired by the loading message on the KSA Academy site.
Generated: DETERMINISTIC_a635c37c62aad796
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates a loading state for a web page.
 * Displays a loading message and a spinner until the loading is complete.
 * 
 * @param {number} duration - The duration in milliseconds for which the loading state should be displayed.
 * @returns {Promise<void>} - A promise that resolves when the loading is complete.
 */
function simulateLoadingState(duration) {
    // Validate the input duration
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Duration must be a positive number.');
    }

    // Create loading message element
    const loadingMessage = document.createElement('div');
    loadingMessage.textContent = 'Loading...';
    loadingMessage.style.position = 'fixed';
    loadingMessage.style.top = '50%';
    loadingMessage.style.left = '50%';
    loadingMessage.style.transform = 'translate(-50%, -50%)';
    loadingMessage.style.fontSize = '24px';
    loadingMessage.style.color = '#333';
    loadingMessage.style.zIndex = '1000';

    // Create spinner element
    const spinner = document.createElement('div');
    spinner.className = 'spinner';
    spinner.style.border = '8px solid #f3f3f3'; // Light grey
    spinner.style.borderTop = '8px solid #3498db'; // Blue
    spinner.style.borderRadius = '50%';
    spinner.style.width = '50px';
    spinner.style.height = '50px';
    spinner.style.animation = 'spin 1s linear infinite';
    loadingMessage.appendChild(spinner);

    // Append loading message to the body
    document.body.appendChild(loadingMessage);

    // Define CSS for spinner animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    `;
    document.head.appendChild(style);

    // Return a promise that resolves after the specified duration
    return new Promise((resolve) => {
        setTimeout(() => {
            // Remove loading message from the DOM
            document.body.removeChild(loadingMessage);
            resolve();
        }, duration);
    });
}

// Example usage
simulateLoadingState(3000) // Simulates loading for 3 seconds
    .then(() => {
        console.log('Loading complete!');
    })
    .catch((error) => {
        console.error('An error occurred:', error);
    });
```
