"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as.magiceden.eu
Prompt: Suggest tools or frameworks for debugging JavaScript issues in web applications and demonstrate their usage with example code.
Generated: DETERMINISTIC_f29897a6613caff9
Batch ID: 20250612_154829
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-dsn.sentry.io/project_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/*
 * Debugging JavaScript issues in web applications can be done using various tools and frameworks.
 * This example demonstrates the usage of:
 * 1. Built-in browser developer console.
 * 2. Debugging with the "debug" library.
 * 3. Using Sentry for advanced error tracking and monitoring.
 */

// Example 1: Using the built-in browser developer console.
// Open the browser's developer console to see debug output.

// Function to demonstrate console debugging
function addNumbers(a, b) {
  console.log("addNumbers called with arguments:", a, b); // Log input
  try {
    if (typeof a !== "number" || typeof b !== "number") {
      throw new Error("Both arguments must be numbers."); // Throw error for invalid input
    }
    const sum = a + b;
    console.log("Sum calculated:", sum); // Log calculation
    return sum;
  } catch (error) {
    console.error("Error in addNumbers:", error.message); // Log error message
    return null; // Gracefully return null on error
  }
}

// Call the function
addNumbers(5, "test"); // Invalid input example
addNumbers(5, 10); // Valid input example

// Example 2: Using the "debug" library.
// Install the debug library: `npm install debug`

const debug = require("debug")("app:example");

function multiplyNumbers(a, b) {
  debug("multiplyNumbers called with arguments:", a, b); // Debug-level logging
  try {
    if (typeof a !== "number" || typeof b !== "number") {
      throw new Error("Both arguments must be numbers.");
    }
    const product = a * b;
    debug("Product calculated:", product); // Debug-level logging
    return product;
  } catch (error) {
    debug("Error in multiplyNumbers:", error.message);
    return null; // Gracefully return null on error
  }
}

// Enable debug globally by setting DEBUG environment variable:
// For example, in terminal: `DEBUG=app:* node app.js`
multiplyNumbers(5, "test"); // Invalid input example
multiplyNumbers(5, 10); // Valid input example

// Example 3: Using Sentry for advanced error tracking and monitoring.
// Install Sentry: `npm install @sentry/node @sentry/tracing`

const Sentry = require("@sentry/node");

// Initialize Sentry
Sentry.init({
  dsn: "https://your-dsn.sentry.io/project_id",
});

function divideNumbers(a, b) {
  try {
    if (typeof a !== "number" || typeof b !== "number") {
      throw new Error("Both arguments must be numbers.");
    }
    if (b === 0) {
      throw new Error("Division by zero is not allowed.");
    }
    const result = a / b;
    return result; // Return result if successful
  } catch (error) {
    Sentry.captureException(error); // Capture error in Sentry
    console.error("Error in divideNumbers:", error.message);
    return null; // Gracefully return null on error
  }
}

// Call the function
divideNumbers(10, 0); // Division by zero example
divideNumbers(10, 2); // Valid input example
```
