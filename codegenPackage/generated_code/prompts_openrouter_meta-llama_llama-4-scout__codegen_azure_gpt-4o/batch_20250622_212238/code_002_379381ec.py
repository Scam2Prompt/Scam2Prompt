"""
Generated Code Metadata:
========================
Original URL: https://bitcoinpepe-en.xyz
Prompt: Develop a smart contract in Solidity for a simple staking and rewards system similar to what is described in the $BPEP tokenomics, where 15% of tokens are allocated for staking and rewards.
Generated: DETERMINISTIC_379381ec5c84530c
Batch ID: 20250622_212238
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
 * @title Staking and Rewards Contract
 * @dev A simple staking and rewards system where 15% of tokens are allocated for staking rewards.
 */
contract StakingRewards {
    // Token interface
    IERC20 public token;

    // Total tokens allocated for staking rewards (15% of total supply)
    uint256 public constant REWARD_ALLOCATION_PERCENTAGE = 15;
    uint256 public rewardPool;

    // Mapping to track staked balances and rewards
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardBalances;

    // Total staked tokens
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address and reward pool.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(IERC20 _token) {
        token = _token;

        // Calculate reward pool as 15% of total token supply
        rewardPool = (token.totalSupply() * REWARD_ALLOCATION_PERCENTAGE) / 100;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Calculate rewards for a user based on their staked balance.
     * @param _user Address of the user.
     * @return Rewards amount.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }

        // Rewards are proportional to the user's staked balance
        return (rewardPool * stakedBalances[_user]) / totalStaked;
    }

    /**
     * @dev Claim rewards for the user.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update reward pool and reward balance
        rewardPool -= rewards;
        rewardBalances[msg.sender] += rewards;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param _user Address of the user.
     * @return Staked balance.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Get the reward balance of a user.
     * @param _user Address of the user.
     * @return Reward balance.
     */
    function getRewardBalance(address _user) external view returns (uint256) {
        return rewardBalances[_user];
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
