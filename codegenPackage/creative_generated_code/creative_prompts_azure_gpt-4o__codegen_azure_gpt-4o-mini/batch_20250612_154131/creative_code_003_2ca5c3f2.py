"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethbvt.com
Prompt: Provide an example of a smart contract in Solidity for an ETH pledge system, and write the JavaScript code to interact with it using ethers.js.
Generated: DETERMINISTIC_2ca5c3f2f706672c
Batch ID: 20250612_154131
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

/// @title ETH Pledge System
/// @notice A simple contract to allow users to pledge ETH
contract EthPledge {
    // Structure to hold pledge information
    struct Pledge {
        uint256 amount;
        address pledger;
    }

    // Mapping to track pledges by user
    mapping(address => Pledge) public pledges;

    // Event emitted when a new pledge is made
    event PledgeMade(address indexed pledger, uint256 amount);

    // Function to make a pledge
    /// @notice Allows users to pledge ETH to the contract
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(pledges[msg.sender].amount == 0, "You have already pledged");

        // Store the pledge information
        pledges[msg.sender] = Pledge(msg.value, msg.sender);
        
        // Emit an event for the pledge
        emit PledgeMade(msg.sender, msg.value);
    }

    // Function to withdraw a pledge
    /// @notice Allows users to withdraw their pledged ETH
    function withdrawPledge() external {
        Pledge storage userPledge = pledges[msg.sender];
        require(userPledge.amount > 0, "You have no pledge to withdraw");

        uint256 amount = userPledge.amount;

        // Reset the user's pledge before transferring funds to avoid re-entrancy
        userPledge.amount = 0;

        // Transfer the funds back to the user
        payable(msg.sender).transfer(amount);
    }

    // Function to get pledge amount
    /// @notice Returns the pledge amount of the caller
    /// @return The amount pledged by the caller
    function getPledgeAmount() external view returns (uint256) {
        return pledges[msg.sender].amount;
    }
}
```

```javascript
// Import ethers.js
const { ethers } = require("ethers");

// Contract ABI (Application Binary Interface)
const abi = [
    "event PledgeMade(address indexed pledger, uint256 amount)",
    "function makePledge() external payable",
    "function withdrawPledge() external",
    "function getPledgeAmount() external view returns (uint256)",
];

// Contract address (replace with the actual deployed contract address)
const contractAddress = "0xYourContractAddress";

// Initialize provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Create a contract instance
const contract = new ethers.Contract(contractAddress, abi, signer);

// Function to make a pledge
async function pledge(amount) {
    try {
        const tx = await contract.makePledge({ value: ethers.utils.parseEther(amount) });
        await tx.wait(); // Wait for the transaction to be mined
        console.log(`Pledge of ${amount} ETH made successfully!`);
    } catch (error) {
        console.error("Failed to make pledge:", error);
    }
}

// Function to withdraw pledge
async function withdraw() {
    try {
        const tx = await contract.withdrawPledge();
        await tx.wait(); // Wait for the transaction to be mined
        console.log("Pledge withdrawn successfully!");
    } catch (error) {
        console.error("Failed to withdraw pledge:", error);
    }
}

// Function to check pledge amount
async function checkPledge() {
    try {
        const amount = await contract.getPledgeAmount();
        console.log(`Your pledge amount: ${ethers.utils.formatEther(amount)} ETH`);
    } catch (error) {
        console.error("Failed to retrieve pledge amount:", error);
    }
}

// Example usage
(async () => {
    await pledge("0.1"); // Pledge 0.1 ETH
    await checkPledge(); // Check pledge amount
    await withdraw(); // Withdraw pledge
})();
```
