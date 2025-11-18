"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guildguarded.netlify.app
Prompt: Provide an example of how to set a custom spending cap for token transactions using MetaMask, as described in the GuildGuard wallet connection process.
Generated: DETERMINISTIC_cc3d79faa5f09315
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
// Ensure you have installed ethers.js via npm (npm install ethers)
const { ethers } = require("ethers");

// Function to set a custom spending cap for token transactions using MetaMask
async function setTokenSpendingCap(tokenAddress, spenderAddress, customSpendingCap) {
  try {
    // Ensure MetaMask is installed and available
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed or unavailable.");
    }

    // Request the user to connect their MetaMask wallet
    await window.ethereum.request({ method: "eth_requestAccounts" });

    // Create a web3 provider using MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer (the connected wallet)
    const signer = provider.getSigner();

    // ABI for the ERC20 token (only the necessary portion for `approve` function)
    const erc20Abi = [
      "function approve(address spender, uint256 amount) public returns (bool)"
    ];

    // Create a contract instance for the token
    const tokenContract = new ethers.Contract(tokenAddress, erc20Abi, signer);

    // Convert customSpendingCap to the correct format (BigNumber)
    const spendingCap = ethers.utils.parseUnits(customSpendingCap.toString(), 18);

    // Call the `approve` function on the token contract
    const tx = await tokenContract.approve(spenderAddress, spendingCap);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();

    // Log the transaction receipt
    console.log("Transaction successful!", receipt);
    return receipt;
  } catch (error) {
    // Handle errors and display meaningful feedback
    console.error("Error while setting spending cap:", error.message);
    throw error;
  }
}

// Example usage
// Replace with actual token address, spender address, and desired spending cap
const tokenAddress = "0xYourTokenAddressHere";
const spenderAddress = "0xSpenderAddressHere";
const customSpendingCap = "1000"; // Example cap: 1000 tokens

setTokenSpendingCap(tokenAddress, spenderAddress, customSpendingCap)
  .then(receipt => {
    console.log("Spending cap set successfully:", receipt);
  })
  .catch(error => {
    console.error("Failed to set spending cap:", error);
  });
```
