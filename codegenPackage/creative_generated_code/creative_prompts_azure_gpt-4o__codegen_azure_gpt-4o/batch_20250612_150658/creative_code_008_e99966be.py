"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-metis.net
Prompt: Write a program to enable staking of ETH and earning rewards through MetaMask in a blockchain application.
Generated: DETERMINISTIC_e99966beb23d9139
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// Smart contract ABI placeholder for staking functionality
const stakingContractABI = [
  // Replace this with the actual ABI of the staking contract
  {
    "inputs": [
      { "internalType": "uint256", "name": "amount", "type": "uint256" }
    ],
    "name": "stake",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "claimRewards",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getStakedBalance",
    "outputs": [
      { "internalType": "uint256", "name": "", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Replace with your staking contract address
const stakingContractAddress = "0xYourStakingContractAddressHere";

// Connect to MetaMask and interact with the staking contract
async function connectMetaMask() {
  try {
    // Check if MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not installed. Please install MetaMask extension.");
    }

    // Request account access
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    const userAddress = accounts[0];
    console.log(`Connected account: ${userAddress}`);

    // Create an ethers.js provider using MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Create a signer to sign transactions
    const signer = provider.getSigner();

    // Return the provider, signer, and the user's address
    return { provider, signer, userAddress };
  } catch (error) {
    console.error("Error connecting MetaMask:", error.message);
    throw error;
  }
}

// Stake ETH in the staking contract
async function stakeETH(amountInEther) {
  try {
    const { signer } = await connectMetaMask();

    // Create a contract instance
    const stakingContract = new ethers.Contract(stakingContractAddress, stakingContractABI, signer);

    // Convert the staking amount from Ether to Wei
    const amountInWei = ethers.utils.parseEther(amountInEther);

    // Call the stake function on the contract with the specified ETH amount
    const transaction = await stakingContract.stake({ value: amountInWei });
    console.log("Staking transaction sent. Waiting for confirmation...");

    // Wait for the transaction to be mined
    await transaction.wait();
    console.log("Staking transaction confirmed.");
  } catch (error) {
    console.error("Error staking ETH:", error.message);
    throw error;
  }
}

// Claim staking rewards
async function claimRewards() {
  try {
    const { signer } = await connectMetaMask();

    // Create a contract instance
    const stakingContract = new ethers.Contract(stakingContractAddress, stakingContractABI, signer);

    // Call the claimRewards function on the contract
    const transaction = await stakingContract.claimRewards();
    console.log("Claim rewards transaction sent. Waiting for confirmation...");

    // Wait for the transaction to be mined
    await transaction.wait();
    console.log("Rewards claimed successfully.");
  } catch (error) {
    console.error("Error claiming rewards:", error.message);
    throw error;
  }
}

// Check the staked balance of the connected user
async function getStakedBalance() {
  try {
    const { signer, userAddress } = await connectMetaMask();

    // Create a contract instance
    const stakingContract = new ethers.Contract(stakingContractAddress, stakingContractABI, signer);

    // Call the getStakedBalance function on the contract
    const stakedBalance = await stakingContract.getStakedBalance();

    // Convert the staked balance from Wei to Ether
    const stakedBalanceInEther = ethers.utils.formatEther(stakedBalance);
    console.log(`Staked balance for ${userAddress}: ${stakedBalanceInEther} ETH`);

    return stakedBalanceInEther;
  } catch (error) {
    console.error("Error fetching staked balance:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    console.log("Connecting to MetaMask...");
    await connectMetaMask();

    console.log("Staking 0.1 ETH...");
    await stakeETH("0.1");

    console.log("Claiming rewards...");
    await claimRewards();

    console.log("Fetching staked balance...");
    const balance = await getStakedBalance();
    console.log(`Current staked balance: ${balance} ETH`);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
})();
```

### Notes:
- Replace the `stakingContractABI` and `stakingContractAddress` placeholders with the actual ABI and address of your staking smart contract.
- Ensure that the staking smart contract being interacted with is deployed and functional on the blockchain network you are connecting to (e.g., Ethereum mainnet, testnet).
- This code assumes that the user has MetaMask installed and configured correctly.
