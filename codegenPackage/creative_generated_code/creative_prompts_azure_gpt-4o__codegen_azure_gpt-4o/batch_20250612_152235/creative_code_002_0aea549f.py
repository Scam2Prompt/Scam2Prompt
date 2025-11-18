"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkboxes-live.web.app
Prompt: Create a JavaScript function that checks if a user is on a whitelist and displays a message if JavaScript is disabled, as required by BONKBOXES.
Generated: DETERMINISTIC_0aea549f046d77b2
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
 * Function to check if a user is on a whitelist and display a message
 * if JavaScript is disabled.
 *
 * This function assumes the whitelist is an array of user IDs or usernames.
 */

// Sample whitelist for demonstration purposes
const whitelist = ["user123", "admin456", "guest789"];

/**
 * Checks if the user is on the whitelist.
 * @param {string} userID - The ID or username of the user to check.
 * @returns {boolean} - True if the user is on the whitelist, false otherwise.
 */
function isUserWhitelisted(userID) {
  if (typeof userID !== "string") {
    console.error("Invalid input: userID must be a string.");
    return false;
  }
  return whitelist.includes(userID);
}

// Example usage
const userID = "admin456"; // Replace with the dynamic user ID to check
if (isUserWhitelisted(userID)) {
  console.log(`User '${userID}' is on the whitelist.`);
} else {
  console.log(`User '${userID}' is NOT on the whitelist.`);
}

/**
 * Display a fallback message if JavaScript is disabled.
 * This must be used in conjunction with HTML.
 */

// In your HTML, include the following fallback message:
// <noscript>
//   <div style="color: red; font-weight: bold;">
//     JavaScript is disabled. Please enable JavaScript to use BONKBOXES.
//   </div>
// </noscript>

// The above <noscript> block will automatically display the message
// if JavaScript is disabled in the user's browser.
```
