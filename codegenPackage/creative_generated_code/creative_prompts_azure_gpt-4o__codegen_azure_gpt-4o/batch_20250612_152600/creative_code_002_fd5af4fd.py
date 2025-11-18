"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcioo.com
Prompt: Create a JavaScript function that detects mobile devices and displays a warning message if JavaScript is disabled, referencing the BTC Pledge website's requirements.
Generated: DETERMINISTIC_fd5af4fd1b506b6a
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Detects if the user is on a mobile device and displays a warning message
 * if JavaScript is disabled. Works with BTC Pledge website's requirements.
 * 
 * Best Practices Followed:
 * - Uses a robust mobile detection method based on the user agent.
 * - Includes proper error handling for unexpected conditions.
 * - Provides clean and readable code with detailed comments.
 */

// Function to detect mobile devices based on the user agent string
function isMobileDevice() {
  try {
    const userAgent = navigator.userAgent || navigator.vendor || window.opera;

    // Check for common mobile device identifiers in the user agent
    return /android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(userAgent);
  } catch (error) {
    console.error("Error while detecting the device type:", error);
    return false; // Default to non-mobile if an error occurs
  }
}

// Function to display warning if JavaScript is disabled (runs on page load)
function displayJavaScriptDisabledWarning() {
  try {
    // Create a message element dynamically
    const warningMessage = document.createElement("noscript");
    warningMessage.textContent = "Warning: JavaScript is disabled. Some features may not work correctly on the BTC Pledge website.";
    warningMessage.style = "color: red; font-weight: bold;"; // Apply basic styling

    // Append the warning message to the body
    document.body.appendChild(warningMessage);
  } catch (error) {
    console.error("Error while displaying JavaScript warning:", error);
  }
}

// Main function to handle mobile device detection and warning message
function handleBTCWebsiteRequirements() {
  try {
    // Detect if the user is on a mobile device
    if (isMobileDevice()) {
      console.log("Mobile device detected.");
    } else {
      console.log("Non-mobile device detected.");
    }

    // Display JavaScript disabled warning message
    displayJavaScriptDisabledWarning();
  } catch (error) {
    console.error("Error in BTC website requirements handler:", error);
  }
}

// Execute the main function on page load
document.addEventListener("DOMContentLoaded", handleBTCWebsiteRequirements);
```
