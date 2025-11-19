"""
Generated Code Metadata:
========================
Original URL: https://catalysts.in
Prompt: Write a JavaScript function to dynamically update a message on a website that is under construction.
Generated: DETERMINISTIC_c4f846f51bda9afd
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Updates the construction message on a website with dynamic content.
 * @param {string} elementId - The ID of the HTML element to update.
 * @param {string} message - The message to display.
 * @param {number} [interval=3000] - Interval in milliseconds between updates (optional).
 * @param {string[]} [dynamicTexts=[]] - Array of texts to cycle through (optional).
 * @throws {Error} If the element is not found or parameters are invalid.
 */
function updateConstructionMessage(elementId, message, interval = 3000, dynamicTexts = []) {
    // Validate parameters
    if (!elementId || typeof elementId !== 'string') {
        throw new Error('Invalid elementId: must be a non-empty string');
    }
    if (!message || typeof message !== 'string') {
        throw new Error('Invalid message: must be a non-empty string');
    }
    if (interval && (typeof interval !== 'number' || interval <= 0)) {
        throw new Error('Invalid interval: must be a positive number');
    }
    if (dynamicTexts && (!Array.isArray(dynamicTexts) || dynamicTexts.some(t => typeof t !== 'string'))) {
        throw new Error('Invalid dynamicTexts: must be an array of strings');
    }

    // Get the target element
    const element = document.getElementById(elementId);
    if (!element) {
        throw new Error(`Element with ID '${elementId}' not found`);
    }

    // Set initial message
    element.textContent = message;

    // If dynamic texts are provided, cycle through them
    if (dynamicTexts.length > 0) {
        let currentIndex = 0;
        const baseMessage = message;

        const updateInterval = setInterval(() => {
            currentIndex = (currentIndex + 1) % dynamicTexts.length;
            element.textContent = `${baseMessage} ${dynamicTexts[currentIndex]}`;
        }, interval);

        // Return cleanup function to stop the interval when needed
        return () => clearInterval(updateInterval);
    }

    // Return empty cleanup function if no interval was set
    return () => {};
}

// Example usage:
// updateConstructionMessage(
//     'construction-message',
//     'Website under construction:',
//     2000,
//     ['Coming soon!', 'Stay tuned!', 'Work in progress!']
// );
```
