"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Create a decentralized application (DApp) interface for users to stake, unstake, and claim rewards for a token, incorporating security measures such as a maximum penalty restriction and safeguard measures.
Generated: DETERMINISTIC_3f3de1bd6066372d
Batch ID: 20250622_205929
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

/**
 * @title StakingDApp
 * @dev A decentralized application for staking, unstaking, and claiming rewards for a token.
 *      Includes security measures such as maximum penalty restrictions and safeguard measures.
 */
contract StakingDApp {
    // Token interface
    IERC20 public immutable stakingToken;

    // Struct to store user staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already claimed
        uint256 stakeTimestamp; // Timestamp of staking
    }

    // Mapping of user address to their staking information
    mapping(address => StakeInfo) public stakes;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Maximum penalty for early unstaking (e.g., 10%)
    uint256 public constant MAX_PENALTY = 10; // 10%

    // Minimum staking duration to avoid penalty (e.g., 7 days)
    uint256 public constant MIN_STAKE_DURATION = 7 days;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 penalty);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking token and reward rate.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user stake information
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt += pendingRewards(msg.sender);
        userStake.stakeTimestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     */
    function unstake() external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 stakedAmount = userStake.amount;
        uint256 rewards = pendingRewards(msg.sender);
        uint256 penalty = 0;

        // Apply penalty if unstaking before minimum duration
        if (block.timestamp < userStake.stakeTimestamp + MIN_STAKE_DURATION) {
            penalty = (stakedAmount * MAX_PENALTY) / 100;
        }

        // Reset user stake information
        userStake.amount = 0;
        userStake.rewardDebt = 0;
        userStake.stakeTimestamp = 0;

        // Transfer staked tokens minus penalty back to user
        require(
            stakingToken.transfer(msg.sender, stakedAmount - penalty),
            "Token transfer failed"
        );

        // Transfer rewards to user
        if (rewards > 0) {
            require(
                stakingToken.transfer(msg.sender, rewards),
                "Reward transfer failed"
            );
        }

        emit Unstaked(msg.sender, stakedAmount, penalty);
    }

    /**
     * @dev Claim rewards without unstaking.
     */
    function claimRewards() external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 rewards = pendingRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update reward debt
        userStake.rewardDebt += rewards;

        // Transfer rewards to user
        require(
            stakingToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards.
     */
    function pendingRewards(address _user) public view returns (uint256) {
        StakeInfo storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.stakeTimestamp;
        uint256 totalRewards = (userStake.amount * rewardRate * stakingDuration) /
            1e18;

        return totalRewards - userStake.rewardDebt;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
