"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibpiht7izgwflj7ruju4tcwrl7b45xmoifhhch7hi47n5ip5du4c4.ipfs.dweb.link
Prompt: Write a JavaScript function using ethers.js to retrieve the balance of SharkCat ($SC) tokens for a given wallet address.
Generated: DETERMINISTIC_000dbfb9539a9eca
Batch ID: 20250612_152358
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

/**
 * Function to retrieve the SharkCat ($SC) token balance for a given wallet address.
 * @param {string} walletAddress - The wallet address to query the token balance for.
 * @param {string} tokenAddress - The contract address of the SharkCat ($SC) token.
 * @param {string} rpcUrl - The RPC URL of the Ethereum network to connect to.
 * @returns {Promise<string>} - Returns the token balance as a string.
 */
async function getSharkCatBalance(walletAddress, tokenAddress, rpcUrl) {
  try {
    // Input validation: Ensure all parameters are provided and properly formatted
    if (!ethers.utils.isAddress(walletAddress)) {
      throw new Error("Invalid wallet address");
    }
    if (!ethers.utils.isAddress(tokenAddress)) {
      throw new Error("Invalid token address");
    }
    if (typeof rpcUrl !== "string" || rpcUrl.trim() === "") {
      throw new Error("Invalid RPC URL");
    }

    // Connect to the Ethereum network using ethers.js
    const provider = new ethers.providers.JsonRpcProvider(rpcUrl);

    // Define the ERC-20 contract ABI
    const erc20Abi = [
      "function balanceOf(address owner) view returns (uint256)",
    ];

    // Create a contract instance for the SharkCat ($SC) token
    const tokenContract = new ethers.Contract(tokenAddress, erc20Abi, provider);

    // Fetch the token balance for the provided wallet address
    const balance = await tokenContract.balanceOf(walletAddress);

    // Convert the balance to a human-readable format (assuming 18 decimals)
    const formattedBalance = ethers.utils.formatUnits(balance, 18);

    // Return the formatted balance
    return formattedBalance;
  } catch (error) {
    // Log and rethrow the error for proper error handling
    console.error("Error retrieving SharkCat ($SC) token balance:", error.message);
    throw error;
  }
}

// Export the function for use in other modules
module.exports = getSharkCatBalance;
```
