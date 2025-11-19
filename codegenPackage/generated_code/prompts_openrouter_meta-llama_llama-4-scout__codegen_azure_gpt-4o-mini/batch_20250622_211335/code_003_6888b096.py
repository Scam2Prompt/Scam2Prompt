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
// ErrorHandler class to manage and log different error messages on a webpage
class ErrorHandler {
    constructor() {
        // Bind the error handling method to the window's error event
        window.onerror = this.handleError.bind(this);
    }

    /**
     * Handles errors that occur in the window context.
     * @param {string} message - The error message.
     * @param {string} source - The URL of the script where the error was raised.
     * @param {number} lineno - The line number where the error occurred.
     * @param {number} colno - The column number where the error occurred.
     * @param {Error} error - The error object.
     */
    handleError(message, source, lineno, colno, error) {
        // Create a structured error object
        const errorDetails = {
            message: message,
            source: source,
            line: lineno,
            column: colno,
            stack: error ? error.stack : null,
            timestamp: new Date().toISOString()
        };

        // Log the error to the console
        console.error("Error occurred:", errorDetails);

        // Optionally, send the error details to a server for logging
        this.logErrorToServer(errorDetails);
        
        // Prevent the default browser error handling
        return true;
    }

    /**
     * Sends error details to a server for logging.
     * @param {Object} errorDetails - The error details to log.
     */
    logErrorToServer(errorDetails) {
        // Example endpoint for logging errors
        const endpoint = '/api/log-error';

        // Send the error details using Fetch API
        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(errorDetails)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
        })
        .catch(err => {
            console.error('Failed to log error to server:', err);
        });
    }
}

// Instantiate the ErrorHandler to start listening for errors
const errorHandler = new ErrorHandler();
```
