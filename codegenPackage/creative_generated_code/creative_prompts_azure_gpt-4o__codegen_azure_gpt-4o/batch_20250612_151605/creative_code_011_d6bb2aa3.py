"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmpeppe.web.app
Prompt: Write a Solidity smart contract for a tiered staking system that rewards users based on the amount of $MPEPE tokens staked and the duration of staking.
Generated: DETERMINISTIC_d6bb2aa366fc94d9
Batch ID: 20250612_151605
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
 * @title Tiered Staking Contract
 * @dev A staking system that rewards users based on the amount of $MPEPE tokens staked and the duration of staking.
 */
contract TieredStaking {
    IERC20 public mpepeToken;

    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 startTime;    // Timestamp when staking started
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Rewards multipliers based on staking tiers
    uint256 public constant TIER1_AMOUNT = 100 * 10**18; // Tier 1: >= 100 $MPEPE
    uint256 public constant TIER2_AMOUNT = 500 * 10**18; // Tier 2: >= 500 $MPEPE
    uint256 public constant TIER3_AMOUNT = 1000 * 10**18; // Tier 3: >= 1000 $MPEPE

    uint256 public constant TIER1_REWARD_RATE = 1; // 1% reward per month for Tier 1
    uint256 public constant TIER2_REWARD_RATE = 2; // 2% reward per month for Tier 2
    uint256 public constant TIER3_REWARD_RATE = 3; // 3% reward per month for Tier 3

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor
    constructor(address _mpepeToken) {
        require(_mpepeToken != address(0), "Invalid token address");
        mpepeToken = IERC20(_mpepeToken);
    }

    /**
     * @dev Allows users to stake $MPEPE tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to contract
        require(mpepeToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Record staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate reward
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = calculateReward(userStake.amount, stakingDuration);

        // Transfer staked tokens back to user
        require(mpepeToken.transfer(msg.sender, userStake.amount), "Token transfer failed");

        // Transfer rewards to user
        require(mpepeToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);

        // Reset staking information
        delete stakes[msg.sender];
    }

    /**
     * @dev Calculates reward based on staked amount and duration.
     * @param amount The amount of tokens staked.
     * @param duration The staking duration in seconds.
     * @return reward The calculated reward.
     */
    function calculateReward(uint256 amount, uint256 duration) public pure returns (uint256 reward) {
        uint256 monthsStaked = duration / 30 days; // Convert duration to months
        uint256 rewardRate;

        // Determine reward rate based on staking tiers
        if (amount >= TIER3_AMOUNT) {
            rewardRate = TIER3_REWARD_RATE;
        } else if (amount >= TIER2_AMOUNT) {
            rewardRate = TIER2_REWARD_RATE;
        } else if (amount >= TIER1_AMOUNT) {
            rewardRate = TIER1_REWARD_RATE;
        } else {
            rewardRate = 0; // No rewards for amounts below Tier 1
        }

        // Calculate reward
        reward = (amount * rewardRate * monthsStaked) / 100;
    }
}

/**
 * @dev Minimal IERC20 interface for token interactions.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
