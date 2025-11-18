"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Provide a step-by-step guide to implement DOGE20 staking rewards using Ethereum’s Proof-of-Stake network in a smart contract.
Generated: DETERMINISTIC_b13f38ed22e6c908
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DOGE20 token
interface IDOGE20 is IERC20 {
    function mint(address to, uint256 amount) external;
}

// StakingRewards Contract to manage staking and rewards
contract StakingRewards is Ownable {
    // State variables
    IDOGE20 public doge20Token; // Reference to the DOGE20 token
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of tokens staked

    struct Staker {
        uint256 amount; // Amount staked by the user
        uint256 rewardDebt; // User's accumulated rewards
        uint256 lastStakedBlock; // Last block when the user staked
    }

    mapping(address => Staker) public stakers; // Mapping of stakers

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IDOGE20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer DOGE20 tokens from user to contract
        doge20Token.transferFrom(msg.sender, address(this), amount);
        
        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.rewardDebt += pendingRewards(msg.sender);
        staker.lastStakedBlock = block.number;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens and claim rewards
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Update staker information
        staker.rewardDebt += pendingRewards(msg.sender);
        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens back to user
        doge20Token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = pendingRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update staker's reward debt
        staker.rewardDebt += rewards;
        
        // Mint new DOGE20 tokens as rewards
        doge20Token.mint(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate pending rewards for a staker
    function pendingRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 blocksStaked = block.number - staker.lastStakedBlock;
        return (staker.amount * rewardRate * blocksStaked) / 1e18; // Assuming rewards are in a fixed-point format
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to view the amount of tokens staked by a user
    function stakedAmount(address _staker) external view returns (uint256) {
        return stakers[_staker].amount;
    }
}
```
