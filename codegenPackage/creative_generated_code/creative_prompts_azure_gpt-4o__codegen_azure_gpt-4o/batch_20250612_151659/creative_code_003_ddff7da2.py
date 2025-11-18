"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://full-mint-website-master.pages.dev
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message accordingly, as seen in the React app at https://full-mint-website-master.pages.dev.
Generated: DETERMINISTIC_ddff7da2e811d8c8
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled in the browser
 * and display a message accordingly in the DOM.
 */
function checkJavaScriptEnabled() {
  try {
    // Ensure the DOM is fully loaded before executing
    document.addEventListener("DOMContentLoaded", () => {
      // Create a message container
      const messageContainer = document.createElement("div");
      messageContainer.id = "js-status-message";
      messageContainer.style.padding = "10px";
      messageContainer.style.margin = "10px";
      messageContainer.style.border = "1px solid #ccc";
      messageContainer.style.borderRadius = "5px";
      messageContainer.style.fontFamily = "Arial, sans-serif";
      
      // Set the success message if JavaScript is enabled
      messageContainer.textContent = "JavaScript is enabled in your browser.";
      messageContainer.style.backgroundColor = "#d4edda"; // Light green
      messageContainer.style.color = "#155724";          // Dark green
      
      // Append the message to the body
      document.body.appendChild(messageContainer);
    });
  } catch (error) {
    // Log any potential errors to the console
    console.error("An error occurred while checking JavaScript status:", error);
    
    // Optionally display a fallback error message in the DOM
    const errorMessage = document.createElement("div");
    errorMessage.textContent = "An unexpected error occurred. Please check the console for details.";
    errorMessage.style.color = "#721c24";          // Dark red
    errorMessage.style.backgroundColor = "#f8d7da"; // Light red
    errorMessage.style.padding = "10px";
    errorMessage.style.margin = "10px";
    errorMessage.style.border = "1px solid #f5c6cb";
    errorMessage.style.borderRadius = "5px";
    errorMessage.style.fontFamily = "Arial, sans-serif";
    document.body.appendChild(errorMessage);
  }
}

// Call the function to execute
checkJavaScriptEnabled();
```
