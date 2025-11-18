"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethhix.com
Prompt: Provide an example of a decentralized application (dApp) that allows users to create and manage ETH pledges using Web3.js.
Generated: DETERMINISTIC_bff39e6dec2a521c
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

pragma experimental ABIEncoderV2;

// Smart contract for managing ETH pledges
contract PledgeManager {
    struct Pledge {
        address payable pledger; // The address of the user pledging ETH
        uint256 amount;          // The amount pledged in wei
        bool fulfilled;         // Status of the pledge
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount; // Counter for the pledges

    // Event emitted when a new pledge is created
    event PledgeCreated(uint256 pledgeId, address indexed pledger, uint256 amount);
    // Event emitted when a pledge is fulfilled
    event PledgeFulfilled(uint256 pledgeId);

    // Function to create a new pledge
    function createPledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Increment pledge count and create a new pledge
        pledgeCount++;
        pledges[pledgeCount] = Pledge(payable(msg.sender), msg.value, false);

        emit PledgeCreated(pledgeCount, msg.sender, msg.value);
    }

    // Function to fulfill a pledge and withdraw the amount
    function fulfillPledge(uint256 _pledgeID) external {
        Pledge storage pledge = pledges[_pledgeID];
        require(pledge.pledger == msg.sender, "Only the pledger can fulfill this pledge");
        require(!pledge.fulfilled, "Pledge has already been fulfilled");

        // Mark pledge as fulfilled
        pledge.fulfilled = true;

        // Transfer the funds to the pledger
        pledge.pledger.transfer(pledge.amount);

        emit PledgeFulfilled(_pledgeID);
    }
}
```

```javascript
// Importing required libraries
import Web3 from 'web3';
import pledgeManagerABI from './PledgeManagerABI.json'; // ABI of the smart contract

// Initialize Web3 and the contract
const web3 = new Web3(window.ethereum);
const contractAddress = 'YOUR_CONTRACT_ADDRESS'; // Replace with your contract address
const pledgeManagerContract = new web3.eth.Contract(pledgeManagerABI, contractAddress);

// Function to create a pledge
async function createPledge(amount) {
    if (amount <= 0) {
        console.error("Amount should be greater than zero");
        return;
    }

    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        const accounts = await web3.eth.getAccounts();
        await pledgeManagerContract.methods.createPledge().send({ from: accounts[0], value: web3.utils.toWei(amount.toString(), 'ether') });

        console.log("Pledge created successfully!");
    } catch (error) {
        console.error("Error creating pledge: ", error);
    }
}

// Function to fulfill a pledge
async function fulfillPledge(pledgeID) {
    try {
        const accounts = await web3.eth.getAccounts();
        await pledgeManagerContract.methods.fulfillPledge(pledgeID).send({ from: accounts[0] });

        console.log("Pledge fulfilled successfully!");
    } catch (error) {
        console.error("Error fulfilling pledge: ", error);
    }
}

// Example usage
// createPledge(0.1); // Call this function to create a pledge of 0.1 ETH
// fulfillPledge(1); // Call this function to fulfill the pledge with ID 1
```

Ensure to replace `'YOUR_CONTRACT_ADDRESS'` with the actual deployed contract address when using the JavaScript code.
