"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.888innercircle.com
Prompt: Create a JavaScript snippet that checks for JavaScript errors and logs them to the console for debugging purposes in a web application.
Generated: DETERMINISTIC_89b117f637ff42e0
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Error handling utility for logging JavaScript errors to the console
(function() {
    // Function to log the error details
    function logError(error) {
        if (error instanceof Error) {
            console.error("Error Name: ", error.name);
            console.error("Error Message: ", error.message);
            console.error("Error Stack: ", error.stack);
        } else {
            console.error("Unexpected error:", error);
        }
    }

    // Event listener for uncaught errors
    window.addEventListener('error', function(event) {
        logError(event.error);
    });

    // Event listener for unhandled promise rejections
    window.addEventListener('unhandledrejection', function(event) {
        logError(event.reason);
    });

    // Optionally, you can track the error logging start
    console.log("Error logging initialized.");
})();
```
