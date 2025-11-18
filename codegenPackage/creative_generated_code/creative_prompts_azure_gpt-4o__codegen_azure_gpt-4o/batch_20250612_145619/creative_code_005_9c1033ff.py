"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btxumh.com
Prompt: Write a Solidity smart contract that includes a feature for refunding ETH pledges if certain conditions are not met.
Generated: DETERMINISTIC_9c1033ff82df3e5a
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

/**
 * @title PledgeRefundContract
 * @dev A smart contract that allows users to pledge ETH and provides a refund mechanism
 * if certain conditions are not met within a specified timeframe.
 */
contract PledgeRefundContract {
    // Structure to store pledge details
    struct Pledge {
        address payable pledger; // Address of the pledger
        uint256 amount;          // Amount of ETH pledged
    }

    // State variables
    address public owner;                // Owner of the contract
    uint256 public goal;                 // Funding goal in wei
    uint256 public deadline;             // Deadline timestamp for reaching the goal
    uint256 public totalPledged;         // Total amount of ETH pledged
    bool public goalReached;             // Boolean indicating if the goal was reached
    mapping(address => Pledge) public pledges; // Mapping to track pledges by address

    // Events
    event Pledged(address indexed pledger, uint256 amount);
    event Refunded(address indexed pledger, uint256 amount);
    event GoalReached(uint256 totalAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier beforeDeadline() {
        require(block.timestamp <= deadline, "Deadline has passed");
        _;
    }

    modifier afterDeadline() {
        require(block.timestamp > deadline, "Deadline has not passed yet");
        _;
    }

    // Constructor
    constructor(uint256 _goal, uint256 _durationInDays) {
        require(_goal > 0, "Goal must be greater than 0");
        require(_durationInDays > 0, "Duration must be greater than 0");

        owner = msg.sender; // Set contract deployer as the owner
        goal = _goal; // Set the funding goal
        deadline = block.timestamp + (_durationInDays * 1 days); // Set the deadline
    }

    /**
     * @dev Allows users to pledge ETH to the contract, before the deadline.
     */
    function pledge() external payable beforeDeadline {
        require(msg.value > 0, "Pledge amount must be greater than 0");

        // Update the user's pledge and the total pledged amount
        Pledge storage userPledge = pledges[msg.sender];
        userPledge.pledger = payable(msg.sender);
        userPledge.amount += msg.value;
        totalPledged += msg.value;

        // Emit the pledge event
        emit Pledged(msg.sender, msg.value);

        // Check if the goal has been reached
        if (totalPledged >= goal) {
            goalReached = true;
            emit GoalReached(totalPledged);
        }
    }

    /**
     * @dev Allows pledgers to claim a refund if the funding goal was not met after the deadline.
     */
    function claimRefund() external afterDeadline {
        require(!goalReached, "Goal was reached, refunds are not available");
        
        Pledge storage userPledge = pledges[msg.sender];
        uint256 amountToRefund = userPledge.amount;

        require(amountToRefund > 0, "No funds to refund");

        // Reset the user's pledge before transferring ETH
        userPledge.amount = 0;

        // Transfer the ETH back to the pledger
        (bool success, ) = userPledge.pledger.call{value: amountToRefund}("");
        require(success, "ETH transfer failed");

        // Emit the refund event
        emit Refunded(msg.sender, amountToRefund);
    }

    /**
     * @dev Allows the owner to withdraw all funds if the funding goal is met.
     */
    function withdrawFunds() external onlyOwner afterDeadline {
        require(goalReached, "Funding goal not reached");
        require(address(this).balance > 0, "No funds to withdraw");

        // Transfer the contract's balance to the owner
        (bool success, ) = payable(owner).call{value: address(this).balance}("");
        require(success, "ETH transfer to owner failed");
    }
}
```
