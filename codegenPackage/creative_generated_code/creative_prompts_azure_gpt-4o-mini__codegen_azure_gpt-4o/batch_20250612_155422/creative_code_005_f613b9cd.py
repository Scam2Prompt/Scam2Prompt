"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralised-node.pages.dev
Prompt: What code can I use to facilitate token staking within a decentralized finance platform?
Generated: DETERMINISTIC_f613b9cddfd9dec4
Batch ID: 20250612_155422
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
 * @title TokenStaking
 * @dev A contract to facilitate token staking within a decentralized finance (DeFi) platform.
 */
contract TokenStaking {
    // ERC-20 token interface
    IERC20 public stakingToken;

    // Mapping to track staked balances of each user
    mapping(address => uint256) public stakedBalances;

    // Mapping to track staking timestamps for each user
    mapping(address => uint256) public stakingTimestamps;

    // Reward rate (e.g., 10% annual rate -> 10 / 100 / (365 * 24 * 60 * 60) for per-second rate)
    uint256 public rewardRate = 10; // Example: 10% per year
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Events for logging
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsWithdrawn(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking token.
     * @param _stakingToken Address of the ERC-20 token used for staking.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and withdraw rewards.
     */
    function unstakeTokens() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);

        // Reset user's staking balance and timestamp
        stakedBalances[msg.sender] = 0;
        stakingTimestamps[msg.sender] = 0;

        // Transfer staked tokens back to the user
        bool success = stakingToken.transfer(msg.sender, stakedAmount);
        require(success, "Token transfer failed");

        // Transfer rewards to the user
        if (reward > 0) {
            success = stakingToken.transfer(msg.sender, reward);
            require(success, "Reward transfer failed");
        }

        emit TokensUnstaked(msg.sender, stakedAmount);
        emit RewardsWithdrawn(msg.sender, reward);
    }

    /**
     * @dev Calculate the staking rewards for a user based on time and rate.
     * @param user Address of the user to calculate rewards for.
     * @return reward The calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        uint256 stakedAmount = stakedBalances[user];
        uint256 stakingDuration = block.timestamp - stakingTimestamps[user];

        reward = (stakedAmount * rewardRate * stakingDuration) / (100 * SECONDS_IN_YEAR);
    }

    /**
     * @dev Get the staked balance for a user.
     * @param user Address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}

// Minimal ERC-20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
