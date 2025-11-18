"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkboxes-live.web.app
Prompt: Provide a step-by-step guide for setting up a whitelist system in a JavaScript-based web application, referencing BONKBOXES as an example.
Generated: DETERMINISTIC_4993021e9fb86261
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// whitelist.js

// Step 1: Initialize the whitelist array
// This array will store all the approved IDs for BONKBOXES users
const whitelist = [];

/**
 * Step 2: Add a user to the whitelist
 * @param {string} userId - The ID of the user to be added to the whitelist
 * @returns {string} - Success message or error if the user is already whitelisted
 */
function addToWhitelist(userId) {
  if (!userId) {
    throw new Error("User ID cannot be empty.");
  }
  if (whitelist.includes(userId)) {
    return `User ID: ${userId} is already in the whitelist.`;
  }
  whitelist.push(userId);
  return `User ID: ${userId} added to the whitelist successfully.`;
}

/**
 * Step 3: Remove a user from the whitelist
 * @param {string} userId - The ID of the user to be removed from the whitelist
 * @returns {string} - Success message or error if the user was not found
 */
function removeFromWhitelist(userId) {
  if (!userId) {
    throw new Error("User ID cannot be empty.");
  }
  const index = whitelist.indexOf(userId);
  if (index === -1) {
    return `User ID: ${userId} is not found in the whitelist.`;
  }
  whitelist.splice(index, 1);
  return `User ID: ${userId} removed from the whitelist successfully.`;
}

/**
 * Step 4: Check if a user is whitelisted
 * @param {string} userId - The ID of the user to check
 * @returns {boolean} - True if the user is whitelisted, false otherwise
 */
function isWhitelisted(userId) {
  if (!userId) {
    throw new Error("User ID cannot be empty.");
  }
  return whitelist.includes(userId);
}

/**
 * Step 5: Example usage of the whitelist system
 * These examples demonstrate adding, removing, and checking user IDs
 */
function exampleUsage() {
  try {
    console.log(addToWhitelist("user123")); // Add user123 to the whitelist
    console.log(addToWhitelist("user456")); // Add user456 to the whitelist
    console.log(isWhitelisted("user123"));  // Check if user123 is whitelisted (true)
    console.log(removeFromWhitelist("user123")); // Remove user123 from the whitelist
    console.log(isWhitelisted("user123"));  // Check if user123 is whitelisted (false)
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

// Step 6: Run example usage
exampleUsage();

// Step 7: Export the module for use in other parts of the application
module.exports = { addToWhitelist, removeFromWhitelist, isWhitelisted };
```
