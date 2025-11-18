"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-sophon.com
Prompt: Write a Solidity contract that integrates the SOPH token for staking rewards, following the guidelines provided in the Sophon documentation.
Generated: DETERMINISTIC_6da3afe67190c088
Batch ID: 20250612_152658
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
 * @title SOPH Token Staking Contract
 * @dev This contract allows users to stake SOPH tokens and earn rewards.
 * The contract integrates SOPH token following the guidelines in the Sophon documentation.
 */
interface ISophToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract SophStaking {
    // Address of the SOPH token contract
    ISophToken public sophToken;

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of user addresses to their rewards
    mapping(address => uint256) public rewards;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate per token per second
    uint256 public rewardRate;

    // Mapping to track last update timestamp for each user
    mapping(address => uint256) public lastUpdateTime;

    // Events for staking, withdrawing, and claiming rewards
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with SOPH token address and reward rate.
     * @param _sophToken Address of the SOPH token contract.
     * @param _rewardRate Reward rate per token per second.
     */
    constructor(address _sophToken, uint256 _rewardRate) {
        require(_sophToken != address(0), "Invalid SOPH token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        sophToken = ISophToken(_sophToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for a user.
     * This is called before any state-changing operation.
     * @param user Address of the user.
     */
    modifier updateReward(address user) {
        rewards[user] += _earned(user);
        lastUpdateTime[user] = block.timestamp;
        _;
    }

    /**
     * @dev Allows users to stake SOPH tokens for rewards.
     * @param amount Amount of SOPH tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        require(
            sophToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked SOPH tokens.
     * @param amount Amount of SOPH tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient balance");

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        require(sophToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their earned rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        require(sophToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate earned rewards for a user.
     * @param user Address of the user.
     * @return Earned rewards for the user.
     */
    function _earned(address user) internal view returns (uint256) {
        return
            (stakedBalances[user] *
                rewardRate *
                (block.timestamp - lastUpdateTime[user])) / 1e18;
    }

    /**
     * @dev Returns the total rewards earned by a user.
     * @param user Address of the user.
     * @return Total rewards earned by the user.
     */
    function totalRewards(address user) external view returns (uint256) {
        return rewards[user] + _earned(user);
    }
}
```
