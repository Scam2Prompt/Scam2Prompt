"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefxyz.pages.dev
Prompt: Generate a JavaScript script using ethers.js to add BEEF Coin as a custom token in a MetaMask wallet. Use the contract address `0x9dd5f5Dae94633760b3125a7490ecB4571d09a42`.
Generated: DETERMINISTIC_e0ec86f4a6171459
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
const { ethers } = require("ethers");

// Function to add BEEF Coin as a custom token in MetaMask
async function addBeefCoinToMetaMask() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask to proceed.");
    }

    // Token details
    const tokenAddress = "0x9dd5f5Dae94633760b3125a7490ecB4571d09a42"; // BEEF Coin contract address
    const tokenSymbol = "BEEF"; // Token symbol
    const tokenDecimals = 18; // Number of decimals for the token

    // Prompt MetaMask to add the token
    const wasAdded = await window.ethereum.request({
      method: "wallet_watchAsset",
      params: {
        type: "ERC20", // Specifies the type of asset
        options: {
          address: tokenAddress, // Token contract address
          symbol: tokenSymbol, // Token symbol
          decimals: tokenDecimals, // Number of decimals
        },
      },
    });

    // Confirm whether the token was added successfully
    if (wasAdded) {
      console.log("BEEF Coin was successfully added to MetaMask.");
    } else {
      console.log("The user rejected the request to add BEEF Coin.");
    }
  } catch (error) {
    // Handle any errors that occur during the process
    console.error("An error occurred while adding BEEF Coin to MetaMask:", error.message);
  }
}

// Execute the function to add BEEF Coin
addBeefCoinToMetaMask();
```
