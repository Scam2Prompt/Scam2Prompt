"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-phantomwallet.us
Prompt: Create a script to filter and hide spam NFTs in Phantom Wallet using its blocklist functionality. Include a method to view blocked items if needed.
Generated: DETERMINISTIC_16e22d8c7453dec0
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Phantom Wallet Spam NFT Filter Script
// This script filters spam NFTs in Phantom Wallet using its blocklist functionality
// and provides a method to view blocked items.

const phantom = window.solana; // Ensure Phantom Wallet is connected and accessible

// Function to block spam NFTs by adding them to the blocklist
async function blockSpamNFTs(nftAddresses) {
  if (!phantom || !phantom.isConnected) {
    console.error("Phantom Wallet not connected or unavailable.");
    return;
  }

  try {
    const blocklist = phantom.getBlocklist();

    // Add provided NFT addresses to the blocklist
    nftAddresses.forEach((address) => {
      blocklist.add(address);
    });

    console.log("Spam NFTs successfully blocked.");
  } catch (error) {
    console.error("Error blocking spam NFTs:", error.message);
  }
}

// Function to view currently blocked items
function viewBlockedItems() {
  if (!phantom || !phantom.isConnected) {
    console.error("Phantom Wallet not connected or unavailable.");
    return;
  }

  try {
    const blocklist = phantom.getBlocklist();
    const blockedItems = blocklist.getAll();

    console.log("Blocked items:", blockedItems);
    return blockedItems;
  } catch (error) {
    console.error("Error fetching blocked items:", error.message);
  }
}

// Example usage
(async function run() {
  const spamNFTs = [
    "ExampleNFTAddress1",
    "ExampleNFTAddress2",
    "ExampleNFTAddress3",
  ]; // Replace with actual spam NFT addresses

  // Block spam NFTs
  await blockSpamNFTs(spamNFTs);

  // View blocked items
  const blockedItems = viewBlockedItems();
  console.log("Currently blocked NFTs:", blockedItems);
})();
```

> Note: This script assumes Phantom Wallet provides a JavaScript API with `getBlocklist`, `add`, and `getAll` methods. Replace the relevant parts with the actual Phantom Wallet SDK/API if necessary. Ensure proper permissions and user interaction for wallet access.
