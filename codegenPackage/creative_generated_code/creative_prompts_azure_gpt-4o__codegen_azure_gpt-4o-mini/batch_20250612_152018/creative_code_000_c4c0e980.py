"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareairdrop.com
Prompt: Write a smart contract using Flare's EVM-compatible platform to create a decentralized liquidity pool that supports staking and yield farming.
Generated: DETERMINISTIC_c4c0e9809e5f06d1
Batch ID: 20250612_152018
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Main contract for the decentralized liquidity pool
contract LiquidityPool is Ownable {
    using SafeMath for uint256;

    // Struct to represent a user's stake
    struct UserStake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their stakes
    mapping(address => UserStake) public userStakes;

    // Variables for the staking token and reward token
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Variables for managing pool state
    uint256 public totalStaked; // Total amount staked in the pool
    uint256 public accRewardPerShare; // Accumulated rewards per share
    uint256 public rewardsPerBlock; // Rewards distributed per block
    uint256 public lastRewardBlock; // Last block when rewards were distributed

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with staking and reward tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardsPerBlock) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardsPerBlock = _rewardsPerBlock;
        lastRewardBlock = block.number;
    }

    // Function to stake tokens in the liquidity pool
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Update pending rewards before staking
        updatePool();

        UserStake storage user = userStakes[msg.sender];
        // Update user stake amount and total staked
        user.amount = user.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to un-stake tokens from the liquidity pool
    function unstake(uint256 _amount) external {
        UserStake storage user = userStakes[msg.sender];
        require(user.amount >= _amount, "Insufficient stake amount");
        
        // Update pending rewards before unstaking
        updatePool();

        // Update user stake amount and total staked
        user.amount = user.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updatePool();
        UserStake storage user = userStakes[msg.sender];
        
        uint256 pendingRewards = user.amount.mul(accRewardPerShare).div(1e12).sub(user.rewardDebt);
        require(pendingRewards > 0, "No rewards to claim");

        // Update user's reward debt
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e12);
        
        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Internal function to update the pool's state and distribute rewards
    function updatePool() internal {
        if (block.number <= lastRewardBlock) {
            return; // No rewards to distribute if no new blocks
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number; // Update block number if no stakes
            return;
        }

        // Calculate the number of new rewards
        uint256 multiplier = block.number.sub(lastRewardBlock);
        uint256 reward = multiplier.mul(rewardsPerBlock);

        // Update accumulated rewards per share
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e12).div(totalStaked));
        lastRewardBlock = block.number; // Update last reward block
    }
}
```
