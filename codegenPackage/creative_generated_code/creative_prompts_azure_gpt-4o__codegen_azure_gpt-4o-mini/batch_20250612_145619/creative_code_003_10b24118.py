"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imptp.com
Prompt: Create a smart contract in Solidity for an ETH pledge system, inspired by the functionality described on imptp.com.
Generated: DETERMINISTIC_10b24118a62ed2da
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

/// @title ETH Pledge System
/// @author Your Name
/// @notice This contract allows users to pledge ETH and withdraw it after a certain period
contract ETHPledge {
    // Struct to hold pledge information
    struct Pledge {
        uint256 amount; // Amount pledged
        uint256 timestamp; // Timestamp of the pledge
        bool withdrawn; // Status of the withdrawal
    }

    // Mapping to store user pledges
    mapping(address => Pledge) public pledges;

    // Event emitted when a pledge is created
    event Pledged(address indexed user, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to check if the caller has an active pledge
    modifier hasActivePledge() {
        require(pledges[msg.sender].amount > 0, "No active pledge found.");
        _;
    }

    // Modifier to check if the pledge can be withdrawn
    modifier canWithdraw() {
        require(block.timestamp >= pledges[msg.sender].timestamp + 30 days, "Pledge is still locked.");
        require(!pledges[msg.sender].withdrawn, "Pledge already withdrawn.");
        _;
    }

    /// @notice Pledge ETH to the contract
    /// @dev The amount must be greater than zero
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero.");
        
        // Ensure that the user does not already have an active pledge
        require(pledges[msg.sender].amount == 0, "You already have an active pledge.");

        // Create a new pledge
        pledges[msg.sender] = Pledge({
            amount: msg.value,
            timestamp: block.timestamp,
            withdrawn: false
        });

        emit Pledged(msg.sender, msg.value);
    }

    /// @notice Withdraw the pledged ETH after the lock period
    /// @dev Can only be called by the user who made the pledge
    function withdraw() external hasActivePledge canWithdraw {
        uint256 amount = pledges[msg.sender].amount;

        // Mark the pledge as withdrawn
        pledges[msg.sender].withdrawn = true;

        // Transfer the ETH back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed.");

        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Get the pledge details of the caller
    /// @return amount The amount pledged
    /// @return timestamp When the pledge was made
    /// @return withdrawn If the pledge has been withdrawn
    function getPledgeDetails() external view returns (uint256 amount, uint256 timestamp, bool withdrawn) {
        Pledge memory pledge = pledges[msg.sender];
        return (pledge.amount, pledge.timestamp, pledge.withdrawn);
    }
}
```
