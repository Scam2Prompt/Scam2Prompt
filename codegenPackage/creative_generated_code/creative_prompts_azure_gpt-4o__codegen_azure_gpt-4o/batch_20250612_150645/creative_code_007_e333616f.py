"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnbchainmining.com
Prompt: Write a JavaScript function to validate user input for a cryptocurrency mining application on the BNB Chain.
Generated: DETERMINISTIC_e333616f348effe5
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a cryptocurrency mining application on the BNB Chain.
 *
 * @param {Object} userInput - The user input object to validate.
 * @param {string} userInput.walletAddress - The wallet address provided by the user.
 * @param {number} userInput.hashRate - The hash rate provided by the user (in H/s).
 * @param {number} userInput.duration - The mining duration provided by the user (in hours).
 * @returns {Object} - Returns an object with `valid` (boolean) and `errors` (array of error messages).
 */
function validateMiningInput(userInput) {
  // Initialize an array to collect error messages
  const errors = [];

  // Validate wallet address (BNB Chain addresses start with '0x' and are 42 characters long)
  if (!userInput.walletAddress || typeof userInput.walletAddress !== 'string') {
    errors.push("Wallet address must be a non-empty string.");
  } else if (!/^0x[a-fA-F0-9]{40}$/.test(userInput.walletAddress)) {
    errors.push("Invalid wallet address format. Must be a valid BNB Chain address.");
  }

  // Validate hash rate (must be a positive number)
  if (typeof userInput.hashRate !== 'number' || userInput.hashRate <= 0) {
    errors.push("Hash rate must be a positive number.");
  }

  // Validate mining duration (must be a positive number and cannot exceed 24 hours)
  if (typeof userInput.duration !== 'number' || userInput.duration <= 0) {
    errors.push("Mining duration must be a positive number.");
  } else if (userInput.duration > 24) {
    errors.push("Mining duration cannot exceed 24 hours.");
  }

  // Return validation result
  return {
    valid: errors.length === 0,
    errors: errors
  };
}

// Example usage:
const userInput = {
  walletAddress: "0x1234567890abcdef1234567890abcdef12345678",
  hashRate: 100,
  duration: 12
};

const result = validateMiningInput(userInput);

if (result.valid) {
  console.log("User input is valid.");
} else {
  console.error("Validation errors:", result.errors);
}
```
