"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Generate a smart contract for BlastUP's tier-based staking system, ensuring token holders receive rewards and loyalty benefits based on their staked amount.
Generated: DETERMINISTIC_02fe144a8f8031f0
Batch ID: 20250612_152924
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BlastUP Staking Smart Contract
 * @dev Implements a tier-based staking system where token holders can stake their tokens to receive rewards and loyalty benefits.
 */
contract BlastUPStaking is Ownable, ReentrancyGuard {
    // Struct to define a staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 tier;
        uint256 lastUpdate;
    }

    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward token
    IERC20 public rewardToken;

    // Staking token
    IERC20 public stakingToken;

    // Reward rate per tier
    mapping(uint256 => uint256) public rewardRates;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to check if the user has staked
    modifier hasStaked() {
        require(stakers[msg.sender].amountStaked > 0, "No staked tokens");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with staking and reward tokens.
     * @param _stakingToken Address of the staking token (e.g., ERC20)
     * @param _rewardToken Address of the reward token (e.g., ERC20)
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;

        // Define reward rates for different tiers
        rewardRates[1] = 100; // Tier 1: 100 rewards per staked token
        rewardRates[2] = 200; // Tier 2: 200 rewards per staked token
        rewardRates[3] = 300; // Tier 3: 300 rewards per staked token
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        totalStaked += amount;

        // Update tier based on amount staked
        updateTier(msg.sender);
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens.
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant hasStaked {
        require(amount > 0 && amount <= stakers[msg.sender].amountStaked, "Invalid unstake amount");

        // Calculate and claim rewards before unstaking
        claimRewards();

        // Update the user's staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards for the staker.
     */
    function claimRewards() public nonReentrant hasStaked {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingReward = calculateRewards(msg.sender);

        require(pendingReward > 0, "No rewards to claim");
        
        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, pendingReward);
        staker.rewardDebt += pendingReward;

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Function to calculate rewards based on staked amount and tier.
     * @param user Address of the user
     * @return uint256 Amount of rewards to be claimed
     */
    function calculateRewards(address user) internal view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 tierRewardRate = rewardRates[staker.tier];
        return (staker.amountStaked * tierRewardRate) - staker.rewardDebt;
    }

    /**
     * @dev Update the staker's tier based on their staked amount.
     * @param user Address of the user
     */
    function updateTier(address user) internal {
        Staker storage staker = stakers[user];
        if (staker.amountStaked >= 1000 * 10 ** 18) {
            staker.tier = 3; // Tier 3 for 1000+ staked tokens
        } else if (staker.amountStaked >= 500 * 10 ** 18) {
            staker.tier = 2; // Tier 2 for 500+ staked tokens
        } else {
            staker.tier = 1; // Tier 1 for less than 500 staked tokens
        }
    }

    /**
     * @dev Function to withdraw the contract's balance of the reward token (only owner).
     */
    function withdrawRewardTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        rewardToken.transfer(owner(), amount);
    }

    /**
     * @dev Function to withdraw the contract's balance of the staking token (only owner).
     */
    function withdrawStakingTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        stakingToken.transfer(owner(), amount);
    }
}
```
