"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-icu.pages.dev
Prompt: Create a JavaScript function using Ethers.js to connect a Coinbase Wallet, validate the wallet, and initiate a DOGE20 token purchase transaction.
Generated: DETERMINISTIC_52b9b83c86ec5d1f
Batch ID: 20250612_152710
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

// Function to connect Coinbase Wallet, validate wallet, and initiate DOGE20 token purchase
async function purchaseDoge20Token(walletProviderUrl, contractAddress, contractAbi, recipientAddress, tokenAmount) {
  try {
    // Step 1: Create a provider using the wallet's provider URL
    const provider = new ethers.providers.JsonRpcProvider(walletProviderUrl);

    // Step 2: Request the user's wallet connection
    const signer = provider.getSigner();

    // Step 3: Get the user's wallet address
    const walletAddress = await signer.getAddress();
    console.log("Connected Wallet Address:", walletAddress);

    // Step 4: Validate the wallet address
    if (!ethers.utils.isAddress(walletAddress)) {
      throw new Error("Invalid wallet address detected.");
    }

    // Step 5: Connect to the DOGE20 token smart contract
    const doge20Contract = new ethers.Contract(contractAddress, contractAbi, signer);

    // Step 6: Validate recipient address
    if (!ethers.utils.isAddress(recipientAddress)) {
      throw new Error("Invalid recipient address detected.");
    }

    // Step 7: Define transaction details and execute token purchase
    console.log(`Initiating purchase of ${tokenAmount} DOGE20 tokens for recipient: ${recipientAddress}`);
    const transactionResponse = await doge20Contract.transfer(recipientAddress, ethers.utils.parseUnits(tokenAmount.toString(), 18));

    // Step 8: Wait for the transaction confirmation
    const receipt = await transactionResponse.wait();
    console.log("Transaction Successful! Receipt:", receipt);

    return receipt;
  } catch (error) {
    console.error("Error during token purchase:", error.message);
    throw error;
  }
}

module.exports = { purchaseDoge20Token };
```

**Prerequisites:**
1. `walletProviderUrl` should point to the Coinbase Wallet's supported RPC endpoint.
2. `contractAddress` and `contractAbi` must be the deployed DOGE20 token contract's address and ABI.
3. `ethers` library must be installed (`npm install ethers`) before utilizing this function.
