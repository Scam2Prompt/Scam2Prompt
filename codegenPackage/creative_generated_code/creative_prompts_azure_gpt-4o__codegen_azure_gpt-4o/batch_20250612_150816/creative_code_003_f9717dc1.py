"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonemv.com
Prompt: Create a JavaScript function using ethers.js or web3.js to connect a wallet and verify eligibility for claiming rewards, similar to the REWARD Portal v2 process.
Generated: DETERMINISTIC_f9717dc196bc71be
Batch ID: 20250612_150816
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
 * Connects to a user's wallet and verifies eligibility for claiming rewards.
 * @param {string} contractAddress - The smart contract address for rewards.
 * @param {Array} eligibleAddresses - An array of addresses eligible for rewards.
 * @returns {Promise<{connected: boolean, eligible: boolean, address: string}>}
 */
async function connectWalletAndCheckEligibility(contractAddress, eligibleAddresses) {
  try {
    // Ensure the browser has an Ethereum provider (e.g., MetaMask)
    if (!window.ethereum) {
      throw new Error("No Ethereum provider detected. Please install MetaMask.");
    }

    // Request account access
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    await provider.send("eth_requestAccounts", []);
    const signer = provider.getSigner();

    // Get the connected wallet's address
    const walletAddress = await signer.getAddress();

    // Verify that the smart contract exists
    const contract = new ethers.Contract(
      contractAddress,
      [
        // Example ABI for a function `isEligible(address)`
        "function isEligible(address) view returns (bool)"
      ],
      signer
    );

    // Check eligibility using the contract
    const eligibleOnContract = await contract.isEligible(walletAddress);

    // Check eligibility in the provided list
    const eligibleInList = eligibleAddresses.includes(walletAddress);

    return {
      connected: true,
      eligible: eligibleOnContract && eligibleInList,
      address: walletAddress,
    };
  } catch (error) {
    console.error("Error connecting wallet or verifying eligibility:", error.message);

    return {
      connected: false,
      eligible: false,
      address: null,
    };
  }
}

// Example usage:
// const contractAddress = "0xYourSmartContractAddressHere";
// const eligibleAddresses = ["0xAddress1", "0xAddress2"];
// connectWalletAndCheckEligibility(contractAddress, eligibleAddresses)
//   .then(console.log)
//   .catch(console.error);
```
