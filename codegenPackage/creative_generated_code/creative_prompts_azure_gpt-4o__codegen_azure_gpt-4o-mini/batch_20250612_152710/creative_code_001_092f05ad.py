"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Generate Solidity code for a smart contract that mimics the DOGE20 staking mechanism, including features like distributing rewards based on the percentage of the staking pool.
Generated: DETERMINISTIC_092f05adfce60e01
Batch ID: 20250612_152710
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20Staking is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for calculating rewards
    }

    IERC20 public stakingToken; // ERC20 token to be staked
    uint256 public totalStaked; // Total amount staked in the contract
    uint256 public accRewardPerShare; // Accumulated rewards per share
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastRewardBlock; // Last block number when rewards were distributed

    mapping(address => Stake) public stakes; // Mapping of user addresses to their staking information

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        updatePool();
        
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount; // Increase user's staked amount
        userStake.rewardDebt = userStake.amount * accRewardPerShare / 1e12; // Update reward debt

        totalStaked += amount; // Update total staked amount

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        updatePool();

        // Calculate pending rewards before unstaking
        uint256 pendingRewards = (userStake.amount * accRewardPerShare / 1e12) - userStake.rewardDebt;
        if (pendingRewards > 0) {
            // Transfer rewards to the user
            require(stakingToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");
            emit RewardClaimed(msg.sender, pendingRewards);
        }

        // Update user's stake
        userStake.amount -= amount;
        userStake.rewardDebt = userStake.amount * accRewardPerShare / 1e12; // Update reward debt

        totalStaked -= amount; // Update total staked amount

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Internal function to update the pool rewards
    function updatePool() internal {
        if (block.number <= lastRewardBlock) {
            return; // No rewards to distribute
        }

        uint256 multiplier = block.number - lastRewardBlock; // Calculate block multiplier
        uint256 reward = multiplier * rewardRate; // Calculate total rewards
        accRewardPerShare += (reward * 1e12) / totalStaked; // Update accumulated rewards per share

        lastRewardBlock = block.number; // Update last reward block
    }

    // Function to get the user's pending rewards
    function pendingRewards(address user) external view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 currentAccRewardPerShare = accRewardPerShare;

        // Calculate potential rewards if the pool were to be updated now
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 multiplier = block.number - lastRewardBlock;
            uint256 reward = multiplier * rewardRate;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }

        return (userStake.amount * currentAccRewardPerShare / 1e12) - userStake.rewardDebt; // Calculate pending rewards
    }
}
```
