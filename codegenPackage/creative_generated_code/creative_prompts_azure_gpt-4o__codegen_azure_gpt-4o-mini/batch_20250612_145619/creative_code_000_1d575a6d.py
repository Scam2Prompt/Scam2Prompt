"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjxn.com
Prompt: Write a smart contract in Solidity to implement a pledge system for Ethereum, ensuring contributions are tracked and funds are securely held until a goal is met.
Generated: DETERMINISTIC_1d575a6d2d4fb87d
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

contract PledgeSystem {
    // State variables to track contributions and goal
    address public owner;  // The owner of the contract
    uint256 public goalAmount;  // The goal amount for the pledge
    uint256 public totalContributions;  // Total contributions received
    mapping(address => uint256) public contributions;  // Contributions by each address
    bool public goalMet;  // Boolean flag to indicate if the goal has been met

    // Events to log important actions
    event ContributionReceived(address indexed contributor, uint256 amount);
    event GoalAchieved(uint256 totalAmount);
    event FundsWithdrawn(address indexed owner, uint256 amount);
    
    // Modifiers to restrict access
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: Only owner can perform this action.");
        _;
    }

    modifier goalNotMet() {
        require(!goalMet, "Cannot contribute: goal already met.");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _goalAmount) {
        require(_goalAmount > 0, "Goal amount must be greater than zero.");
        owner = msg.sender;
        goalAmount = _goalAmount;
        totalContributions = 0;
        goalMet = false;
    }

    // Function to contribute to the pledge
    function contribute() external payable goalNotMet {
        require(msg.value > 0, "Contribution must be greater than zero.");
        
        // Track the contribution
        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;

        emit ContributionReceived(msg.sender, msg.value);

        // Check if the goal has been met
        if (totalContributions >= goalAmount) {
            goalMet = true;
            emit GoalAchieved(totalContributions);
        }
    }

    // Function for the owner to withdraw funds if the goal has been met
    function withdrawFunds() external onlyOwner {
        require(goalMet, "Cannot withdraw: goal has not been met.");
        
        uint256 amount = address(this).balance;
        require(amount > 0, "No funds available to withdraw.");

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Transfer failed: Unable to withdraw funds.");
        
        emit FundsWithdrawn(owner, amount);
    }

    // Function to check the contract balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to get the contribution of a specific address
    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }
}
```
