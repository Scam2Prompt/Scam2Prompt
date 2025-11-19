"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbbscclaim.pages.dev
Prompt: Create a Solidity smart contract that simulates the Bitcoin block reward schedule for staking BTCBSC tokens, paying out rewards every 10 minutes.
Generated: DETERMINISTIC_a9e5dbe58ff5bb60
Batch ID: 20250612_161112
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
 * @title BTCBSCRewardSchedule
 * @dev A smart contract that simulates the Bitcoin block reward schedule while allowing users to stake BTCBSC tokens and receive rewards.
 */
contract BTCBSCRewardSchedule {
    // Token interface
    IERC20 public btcbscToken;

    // Reward schedule constants based on Bitcoin halving (every 210,000 blocks)
    uint256 public constant INITIAL_REWARD = 50 ether; // Initial reward per 10 minutes.
    uint256 public constant HALVING_INTERVAL = 210000 * 10 minutes; // Halving happens every 210,000 blocks (~4 years).
    uint256 public constant BLOCK_INTERVAL = 10 minutes; // Reward interval.

    // Contract state variables
    uint256 public startTime; // Contract start time.
    uint256 public totalStaked; // Track total staked tokens.
    uint256 public lastRewardTime; // Last time rewards were distributed.

    // User staking data
    struct StakeInfo {
        uint256 amountStaked; // Amount staked by the user.
        uint256 rewardDebt; // Reward debt for the user.
    }
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor
    constructor(address _btcbscToken) {
        btcbscToken = IERC20(_btcbscToken);
        startTime = block.timestamp;
        lastRewardTime = startTime;
    }

    // Modifier to ensure correct timing for rewards
    modifier updateRewards() {
        _updateRewards();
        _;
    }

    /**
     * @dev Stake BTCBSC tokens to earn rewards.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards {
        require(_amount > 0, "Cannot stake zero tokens");

        StakeInfo storage userStake = stakes[msg.sender];

        // Transfer tokens to the contract
        btcbscToken.transferFrom(msg.sender, address(this), _amount);

        // Update user staking data
        userStake.amountStaked += _amount;
        userStake.rewardDebt += _pendingReward(msg.sender);

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake BTCBSC tokens and claim rewards.
     */
    function unstake() external updateRewards {
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 amountToUnstake = userStake.amountStaked;

        require(amountToUnstake > 0, "No tokens to unstake");

        uint256 pendingReward = _pendingReward(msg.sender);

        // Reset user staking data
        userStake.amountStaked = 0;
        userStake.rewardDebt = 0;

        // Transfer staked tokens back to the user
        btcbscToken.transfer(msg.sender, amountToUnstake);

        // Transfer rewards to the user
        if (pendingReward > 0) {
            btcbscToken.transfer(msg.sender, pendingReward);
            emit RewardPaid(msg.sender, pendingReward);
        }

        totalStaked -= amountToUnstake;

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Internal function to update rewards based on the Bitcoin block reward schedule.
     */
    function _updateRewards() internal {
        uint256 elapsedTime = block.timestamp - lastRewardTime;

        // Distribute rewards only for elapsed intervals
        if (elapsedTime >= BLOCK_INTERVAL) {
            uint256 intervals = elapsedTime / BLOCK_INTERVAL;

            // Calculate halved reward based on elapsed time
            uint256 halvingCount = (block.timestamp - startTime) / HALVING_INTERVAL;
            uint256 currentReward = INITIAL_REWARD >> halvingCount; // Halve the reward every interval.

            // Distribute rewards to all stakers proportionally
            lastRewardTime += intervals * BLOCK_INTERVAL;
        }
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user The address of the user.
     * @return The pending reward for the user.
     */
    function _pendingReward(address _user) internal view returns (uint256) {
        StakeInfo storage userStake = stakes[_user];
        uint256 userShare = userStake.amountStaked / totalSt
