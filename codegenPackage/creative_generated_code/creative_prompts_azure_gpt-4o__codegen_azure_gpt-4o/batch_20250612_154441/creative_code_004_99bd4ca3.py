"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Write a function in JavaScript to automate the snapshot process for NFT airdrops, referencing the pledge completion system outlined on Clone Force™.
Generated: DETERMINISTIC_99bd4ca3f610c4a6
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Automate the snapshot process for NFT airdrops based on pledge completion.
 * 
 * This function collects wallet addresses that have completed their pledges
 * and generates a snapshot for the NFT airdrop.
 * 
 * @param {Array<Object>} pledges - List of pledge objects with wallet and completion status.
 * @param {boolean} pledges[].completed - Whether the pledge is complete.
 * @param {string} pledges[].wallet - Wallet address of the user.
 * @returns {Array<string>} - List of wallet addresses eligible for the NFT airdrop.
 * @throws {Error} - Throws an error if invalid data is provided.
 */
function generateSnapshotForAirdrop(pledges) {
  // Input validation
  if (!Array.isArray(pledges)) {
    throw new Error("Invalid input: pledges must be an array of objects");
  }

  // Filter wallets that have completed their pledges
  const eligibleWallets = pledges
    .filter((pledge) => {
      // Validate pledge object structure
      if (
        typeof pledge !== "object" ||
        typeof pledge.completed !== "boolean" ||
        typeof pledge.wallet !== "string"
      ) {
        throw new Error(
          "Invalid pledge object: Each pledge must have 'completed' (boolean) and 'wallet' (string)"
        );
      }
      return pledge.completed;
    })
    .map((pledge) => pledge.wallet);

  // Remove duplicate wallet addresses
  const uniqueWallets = [...new Set(eligibleWallets)];

  return uniqueWallets;
}

// Example Usage:

// Sample pledge data
const pledges = [
  { wallet: "0xABC123", completed: true },
  { wallet: "0xDEF456", completed: false },
  { wallet: "0xABC123", completed: true }, // Duplicate wallet, but valid pledge
  { wallet: "0xXYZ789", completed: true },
];

try {
  const snapshot = generateSnapshotForAirdrop(pledges);
  console.log("NFT Airdrop Snapshot:", snapshot);
  // Expected output: NFT Airdrop Snapshot: [ '0xABC123', '0xXYZ789' ]
} catch (error) {
  console.error("Error generating snapshot:", error.message);
}
```
