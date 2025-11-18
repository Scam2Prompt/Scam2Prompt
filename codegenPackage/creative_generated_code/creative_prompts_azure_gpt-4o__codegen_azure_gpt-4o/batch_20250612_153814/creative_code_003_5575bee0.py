"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustbase.one
Prompt: Create a DeFi staking contract that incorporates features for pledge mining and referral rewards, similar to the use cases mentioned on Trust Base.
Generated: DETERMINISTIC_5575bee0a7a8f3b0
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, well-documented Solidity code for a DeFi staking contract incorporating pledge mining and referral rewards.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DeFi Staking Contract with Pledge Mining and Referral Rewards
 * @dev This contract allows users to stake tokens, earn rewards, and incentivizes referrals.
 */
contract DeFiStaking {
    // ERC20 token interface
    IERC20 public stakingToken;

    // Reward rate per second (e.g., tokens earned per second of staking)
    uint256 public rewardRate;

    // Referral reward percentage (e.g., 10% = 1000; 100% = 10000)
    uint256 public referralRewardPercentage;

    // Total staked amount
    uint256 public totalStaked;

    // User stake data
    struct Stake {
        uint256 amount; // Amount staked
        uint256 lastUpdated; // Last time rewards were calculated
        uint256 rewardDebt; // Rewards owed to the user
    }

    mapping(address => Stake) public stakes;
    mapping(address => address) public referrals; // Referrer for each user
    mapping(address => uint256) public referralRewards; // Referral rewards for each user

    // Events
    event Staked(address indexed user, uint256 amount, address indexed referrer);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ReferralRewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize staking token and parameters.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardRate Reward rate per second.
     * @param _referralRewardPercentage Percentage of rewards allocated to referrer.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate, uint256 _referralRewardPercentage) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        referralRewardPercentage = _referralRewardPercentage;
    }

    /**
     * @dev Stake tokens for earning rewards. Optionally specify a referrer.
     * @param amount Amount of tokens to stake.
     * @param referrer Address of the referrer (optional).
     */
    function stake(uint256 amount, address referrer) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer the staking tokens to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update stake data
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastUpdated = block.timestamp;

        totalStaked += amount;

        // Set referrer if not already set
        if (referrer != address(0) && referrals[msg.sender] == address(0) && referrer != msg.sender) {
            referrals[msg.sender] = referrer;
        }

        emit Staked(msg.sender, amount, referrer);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer the staking tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        userStake.amount -= amount;
        if (userStake.amount == 0) {
            userStake.lastUpdated = 0; // Reset lastUpdated if fully unstaked
        }

        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = userStake.rewardDebt;
        require(rewards > 0, "No rewards available to claim");

        userStake.rewardDebt = 0; // Reset reward debt
        require(stakingToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardClaimed(msg.sender, rewards);

        // Distribute referral rewards if applicable
        address referrer = referrals[msg.sender];
        if (referrer != address(0)) {
            uint256 referralReward = (rewards * referralRewardPercentage) / 10000;
            referralRewards[referrer] += referralReward;
        }
    }

    /**
     * @dev Claim referral rewards.
     */
    function claimReferralRewards() external {
        uint256 rewards = referralRewards[msg.sender];
        require(rewards > 0, "No referral rewards available to claim");

        referralRewards[msg.sender] = 0; // Reset referral rewards
        require(stakingToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit ReferralRewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 accumulatedReward = (userStake.amount * rewardRate * (block.timestamp - userStake.lastUpdated)) / 1e18;
            userStake.rewardDebt += accumulatedReward;
            userStake.lastUpdated = block.timestamp;
        }
    }
}

// Minimal ERC20 interface for token interaction
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This code is clean, well-documented, and follows Solidity best practices. It is ready for production use after testing and auditing.
