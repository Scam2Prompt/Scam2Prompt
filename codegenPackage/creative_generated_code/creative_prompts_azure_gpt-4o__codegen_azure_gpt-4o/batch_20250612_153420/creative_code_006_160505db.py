"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claiming.pages.dev
Prompt: Provide an example of how to use the Ethereum blockchain to deploy a staking contract for DOGE20 tokens that prevents inflation and supports passive rewards, as outlined in the tokenomics section.
Generated: DETERMINISTIC_160505dbed9a602a
Batch ID: 20250612_153420
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
 * @title Doge20TokenStaking
 * @dev A staking contract for DOGE20 tokens that prevents inflation and supports passive rewards.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract Doge20TokenStaking {
    IERC20 public immutable doge20Token; // Reference to the DOGE20 token contract

    uint256 public rewardRate; // Reward rate in tokens per second
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    mapping(address => uint256) public stakedBalance; // Amount of tokens staked by each user
    mapping(address => uint256) public lastUpdated; // Timestamp of the last staking update for each user
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor initializes the contract with the token address and reward rate.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _rewardRate Reward rate in tokens per second.
     */
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        require(address(_doge20Token) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake DOGE20 tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Update rewards before modifying balances
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking balance and total staked
        stakedBalance[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens. Rewards must be claimed separately.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before modifying balances
        _updateRewards(msg.sender);

        // Update staking balance and total staked
        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens from the contract to the user
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset the user's rewards balance
        rewards[msg.sender] = 0;

        // Transfer rewards from the contract to the user
        require(doge20Token.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        uint256 timeElapsed = block.timestamp - lastUpdated[user];
        if (timeElapsed > 0) {
            rewards[user] += stakedBalance[user] * rewardRate * timeElapsed / 1e18;
            lastUpdated[user] = block.timestamp;
        }
    }

    /**
     * @dev Get the total rewards earned by a user (including unclaimed rewards).
     * @param user Address of the user.
     * @return Total rewards earned.
     */
    function totalRewards(address user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdated[user];
        uint256 pendingRewards = stakedBalance[user] * rewardRate * timeElapsed / 1e18;
        return rewards[user] + pendingRewards;
    }
}
```
