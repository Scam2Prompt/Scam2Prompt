"""
Generated Code Metadata:
========================
Original URL: https://ethjxn.com
Prompt: Write a smart contract in Solidity to implement a pledge system for Ethereum, ensuring contributions are tracked and funds are securely held until a goal is met.
Generated: DETERMINISTIC_1d575a6d2d4fb87d
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

/**
 * @title PledgeSystem
 * @dev A smart contract for tracking contributions towards a funding goal
 * Funds are securely held until the goal is met
 */
contract PledgeSystem {
    // State variables
    address public immutable owner;
    uint256 public immutable fundingGoal;
    uint256 public immutable deadline;
    uint256 public totalContributions;
    bool public isGoalMet;
    bool public isClosed;

    // Mapping to track individual contributions
    mapping(address => uint256) public contributions;

    // Events
    event ContributionMade(address indexed contributor, uint256 amount);
    event GoalReached(uint256 totalAmount);
    event FundsWithdrawn(uint256 amount);
    event RefundIssued(address indexed contributor, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier beforeDeadline() {
        require(block.timestamp < deadline, "Deadline has passed");
        _;
    }

    modifier afterDeadline() {
        require(block.timestamp >= deadline, "Deadline not reached yet");
        _;
    }

    modifier whenNotClosed() {
        require(!isClosed, "Pledge system is closed");
        _;
    }

    /**
     * @dev Constructor sets the funding goal and deadline
     * @param _fundingGoal The target amount to be raised (in wei)
     * @param _durationInDays The duration of the campaign in days
     */
    constructor(uint256 _fundingGoal, uint256 _durationInDays) {
        require(_fundingGoal > 0, "Funding goal must be greater than 0");
        require(_durationInDays > 0, "Duration must be greater than 0");

        owner = msg.sender;
        fundingGoal = _fundingGoal;
        deadline = block.timestamp + (_durationInDays * 1 days);
    }

    /**
     * @dev Allows users to contribute to the pledge
     */
    function contribute() external payable beforeDeadline whenNotClosed {
        require(msg.value > 0, "Contribution must be greater than 0");

        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;

        emit ContributionMade(msg.sender, msg.value);

        if (!isGoalMet && totalContributions >= fundingGoal) {
            isGoalMet = true;
            emit GoalReached(totalContributions);
        }
    }

    /**
     * @dev Allows the owner to withdraw funds if goal is met
     */
    function withdrawFunds() external onlyOwner whenNotClosed {
        require(isGoalMet, "Funding goal not met");
        require(address(this).balance > 0, "No funds to withdraw");

        isClosed = true;
        uint256 amount = address(this).balance;
        payable(owner).transfer(amount);

        emit FundsWithdrawn(amount);
    }

    /**
     * @dev Allows contributors to get refunds if goal is not met by deadline
     */
    function getRefund() external afterDeadline whenNotClosed {
        require(!isGoalMet, "Goal was met, no refunds available");
        require(contributions[msg.sender] > 0, "No contribution to refund");

        uint256 amount = contributions[msg.sender];
        contributions[msg.sender] = 0;
        payable(msg.sender).transfer(amount);

        emit RefundIssued(msg.sender, amount);
    }

    /**
     * @dev Returns the current balance of the contract
     * @return The contract balance in wei
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Returns the time remaining until deadline
     * @return Time remaining in seconds
     */
    function getTimeRemaining() external view returns (uint256) {
        if (block.timestamp >= deadline) {
            return 0;
        }
        return deadline - block.timestamp;
    }
}
```
