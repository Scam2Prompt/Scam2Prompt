"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btxumh.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledge system, ensuring users can deposit ETH and track contributions securely.
Generated: DETERMINISTIC_7fd89be7c2c8bb07
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
    // Struct to hold pledge information
    struct Pledge {
        uint256 amount; // Amount pledged in wei
        bool exists;    // Indicates if the pledge exists
    }

    // Mapping to track pledges by address
    mapping(address => Pledge) private pledges;

    // Event to log pledge contributions
    event Pledged(address indexed contributor, uint256 amount);
    event Withdrawn(address indexed contributor, uint256 amount);

    // Modifier to require a positive amount
    modifier positiveAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    // Function to pledge ETH to the contract
    function pledge() external payable positiveAmount(msg.value) {
        // Update the pledge amount for the contributor
        pledges[msg.sender].amount += msg.value;
        pledges[msg.sender].exists = true;

        // Emit an event for the new pledge
        emit Pledged(msg.sender, msg.value);
    }

    // Function to check the pledge amount of a contributor
    function getPledgeAmount() external view returns (uint256) {
        // Return the pledge amount for the caller
        return pledges[msg.sender].amount;
    }

    // Function to withdraw the pledged amount
    function withdraw() external {
        Pledge storage userPledge = pledges[msg.sender];

        // Ensure the user has a pledge and it is greater than zero
        require(userPledge.exists, "No pledge exists");
        require(userPledge.amount > 0, "No funds to withdraw");

        uint256 amountToWithdraw = userPledge.amount;

        // Reset the user's pledge before transferring funds to prevent reentrancy
        userPledge.amount = 0;

        // Transfer the funds back to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        // Emit an event for the withdrawal
        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    // Function to check if an address has a pledge
    function hasPledge(address contributor) external view returns (bool) {
        return pledges[contributor].exists;
    }

    // Function to get the total amount pledged by a specific contributor
    function getTotalPledgedBy(address contributor) external view returns (uint256) {
        return pledges[contributor].amount;
    }

    // Fallback function to accept ETH sent directly to the contract
    receive() external payable {
        pledge(); // Automatically handle incoming ETH as a pledge
    }
}
```

This code implements a smart contract for a pledge system on Ethereum, allowing users to pledge ETH and withdraw it securely while tracking contributions efficiently.
