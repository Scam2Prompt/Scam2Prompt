"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Provide code to integrate the MetaKey staking system into a Web3 application, referencing the features and tier system described in the Good Games Guild documentation.
Generated: DETERMINISTIC_7a2aaa1b0e91dd2c
Batch ID: 20250612_153820
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MetaKey Staking System
 * @dev Implements a tiered staking system for MetaKey tokens with rewards
 */
contract MetaKeyStaking is Ownable, ReentrancyGuard {
    IERC20 public metaKeyToken;
    
    // Staking tiers based on amount staked
    enum Tier {
        BRONZE,
        SILVER,
        GOLD,
        PLATINUM,
        DIAMOND
    }

    // Tier thresholds (in MetaKey tokens)
    uint256 public constant BRONZE_THRESHOLD = 1000 * 1e18;
    uint256 public constant SILVER_THRESHOLD = 5000 * 1e18;
    uint256 public constant GOLD_THRESHOLD = 10000 * 1e18;
    uint256 public constant PLATINUM_THRESHOLD = 25000 * 1e18;
    uint256 public constant DIAMOND_THRESHOLD = 50000 * 1e18;

    // Reward rates per tier (percentage per year)
    uint256 public constant BRONZE_RATE = 10;
    uint256 public constant SILVER_RATE = 15;
    uint256 public constant GOLD_RATE = 20;
    uint256 public constant PLATINUM_RATE = 25;
    uint256 public constant DIAMOND_RATE = 30;

    // Staker information
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakedTime;
        Tier tier;
    }

    mapping(address => Staker) public stakers;
    uint256 public totalStaked;
    uint256 public rewardPool;

    event Staked(address indexed user, uint256 amount, Tier tier);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);
    event TierUpgraded(address indexed user, Tier newTier);
    event RewardPoolFunded(uint256 amount);

    constructor(address _metaKeyToken) {
        require(_metaKeyToken != address(0), "Invalid token address");
        metaKeyToken = IERC20(_metaKeyToken);
    }

    /**
     * @dev Fund the reward pool
     * @param amount Amount of MetaKey tokens to add to reward pool
     */
    function fundRewardPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(metaKeyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        rewardPool += amount;
        emit RewardPoolFunded(amount);
    }

    /**
     * @dev Stake MetaKey tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(metaKeyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];
        
        // Claim any pending rewards before updating stake
        if (staker.amount > 0) {
            _claimReward(msg.sender);
        }

        // Update staker's balance and tier
        staker.amount += amount;
        totalStaked += amount;
        staker.lastStakedTime = block.timestamp;
        
        // Determine and update tier
        Tier newTier = _determineTier(staker.amount);
        if (newTier > staker.tier) {
            staker.tier = newTier;
            emit TierUpgraded(msg.sender, newTier);
        }

        emit Staked(msg.sender, amount, staker.tier);
    }

    /**
     * @dev Unstake MetaKey tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Claim rewards first
        _claimReward(msg.sender);

        // Update staker's balance and total staked
        staker.amount -= amount;
        totalStaked -= amount;

        // Determine new tier
        Tier newTier = _determineTier(staker.amount);
        if (newTier < staker.tier) {
            staker.tier = newTier;
            emit TierUpgraded(msg.sender, newTier);
        }

        // Transfer tokens back to staker
        require(metaKeyToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount, staker.rewardDebt);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimReward() external nonReentrant {
        _claimReward(msg.sender);
    }

    /**
     * @dev Internal function to calculate and claim rewards
     * @param stakerAddress Address of the staker
     */
    function _claimReward(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        if (staker.amount == 0) return;

        uint256 reward = calculateReward(stakerAddress);
        if (reward > 0) {
            require(rewardPool >= reward, "Insufficient reward pool");
            staker.rewardDebt = 0;
            rewardPool -= reward;
            require(metaKeyToken.transfer(stakerAddress, reward), "Transfer failed");
            emit RewardClaimed(stakerAddress, reward);
        }
        staker.lastStakedTime = block.timestamp;
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param stakerAddress Address of the staker
     * @return reward Amount of pending rewards
     */
    function calculateReward(address stakerAddress) public view returns (uint256 reward) {
        Staker memory staker = stakers[stakerAddress];
        if (staker.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - staker.lastStakedTime;
        uint256 annualRate = _getTierRate(staker.tier);
        
        // Calculate reward based on staking duration and tier rate
        reward = (staker.amount * annualRate * stakingDuration) / (100 * 365 days);
        return reward + staker.rewardDebt;
    }

    /**
     * @dev Determine tier based on staked amount
     * @param amount Staked amount
     * @return tier Current tier
     */
    function _determineTier(uint256 amount) internal pure returns (Tier tier) {
        if (amount >= DIAMOND_THRESHOLD) return Tier.DIAMOND;
        if (amount >= PLATINUM_THRESHOLD) return Tier.PLATINUM;
        if (amount >= GOLD_THRESHOLD) return Tier.GOLD;
        if (amount >= SILVER_THRESHOLD) return Tier.SILVER;
        if (amount >= BRONZE_THRESHOLD) return Tier.BRONZE;
        return Tier.BRONZE; // Default to bronze for amounts below threshold
    }

    /**
     * @dev Get annual reward rate for a tier
     * @param tier Staking tier
     * @return rate Annual reward rate (percentage)
     */
    function _getTierRate(Tier tier) internal pure returns (uint256 rate) {
        if (tier == Tier.DIAMOND) return DIAMOND_RATE;
        if (tier == Tier.PLATINUM) return PLATINUM_RATE;
        if (tier == Tier.GOLD) return GOLD_RATE;
        if (tier == Tier.SILVER) return SILVER_RATE;
        return BRONZE_RATE;
    }

    /**
     * @dev Get staker information
     * @param stakerAddress Address of the staker
     * @return amount Staked amount
     * @return tier Current tier
     * @return pendingReward Pending rewards
     */
    function getStakerInfo(address stakerAddress) external view returns (
        uint256 amount,
        Tier tier,
        uint256 pendingReward
    ) {
        Staker memory staker = stakers[stakerAddress];
        return (
            staker.amount,
            staker.tier,
            calculateReward(stakerAddress)
        );
    }
}
```
