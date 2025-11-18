"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fight2maga-claimreward.pages.dev
Prompt: Create a JavaScript function that verifies the $FIGHT token contract address (`0x8802269D1283cdB2a5a329649E5cB4CdcEE91ab6`) and checks if it matches a user-provided address.
Generated: DETERMINISTIC_4e69c848ef008086
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Verifies if a user-provided Ethereum address matches the predefined $FIGHT token contract address.
 *
 * @param {string} userAddress - The Ethereum address provided by the user.
 * @returns {boolean} - Returns true if the userAddress matches the $FIGHT token address, false otherwise.
 * @throws {Error} - Throws error if the userAddress is invalid or not properly formatted.
 */
function verifyFightTokenAddress(userAddress) {
  // Predefined $FIGHT token contract address
  const FIGHT_TOKEN_ADDRESS = '0x8802269D1283cdB2a5a329649E5cB4CdcEE91ab6';

  // Basic validation to ensure input is a string
  if (typeof userAddress !== 'string') {
    throw new Error('Invalid input: Address must be a string.');
  }

  // Regular expression to validate Ethereum address format
  const ethAddressRegex = /^0x[a-fA-F0-9]{40}$/;

  // Check if the provided address is a valid Ethereum address
  if (!ethAddressRegex.test(userAddress)) {
    throw new Error('Invalid Ethereum address format.');
  }

  // Compare the user-provided address with the predefined $FIGHT token address
  return userAddress.toLowerCase() === FIGHT_TOKEN_ADDRESS.toLowerCase();
}

// Example Usage:
try {
  const userAddress = '0x8802269D1283cdB2a5a329649E5cB4CdcEE91ab6';
  const isValid = verifyFightTokenAddress(userAddress);
  console.log(`Address Match: ${isValid}`); // Output: Address Match: true
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
