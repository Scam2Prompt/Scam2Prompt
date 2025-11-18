"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Write a smart contract in Solidity for a staking pool that operates on the Linea network, supports compounding rewards, and adjusts investor tiers based on staking duration, similar to the pools described on SidusPad.
Generated: DETERMINISTIC_4d26f8820ab267d3
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title StakingPool
 * @dev A smart contract for a staking pool with compounding rewards and tier adjustment based on staking duration.
 * Designed to operate on the Linea network.
 */
contract StakingPool {
    // Struct to hold information about an individual staker
    struct Staker {
        uint256 amountStaked;     // Amount staked by the user
        uint256 rewards;          // Accumulated rewards
        uint256 stakingStartTime; // Timestamp when staking started
        uint256 lastUpdated;      // Last time rewards were updated
        uint8 tier;               // Investor tier based on staking duration
    }

    // Tier durations in seconds (example: 30 days, 90 days, 180 days)
    uint256 public constant TIER_1_DURATION = 30 days;
    uint256 public constant TIER_2_DURATION = 90 days;
    uint256 public constant TIER_3_DURATION = 180 days;

    // Reward rate (example: 10% annual rate scaled down for seconds)
    uint256 public constant ANNUAL_REWARD_RATE = 10; // 10%
    uint256 public constant SECONDS_IN_YEAR = 365 days;
    
    // Owner of the contract
    address public owner;

    // Mapping to store stakers' information
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 rewards);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Modifier to ensure positive staking amounts
    modifier positiveAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake tokens in the pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external positiveAmount(amount) {
        Staker storage staker = stakers[msg.sender];

        // Update rewards before modifying stake
        _updateRewards(msg.sender);

        // Update staking details
        staker.amountStaked += amount;
        staker.stakingStartTime = block.timestamp;
        staker.lastUpdated = block.timestamp;

        // Emit the event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        // Update rewards before withdrawing
        _updateRewards(msg.sender);

        uint256 amountToWithdraw = staker.amountStaked;
        staker.amountStaked = 0;

        // Transfer staked tokens back to the user
        // (Assume transfer logic is added here, e.g., ERC20 transfer)

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Allows users to claim accumulated rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Update rewards
        _updateRewards(msg.sender);

        uint256 rewardsToClaim = staker.rewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        staker.rewards = 0;

        // Transfer rewards to the user
        // (Assume transfer logic is added here, e.g., ERC20 transfer)

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Internal function to update rewards for a given staker.
     * @param stakerAddress Address of the staker to update.
     */
    function _updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];

        if (staker.amountStaked > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastUpdated;
            uint256 annualRewards = (staker.amountStaked * ANNUAL_REWARD_RATE) / 100;
            uint256 rewardsAccrued = (annualRewards * timeElapsed) / SECONDS_IN_YEAR;

            staker.rewards += rewardsAccrued;
            staker.lastUpdated = block.timestamp;

            // Update tier based on staking duration
            _updateTier(stakerAddress);
        }
    }

    /**
     * @dev Internal function to update the tier of a staker based on staking duration.
     * @param stakerAddress Address of the staker to update.
     */
    function _updateTier(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        uint256 stakingDuration = block.timestamp - staker.stakingStartTime;

        if (stakingDuration >= TIER_3_DURATION) {
            staker.tier = 3;
        } else if (stakingDuration >= TIER_2_DURATION) {
            staker.tier = 2;
        } else if (stakingDuration >= TIER_1_DURATION) {
            staker.tier = 1;
        } else {
            staker.tier = 0; // Default tier
        }
    }
}
```
