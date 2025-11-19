"""
Generated Code Metadata:
========================
Original URL: https://staking.chainbase.co
Prompt: "How would you implement a staking contract for a new cryptocurrency using Solidity, inspired by platforms like Chainbase?"
Generated: DETERMINISTIC_5008779e0b2de617
Batch ID: 20250622_212001
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
 * @title StakingContract
 * @dev A simple staking contract for a new cryptocurrency.
 * Users can stake tokens, earn rewards, and withdraw their stake.
 */
contract StakingContract {
    // Token interface
    IERC20 public immutable stakingToken;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to their staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to their reward debt
    mapping(address => uint256) public rewardDebt;

    // Last time rewards were updated
    uint256 public lastUpdateTime;

    // Accumulated rewards per token
    uint256 public accRewardPerToken;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the token to be staked.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards before executing a function.
     */
    modifier updateRewards() {
        accRewardPerToken = _calculateAccRewardPerToken();
        lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update user rewards
        _updateUserRewards(msg.sender);

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staked balances
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user rewards
        _updateUserRewards(msg.sender);

        // Update staked balances
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external updateRewards {
        // Update user rewards
        _updateUserRewards(msg.sender);

        uint256 reward = rewardDebt[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        rewardDebt[msg.sender] = 0;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Internal function to update user rewards.
     * @param user Address of the user.
     */
    function _updateUserRewards(address user) internal {
        uint256 userReward = _calculateUserReward(user);
        rewardDebt[user] += userReward;
    }

    /**
     * @dev Calculate accumulated rewards per token.
     * @return Accumulated rewards per token.
     */
    function _calculateAccRewardPerToken() internal view returns (uint256) {
        if (totalStaked == 0) {
            return accRewardPerToken;
        }
        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        return accRewardPerToken + (timeElapsed * rewardRate * 1e18) / totalStaked;
    }

    /**
     * @dev Calculate rewards for a specific user.
     * @param user Address of the user.
     * @return Rewards for the user.
     */
    function _calculateUserReward(address user) internal view returns (uint256) {
        return (stakedBalances[user] * accRewardPerToken) / 1e18 - rewardDebt[user];
    }
}

/**
 * @dev Interface for ERC20 token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
