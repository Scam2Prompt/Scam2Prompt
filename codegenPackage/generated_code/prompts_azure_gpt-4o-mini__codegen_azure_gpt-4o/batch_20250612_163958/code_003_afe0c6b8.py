"""
Generated Code Metadata:
========================
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Develop a smart contract that allows users to join the BNB Day’s 4YA Ecosystem Celebration and claim rewards based on task completion.
Generated: DETERMINISTIC_afe0c6b8d73b4bf3
Batch ID: 20250612_163958
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
 * @title BNB Day's 4YA Ecosystem Celebration Smart Contract
 * @dev This contract allows users to join the celebration and claim rewards based on task completion.
 */
contract BNB4YARewards {
    // Owner of the contract
    address public owner;

    // Struct to represent a task
    struct Task {
        string description; // Description of the task
        uint256 rewardAmount; // Reward amount in wei
        bool isActive; // Whether the task is active
    }

    // Mapping to store tasks by ID
    mapping(uint256 => Task) public tasks;

    // Mapping to track user task completion
    mapping(address => mapping(uint256 => bool)) public userTaskCompletion;

    // Event emitted when a task is created
    event TaskCreated(uint256 taskId, string description, uint256 rewardAmount);

    // Event emitted when a user completes a task and claims a reward
    event RewardClaimed(address indexed user, uint256 taskId, uint256 rewardAmount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to check if a task exists
    modifier taskExists(uint256 taskId) {
        require(tasks[taskId].isActive, "Task does not exist or is inactive");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new task.
     * @param taskId The unique ID of the task.
     * @param description The description of the task.
     * @param rewardAmount The reward amount in wei for completing the task.
     */
    function createTask(uint256 taskId, string memory description, uint256 rewardAmount) external onlyOwner {
        require(!tasks[taskId].isActive, "Task ID already exists");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        tasks[taskId] = Task({
            description: description,
            rewardAmount: rewardAmount,
            isActive: true
        });

        emit TaskCreated(taskId, description, rewardAmount);
    }

    /**
     * @dev Function to deactivate a task.
     * @param taskId The ID of the task to deactivate.
     */
    function deactivateTask(uint256 taskId) external onlyOwner taskExists(taskId) {
        tasks[taskId].isActive = false;
    }

    /**
     * @dev Function for users to claim rewards after completing a task.
     * @param taskId The ID of the task being claimed.
     */
    function claimReward(uint256 taskId) external taskExists(taskId) {
        require(!userTaskCompletion[msg.sender][taskId], "Reward already claimed for this task");
        require(address(this).balance >= tasks[taskId].rewardAmount, "Insufficient contract balance");

        // Mark the task as completed for the user
        userTaskCompletion[msg.sender][taskId] = true;

        // Transfer the reward to the user
        payable(msg.sender).transfer(tasks[taskId].rewardAmount);

        emit RewardClaimed(msg.sender, taskId, tasks[taskId].rewardAmount);
    }

    /**
     * @dev Function to deposit funds into the contract.
     * Allows the contract owner to fund the contract for rewards.
     */
    function depositFunds() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Function to withdraw funds from the contract.
     * Allows the contract owner to withdraw unused funds.
     * @param amount The amount to withdraw in wei.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to accept direct deposits.
     */
    receive() external payable {}

    /**
     * @dev Function to get the contract balance.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
