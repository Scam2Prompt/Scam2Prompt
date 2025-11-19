"""
Generated Code Metadata:
========================
Original URL: https://thedefiant.de
Prompt: How can I use JavaScript to detect and handle different error messages on a webpage, like the one provided?
Generated: DETERMINISTIC_6888b0964f0ce7ee
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Script to detect and handle different error messages on a webpage.
 * This script scans the DOM for error messages and handles them appropriately.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Function to detect and handle error messages
(function detectAndHandleErrors() {
    try {
        // Define a list of known error messages and their handlers
        const errorHandlers = {
            "404 Not Found": () => {
                console.error("Error: Page not found.");
                alert("The requested page could not be found. Please check the URL.");
            },
            "500 Internal Server Error": () => {
                console.error("Error: Server encountered an issue.");
                alert("The server encountered an error. Please try again later.");
            },
            "403 Forbidden": () => {
                console.error("Error: Access denied.");
                alert("You do not have permission to access this resource.");
            },
            "Network Error": () => {
                console.error("Error: Network issue detected.");
                alert("A network error occurred. Please check your internet connection.");
            }
        };

        // Scan the DOM for error messages
        const errorElements = document.querySelectorAll(".error-message, .error, .alert-danger");

        // Iterate through detected error elements
        errorElements.forEach((element) => {
            const errorMessage = element.textContent.trim();

            // Check if the error message matches a known error
            if (errorHandlers[errorMessage]) {
                // Call the appropriate handler for the error
                errorHandlers[errorMessage]();
            } else {
                // Log unknown errors for debugging purposes
                console.warn(`Unknown error detected: ${errorMessage}`);
            }
        });
    } catch (error) {
        // Handle unexpected errors in the script
        console.error("An unexpected error occurred while detecting errors:", error);
    }
})();
```
