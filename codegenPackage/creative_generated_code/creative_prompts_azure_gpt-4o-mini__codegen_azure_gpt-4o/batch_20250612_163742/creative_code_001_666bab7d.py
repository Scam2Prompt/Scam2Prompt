"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdddd.pages.dev
Prompt: Write a JavaScript function that checks if the user is on a desktop and prompts them to switch devices if they are not.
Generated: DETERMINISTIC_666bab7d8708cd79
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if the user is on a desktop device.
 * If not, it prompts them to switch devices.
 */
function checkDeviceAndPrompt() {
  try {
    // Detect the user's device type based on the user agent string
    const isDesktop = window.navigator.userAgent.match(/Windows|Macintosh|Linux/);

    if (isDesktop) {
      console.log("You are using a desktop device.");
    } else {
      // Prompt the user to consider switching to a desktop device
      alert("It looks like you're not on a desktop device. For the best experience, please switch to a desktop.");
    }
  } catch (error) {
    // Log any unexpected errors to the console
    console.error("An error occurred while detecting the device:", error);
  }
}

// Execute the function
checkDeviceAndPrompt();
```
