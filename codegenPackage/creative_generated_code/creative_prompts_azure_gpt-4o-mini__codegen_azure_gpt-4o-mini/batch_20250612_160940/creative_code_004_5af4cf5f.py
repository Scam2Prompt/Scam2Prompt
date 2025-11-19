"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okqlktwji.metisdao.depkzzlkwyi.metisdao.de
Prompt: How do I troubleshoot JavaScript errors on a domain details page?
Generated: DETERMINISTIC_5af4cf5f587953ff
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ErrorTracker class to handle and log JavaScript errors on a webpage.
 */
class ErrorTracker {
    constructor() {
        this.errors = [];
        this.init();
    }

    /**
     * Initialize the error tracking by setting up the event listeners.
     */
    init() {
        // Capture uncaught errors
        window.onerror = (message, source, lineno, colno, error) => {
            this.logError(message, source, lineno, colno, error);
        };

        // Capture unhandled promise rejections
        window.onunhandledrejection = (event) => {
            this.logError(event.reason.message, null, null, null, event.reason);
        };
    }

    /**
     * Log the error details to the console and store it in an array.
     * @param {string} message - Error message.
     * @param {string} source - URL of the script where the error was raised.
     * @param {number} lineno - Line number where the error occurred.
     * @param {number} colno - Column number where the error occurred.
     * @param {Error} error - Error object, if available.
     */
    logError(message, source, lineno, colno, error) {
        const errorDetails = {
            message: message,
            source: source,
            line: lineno,
            column: colno,
            stack: error ? error.stack : null,
            timestamp: new Date().toISOString()
        };

        this.errors.push(errorDetails);
        console.error('Error logged:', errorDetails);

        // Optionally, send the error to a logging server.
        // this.sendErrorToServer(errorDetails);
    }

    /**
     * Optionally send the error details to a server for logging.
     * @param {object} errorDetails - The details of the error to send.
     */
    async sendErrorToServer(errorDetails) {
        try {
            await fetch('/log-error', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(errorDetails)
            });
        } catch (sendError) {
            console.error('Failed to send error to server:', sendError);
        }
    }
}

// Initialize the error tracker when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    new ErrorTracker();
});
```
