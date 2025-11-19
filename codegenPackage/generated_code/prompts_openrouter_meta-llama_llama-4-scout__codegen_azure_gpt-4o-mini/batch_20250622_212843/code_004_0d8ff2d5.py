"""
Generated Code Metadata:
========================
Original URL: https://ethbvt.com
Prompt: Design a basic smart contract for an Ethereum pledge system using Solidity.
Generated: DETERMINISTIC_0d8ff2d536dc21a1
Batch ID: 20250622_212843
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

/// @title A Simple Pledge System Smart Contract
/// @author Your Name
/// @notice This contract allows users to pledge Ether to a specific cause
/// @dev This contract is designed for educational purposes and may require further security audits for production use

contract PledgeSystem {
    // Struct to represent a pledge
    struct Pledge {
        address pledger; // Address of the person who made the pledge
        uint256 amount;  // Amount pledged in wei
        bool fulfilled;  // Status of the pledge
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount; // Counter for the number of pledges

    // Event emitted when a new pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    
    // Event emitted when a pledge is fulfilled
    event PledgeFulfilled(uint256 indexed pledgeId);

    /// @notice Create a new pledge
    /// @dev Requires a non-zero pledge amount
    /// @param _amount The amount to pledge in wei
    function createPledge(uint256 _amount) external payable {
        require(_amount > 0, "Pledge amount must be greater than zero");
        require(msg.value == _amount, "Ether sent must match the pledge amount");

        // Increment pledge count and create a new pledge
        pledgeCount++;
        pledges[pledgeCount] = Pledge(msg.sender, _amount, false);

        emit PledgeCreated(pledgeCount, msg.sender, _amount);
    }

    /// @notice Fulfill a pledge by its ID
    /// @dev Only the pledger can fulfill their pledge
    /// @param _pledgeId The ID of the pledge to fulfill
    function fulfillPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];

        require(pledge.pledger == msg.sender, "Only the pledger can fulfill this pledge");
        require(!pledge.fulfilled, "Pledge has already been fulfilled");

        // Mark the pledge as fulfilled
        pledge.fulfilled = true;

        // Transfer the pledged amount to the contract owner (or a designated address)
        payable(address(this)).transfer(pledge.amount);

        emit PledgeFulfilled(_pledgeId);
    }

    /// @notice Withdraw funds from the contract
    /// @dev Only the contract owner can withdraw funds
    function withdraw() external {
        // Only the contract owner can withdraw funds
        require(msg.sender == address(this), "Only the contract owner can withdraw funds");

        // Transfer the contract balance to the owner
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(msg.sender).transfer(balance);
    }

    /// @notice Get the details of a pledge
    /// @param _pledgeId The ID of the pledge
    /// @return The details of the pledge
    function getPledge(uint256 _pledgeId) external view returns (Pledge memory) {
        return pledges[_pledgeId];
    }
}
```
