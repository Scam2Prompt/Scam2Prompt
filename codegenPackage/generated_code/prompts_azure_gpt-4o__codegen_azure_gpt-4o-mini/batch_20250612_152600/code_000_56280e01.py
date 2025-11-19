"""
Generated Code Metadata:
========================
Original URL: https://ethwish.com
Prompt: Write a smart contract in Solidity that allows users to create an ETH pledge with customizable conditions for withdrawal. Include functionality for tracking pledges and validating conditions.
Generated: DETERMINISTIC_56280e016fe83837
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PledgeManager {
    // Struct to represent a pledge
    struct Pledge {
        address pledger; // Address of the user who made the pledge
        uint256 amount;  // Amount of ETH pledged
        uint256 unlockTime; // Time when the pledge can be withdrawn
        bool isWithdrawn; // Status of the pledge withdrawal
    }

    // Mapping to track pledges by their unique ID
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount; // Counter for unique pledge IDs

    // Event emitted when a new pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount, uint256 unlockTime);
    
    // Event emitted when a pledge is withdrawn
    event PledgeWithdrawn(uint256 indexed pledgeId, address indexed pledger, uint256 amount);

    // Function to create a new pledge
    function createPledge(uint256 _unlockTime) external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");
        require(_unlockTime > block.timestamp, "Unlock time must be in the future");

        // Create a new pledge
        pledgeCount++;
        pledges[pledgeCount] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            unlockTime: _unlockTime,
            isWithdrawn: false
        });

        emit PledgeCreated(pledgeCount, msg.sender, msg.value, _unlockTime);
    }

    // Function to withdraw a pledge after the unlock time
    function withdrawPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];

        // Validate pledge existence and status
        require(pledge.pledger == msg.sender, "Only the pledger can withdraw");
        require(!pledge.isWithdrawn, "Pledge has already been withdrawn");
        require(block.timestamp >= pledge.unlockTime, "Pledge is still locked");

        // Mark pledge as withdrawn
        pledge.isWithdrawn = true;

        // Transfer the pledged amount back to the pledger
        (bool success, ) = msg.sender.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        emit PledgeWithdrawn(_pledgeId, msg.sender, pledge.amount);
    }

    // Function to get pledge details
    function getPledge(uint256 _pledgeId) external view returns (address, uint256, uint256, bool) {
        Pledge storage pledge = pledges[_pledgeId];
        return (pledge.pledger, pledge.amount, pledge.unlockTime, pledge.isWithdrawn);
    }
}
```
