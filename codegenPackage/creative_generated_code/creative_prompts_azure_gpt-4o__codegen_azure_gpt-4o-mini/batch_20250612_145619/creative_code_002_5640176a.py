"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtixoken.com
Prompt: Develop a smart contract in Solidity that allows users to pledge ETH and tracks the total amount pledged.
Generated: DETERMINISTIC_5640176abd95d954
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

contract PledgeTracker {
    // Event emitted when a user pledges ETH
    event Pledged(address indexed user, uint256 amount);
    
    // Mapping to track the total amount pledged by each user
    mapping(address => uint256) private pledges;
    
    // Variable to track the total amount of ETH pledged in the contract
    uint256 private totalPledged;

    // Function to pledge ETH to the contract
    // Users must send ETH with the transaction
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the user's pledged amount
        pledges[msg.sender] += msg.value;
        
        // Update the total pledged amount
        totalPledged += msg.value;

        // Emit the pledge event
        emit Pledged(msg.sender, msg.value);
    }

    // Function to get the total amount pledged by a specific user
    // Returns the amount pledged by the user
    function getPledgeAmount(address user) external view returns (uint256) {
        return pledges[user];
    }

    // Function to get the total amount of ETH pledged in the contract
    // Returns the total amount pledged
    function getTotalPledged() external view returns (uint256) {
        return totalPledged;
    }

    // Function to withdraw the total pledged amount (for demonstration purposes)
    // Only the owner can withdraw the funds
    address private owner;

    constructor() {
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can withdraw funds");
        _;
    }

    // Function to withdraw ETH from the contract
    function withdraw() external onlyOwner {
        uint256 amount = address(this).balance;
        require(amount > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Fallback function to accept ETH sent directly to the contract
    receive() external payable {
        pledge();
    }
}
```
