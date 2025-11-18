"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Write Solidity code for a staking mechanism that offers a 90% APY reward for staked tokens, with a 16-week vesting period for rewards, as outlined in the BTFD staking system.
Generated: DETERMINISTIC_64efff6414626018
Batch ID: 20250612_154029
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
 * @title Staking Contract with 90% APY Rewards and 16-Week Vesting Period
 * @dev This contract enables users to stake their tokens, earn rewards at 90% APY, and claim rewards after a 16-week vesting period.
 */
contract StakingContract {
    // State variables
    IERC20 public stakingToken; // Token to be staked
    uint256 public constant APY = 90; // Annual Percentage Yield (90%)
    uint256 public constant VESTING_PERIOD = 16 weeks; // Vesting period for rewards
    uint256 public constant SECONDS_IN_YEAR = 365 days;

    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 reward; // Accrued reward
        uint256 timestamp; // Timestamp of staking
        uint256 vestingEnd; // Timestamp when rewards become claimable
    }

    mapping(address => Stake) public stakes; // Maps each user to their staking details

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @notice Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid staking amount");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // If already staked, calculate and update any pending rewards
        if (userStake.amount > 0) {
            uint256 pendingReward = calculateReward(msg.sender);
            userStake.reward += pendingReward;
        }

        // Update staking information
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;
        userStake.vestingEnd = block.timestamp + VESTING_PERIOD;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens and stop earning rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Calculate unclaimed rewards
        uint256 pendingReward = calculateReward(msg.sender);

        // Transfer staked tokens back to the user
        uint256 stakedAmount = userStake.amount;
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Reset staking information
        userStake.amount = 0;
        userStake.reward += pendingReward;
        userStake.timestamp = 0;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Claim vested rewards after the vesting period.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.vestingEnd <= block.timestamp, "Rewards are still vesting");
        require(userStake.reward > 0, "No rewards to claim");

        uint256 rewardAmount = userStake.reward;

        // Reset rewards
        userStake.reward = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Calculate the pending rewards for a staker.
     * @param _user Address of the staker.
     * @return Pending rewards for the user.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0 || userStake.timestamp == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 yearlyReward = (userStake.amount * APY) / 100;
        uint256 pendingReward = (yearlyReward * stakingDuration) / SECONDS_IN_YEAR;

        return pendingReward;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
