"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getin.co.il
Prompt: What are the best practices for handling JavaScript errors in a web application to improve user experience?
Generated: DETERMINISTIC_429e4500aa2a2f22
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Error handling utility for web applications
class ErrorHandler {
    constructor() {
        // Initialize an array to keep track of error logs
        this.errorLogs = [];
    }

    // Method to log an error with a custom message
    logError(error, customMessage = '') {
        const errorDetails = {
            message: error.message || 'Unknown error',
            stack: error.stack || 'No stack trace available',
            customMessage: customMessage,
            timestamp: new Date().toISOString()
        };
        this.errorLogs.push(errorDetails);
        this.sendToServer(errorDetails);
        this.displayUserFriendlyMessage(customMessage);
    }

    // Method to send error details to server for logging (replace with your endpoint)
    async sendToServer(errorDetails) {
        try {
            const response = await fetch('/api/log-error', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(errorDetails)
            });

            if (!response.ok) {
                console.error('Failed to log error on server:', response.statusText);
            }
        } catch (networkError) {
            console.error('Network error while logging the error:', networkError);
        }
    }

    // Method to display a user-friendly message
    displayUserFriendlyMessage(customMessage) {
        // Custom implementation to show a notification to the user
        const userFriendlyMessage = customMessage || 'Something went wrong. Please try again later.';
        alert(userFriendlyMessage); // Replace with a user-friendly UI notification in production
    }
}

// Initialize the error handler
const errorHandler = new ErrorHandler();

// Global error handling for uncaught exceptions
window.onerror = function (message, source, lineno, colno, error) {
    errorHandler.logError(error || new Error(message), 'An unexpected error occurred.');
};

// Global error handling for unhandled promise rejections
window.onunhandledrejection = function (event) {
    errorHandler.logError(event.reason || new Error('Unhandled promise rejection'), 'A promise error occurred.');
};

// Example function that could throw an error
function riskyOperation() {
    try {
        // Code that may throw an error
        throw new Error('Simulated error in risky operation.');
    } catch (error) {
        errorHandler.logError(error, 'Error occurred during risky operation.');
    }
}

// Call the example function
riskyOperation();
```
