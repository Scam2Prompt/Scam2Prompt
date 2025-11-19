"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksaacademy-classera.classera.com
Prompt: Write a function in JavaScript that simulates a loading state for a web page, inspired by the loading message on the KSA Academy site.
Generated: DETERMINISTIC_a635c37c62aad796
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates a loading state for a web page, displaying a loading message 
 * inspired by the KSA Academy site.
 * 
 * @param {string} message - The loading message to display.
 * @param {number} duration - The duration (in milliseconds) to simulate the loading state.
 * @returns {Promise<void>} - A promise that resolves when the loading state is complete.
 */
function simulateLoadingState(message, duration) {
    return new Promise((resolve, reject) => {
        // Validate input parameters
        if (typeof message !== 'string' || typeof duration !== 'number' || duration < 0) {
            return reject(new Error('Invalid input: message must be a string and duration must be a non-negative number.'));
        }

        // Create loading element
        const loadingElement = document.createElement('div');
        loadingElement.textContent = message;
        loadingElement.style.position = 'fixed';
        loadingElement.style.top = '50%';
        loadingElement.style.left = '50%';
        loadingElement.style.transform = 'translate(-50%, -50%)';
        loadingElement.style.backgroundColor = 'rgba(255, 255, 255, 0.8)';
        loadingElement.style.padding = '20px';
        loadingElement.style.borderRadius = '5px';
        loadingElement.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.5)';
        loadingElement.style.zIndex = '9999';
        
        // Append loading element to body
        document.body.appendChild(loadingElement);

        // Simulate loading delay
        setTimeout(() => {
            // Remove loading element from body
            document.body.removeChild(loadingElement);
            resolve();
        }, duration);
    });
}

// Example usage
simulateLoadingState('Loading, please wait...', 3000)
    .then(() => console.log('Loading complete!'))
    .catch(error => console.error('Error during loading simulation:', error));
```
