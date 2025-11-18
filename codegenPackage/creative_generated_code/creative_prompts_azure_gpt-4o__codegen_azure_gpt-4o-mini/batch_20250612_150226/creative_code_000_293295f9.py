"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harvesters-app.pages.dev
Prompt: Write JavaScript code to enable and check if JavaScript is running correctly in a web application like Harvest App.
Generated: DETERMINISTIC_293295f9e95bb56f
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * JavaScript Check Utility
 * This utility checks if JavaScript is enabled and running correctly in the web application.
 * It displays an alert message based on the result.
 */

// Function to check if JavaScript is enabled
function checkJavaScript() {
    try {
        // Creating a test element
        const testElement = document.createElement('div');
        // Setting a test property
        testElement.textContent = 'JavaScript is enabled!';
        
        // Appending the test element to the body
        document.body.appendChild(testElement);
        
        // Displaying a success message
        alert(testElement.textContent);
    } catch (error) {
        console.error('Error while checking JavaScript:', error);
        
        // Displaying an error message if something goes wrong
        alert('JavaScript is not running correctly. Please check your browser settings.');
    }
}

// Execute the check when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', (event) => {
    checkJavaScript();
});
```
