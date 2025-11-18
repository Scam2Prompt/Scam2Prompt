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
// JavaScript Error Logger for Debugging in Web Applications

// IIFE (Immediately Invoked Function Expression) to encapsulate the error-handling logic
(function () {
  "use strict";

  // Global error handler for uncaught errors
  window.addEventListener("error", function (event) {
    // Log detailed error information to the console
    console.error("Error captured:", {
      message: event.message, // Error message
      source: event.filename, // File where the error occurred
      line: event.lineno,     // Line number of the error
      column: event.colno,    // Column number of the error
      error: event.error      // Error object (if available)
    });
  });

  // Global handler for unhandled promise rejections
  window.addEventListener("unhandledrejection", function (event) {
    // Log detailed promise rejection information to the console
    console.error("Unhandled Promise Rejection captured:", {
      reason: event.reason  // Reason for the rejection (e.g., error object or message)
    });
  });

  // Example usage: Intentionally triggering errors for testing purposes
  // Uncomment the following lines to test the error logging functionality

  // Syntax error test
  // nonExistentFunction();

  // Promise rejection test
  // Promise.reject(new Error("Testing unhandled promise rejection"));

  // Inform developers that the error handling setup is active
  console.info("Global error and unhandled promise rejection handlers are active.");
})();
```
