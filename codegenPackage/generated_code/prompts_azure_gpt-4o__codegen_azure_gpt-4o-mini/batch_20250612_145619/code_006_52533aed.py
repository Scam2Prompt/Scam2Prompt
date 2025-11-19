"""
Generated Code Metadata:
========================
Original URL: https://ethjxn.com
Prompt: Create a Solidity function that refunds ETH to contributors if a pledge goal is not met within a specified timeframe.
Generated: DETERMINISTIC_52533aede932886e
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

contract PledgeRefund {
    // State variables
    address public owner;
    uint256 public pledgeGoal;
    uint256 public pledgeDeadline;
    mapping(address => uint256) public contributions;
    bool public goalMet;

    // Events
    event Pledged(address indexed contributor, uint256 amount);
    event Refunded(address indexed contributor, uint256 amount);
    event GoalMet();

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _pledgeGoal, uint256 _duration) {
        owner = msg.sender;
        pledgeGoal = _pledgeGoal;
        pledgeDeadline = block.timestamp + _duration;
        goalMet = false;
    }

    // Function to pledge ETH
    function pledge() external payable {
        require(block.timestamp < pledgeDeadline, "Pledge period has ended");
        require(msg.value > 0, "Must pledge a positive amount");

        contributions[msg.sender] += msg.value;
        emit Pledged(msg.sender, msg.value);

        // Check if the goal is met
        if (address(this).balance >= pledgeGoal) {
            goalMet = true;
            emit GoalMet();
        }
    }

    // Function to refund contributions if the goal is not met
    function refund() external {
        require(block.timestamp >= pledgeDeadline, "Pledge period is still active");
        require(!goalMet, "Goal has been met, no refunds available");

        uint256 amount = contributions[msg.sender];
        require(amount > 0, "No contributions to refund");

        // Reset the contributor's contribution to prevent re-entrancy
        contributions[msg.sender] = 0;

        // Transfer the ETH back to the contributor
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Refund failed");

        emit Refunded(msg.sender, amount);
    }

    // Function to withdraw funds if the goal is met (only owner)
    function withdraw() external onlyOwner {
        require(goalMet, "Goal not met, cannot withdraw");
        
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the contract balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept ETH
    receive() external payable {
        pledge();
    }
}
```
