"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-three.vercel.app
Prompt: Write code to troubleshoot JavaScript errors when running a SUI-based app.
Generated: DETERMINISTIC_2f1ce66f26ccd15d
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SUI Troubleshooting Utility
// This script provides a utility to troubleshoot JavaScript errors in a SUI-based application.

(function () {
    // Function to log errors to the console with a custom message
    function logError(message, error) {
        console.error(`${message}:`, error);
    }

    // Function to handle uncaught exceptions
    function handleUncaughtException(error) {
        logError("Uncaught Exception", error);
    }

    // Function to handle unhandled promise rejections
    function handleUnhandledRejection(reason) {
        logError("Unhandled Promise Rejection", reason);
    }

    // Function to initialize error handling
    function initializeErrorHandling() {
        // Set up global error handler for uncaught exceptions
        window.onerror = function (message, source, lineno, colno, error) {
            logError(`Error occurred at ${source}:${lineno}:${colno}`, error);
            return true; // Prevent default browser error handling
        };

        // Set up global error handler for unhandled promise rejections
        window.onunhandledrejection = function (event) {
            handleUnhandledRejection(event.reason);
            event.preventDefault(); // Prevent default browser handling
        };

        // Attach a handler to listen for any additional errors
        document.addEventListener('error', function (event) {
            if (event.target.tagName === 'SCRIPT') {
                logError(`Script error: ${event.target.src}`, event.error);
            }
        }, true);
    }

    // Execute the error handling initialization
    initializeErrorHandling();
})();
```
