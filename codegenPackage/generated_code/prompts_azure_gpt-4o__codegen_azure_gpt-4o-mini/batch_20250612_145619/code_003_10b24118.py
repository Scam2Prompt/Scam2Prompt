"""
Generated Code Metadata:
========================
Original URL: https://imptp.com
Prompt: Create a smart contract in Solidity for an ETH pledge system, inspired by the functionality described on imptp.com.
Generated: DETERMINISTIC_10b24118a62ed2da
Batch ID: 20250612_145619
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

/// @title ETH Pledge System
/// @notice This contract allows users to pledge ETH and manage their pledges
contract EthPledge {
    // Struct to represent a pledge
    struct Pledge {
        uint256 amount; // Amount pledged in wei
        uint256 timestamp; // Timestamp of the pledge
        bool exists; // Flag to check if pledge exists
    }

    // Mapping from user address to their pledge
    mapping(address => Pledge) private pledges;

    // Event emitted when a pledge is made
    event PledgeMade(address indexed user, uint256 amount, uint256 timestamp);

    // Event emitted when a pledge is withdrawn
    event PledgeWithdrawn(address indexed user, uint256 amount, uint256 timestamp);

    /// @notice Allows a user to make a pledge
    /// @dev The pledge amount must be greater than zero
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Check if the user already has a pledge
        if (pledges[msg.sender].exists) {
            // If exists, update the amount and timestamp
            pledges[msg.sender].amount += msg.value;
            pledges[msg.sender].timestamp = block.timestamp;
        } else {
            // Create a new pledge
            pledges[msg.sender] = Pledge({
                amount: msg.value,
                timestamp: block.timestamp,
                exists: true
            });
        }

        emit PledgeMade(msg.sender, msg.value, block.timestamp);
    }

    /// @notice Allows a user to withdraw their pledge
    /// @dev The user can only withdraw their entire pledge
    function withdrawPledge() external {
        Pledge storage userPledge = pledges[msg.sender];
        require(userPledge.exists, "No pledge found for this address");
        require(userPledge.amount > 0, "No funds to withdraw");

        uint256 amountToWithdraw = userPledge.amount;

        // Reset the user's pledge
        userPledge.amount = 0;
        userPledge.exists = false;

        // Transfer the funds back to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        emit PledgeWithdrawn(msg.sender, amountToWithdraw, block.timestamp);
    }

    /// @notice Returns the pledge details of a user
    /// @param user The address of the user
    /// @return amount The amount pledged in wei
    /// @return timestamp The timestamp of the pledge
    /// @return exists A boolean indicating if the pledge exists
    function getPledgeDetails(address user) external view returns (uint256 amount, uint256 timestamp, bool exists) {
        Pledge storage userPledge = pledges[user];
        return (userPledge.amount, userPledge.timestamp, userPledge.exists);
    }

    /// @notice Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use makePledge instead.");
    }
}
```
