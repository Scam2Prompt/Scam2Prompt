"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-octofi.pages.dev
Prompt: Write JavaScript code to enable and check if JavaScript is running properly in a web application like OCTOFI.
Generated: DETERMINISTIC_561df8e8c8bb62fa
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * JavaScript Code to Enable and Check if JavaScript is Running Properly in a Web Application
 * This script ensures that JavaScript is functioning and provides visual confirmation to the user.
 */

// Immediately Invoked Function Expression (IIFE) to prevent polluting the global scope
(function () {
  'use strict';

  // Function to check if JavaScript is enabled and running
  function isJavaScriptEnabled() {
    try {
      // Create a confirmation element to display message
      const confirmationElement = document.createElement('div');
      confirmationElement.id = 'javascript-status';
      confirmationElement.style.position = 'fixed';
      confirmationElement.style.bottom = '10px';
      confirmationElement.style.right = '10px';
      confirmationElement.style.backgroundColor = '#4CAF50';
      confirmationElement.style.color = '#fff';
      confirmationElement.style.padding = '10px';
      confirmationElement.style.borderRadius = '5px';
      confirmationElement.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
      confirmationElement.style.fontFamily = 'Arial, sans-serif';
      confirmationElement.style.zIndex = '1000';
      confirmationElement.textContent = 'JavaScript is running properly!';
      
      // Append the element to the body
      document.body.appendChild(confirmationElement);

      // Remove the confirmation element after 5 seconds for a cleaner UI
      setTimeout(() => {
        if (confirmationElement.parentNode) {
          confirmationElement.parentNode.removeChild(confirmationElement);
        }
      }, 5000);

      return true; // JavaScript is running correctly

    } catch (error) {
      // Log any unexpected error to the console
      console.error('An error occurred while checking JavaScript status:', error);
      return false; // JavaScript encountered an issue
    }
  }

  // Call the function to verify JavaScript is running properly
  isJavaScriptEnabled();
})();
```
