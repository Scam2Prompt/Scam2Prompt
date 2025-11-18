"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Write a script using ethers.js to connect a user's wallet to the DOGE20 staking contract and display their stakeable balance.
Generated: DETERMINISTIC_980c9c1c0415114f
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required Dependencies:
// Install ethers.js with: npm install ethers

// Import ethers.js library
const { ethers } = require("ethers");

// Define the staking contract ABI
const stakingContractABI = [
  // Replace this array with the actual ABI of the DOGE20 staking contract
  {
    "constant": true,
    "inputs": [],
    "name": "stakeableBalance",
    "outputs": [{ "name": "", "type": "uint256" }],
    "type": "function"
  }
];

// Define the staking contract address
const stakingContractAddress = "0xYourStakingContractAddressHere"; // Replace with the actual contract address

// Main function to connect wallet and fetch stakeable balance
async function connectWalletAndFetchBalance() {
  try {
    // Check if the browser has an Ethereum provider (e.g., MetaMask)
    if (!window.ethereum) {
      throw new Error("No Ethereum provider found. Please install MetaMask.");
    }

    // Request wallet connection
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    await provider.send("eth_requestAccounts", []); // Prompt user to connect wallet

    // Get the signer (user's wallet)
    const signer = provider.getSigner();
    const userAddress = await signer.getAddress();
    console.log(`Connected wallet address: ${userAddress}`);

    // Connect to the staking contract
    const stakingContract = new ethers.Contract(stakingContractAddress, stakingContractABI, signer);

    // Fetch the user's stakeable balance
    const stakeableBalance = await stakingContract.stakeableBalance();
    console.log(`Stakeable Balance: ${ethers.utils.formatEther(stakeableBalance)} DOGE20`);
  } catch (error) {
    // Handle errors gracefully
    console.error("Error:", error.message || error);
  }
}

// Run the main function
connectWalletAndFetchBalance();
```

Make sure to replace the `stakingContractAddress` and `stakingContractABI` with the actual data from your DOGE20 staking contract.
