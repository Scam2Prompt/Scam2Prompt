"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bogeonbase.pages.dev
Prompt: Develop a smart contract for staking $BOGE tokens on the Base blockchain. Include functionality for depositing tokens, calculating rewards, and withdrawing tokens.
Generated: DETERMINISTIC_5bd32c1053923cbd
Batch ID: 20250612_145619
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
 * @title BOGE Staking Smart Contract
 * @dev A contract for staking BOGE tokens, calculating rewards, and withdrawing tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}

contract BOGEStaking {
    // Address of the BOGE token contract
    IERC20 public immutable bogeToken;

    // Reward rate per second (e.g., 100 BOGE tokens = 100 * 10^18 for 1 reward unit per second)
    uint256 public rewardRate;

    // Struct to hold staking info for each user
    struct Stake {
        uint256 amount; // Amount of BOGE tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastStakedTime; // Timestamp of the last staking action
    }

    mapping(address => Stake) public stakes;

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount, uint256 reward);
    event RewardsClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _bogeToken, uint256 _rewardRate) {
        require(address(_bogeToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        bogeToken = _bogeToken;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Allows users to stake BOGE tokens.
     * @param _amount The number of tokens to stake.
     */
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Calculate pending rewards before updating stake
        uint256 pendingRewards = _calculateRewards(msg.sender);

        // Update staking info
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt += pendingRewards;
        userStake.lastStakedTime = block.timestamp;

        // Transfer tokens from the user to the contract
        require(bogeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @notice Allows users to withdraw staked tokens and rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 pendingRewards = _calculateRewards(msg.sender);

        // Total payout is staked amount + pending rewards
        uint256 totalPayout = userStake.amount + pendingRewards;

        // Reset staking info
        userStake.amount = 0;
        userStake.rewardDebt = 0;
        userStake.lastStakedTime = 0;

        // Transfer tokens back to the user
        require(bogeToken.transfer(msg.sender, totalPayout), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, userStake.amount, pendingRewards);
    }

    /**
     * @notice Allows users to claim only their rewards without withdrawing staked tokens.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 pendingRewards = _calculateRewards(msg.sender);

        require(pendingRewards > 0, "No rewards to claim");

        // Update reward debt
        userStake.rewardDebt += pendingRewards;
        userStake.lastStakedTime = block.timestamp;

        // Transfer rewards to the user
        require(bogeToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @notice Calculates the pending rewards for a user.
     * @param _user The address of the user.
     * @return The amount of pending rewards.
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        Stake memory userStake = stakes[_user];

        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.lastStakedTime;

        // Rewards formula: staked tokens * reward rate * staking duration
        uint256 totalRewards = (userStake.amount * rewardRate * stakingDuration) / 1e18;

        // Subtract rewards already paid out
        return totalRewards - userStake.rewardDebt;
    }
}
```
