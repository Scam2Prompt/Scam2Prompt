"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devoursol.com
Prompt: Write a JavaScript function that checks for user verification before allowing access to a web application.
Generated: DETERMINISTIC_b5d390805c70ba85
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check user verification before granting access to a web application.
 * This function simulates a user verification process and ensures proper error handling.
 * 
 * @param {Object} user - The user object containing user details.
 * @param {boolean} user.isVerified - Indicates whether the user is verified.
 * @throws Will throw an error if the user object is invalid or the user is not verified.
 * @returns {string} A success message if the user is verified.
 */
function checkUserVerification(user) {
  // Ensure a valid user object is provided
  if (!user || typeof user !== 'object') {
    throw new Error("Invalid user object provided.");
  }

  // Check if the user has the 'isVerified' property
  if (!('isVerified' in user)) {
    throw new Error("Missing 'isVerified' property in user object.");
  }

  // Check if the user is verified
  if (!user.isVerified) {
    throw new Error("Access denied: User is not verified.");
  }

  // Return success message if verification passes
  return "Access granted: User is verified.";
}

// Example usage:
try {
  const user = { isVerified: true }; // Simulated user object
  console.log(checkUserVerification(user)); // Expected output: "Access granted: User is verified."
} catch (error) {
  console.error(error.message); // Handle errors gracefully
}
```
