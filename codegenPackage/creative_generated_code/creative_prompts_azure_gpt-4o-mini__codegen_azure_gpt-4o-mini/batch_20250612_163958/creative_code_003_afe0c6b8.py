"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Develop a smart contract that allows users to join the BNB Day’s 4YA Ecosystem Celebration and claim rewards based on task completion.
Generated: DETERMINISTIC_afe0c6b8d73b4bf3
Batch ID: 20250612_163958
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title BNBDay4YAEcosystem
 * @dev Smart contract for managing user participation in the BNB Day's 4YA Ecosystem Celebration
 */
contract BNBDay4YAEcosystem is Ownable {
    // Token to be used for rewards
    IERC20 public rewardToken;

    // Struct representing a user
    struct User {
        bool joined;       // Indicates if the user has joined
        uint256 tasksDone; // Count of completed tasks
        bool claimed;      // Indicates if rewards have been claimed
    }

    // Mapping of addresses to user data
    mapping(address => User) public users;

    // Events for logging actions
    event UserJoined(address indexed user);
    event TaskCompleted(address indexed user);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Reward distribution setup
    uint256 public constant REWARD_PER_TASK = 10 * 10**18; // Example reward amount in token's smallest unit

    /**
     * @dev Constructor to set up the reward token.
     * @param _rewardToken Address of the reward token contract.
     */
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    /**
     * @dev Allows a user to join the ecosystem celebration.
     */
    function join() external {
        require(!users[msg.sender].joined, "User already joined.");
        
        users[msg.sender] = User({
            joined: true,
            tasksDone: 0,
            claimed: false
        });

        emit UserJoined(msg.sender);
    }

    /**
     * @dev Allows a user to complete a task.
     */
    function completeTask() external {
        require(users[msg.sender].joined, "User has not joined.");
        require(!users[msg.sender].claimed, "Rewards already claimed.");

        users[msg.sender].tasksDone += 1;

        emit TaskCompleted(msg.sender);
    }

    /**
     * @dev Allows the user to claim rewards based on completed tasks.
     */
    function claimRewards() external {
        User storage user = users[msg.sender];
        
        require(user.joined, "User has not joined.");
        require(!user.claimed, "Rewards already claimed.");

        uint256 rewardAmount = user.tasksDone * REWARD_PER_TASK;

        require(rewardAmount > 0, "No rewards available to claim.");
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient rewards in contract.");

        user.claimed = true;

        // Transfer the reward to the user
        rewardToken.transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract.");

        rewardToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed.");
    }
}
```
