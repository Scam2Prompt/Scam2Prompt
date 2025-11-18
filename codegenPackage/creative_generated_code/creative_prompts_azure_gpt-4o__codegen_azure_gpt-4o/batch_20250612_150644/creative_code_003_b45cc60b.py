"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-compound.com
Prompt: Create a script to enable staking of ETH via MetaMask, allowing users to earn rewards and secure the network.
Generated: DETERMINISTIC_b45cc60b370df9fb
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";

// Initialize constants
const stakingContractAddress = "0xYourStakingContractAddress"; // Replace this with the actual staking contract address
const stakingContractABI = [
  // Replace with the actual ABI of your staking contract
  {
    "inputs": [
      { "internalType": "uint256", "name": "amount", "type": "uint256" }
    ],
    "name": "stake",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  }
];

// Connect to MetaMask wallet
async function connectMetaMask() {
  if (!window.ethereum) {
    alert("MetaMask is not installed. Please install MetaMask and try again.");
    return null;
  }

  try {
    await window.ethereum.request({ method: "eth_requestAccounts" });
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    return signer;
  } catch (error) {
    console.error("Failed to connect MetaMask:", error);
    alert("Error connecting to MetaMask. Please try again.");
    return null;
  }
}

// Stake ETH via the staking smart contract
async function stakeETH(amountInEther) {
  const signer = await connectMetaMask();
  if (!signer) return;

  try {
    // Instantiate the staking contract
    const stakingContract = new ethers.Contract(
      stakingContractAddress,
      stakingContractABI,
      signer
    );

    // Convert the amount to Wei (smallest unit of ETH)
    const amountInWei = ethers.utils.parseEther(amountInEther);

    // Call the `stake` function on the contract
    const tx = await stakingContract.stake(amountInWei, {
      value: amountInWei, // Send ETH along with the transaction
    });

    console.log("Transaction initiated. Waiting for confirmation...");
    await tx.wait(); // Wait for the transaction to be mined
    console.log("Transaction confirmed:", tx);

    alert("ETH staked successfully!");
  } catch (error) {
    console.error("Failed to stake ETH:", error);
    alert("Error staking ETH. Please check the console for details.");
  }
}

// UI Interaction - Example button to stake ETH
document.getElementById("stakeButton").addEventListener("click", async () => {
  const amount = document.getElementById("stakeAmount").value;
  if (amount && parseFloat(amount) > 0) {
    await stakeETH(amount);
  } else {
    alert("Please enter a valid amount of ETH to stake.");
  }
});

// HTML Elements (for demonstration purposes)
// Ensure you have corresponding HTML elements with these IDs in your front-end
// Example: <input id="stakeAmount" type="text" placeholder="Enter amount of ETH">
// Example: <button id="stakeButton">Stake ETH</button>
```
