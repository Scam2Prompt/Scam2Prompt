"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: Create a Solidity smart contract that integrates gamification features for educational milestones, allowing users to earn IQRA Tokens upon completing specific tasks or quizzes.
Generated: DETERMINISTIC_cee9cd50cb5ad4c3
Batch ID: 20250612_151246
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

contract IQRAGame {
    // State variable to store the IQRA Token balance of each user
    mapping(address => uint256) public balances;

    // State variable to track completed tasks by users
    mapping(address => mapping(uint256 => bool)) public completedTasks;

    // Event to log token transfers
    event TokensEarned(address indexed user, uint256 amount);
    event TaskCompleted(address indexed user, uint256 taskId);

    // Constant value for IQRA Token reward per task
    uint256 public constant REWARD_PER_TASK = 10 * 10 ** 18; // 10 IQRA Tokens

    // Modifier to ensure the task is not already completed
    modifier taskNotCompleted(uint256 taskId) {
        require(!completedTasks[msg.sender][taskId], "Task already completed.");
        _;
    }

    // Function to complete a task and earn IQRA Tokens
    function completeTask(uint256 taskId) external taskNotCompleted(taskId) {
        // Mark the task as completed for the user
        completedTasks[msg.sender][taskId] = true;

        // Update the user's balance
        balances[msg.sender] += REWARD_PER_TASK;

        // Emit events for tracking
        emit TokensEarned(msg.sender, REWARD_PER_TASK);
        emit TaskCompleted(msg.sender, taskId);
    }

    // Function to check the IQRA Token balance of the caller
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Function to transfer IQRA Tokens to another user
    function transferTokens(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        // Transfer tokens
        balances[msg.sender] -= amount;
        balances[to] += amount;

        // Emit transfer event
        emit TokensEarned(to, amount); // Reusing the event to log token receipt
    }
}
```
