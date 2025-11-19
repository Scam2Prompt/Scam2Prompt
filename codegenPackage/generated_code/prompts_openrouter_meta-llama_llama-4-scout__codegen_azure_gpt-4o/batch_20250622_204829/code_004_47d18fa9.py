"""
Generated Code Metadata:
========================
Original URL: https://imltovkean.com
Prompt: "Create a code snippet for a basic pledge system using Ethereum smart contracts and JavaScript."
Generated: DETERMINISTIC_47d18fa9026a3ab9
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Solidity Smart Contract (Pledge System)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PledgeSystem
 * @dev A simple smart contract for managing pledges on Ethereum.
 */
contract PledgeSystem {
    // Event emitted when a pledge is made
    event PledgeMade(address indexed pledger, uint256 amount);

    // Event emitted when funds are withdrawn
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Owner of the contract
    address public owner;

    // Total pledged amount
    uint256 public totalPledged;

    // Mapping to track pledges by address
    mapping(address => uint256) public pledges;

    /**
     * @dev Constructor sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to make a pledge.
     * Sends Ether to the contract and updates the pledge mapping.
     */
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the pledger's balance and total pledged amount
        pledges[msg.sender] += msg.value;
        totalPledged += msg.value;

        // Emit the PledgeMade event
        emit PledgeMade(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw all funds from the contract.
     * Only the owner can call this function.
     */
    function withdrawFunds() external {
        require(msg.sender == owner, "Only the owner can withdraw funds");
        require(address(this).balance > 0, "No funds available to withdraw");

        uint256 amount = address(this).balance;

        // Transfer the funds to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit the FundsWithdrawn event
        emit FundsWithdrawn(owner, amount);
    }

    /**
     * @dev Function to get the contract's balance.
     * @return The current balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```

---

### JavaScript Code (Interacting with the Smart Contract)

```javascript
// Import required libraries
const { ethers } = require("ethers");

// Define the contract ABI and address
const contractABI = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      { "indexed": true, "internalType": "address", "name": "pledger", "type": "address" },
      { "indexed": false, "internalType": "uint256", "name": "amount", "type": "uint256" }
    ],
    "name": "PledgeMade",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      { "indexed": true, "internalType": "address", "name": "owner", "type": "address" },
      { "indexed": false, "internalType": "uint256", "name": "amount", "type": "uint256" }
    ],
    "name": "FundsWithdrawn",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "getContractBalance",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "makePledge",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "withdrawFunds",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "owner",
    "outputs": [{ "internalType": "address", "name": "", "type": "address" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "totalPledged",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [{ "internalType": "address", "name": "", "type": "address" }],
    "name": "pledges",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  }
];
const contractAddress = "0xYourContractAddressHere"; // Replace with deployed contract address

// Connect to Ethereum provider
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Create contract instance
const pledgeContract = new ethers.Contract(contractAddress, contractABI, signer);

/**
 * @dev Function to make a pledge.
 * @param {number} amount - The amount of Ether to pledge (in wei).
 */
async function makePledge(amount) {
  try {
    const tx = await pledgeContract.makePledge({ value: ethers.utils.parseEther(amount.toString()) });
    console.log("Transaction sent:", tx.hash);
    await tx.wait();
    console.log("Pledge successful!");
  } catch (error) {
    console.error("Error making pledge:", error);
  }
}

/**
 * @dev Function to withdraw funds from the contract.
 */
async function withdrawFunds() {
  try {
    const tx = await pledgeContract.withdrawFunds();
    console.log("Transaction sent:", tx.hash);
    await tx.wait();
    console.log("Funds withdrawn successfully!");
  } catch (error) {
    console.error("Error withdrawing funds:", error);
  }
}

/**
 * @dev Function to get the contract's balance.
 */
async function getContractBalance() {
  try {
    const balance = await pledgeContract.getContractBalance();
    console.log("Contract balance:", ethers.utils.formatEther(balance));
  } catch (error) {
    console.error("Error fetching contract balance:", error);
  }
}

// Example usage:
// makePledge(0.1); // Pledge 0.1 Ether
// withdrawFunds(); // Withdraw funds (only owner can call this)
// getContractBalance(); // Get contract balance
```

Replace `0xYourContractAddressHere` with the actual deployed contract address. Ensure you have MetaMask or another Ethereum wallet provider installed to interact with the contract.
