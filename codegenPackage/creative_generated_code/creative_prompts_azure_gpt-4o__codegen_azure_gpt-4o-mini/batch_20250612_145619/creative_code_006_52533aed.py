"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjxn.com
Prompt: Create a Solidity function that refunds ETH to contributors if a pledge goal is not met within a specified timeframe.
Generated: DETERMINISTIC_52533aede932886e
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

contract Crowdfunding {
    // State variables
    address public owner;
    uint public pledgeGoal;
    uint public pledgeDeadline;
    mapping(address => uint) public contributions;
    uint public totalContributions;
    bool public goalMet;

    // Events
    event Pledged(address indexed contributor, uint amount);
    event Refunded(address indexed contributor, uint amount);
    event GoalReached();

    // Constructor to initialize the contract
    constructor(uint _pledgeGoal, uint _durationInDays) {
        owner = msg.sender;
        pledgeGoal = _pledgeGoal;
        pledgeDeadline = block.timestamp + (_durationInDays * 1 days);
        goalMet = false;
    }

    // Function to pledge ETH
    function pledge() external payable {
        require(block.timestamp < pledgeDeadline, "Pledge period has ended");
        require(msg.value > 0, "Contribution must be greater than 0");

        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;

        emit Pledged(msg.sender, msg.value);

        // Check if the pledge goal is met
        if (totalContributions >= pledgeGoal) {
            goalMet = true;
            emit GoalReached();
        }
    }

    // Function to refund contributors if the goal is not met
    function refund() external {
        require(block.timestamp >= pledgeDeadline, "Pledge period is not over yet");
        require(!goalMet, "Pledge goal has been met, no refunds");

        uint amount = contributions[msg.sender];
        require(amount > 0, "No contributions to refund");

        // Reset the contributor's contribution before sending ETH to prevent re-entrancy attacks
        contributions[msg.sender] = 0;
        totalContributions -= amount;

        // Transfer ETH back to the contributor
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Refund transfer failed");

        emit Refunded(msg.sender, amount);
    }

    // Function to withdraw funds if the goal is met (optional)
    function withdraw() external {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(goalMet, "Pledge goal not met, cannot withdraw");

        uint amount = address(this).balance;
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdraw transfer failed");
    }

    // Function to check the contract's balance (for convenience)
    function contractBalance() external view returns (uint) {
        return address(this).balance;
    }
}
```
