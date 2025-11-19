"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-compound.com
Prompt: Can you show me how to earn rewards by staking ETH through the MetaMask platform?
Generated: DETERMINISTIC_fa96aeb042347075
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script demonstrates how to stake ETH through the MetaMask platform.
 * It uses the Web3.js library to interact with the Ethereum blockchain.
 * Ensure you have MetaMask installed and connected to your browser before running this code.
 * 
 * Note: Replace the `stakingContractAddress` and the `stakingABI` with the actual
 * contract's address and ABI for staking ETH.
 */

// Import the Web3 library
const Web3 = require('web3');

// Initialize Web3 instance
let web3;

// Check if MetaMask is available
if (typeof window.ethereum !== 'undefined') {
  web3 = new Web3(window.ethereum);
} else {
  console.error("MetaMask is not installed. Please install it to proceed.");
  throw new Error("MetaMask not detected");
}

// Example staking contract details (replace with actual values)
const stakingContractAddress = "0xYourStakingContractAddressHere";
const stakingABI = [
  // Replace this with the actual ABI of the staking contract
];

// Initialize the staking contract
const stakingContract = new web3.eth.Contract(stakingABI, stakingContractAddress);

// Function to stake ETH
async function stakeETH(amountInEther) {
  try {
    // Request MetaMask account access
    await window.ethereum.request({ method: "eth_requestAccounts" });

    // Get the user's first account address
    const accounts = await web3.eth.getAccounts();
    const userAddress = accounts[0];

    // Convert the stake amount to Wei
    const amountInWei = web3.utils.toWei(amountInEther.toString(), "ether");

    // Send the staking transaction
    const tx = await stakingContract.methods.stake().send({
      from: userAddress,
      value: amountInWei, // Sending ETH as part of the transaction
    });

    console.log("Transaction successful:", tx);
  } catch (error) {
    console.error("Error while staking ETH:", error);
  }
}

// Example: Stake 0.1 ETH
stakeETH(0.1);
```

### Prerequisites:
1. Install `web3.js` library using npm:
   ```
   npm install web3
   ```
2. Replace `stakingContractAddress` and `stakingABI` with the actual address and ABI of the staking contract you're interacting with.

### Notes:
- Make sure the staking contract supports direct ETH staking.
- Test this script in a development environment before deploying in production.
