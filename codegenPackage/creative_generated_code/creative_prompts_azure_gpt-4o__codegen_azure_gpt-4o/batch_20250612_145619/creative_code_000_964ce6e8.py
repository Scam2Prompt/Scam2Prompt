"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethphb.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledge system, ensuring compatibility with the features described on ETH Pledge.
Generated: DETERMINISTIC_964ce6e85490bea2
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

/// @title Pledge System Smart Contract
/// @dev A smart contract for creating and managing pledges on the Ethereum blockchain
contract PledgeSystem {
    // Event emitted when a new pledge is created
    event PledgeCreated(uint256 pledgeId, address indexed pledger, uint256 amount, uint256 timestamp);

    // Event emitted when a pledge is withdrawn
    event PledgeWithdrawn(uint256 pledgeId, uint256 amount, uint256 timestamp);

    // Event emitted when a pledge is updated
    event PledgeUpdated(uint256 pledgeId, uint256 newAmount, uint256 timestamp);

    // Struct to store pledge details
    struct Pledge {
        address pledger; // Address of the pledger
        uint256 amount;  // Amount pledged in wei
        uint256 timestamp; // Timestamp of creation
        bool isWithdrawn; // Flag to indicate if pledge is withdrawn
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => Pledge) public pledges;
    uint256 public nextPledgeId; // ID counter for pledges

    /// @notice Create a new pledge
    /// @dev Stores the pledge information in the contract state
    /// @param _amount The amount of ETH being pledged (in wei)
    function createPledge(uint256 _amount) external payable {
        require(msg.value == _amount, "Sent value must match the pledge amount");
        require(_amount > 0, "Pledge amount must be greater than zero");

        // Create a new pledge and store it in the mapping
        pledges[nextPledgeId] = Pledge({
            pledger: msg.sender,
            amount: _amount,
            timestamp: block.timestamp,
            isWithdrawn: false
        });

        // Emit event for the new pledge
        emit PledgeCreated(nextPledgeId, msg.sender, _amount, block.timestamp);

        // Increment pledge ID for the next pledge
        nextPledgeId++;
    }

    /// @notice Withdraw a pledge by ID
    /// @dev Allows the creator of a pledge to withdraw their pledged funds
    /// @param _pledgeId The ID of the pledge to withdraw
    function withdrawPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.pledger == msg.sender, "Only the pledger can withdraw their pledge");
        require(!pledge.isWithdrawn, "Pledge has already been withdrawn");
        require(pledge.amount > 0, "Pledge amount must be greater than zero");

        uint256 amountToWithdraw = pledge.amount;
        pledge.isWithdrawn = true;

        // Transfer the pledged funds back to the pledger
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        // Emit event for the withdrawal
        emit PledgeWithdrawn(_pledgeId, amountToWithdraw, block.timestamp);
    }

    /// @notice Update the amount of an existing pledge
    /// @dev Allows the creator of a pledge to update their pledged amount
    /// @param _pledgeId The ID of the pledge to update
    /// @param _newAmount The new pledge amount (in wei)
    function updatePledge(uint256 _pledgeId, uint256 _newAmount) external payable {
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.pledger == msg.sender, "Only the pledger can update their pledge");
        require(!pledge.isWithdrawn, "Cannot update a withdrawn pledge");
        require(_newAmount > 0, "New amount must be greater than zero");

        // If the new amount is greater than the current amount, require additional ETH sent
        if (_newAmount > pledge.amount) {
            uint256 additionalAmount = _newAmount - pledge.amount;
            require(msg.value == additionalAmount, "Insufficient value sent for the updated pledge");
        }

        // Update the pledge amount
        pledge.amount = _newAmount;

        // Emit event for the updated pledge
        emit PledgeUpdated(_pledgeId, _newAmount, block.timestamp);
    }

    /// @notice Get details of a specific pledge
    /// @dev Returns the details of a pledge by ID
    /// @param _pledgeId The ID of the pledge
    /// @return Pledge details (address, amount, timestamp, isWithdrawn)
    function getPledge(uint256 _pledgeId) external view returns (Pledge memory) {
        return pledges[_pledgeId];
    }
}
```
