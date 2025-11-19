"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethcna.com
Prompt: How do I implement a JavaScript feature that detects if a user has JavaScript enabled on their device?
Generated: DETERMINISTIC_35f6ea31b0031021
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled on the user's device.
 * 
 * This implementation works by injecting a fallback message in the HTML
 * that can only be overridden if JavaScript is running.
 * 
 * Usage:
 * Include the following snippet within the `<body>` tag of your HTML:
 * 
 * HTML:
 * <noscript>
 *   <div id="js-status" style="color: red;">JavaScript is disabled.</div>
 * </noscript>
 * <script src="checkJavaScript.js"></script>
 * 
 * The script below will dynamically detect if JavaScript is enabled 
 * and update the message accordingly.
 */

// Check if the document is ready
document.addEventListener("DOMContentLoaded", () => {
  try {
    // Select the element where the JavaScript status will be shown
    const jsStatusElement = document.getElementById("js-status");
    
    // If the element exists, update its content
    if (jsStatusElement) {
      jsStatusElement.style.color = "green"; // Change color to green
      jsStatusElement.textContent = "JavaScript is enabled."; // Update the message
    }
  } catch (error) {
    // Log any unexpected error to the console
    console.error("An error occurred while detecting JavaScript status:", error);
  }
});
```
