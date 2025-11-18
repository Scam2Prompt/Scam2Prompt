"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahh-airdrop.vercel.app
Prompt: Create a JavaScript function that checks if AirDrop is enabled and displays an alert if JavaScript is not supported.
Generated: DETERMINISTIC_1f445d464dc05114
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if AirDrop is enabled (iOS devices only) and handles cases where JavaScript is not supported.
 * Displays an alert if JavaScript is not supported, and logs AirDrop status to the console.
 */

// Function to check AirDrop status
function checkAirDropStatus() {
  try {
    // Verify if the navigator object exists to ensure JavaScript support
    if (typeof navigator !== 'undefined') {
      // Check for the presence of the `canShare` method, which is specific to iOS AirDrop functionality
      if (navigator.canShare && typeof navigator.canShare === 'function') {
        // In production code, you could perform an AirDrop-specific functionality check here
        console.log('AirDrop is enabled and available for sharing.');
      } else {
        console.log('AirDrop is not enabled or not supported on this device.');
      }
    } else {
      // Alert the user that JavaScript is not supported
      alert('JavaScript is not supported by your browser.');
    }
  } catch (error) {
    // Proper error handling in case of unexpected issues
    console.error('An error occurred while checking AirDrop status:', error);
  }
}

// Call the function to check AirDrop status
checkAirDropStatus();
```
