"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Create a rewards program for a blockchain-based marketplace like Pushd, where users earn tokens for completing specific tasks or milestones. Include token distribution logic in the code.
Generated: DETERMINISTIC_7b297df650d3726a
Batch ID: 20250612_145923
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
 * @title RewardsProgram
 * @dev A contract for managing token rewards for users in a blockchain marketplace.
 * Users earn tokens for completing tasks or reaching milestones.
 */
contract RewardsProgram {
    // Token contract interface
    IERC20 public rewardsToken;

    // Owner of the contract
    address public owner;

    // Mapping to track user balances
    mapping(address => uint256) public userRewards;

    // Events
    event TaskCompleted(address indexed user, uint256 rewardAmount);
    event MilestoneReached(address indexed user, uint256 rewardAmount);
    event RewardsWithdrawn(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Constructor to set the token address and owner
    constructor(address _rewardsTokenAddress) {
        require(_rewardsTokenAddress != address(0), "Invalid token address");
        rewardsToken = IERC20(_rewardsTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Distribute rewards when a user completes a task.
     * @param user Address of the user.
     * @param rewardAmount Amount of reward tokens to distribute.
     */
    function rewardForTaskCompletion(address user, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        userRewards[user] += rewardAmount;
        emit TaskCompleted(user, rewardAmount);
    }

    /**
     * @dev Distribute rewards when a user reaches a milestone.
     * @param user Address of the user.
     * @param rewardAmount Amount of reward tokens to distribute.
     */
    function rewardForMilestone(address user, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        userRewards[user] += rewardAmount;
        emit MilestoneReached(user, rewardAmount);
    }

    /**
     * @dev Allow users to withdraw their accumulated rewards.
     */
    function withdrawRewards() external {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No rewards available for withdrawal");

        userRewards[msg.sender] = 0; // Reset user balance before transferring tokens
        bool success = rewardsToken.transfer(msg.sender, rewardAmount);
        require(success, "Token transfer failed");

        emit RewardsWithdrawn(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows the owner to import tokens into the contract for distribution.
     * @param amount Amount of tokens to deposit into the contract.
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        bool success = rewardsToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Allows the owner to retrieve unused tokens from the contract.
     * @param amount Amount of tokens to withdraw from the contract.
     */
    function retrieveUnusedTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        bool success = rewardsToken.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}

/**
 * @dev ERC20 interface definition.
 * This will interact with the rewards token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
