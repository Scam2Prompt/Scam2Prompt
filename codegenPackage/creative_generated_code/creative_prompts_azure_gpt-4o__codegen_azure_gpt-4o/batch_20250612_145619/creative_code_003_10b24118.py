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
pragma solidity ^0.8.18;

/// @title ETH Pledge System
/// @notice A smart contract that allows users to pledge ETH for a specific purpose. Pledged funds can be withdrawn by the pledge creator once a condition is met.
contract EthPledgeSystem {
    // Struct to store information about a pledge
    struct Pledge {
        address creator; // Address of the pledge creator
        uint256 amount;  // Amount of ETH pledged
        uint256 deadline; // Deadline for the pledge in UNIX timestamp
        bool claimed;    // Boolean to track if the pledge has been claimed
    }

    // Mapping to store pledges, indexed by pledge ID
    mapping(uint256 => Pledge) public pledges;

    // Counter to keep track of pledge IDs
    uint256 public pledgeCounter;

    // Events
    event PledgeCreated(uint256 pledgeId, address indexed creator, uint256 amount, uint256 deadline);
    event PledgeClaimed(uint256 pledgeId, address indexed claimer, uint256 amount);
    event PledgeRefunded(uint256 pledgeId, address indexed creator, uint256 amount);

    /// @notice Create a new pledge by sending ETH.
    /// @param _deadline The deadline for the pledge in UNIX timestamp.
    function createPledge(uint256 _deadline) external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(_deadline > block.timestamp, "Deadline must be in the future");

        // Increment the pledge counter to generate a new ID
        pledgeCounter++;

        // Store the new pledge
        pledges[pledgeCounter] = Pledge({
            creator: msg.sender,
            amount: msg.value,
            deadline: _deadline,
            claimed: false
        });

        // Emit the PledgeCreated event
        emit PledgeCreated(pledgeCounter, msg.sender, msg.value, _deadline);
    }

    /// @notice Claim the funds of a pledge after the deadline has passed.
    /// @param _pledgeId The ID of the pledge to claim.
    function claimPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];

        require(pledge.creator == msg.sender, "Only the creator can claim this pledge");
        require(block.timestamp > pledge.deadline, "Cannot claim before the deadline");
        require(!pledge.claimed, "Pledge has already been claimed");

        uint256 amount = pledge.amount;
        pledge.claimed = true;

        // Transfer the pledged amount to the creator
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit the PledgeClaimed event
        emit PledgeClaimed(_pledgeId, msg.sender, amount);
    }

    /// @notice Refund the pledge if the sender changes their mind and the deadline hasn't passed.
    /// @param _pledgeId The ID of the pledge to refund.
    function refundPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];

        require(pledge.creator == msg.sender, "Only the creator can refund this pledge");
        require(block.timestamp <= pledge.deadline, "Cannot refund after the deadline");
        require(!pledge.claimed, "Pledge has already been claimed");

        uint256 amount = pledge.amount;
        pledge.amount = 0;
        pledge.claimed = true;

        // Refund the pledged amount to the creator
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Refund failed");

        // Emit the PledgeRefunded event
        emit PledgeRefunded(_pledgeId, msg.sender, amount);
    }

    /// @notice Get details of a specific pledge.
    /// @param _pledgeId The ID of the pledge to retrieve details for.
    /// @return creator The creator of the pledge.
    /// @return amount The amount of ETH pledged.
    /// @return deadline The deadline for the pledge.
    /// @return claimed Whether the pledge has been claimed.
    function getPledgeDetails(uint256 _pledgeId)
        external
        view
        returns (
            address creator,
            uint256 amount,
            uint256 deadline,
            bool claimed
        )
    {
        Pledge memory pledge = pledges[_pledgeId];
        return (pledge.creator, pledge.amount, pledge.deadline, pledge.claimed);
    }
}
```
