"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Generate code in Solidity for a staking contract that supports dynamic reward distribution based on token holdings and staking duration, modeled after the MemeVault protocol.
Generated: DETERMINISTIC_4496dc188199549e
Batch ID: 20250612_154133
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
 * @title Staking Contract with Dynamic Reward Distribution
 * @notice This contract allows users to stake tokens and earn rewards based
 *         on their token holdings and staking duration.
 */
contract StakingContract {
    // Token interface for transferring tokens
    IERC20 public immutable stakingToken;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 rewardDebt; // Rewards already paid out or calculated
    }

    // Mapping from user address to their staking details
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (dynamic distribution calculation based on stake duration)
    uint256 public rewardRatePerSecond;

    // Events for tracking activity
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, uint256 _rewardRatePerSecond) {
        stakingToken = _stakingToken; // Token used for staking
        rewardRatePerSecond = _rewardRatePerSecond; // Initial reward rate
    }

    /**
     * @notice Stake tokens in the contract
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        // Update user's staking information
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = calculateReward(msg.sender);

        userStake.rewardDebt += pendingReward; // Update reward debt
        userStake.amount += amount; // Increase staked amount
        userStake.startTime = block.timestamp; // Reset staking timestamp
        totalStaked += amount; // Update total staked tokens

        // Transfer tokens to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked tokens and claim rewards
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amount;
        require(stakedAmount > 0, "No tokens to withdraw");

        uint256 pendingReward = calculateReward(msg.sender);
        uint256 totalReward = userStake.rewardDebt + pendingReward;

        // Reset user's stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardDebt = 0;
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards to user
        require(
            stakingToken.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );
        if (totalReward > 0) {
            require(
                stakingToken.transfer(msg.sender, totalReward),
                "Reward transfer failed"
            );
        }

        emit Withdrawn(msg.sender, stakedAmount);
        emit RewardPaid(msg.sender, totalReward);
    }

    /**
     * @notice Calculate the pending reward for a user based on staking duration and amount
     * @param user The address of the user
     * @return The calculated reward
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0 || userStake.startTime == 0) {
            return 0;
        }

        uint256 duration = block.timestamp - userStake.startTime; // Staking duration
        uint256 reward = (userStake.amount * rewardRatePerSecond * duration) / totalStaked;

        return reward;
    }

    /**
     * @notice Updates the reward rate per second
     * @param newRewardRate New reward rate per second
     */
    function updateRewardRate(uint256 newRewardRate) external {
        // TODO: Add access control for this function (e.g., onlyOwner modifier)
        rewardRatePerSecond = newRewardRate;
    }
}

// Minimal IERC20 interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
