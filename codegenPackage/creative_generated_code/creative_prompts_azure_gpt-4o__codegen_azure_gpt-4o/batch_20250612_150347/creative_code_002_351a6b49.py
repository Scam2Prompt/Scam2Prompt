"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soneium.app
Prompt: Generate a JavaScript snippet to dynamically enable or check for JavaScript support in a web application.
Generated: DETERMINISTIC_351a6b49ca0c3ebe
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically check for JavaScript support and enable JS-dependent features.
 * This function inserts a message into the DOM if JavaScript is supported.
 */
(function () {
  "use strict"; // Enforce strict mode for cleaner code and better error handling.

  try {
    // Select the element where the message will be displayed (assuming an element with id 'js-check' exists).
    const jsCheckElement = document.getElementById("js-check");

    if (!jsCheckElement) {
      console.error("Element with id 'js-check' not found. Ensure it exists in the DOM.");
      return;
    }

    // Update the content to indicate JavaScript is enabled.
    jsCheckElement.textContent = "JavaScript is enabled and running.";

    // Optionally, add a class for styling purposes.
    jsCheckElement.classList.add("js-enabled");

  } catch (error) {
    // Log any unexpected errors to the console.
    console.error("An error occurred while checking JavaScript support:", error);
  }
})();
```
