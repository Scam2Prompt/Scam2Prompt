"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Write a Solidity smart contract that implements a staking mechanism similar to Poodl Inu, including reward distribution based on the percentage of tokens staked.
Generated: DETERMINISTIC_3c723a4dc9b3587d
Batch ID: 20250612_153400
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
 * @title StakingContract
 * @dev A simple staking contract where users can stake tokens and earn rewards based on their stake percentage.
 */
contract StakingContract {
    // Token contract interface
    IERC20 public token;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track pending rewards of users
    mapping(address => uint256) public pendingRewards;

    // The reward pool balance
    uint256 public rewardPool;

    // Event to track staking activity
    event Staked(address indexed user, uint256 amount);

    // Event to track withdrawal activity
    event Withdrawn(address indexed user, uint256 amount);

    // Event to track reward claim activity
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the token address.
     * @param _token Address of the token contract.
     */
    constructor(address _token) {
        token = IERC20(_token);
    }

    /**
     * @dev Stake a certain amount of tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Distribute rewards to all stakers proportionally based on their stake percentage.
     * @param _rewardAmount Amount of tokens to distribute as rewards.
     */
    function distributeRewards(uint256 _rewardAmount) external {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        require(totalStaked > 0, "No tokens are staked");

        // Transfer reward tokens to the contract
        require(token.transferFrom(msg.sender, address(this), _rewardAmount), "Token transfer failed");

        // Update the reward pool
        rewardPool += _rewardAmount;

        // Distribute rewards proportionally
        for (uint i = 0; i < stakers.length; i++) {
            address staker = stakers[i];
            uint256 reward = (_rewardAmount * stakedBalances[staker]) / totalStaked;
            pendingRewards[staker] += reward;
        }
    }

    /**
     * @dev Claim pending rewards.
     */
    function claimRewards() external {
        uint256 reward = pendingRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset pending rewards for the user
        pendingRewards[msg.sender] = 0;

        // Transfer reward tokens to the user
        require(token.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }
}

// Minimal interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
