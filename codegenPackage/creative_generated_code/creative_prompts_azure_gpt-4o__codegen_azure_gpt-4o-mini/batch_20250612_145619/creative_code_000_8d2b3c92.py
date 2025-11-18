"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethzao.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledging system, ensuring compatibility with mobile devices and requiring JavaScript for user interaction.
Generated: DETERMINISTIC_8d2b3c9290395608
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PledgeSystem {
    struct Pledge {
        address pledger;
        uint256 amount;
        bool fulfilled;
    }

    // Mapping to store pledges by their ID
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount;

    // Events to log pledge actions
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    event PledgeFulfilled(uint256 indexed pledgeId);
    event PledgeWithdrawn(uint256 indexed pledgeId, address indexed pledger, uint256 amount);

    // Function to create a new pledge
    function createPledge() external payable {
        require(msg.value > 0, "You must pledge a positive amount");

        pledgeCount++;
        pledges[pledgeCount] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            fulfilled: false
        });

        emit PledgeCreated(pledgeCount, msg.sender, msg.value);
    }

    // Function to fulfill a pledge
    function fulfillPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.pledger != address(0), "Pledge does not exist");
        require(!pledge.fulfilled, "Pledge already fulfilled");
        require(msg.sender == pledge.pledger, "Only the pledger can fulfill the pledge");

        pledge.fulfilled = true;
        emit PledgeFulfilled(_pledgeId);
    }

    // Function to withdraw a fulfilled pledge
    function withdrawPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.pledger != address(0), "Pledge does not exist");
        require(pledge.fulfilled, "Pledge must be fulfilled before withdrawal");
        require(msg.sender == pledge.pledger, "Only the pledger can withdraw the pledge");

        uint256 amount = pledge.amount;
        pledge.amount = 0; // Prevent re-entrancy
        payable(msg.sender).transfer(amount);

        emit PledgeWithdrawn(_pledgeId, msg.sender, amount);
    }
}
```

```javascript
// JavaScript for interacting with the PledgeSystem smart contract

const Web3 = require('web3');
const contractABI = [/* ABI from compiled contract */];
const contractAddress = 'YOUR_CONTRACT_ADDRESS';

const web3 = new Web3(window.ethereum);
let contract;

// Function to connect to MetaMask
async function connect() {
    if (window.ethereum) {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        contract = new web3.eth.Contract(contractABI, contractAddress);
        console.log('Connected to the PledgeSystem contract');
    } else {
        alert('Please install MetaMask!');
    }
}

// Function to create a pledge
async function createPledge(amount) {
    const accounts = await web3.eth.getAccounts();
    try {
        await contract.methods.createPledge().send({ from: accounts[0], value: web3.utils.toWei(amount, 'ether') });
        alert('Pledge created successfully!');
    } catch (error) {
        console.error('Error creating pledge:', error);
    }
}

// Function to fulfill a pledge
async function fulfillPledge(pledgeId) {
    const accounts = await web3.eth.getAccounts();
    try {
        await contract.methods.fulfillPledge(pledgeId).send({ from: accounts[0] });
        alert('Pledge fulfilled successfully!');
    } catch (error) {
        console.error('Error fulfilling pledge:', error);
    }
}

// Function to withdraw a fulfilled pledge
async function withdrawPledge(pledgeId) {
    const accounts = await web3.eth.getAccounts();
    try {
        await contract.methods.withdrawPledge(pledgeId).send({ from: accounts[0] });
        alert('Pledge withdrawn successfully!');
    } catch (error) {
        console.error('Error withdrawing pledge:', error);
    }
}
```

This code provides a smart contract for a pledging system using Solidity and a JavaScript interface for interacting with Metamask on mobile devices. Ensure the contract address and ABI are properly set for deployment and interaction.
