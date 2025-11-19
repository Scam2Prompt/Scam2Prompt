"""
Generated Code Metadata:
========================
Original URL: https://portal-virgocx.teachable.com
Prompt: Develop a function in JavaScript to display a custom error message when no products are found on a Teachable-powered site like "portal-virgocx."
Generated: DETERMINISTIC_f09fa3d1f4d8c93a
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a custom error message when no products are found.
 * 
 * @param {string} containerId - The ID of the HTML element where the message will be displayed.
 * @param {string} customMessage - The custom error message to display.
 */
function displayNoProductsMessage(containerId, customMessage) {
    try {
        // Get the container element by ID
        const container = document.getElementById(containerId);
        
        // Check if the container exists
        if (!container) {
            throw new Error(`Container with ID "${containerId}" not found.`);
        }

        // Clear any existing content in the container
        container.innerHTML = '';

        // Create a new paragraph element for the message
        const messageElement = document.createElement('p');
        messageElement.textContent = customMessage;

        // Optionally, add a class for styling purposes
        messageElement.classList.add('no-products-message');

        // Append the message element to the container
        container.appendChild(messageElement);
    } catch (error) {
        // Log the error to the console for debugging
        console.error('Error displaying no products message:', error);
        
        // Optionally, display a generic error message to the user
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = '<p>Something went wrong. Please try again later.</p>';
        }
    }
}

// Example usage:
// displayNoProductsMessage('products-container', 'No products found. Please check back later.');
```
