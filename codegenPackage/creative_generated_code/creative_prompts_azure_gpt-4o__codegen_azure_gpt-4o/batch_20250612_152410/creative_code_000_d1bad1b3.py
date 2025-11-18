"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcetfcoinn.pages.dev
Prompt: Write an Ethereum smart contract for staking BTCETF tokens, allowing users to lock tokens and earn rewards based on the total staked amount, as described in the BTCETF roadmap.
Generated: DETERMINISTIC_d1bad1b3396e866f
Batch ID: 20250612_152410
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
 * @title BTCETF Staking Contract
 * @dev This contract allows users to stake BTCETF tokens and earn rewards based on the total staked amount.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BTCETFStaking {
    // Token used for staking
    IERC20 public immutable btcetfToken;

    // Reward rate, e.g., 100 means 1% reward per staking period
    uint256 public rewardRate;

    // Duration for the staking period in seconds
    uint256 public stakingPeriod;

    // Tracks the total staked balance across all users
    uint256 public totalStaked;

    // Struct to store user staking information
    struct Staker {
        uint256 stakedAmount;
        uint256 stakingStart;
        uint256 rewardsClaimed;
    }

    // Mapping from user address to their staking information
    mapping(address => Staker) public stakers;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor initializes the staking contract.
     * @param tokenAddress Address of the BTCETF token contract.
     * @param _rewardRate Reward rate for staking.
     * @param _stakingPeriod Duration of the staking period in seconds.
     */
    constructor(
        address tokenAddress,
        uint256 _rewardRate,
        uint256 _stakingPeriod
    ) {
        require(tokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        require(_stakingPeriod > 0, "Staking period must be greater than zero");

        btcetfToken = IERC20(tokenAddress);
        rewardRate = _rewardRate;
        stakingPeriod = _stakingPeriod;
    }

    /**
     * @dev Stake BTCETF tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];

        // Transfer tokens from the user to the contract
        require(
            btcetfToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        if (staker.stakedAmount > 0) {
            // Claim pending rewards if user already has staked tokens
            _claimRewards(msg.sender);
        }

        // Update user's staking information
        staker.stakedAmount += amount;
        staker.stakingStart = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake BTCETF tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than zero");
        require(staker.stakedAmount >= amount, "Insufficient staked balance");

        // Claim pending rewards before unstaking
        _claimRewards(msg.sender);

        // Update user's staking information
        staker.stakedAmount -= amount;

        // Update total staked amount
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(btcetfToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and distribute rewards.
     * @param user Address of the user claiming rewards.
     */
    function _claimRewards(address user) internal {
        Staker storage staker = stakers[user];

        // Calculate the reward
        uint256 stakingDuration = block.timestamp - staker.stakingStart;
        uint256 reward = (staker.stakedAmount * rewardRate * stakingDuration) / (stakingPeriod * 100);

        require(reward > 0, "No rewards to claim");

        // Reset staking start time
        staker.stakingStart = block.timestamp;

        // Update rewards claimed by the user
        staker.rewardsClaimed += reward;

        // Transfer rewards to the user
        require(btcetfToken.transfer(user, reward), "Reward transfer failed");

        emit RewardsClaimed(user, reward);
    }

    /**
     * @dev Get pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards amount.
     */
    function getPendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 stakingDuration = block.timestamp - staker.stakingStart;
        uint256 reward = (staker.stakedAmount * rewardRate * stakingDuration) / (stakingPeriod * 100);
        return reward;
    }
}
```
