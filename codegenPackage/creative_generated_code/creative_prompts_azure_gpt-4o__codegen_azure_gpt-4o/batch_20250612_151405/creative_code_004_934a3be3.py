"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiland-website.pages.dev
Prompt: Write a smart contract to enable token rewards for users engaging in gamified activities on a decentralized finance platform like DeFi Land.
Generated: DETERMINISTIC_934a3be33f585722
Batch ID: 20250612_151405
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
 * @title TokenRewardContract
 * @dev Smart contract for rewarding users with tokens for engaging in gamified activities
 * on a decentralized finance platform.
 */
contract TokenRewardContract {
    // Address of the token contract used for rewards
    IERC20 public rewardToken;

    // Owner of the contract
    address public owner;

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // Events
    event RewardDistributed(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardToken Address of the token contract used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute rewards to a user.
     * @param user Address of the user to be rewarded.
     * @param amount Amount of tokens to reward the user.
     */
    function distributeReward(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        userRewards[user] += amount;
        emit RewardDistributed(user, amount);
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimReward() external {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance before transferring to prevent reentrancy attack
        userRewards[msg.sender] = 0;

        // Transfer the reward tokens to the user
        require(rewardToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to allow the owner to retrieve excess tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.transfer(owner, amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
