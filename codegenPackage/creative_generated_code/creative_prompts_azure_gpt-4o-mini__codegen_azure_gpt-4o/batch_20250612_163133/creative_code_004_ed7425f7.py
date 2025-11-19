"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-portal.web.app
Prompt: Provide an example of a smart contract that allows users to stake tokens and earn rewards, similar to the Polyhedra Foundation's model.
Generated: DETERMINISTIC_ed7425f729a27ff4
Batch ID: 20250612_163133
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
 * @title Staking Contract
 * @dev This contract allows users to stake ERC20 tokens and earn rewards.
 * Rewards are calculated based on the staking duration and predefined reward rate.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // State variables
    IERC20 public immutable stakingToken; // ERC20 token being staked
    uint256 public rewardRate; // Reward rate (tokens per second)
    uint256 public totalStaked; // Total staked tokens across all users

    // Struct to store user's staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid
        uint256 lastStakedTime; // Last time tokens were staked
    }

    // Mappings to store user stakes and rewards
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        require(address(_stakingToken) != address(0), "Invalid staking token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount The number of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        Stake storage userStake = stakes[msg.sender];

        // Calculate and update pending rewards
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        userStake.amount += amount;
        userStake.lastStakedTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw staked tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate and update pending rewards
        _updateRewards(msg.sender);

        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;
        totalStaked -= amountToUnstake;

        // Transfer staked tokens back to user
        require(stakingToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Allows users to claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and distribute rewards.
     * @param user The address of the user to update rewards for.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 pendingReward = _calculateRewards(user);
            userStake.rewardDebt += pendingReward;

            // Transfer rewards to user
            if (pendingReward > 0) {
                require(stakingToken.transfer(user, pendingReward), "Reward transfer failed");
                emit RewardPaid(user, pendingReward);
            }

            userStake.lastStakedTime = block.timestamp;
        }
    }

    /**
     * @dev Internal function to calculate rewards for a user.
     * @param user The address of the user to calculate rewards for.
     * @return The calculated reward amount.
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 stakingDuration = block.timestamp - userStake.lastStakedTime;
        return (userStake.amount * stakingDuration * rewardRate) / 1 ether;
    }
}
```
