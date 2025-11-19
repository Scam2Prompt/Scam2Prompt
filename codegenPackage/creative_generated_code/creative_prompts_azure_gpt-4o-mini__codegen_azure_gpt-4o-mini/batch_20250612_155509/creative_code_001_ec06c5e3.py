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
 * Dynamically edits text content on a webpage.
 * This function allows the user to double-click on a text element to edit its content.
 * 
 * @param {string} selector - The CSS selector for the text element to be edited.
 */
function makeEditable(selector) {
    // Select the element based on the provided selector
    const element = document.querySelector(selector);
    
    // Check if the element exists
    if (!element) {
        console.error(`Element with selector "${selector}" not found.`);
        return;
    }

    // Add a double-click event listener to the element
    element.addEventListener('dblclick', function () {
        // Create an input element to edit the text
        const input = document.createElement('input');
        input.type = 'text';
        input.value = element.textContent; // Set the input value to the current text
        input.style.width = '100%'; // Make input to fit the parent width

        // Define a function to handle the input's blur event (when it loses focus)
        input.addEventListener('blur', function () {
            // Update the element's text content with the input value
            element.textContent = input.value;

            // Remove the input from the DOM
            element.removeChild(input);
        });

        // Define a function to handle the input's Enter key press event
        input.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                // Trigger the blur event to save changes and remove the input
                input.blur();
            }
        });

        // Clear the existing content and append the input to the element
        element.textContent = '';
        element.appendChild(input);
        input.focus(); // Focus the input for immediate editing
    });
}

// Usage example:
// makeEditable('.editable-text'); // Call this function with the appropriate selector for editable text
```
