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

contract Crowdfunding {
    address public owner;
    uint256 public goal;
    uint256 public deadline;
    bool public goalReached;
    bool public refunded;
    
    mapping(address => uint256) public contributions;
    
    event ContributionReceived(address contributor, uint256 amount);
    event GoalReached(uint256 totalAmount);
    event RefundProcessed(address contributor, uint256 amount);
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    modifier campaignActive() {
        require(block.timestamp < deadline, "Campaign has ended");
        _;
    }
    
    modifier campaignEnded() {
        require(block.timestamp >= deadline, "Campaign is still active");
        _;
    }
    
    constructor(uint256 _goal, uint256 _durationInDays) {
        owner = msg.sender;
        goal = _goal;
        deadline = block.timestamp + (_durationInDays * 1 days);
    }
    
    function contribute() external payable campaignActive {
        require(msg.value > 0, "Contribution must be greater than 0");
        contributions[msg.sender] += msg.value;
        emit ContributionReceived(msg.sender, msg.value);
        
        if (address(this).balance >= goal && !goalReached) {
            goalReached = true;
            emit GoalReached(address(this).balance);
        }
    }
    
    function refund() external campaignEnded {
        require(!goalReached, "Goal was reached, no refunds");
        require(!refunded, "Already refunded");
        require(contributions[msg.sender] > 0, "No contribution to refund");
        
        uint256 amount = contributions[msg.sender];
        contributions[msg.sender] = 0;
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Refund transfer failed");
        
        emit RefundProcessed(msg.sender, amount);
    }
    
    function withdrawFunds() external onlyOwner {
        require(goalReached, "Goal not reached");
        require(block.timestamp >= deadline, "Campaign is still active");
        
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }
    
    function extendDeadline(uint256 _additionalDays) external onlyOwner campaignActive {
        deadline += _additionalDays * 1 days;
    }
    
    receive() external payable {
        contribute();
    }
}
```
