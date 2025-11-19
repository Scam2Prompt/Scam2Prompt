"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qwaliconnect.com
Prompt: Write a JavaScript function to dynamically edit text content on a webpage, inspired by the editable features mentioned on Qwali Connect's site.
Generated: DETERMINISTIC_ec06c5e3eb5326f7
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A function to dynamically edit text content on a webpage.
 * Inspired by editable text features from Qwali Connect's site.
 * Allows users to click on text to edit, and saves changes when they click outside the element.
 */

/**
 * Initializes editable text functionality on specified elements.
 * @param {string} selector - CSS selector for elements to make editable.
 */
function makeTextEditable(selector) {
    // Find all elements matching the selector
    const elements = document.querySelectorAll(selector);

    if (!elements.length) {
        console.error("No elements found for the selector:", selector);
        return;
    }

    // Loop through each element and add event listeners for editing behavior
    elements.forEach((element) => {
        // Make the element content editable on click
        element.addEventListener('click', () => {
            element.setAttribute('contenteditable', 'true');
            element.focus();
        });

        // Save changes and remove editable attribute when clicking elsewhere
        element.addEventListener('blur', () => {
            element.removeAttribute('contenteditable');
        });

        // Handle the Enter key to save changes and exit edit mode
        element.addEventListener('keydown', (event) => {
            if (event.key === 'Enter') {
                event.preventDefault(); // Prevent default "Enter" behavior
                element.blur(); // Trigger the blur event to save changes
            }
        });
    });
}

// Example usage:
// Apply editable functionality to all elements with the class "editable"
document.addEventListener('DOMContentLoaded', () => {
    try {
        makeTextEditable('.editable');
    } catch (error) {
        console.error("Error initializing editable text:", error);
    }
});
```
