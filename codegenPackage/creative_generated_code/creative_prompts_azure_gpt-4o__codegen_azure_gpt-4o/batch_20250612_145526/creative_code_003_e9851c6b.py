"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Create a JavaScript function using ethers.js to connect a wallet and retrieve the user's $EMT token balance from the EarthMeta platform.
Generated: DETERMINISTIC_e9851c6b92396f45
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js
const { ethers } = require("ethers");

/**
 * Connects to a user's wallet and retrieves their $EMT token balance.
 * @async
 * @param {string} tokenContractAddress - The contract address of the $EMT token.
 * @param {string} rpcProviderUrl - The RPC URL of the Ethereum network (e.g., Infura or Alchemy).
 * @returns {Promise<string>} - The $EMT token balance of the connected wallet.
 * @throws {Error} Throws an error if wallet connection or balance retrieval fails.
 */
async function getEMTTokenBalance(tokenContractAddress, rpcProviderUrl) {
  try {
    // Ensure ethers.js is properly imported
    if (!ethers) {
      throw new Error("Ethers.js library not found.");
    }

    // Request wallet connection from the user
    if (!window.ethereum) {
      throw new Error("MetaMask or wallet provider not detected.");
    }

    await window.ethereum.request({ method: "eth_requestAccounts" });

    // Initialize the Ethereum provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer (connected wallet)
    const signer = provider.getSigner();

    // Retrieve the user's wallet address
    const walletAddress = await signer.getAddress();

    // Connect to the $EMT token contract
    const tokenAbi = [
      // ERC-20 ABI fragment: balanceOf function
      "function balanceOf(address account) view returns (uint256)",
    ];
    const tokenContract = new ethers.Contract(
      tokenContractAddress,
      tokenAbi,
      provider
    );

    // Fetch the token balance for the connected wallet
    const rawBalance = await tokenContract.balanceOf(walletAddress);

    // Format the balance from Wei to Ether (assuming $EMT has 18 decimals)
    const formattedBalance = ethers.utils.formatUnits(rawBalance, 18);

    return formattedBalance;
  } catch (error) {
    console.error("Failed to retrieve $EMT token balance:", error.message);
    throw error;
  }
}

// Export the function for external usage
module.exports = getEMTTokenBalance;
```
