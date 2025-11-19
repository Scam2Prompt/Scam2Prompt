"""
Generated Code Metadata:
========================
Original URL: https://dodgecoiin20.pages.dev
Prompt: Create a Solidity contract that mimics the DOGE20 staking mechanism, distributing rewards based on the percentage of tokens staked.
Generated: DETERMINISTIC_731fd585bd5ce8cf
Batch ID: 20250612_162346
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
 * @title DOGE20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and earn rewards based on the percentage of tokens staked.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DOGE20Staking {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of user addresses to their pending rewards
    mapping(address => uint256) public rewards;

    // Reward pool balance
    uint256 public rewardPool;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws staked tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the DOGE20 token address.
     * @param _doge20Token Address of the DOGE20 token contract.
     */
    constructor(IERC20 _doge20Token) {
        doge20Token = _doge20Token;
    }

    /**
     * @dev Stake DOGE20 tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's staked balance and the total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the user's staked balance and the total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on the user's staked percentage.
     */
    function claimRewards() external {
        uint256 userStaked = stakedBalances[msg.sender];
        require(userStaked > 0, "No staked balance");

        // Calculate the user's reward based on their staked percentage
        uint256 userReward = (rewardPool * userStaked) / totalStaked;
        require(userReward > 0, "No rewards available");

        // Update the reward pool and the user's rewards
        rewardPool -= userReward;
        rewards[msg.sender] += userReward;

        // Transfer the reward to the user
        require(doge20Token.transfer(msg.sender, userReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, userReward);
    }

    /**
     * @dev Add rewards to the reward pool.
     * @param amount Amount of tokens to add to the reward pool.
     */
    function addRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the sender to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the reward pool balance
        rewardPool += amount;
    }

    /**
     * @dev Get the user's staked balance.
     * @param user Address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Get the user's pending rewards.
     * @param user Address of the user.
     * @return The pending rewards of the user.
     */
    function getPendingRewards(address user) external view returns (uint256) {
        uint256 userStaked = stakedBalances[user];
        if (userStaked == 0 || totalStaked == 0) {
            return 0;
        }
        return (rewardPool * userStaked) / totalStaked;
    }
}
```
