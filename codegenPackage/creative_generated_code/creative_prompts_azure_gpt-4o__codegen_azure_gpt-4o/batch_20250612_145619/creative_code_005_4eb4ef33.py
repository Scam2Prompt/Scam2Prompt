"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtaoekecn.com
Prompt: Write a script to check browser compatibility for Ethereum-related web applications, ensuring JavaScript is enabled as required by the ETH Pledge website.
Generated: DETERMINISTIC_4eb4ef3371da5efc
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Script to check browser compatibility for Ethereum-related web applications
// Ensures JavaScript is enabled and checks for basic browser compatibility

(function () {
  "use strict";

  /**
   * Function to display compatibility status to the user
   * @param {boolean} isCompatible - Indicates whether the browser is compatible
   * @param {string} message - Message to display to the user
   */
  function displayCompatibilityStatus(isCompatible, message) {
    const statusDiv = document.createElement("div");
    statusDiv.style.position = "fixed";
    statusDiv.style.top = "0";
    statusDiv.style.left = "0";
    statusDiv.style.width = "100%";
    statusDiv.style.padding = "10px";
    statusDiv.style.boxSizing = "border-box";
    statusDiv.style.textAlign = "center";
    statusDiv.style.zIndex = "9999";
    statusDiv.style.color = isCompatible ? "green" : "red";
    statusDiv.style.backgroundColor = isCompatible ? "#d4edda" : "#f8d7da";
    statusDiv.style.border = isCompatible ? "1px solid #c3e6cb" : "1px solid #f5c6cb";
    statusDiv.innerText = message;
    document.body.appendChild(statusDiv);
  }

  /**
   * Function to check if JavaScript is enabled and browser supports key Ethereum web app APIs
   */
  function checkCompatibility() {
    try {
      // Ensure Web3 provider (e.g., MetaMask) is available
      const isWeb3Available = typeof window.ethereum !== "undefined";

      // Ensure JavaScript is enabled (this script won't run if JavaScript is disabled)
      const isJavaScriptEnabled = true;

      // Browser must support ES6+ features
      const isES6Supported = (() => {
        try {
          new Function("(a = 0) => a"); // Arrow functions and default params
          return true;
        } catch (e) {
          return false;
        }
      })();

      // Aggregate results
      if (isJavaScriptEnabled && isWeb3Available && isES6Supported) {
        displayCompatibilityStatus(
          true,
          "Your browser is compatible with Ethereum-related web applications."
        );
      } else {
        let errorMessage = "Browser compatibility check failed:\n";

        if (!isWeb3Available) {
          errorMessage += "- Ethereum provider (e.g., MetaMask) is not available.\n";
        }
        if (!isJavaScriptEnabled) {
          errorMessage += "- JavaScript is not enabled.\n";
        }
        if (!isES6Supported) {
          errorMessage += "- Your browser does not support modern JavaScript (ES6+).\n";
        }

        displayCompatibilityStatus(false, errorMessage.trim());
      }
    } catch (error) {
      console.error("An error occurred during compatibility check:", error);
      displayCompatibilityStatus(
        false,
        "An unexpected error occurred during the compatibility check. Please try again."
      );
    }
  }

  // Run the compatibility check when the DOM is fully loaded
  document.addEventListener("DOMContentLoaded", checkCompatibility);
})();
```
