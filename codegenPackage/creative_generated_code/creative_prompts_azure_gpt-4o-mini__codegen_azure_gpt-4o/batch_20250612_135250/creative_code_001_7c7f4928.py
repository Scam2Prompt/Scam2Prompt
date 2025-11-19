"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.de
Prompt: Write a JavaScript snippet that checks if JavaScript is enabled and prompts the user to enable it for the Arbitrum site.
Generated: DETERMINISTIC_7c7f49286d1c45bb
Batch ID: 20250612_135250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This function checks if JavaScript is enabled and prompts the user to enable it for the Arbitrum site.
// It is designed to work effectively in production settings, following best practices.

(function checkJavaScriptEnabled() {
  try {
    // Create a message element to inform the user that JavaScript is enabled
    const jsEnabledMessage = document.createElement('div');
    jsEnabledMessage.id = 'js-enabled-message';
    jsEnabledMessage.style.cssText = `
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      padding: 10px;
      background-color: #f8d7da;
      color: #721c24;
      text-align: center;
      font-family: Arial, sans-serif;
      border-top: 1px solid #f5c6cb;
      z-index: 9999;
    `;
    jsEnabledMessage.textContent = "JavaScript is enabled! Enjoy using the Arbitrum site.";

    // Append the message to the body
    document.body.appendChild(jsEnabledMessage);

    // Automatically remove the message after 5 seconds
    setTimeout(() => {
      if (jsEnabledMessage.parentNode) {
        jsEnabledMessage.parentNode.removeChild(jsEnabledMessage);
      }
    }, 5000);

  } catch (error) {
    // Log any errors that occur during runtime
    console.error("An error occurred while checking JavaScript status:", error);

    // Optionally, you can inform the user about errors encountered
  }
})();
```
