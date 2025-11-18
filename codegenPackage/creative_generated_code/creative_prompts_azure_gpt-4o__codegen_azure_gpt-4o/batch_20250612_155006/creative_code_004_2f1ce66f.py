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
/**
 * Error troubleshooting utility for SUI-based JavaScript applications.
 * This script helps in identifying, logging, and alerting JavaScript errors
 * that occur within a SUI-based app.
 * 
 * Usage: Include this script in your SUI app to capture and report errors.
 */

(() => {
  // Error logger setup
  const errorLog = [];

  /**
   * Logs error details to both console and an internal array for further processing.
   * @param {string} message - The error message.
   * @param {string} source - The file where the error occurred.
   * @param {number} lineno - The line number where the error occurred.
   * @param {number} colno - The column number where the error occurred.
   * @param {Error} error - The error object itself (if available).
   */
  function logError(message, source, lineno, colno, error) {
    const errorDetails = {
      timestamp: new Date().toISOString(), // Record the time of the error
      message,
      source,
      lineno,
      colno,
      stack: error ? error.stack : null, // Include stack trace if available
    };

    // Push error to the internal log
    errorLog.push(errorDetails);

    // Log to the console for immediate visibility
    console.error('Error captured:', errorDetails);
  }

  /**
   * Error handler for uncaught JavaScript errors.
   * Automatically captures errors and sends them to the logger function.
   */
  window.onerror = function (message, source, lineno, colno, error) {
    logError(message, source, lineno, colno, error);

    // Optional: Show a user-friendly alert for critical errors
    alert('An error occurred! Please check the console for details.');
  };

  /**
   * Error handler for unhandled promise rejections.
   * Captures errors from promises and sends them to the logger function.
   */
  window.onunhandledrejection = function (event) {
    logError(
      event.reason.message || 'Unhandled Promise rejection',
      'Unknown source',
      0,
      0,
      event.reason
    );

    // Optional: Log unhandled promise rejection specifically
    console.warn('Unhandled Promise rejection:', event.reason);
  };

  /**
   * Function to get the logged errors for debugging or reporting purposes.
   * @returns {Array} - Array containing all logged errors.
   */
  function getErrorLogs() {
    return [...errorLog];
  }

  /**
   * Example function to simulate an error for testing purposes.
   * Uncomment to test the error handling functionality.
   */
  // function simulateError() {
  //   throw new Error('Test error!');
  // }

  // Expose the error log retrieval function for external use
  window.getErrorLogs = getErrorLogs;

  console.info('Error troubleshooting utility initialized.');
})();
```
