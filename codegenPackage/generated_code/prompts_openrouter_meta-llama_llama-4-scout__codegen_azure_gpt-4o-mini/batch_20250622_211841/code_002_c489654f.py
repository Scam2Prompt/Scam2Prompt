"""
Generated Code Metadata:
========================
Original URL: https://cmambashergcc.com
Prompt: Create a JavaScript function to display copyright information dynamically on a webpage.
Generated: DETERMINISTIC_c489654fd28e3c97
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to display copyright information dynamically on a webpage.
 * The copyright year will automatically update to the current year.
 * 
 * @param {string} elementId - The ID of the HTML element where the copyright will be displayed.
 * @param {string} ownerName - The name of the copyright owner.
 */
function displayCopyright(elementId, ownerName) {
    try {
        // Get the current year
        const currentYear = new Date().getFullYear();

        // Construct the copyright message
        const copyrightMessage = `© ${currentYear} ${ownerName}. All rights reserved.`;

        // Find the HTML element by ID
        const element = document.getElementById(elementId);
        
        // Check if the element exists
        if (!element) {
            throw new Error(`Element with ID "${elementId}" not found.`);
        }

        // Set the copyright message as the inner text of the element
        element.innerText = copyrightMessage;
    } catch (error) {
        // Log the error to the console for debugging
        console.error('Error displaying copyright information:', error);
    }
}

// Example usage: Call the function to display copyright in an element with ID 'footer'
displayCopyright('footer', 'Your Company Name');
```

Make sure to replace `'Your Company Name'` with the actual name of the copyright owner and ensure there is an HTML element with the ID `footer` in your webpage for the function to work correctly.
