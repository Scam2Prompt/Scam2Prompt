"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethbo.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledging system, referencing ETH-specific features like gas optimization and pledge tracking.
Generated: DETERMINISTIC_4eb95631d57477e6
Batch ID: 20250612_154016
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

/// @title Pledging System
/// @notice This contract allows users to make pledges in ETH, track their contributions, and withdraw funds.
/// @dev Uses events to log important actions on the blockchain for transparency.

contract PledgeSystem {

    // Struct to represent a pledge
    struct Pledge {
        uint256 amount;     // The amount pledged in wei
        bool exists;        // Tracks if the pledge exists
    }

    // Mapping to track pledges by address
    mapping(address => Pledge) private pledges;

    // Total amount of ETH pledged
    uint256 public totalPledges;

    // Event emitted when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event Withdrawn(address indexed pledger, uint256 amount);

    /// @notice Allows a user to make a pledge
    /// @dev Requires that the pledge amount is greater than zero
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Check if the pledge already exists
        if (pledges[msg.sender].exists) {
            // Update the existing pledge
            pledges[msg.sender].amount += msg.value;
        } else {
            // Create a new pledge
            pledges[msg.sender] = Pledge(msg.value, true);
        }

        // Update the total pledges
        totalPledges += msg.value;

        // Emit an event for the pledge
        emit Pledged(msg.sender, msg.value);
    }

    /// @notice Allows a user to withdraw their pledge
    /// @dev Requires that the caller has a pledge amount greater than zero
    function withdraw() external {
        Pledge storage pledge = pledges[msg.sender];
        require(pledge.exists, "No pledge exists for this address");
        require(pledge.amount > 0, "No funds to withdraw");

        // Store the amount to withdraw
        uint256 amountToWithdraw = pledge.amount;

        // Reset the user's pledge
        pledge.amount = 0;

        // Update the total pledges
        totalPledges -= amountToWithdraw;

        // Transfer the funds
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        // Emit an event for the withdrawal
        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /// @notice Returns the pledge amount for a specific address
    /// @param pledger The address of the user whose pledge is being queried
    /// @return The amount pledged by the user in wei
    function getPledgeAmount(address pledger) external view returns (uint256) {
        return pledges[pledger].amount;
    }

    /// @notice Returns the total amount of ETH pledged in the contract
    /// @return The total amount of pledges in wei
    function getTotalPledges() external view returns (uint256) {
        return totalPledges;
    }
}
```
