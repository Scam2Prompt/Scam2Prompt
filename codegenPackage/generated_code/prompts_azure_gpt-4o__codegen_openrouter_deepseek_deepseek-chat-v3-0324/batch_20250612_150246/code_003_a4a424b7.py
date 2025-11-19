"""
Generated Code Metadata:
========================
Original URL: https://cb-pay-tam.vercel.app
Prompt: Suggest methods to debug JavaScript errors in a web app that requires JavaScript to run, such as "CB Pay TAM."
Generated: DETERMINISTIC_a4a424b72b2c31ee
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Debugging utility for JavaScript errors in web apps.
 * Provides methods to log, track, and handle errors effectively.
 */
class Debugger {
  /**
   * Initialize the debugger with optional configurations.
   * @param {Object} config - Configuration options.
   * @param {boolean} config.logToConsole - Whether to log errors to console.
   * @param {boolean} config.logToServer - Whether to send errors to server.
   * @param {string} config.serverEndpoint - Server endpoint for error logging.
   */
  constructor(config = {}) {
    this.config = {
      logToConsole: true,
      logToServer: false,
      serverEndpoint: '/log-error',
      ...config,
    };
    this.setupErrorHandlers();
  }

  /**
   * Setup global error handlers for uncaught exceptions and promise rejections.
   */
  setupErrorHandlers() {
    // Handle synchronous errors
    window.addEventListener('error', (event) => {
      this.handleError(event.error || event.message, event.filename, event.lineno, event.colno);
    });

    // Handle unhandled promise rejections
    window.addEventListener('unhandledrejection', (event) => {
      this.handleError(event.reason, 'Unhandled Rejection');
    });
  }

  /**
   * Handle and process errors based on configuration.
   * @param {Error|string} error - The error object or message.
   * @param {string} [source] - Source file where error occurred.
   * @param {number} [line] - Line number where error occurred.
   * @param {number} [column] - Column number where error occurred.
   */
  handleError(error, source, line, column) {
    const errorData = {
      message: error instanceof Error ? error.message : error,
      stack: error instanceof Error ? error.stack : undefined,
      source,
      line,
      column,
      timestamp: new Date().toISOString(),
      userAgent: navigator.userAgent,
      url: window.location.href,
    };

    if (this.config.logToConsole) {
      console.error('Error:', errorData);
    }

    if (this.config.logToServer) {
      this.sendErrorToServer(errorData);
    }
  }

  /**
   * Send error data to the server for logging.
   * @param {Object} errorData - Error information to log.
   */
  async sendErrorToServer(errorData) {
    try {
      const response = await fetch(this.config.serverEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(errorData),
      });

      if (!response.ok) {
        console.error('Failed to log error to server:', response.statusText);
      }
    } catch (err) {
      console.error('Error sending error to server:', err);
    }
  }

  /**
   * Wrap a function with error handling.
   * @param {Function} fn - Function to wrap.
   * @returns {Function} Wrapped function with error handling.
   */
  wrapFunction(fn) {
    return (...args) => {
      try {
        return fn(...args);
      } catch (err) {
        this.handleError(err, 'Wrapped Function');
        throw err; // Re-throw to maintain original behavior
      }
    };
  }

  /**
   * Log a message to the console if logging is enabled.
   * @param {string} message - Message to log.
   * @param {string} [level='log'] - Log level (log, info, warn, error).
   */
  log(message, level = 'log') {
    if (this.config.logToConsole) {
      console[level](`[Debugger] ${message}`);
    }
  }
}

// Example usage:
// const debugger = new Debugger({
//   logToConsole: true,
//   logToServer: true,
//   serverEndpoint: '/api/log-error'
// });

// debugger.wrapFunction(() => {
//   // Potentially error-prone code
// });

// debugger.log('Application initialized', 'info');
```
