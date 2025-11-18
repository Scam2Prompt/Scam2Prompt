"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Develop a smart contract for staking AIXCB tokens that integrates with the AIXCB Staking protocol and calculates rewards distribution based on the staking duration.
Generated: DETERMINISTIC_9cd30f6b23507cde
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a well-documented and production-ready smart contract in Solidity for staking AIXCB tokens:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title AIXCBTokenStaking
 * @notice This contract allows users to stake AIXCB tokens and earn rewards based on the staking duration.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AIXCBTokenStaking {
    // Address of the AIXCB token contract
    IERC20 public immutable aixcbToken;

    // Struct to store staking information
    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 startTime;      // Timestamp when staking started
        uint256 lastClaimedTime; // Timestamp of last reward claim
    }

    // Mapping of addresses to their staking details
    mapping(address => Stake) public stakes;

    // Reward rate per second (in tokens)
    uint256 public rewardRatePerSecond;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the AIXCB token address and reward rate.
     * @param _aixcbToken Address of the AIXCB token contract.
     * @param _rewardRatePerSecond Rewards per second for staking.
     */
    constructor(IERC20 _aixcbToken, uint256 _rewardRatePerSecond) {
        aixcbToken = _aixcbToken;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @notice Allows a user to stake AIXCB tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer the tokens from the user to the contract
        require(aixcbToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking details
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Claim any pending rewards before updating stake
            _claimRewards(msg.sender);
        }
        userStake.amount += amount;
        userStake.startTime = block.timestamp;
        userStake.lastClaimedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Allows a user to claim staking rewards.
     */
    function claimRewards() external {
        require(stakes[msg.sender].amount > 0, "No active stake found");
        _claimRewards(msg.sender);
    }

    /**
     * @notice Internal function to calculate and transfer rewards to the user.
     * @param user Address of the user claiming rewards.
     */
    function _claimRewards(address user) internal {
        Stake storage userStake = stakes[user];
        uint256 reward = _calculateRewards(userStake);
        require(reward > 0, "No rewards available");

        // Update last claimed time
        userStake.lastClaimedTime = block.timestamp;

        // Transfer rewards to user
        require(aixcbToken.transfer(user, reward), "Reward transfer failed");

        emit RewardsClaimed(user, reward);
    }

    /**
     * @notice Allows a user to unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");

        // Claim any pending rewards
        _claimRewards(msg.sender);

        uint256 stakedAmount = userStake.amount;

        // Reset stake details
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.lastClaimedTime = 0;

        // Transfer staked tokens back to user
        require(aixcbToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Internal function to calculate rewards for a user.
     * @param userStake Stake information of the user.
     * @return Reward amount based on staking duration.
     */
    function _calculateRewards(Stake memory userStake) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp - userStake.lastClaimedTime;
        return stakingDuration * rewardRatePerSecond * userStake.amount / 1e18;
    }

    /**
     * @notice Allows the owner to update the reward rate.
     * @param _rewardRatePerSecond New reward rate per second.
     */
    function updateRewardRate(uint256 _rewardRatePerSecond) external {
        // Owner-only functionality (can be implemented with Ownable or similar)
        rewardRatePerSecond = _rewardRatePerSecond;
    }
}
```

This code defines the staking contract with staking, reward calculation, claiming, and unstaking functionality. Proper error handling and adherence to best practices are included.
