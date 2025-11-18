"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethpai.com
Prompt: Write a tutorial-style explanation with code examples for deploying and interacting with an ETH pledge smart contract on the Ethereum testnet.
Generated: DETERMINISTIC_73627bcc28322127
Batch ID: 20250612_150234
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ETH Pledge Contract
 * @dev A simple contract allowing users to pledge ETH and later withdraw it.
 */
contract ETHPledge {
    // Mapping to track the amount pledged by each address
    mapping(address => uint256) public pledges;

    /**
     * @dev Event emitted when a pledge is made.
     * @param pledger Address of the user who made the pledge
     * @param amount Amount of ETH pledged
     */
    event Pledged(address indexed pledger, uint256 amount);

    /**
     * @dev Event emitted when a withdrawal is made.
     * @param receiver Address of the user who withdrew funds
     * @param amount Amount of ETH withdrawn
     */
    event Withdrawn(address indexed receiver, uint256 amount);

    /**
     * @dev Allows users to pledge ETH to the contract.
     * Emits a `Pledged` event on success.
     */
    function pledge() external payable {
        // Ensure a positive amount of ETH is pledged
        require(msg.value > 0, "You must send a positive amount of ETH.");

        // Update the pledge balance for the sender
        pledges[msg.sender] += msg.value;

        // Emit a Pledged event
        emit Pledged(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their pledged ETH from the contract.
     * Emits a `Withdrawn` event on success.
     */
    function withdraw() external {
        // Fetch the pledged amount for the sender
        uint256 amount = pledges[msg.sender];

        // Ensure the sender has pledged ETH to withdraw
        require(amount > 0, "You have no pledged ETH to withdraw.");

        // Reset the sender's pledge balance
        pledges[msg.sender] = 0;

        // Transfer the ETH back to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed.");

        // Emit a Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }
}
```

### Deployment and Interaction Script (JavaScript/Node.js)
```javascript
// Import necessary modules
const { ethers } = require("ethers");
const fs = require("fs");

// Load the compiled contract ABI and bytecode
const contractABI = JSON.parse(fs.readFileSync("./ETHPledgeABI.json", "utf-8"));
const contractBytecode = fs.readFileSync("./ETHPledgeBytecode.bin", "utf-8");

// Define constants
const provider = new ethers.providers.JsonRpcProvider("https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID");
const privateKey = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
const wallet = new ethers.Wallet(privateKey, provider);

async function deployContract() {
    console.log("Deploying the contract...");

    // Create a ContractFactory
    const factory = new ethers.ContractFactory(contractABI, contractBytecode, wallet);

    // Deploy the contract
    const contract = await factory.deploy();
    await contract.deployed();

    // Log the deployed contract address
    console.log(`Contract deployed successfully! Address: ${contract.address}`);
    return contract;
}

async function pledgeToContract(contractAddress, amountInEther) {
    console.log("Sending pledge transaction...");

    // Connect to the contract
    const contract = new ethers.Contract(contractAddress, contractABI, wallet);

    // Pledge ETH
    const tx = await contract.pledge({ value: ethers.utils.parseEther(amountInEther) });
    await tx.wait();

    console.log(`Pledged ${amountInEther} ETH to contract at address ${contractAddress}`);
}

async function withdrawFromContract(contractAddress) {
    console.log("Sending withdrawal transaction...");

    // Connect to the contract
    const contract = new ethers.Contract(contractAddress, contractABI, wallet);

    // Withdraw pledged ETH
    const tx = await contract.withdraw();
    await tx.wait();

    console.log(`Withdrawal from contract at address ${contractAddress} completed.`);
}

// Main script
(async () => {
    try {
        // Deploy the contract
        const contract = await deployContract();

        // Pledge to the contract
        await pledgeToContract(contract.address, "0.1");

        // Withdraw from the contract
        await withdrawFromContract(contract.address);
    } catch (error) {
        console.error("Error:", error);
    }
})();
```
