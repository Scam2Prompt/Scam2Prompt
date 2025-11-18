"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fffrfh.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake stETH and earn MOR tokens as rewards, following the staking mechanism described on the Morpheus platform. Ensure the contract includes a 7-day lockup period for stETH deposits and pro-rata MOR emissions.
Generated: DETERMINISTIC_769b02747fc30435
Batch ID: 20250612_151329
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
 * @title StakingContract
 * @dev A smart contract that allows users to stake stETH and earn MOR tokens as rewards.
 * Features include:
 * - Staking mechanism with a 7-day lockup period for stETH deposits.
 * - Pro-rata emission of MOR tokens as rewards based on staking duration and amount.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // State variables
    IERC20 public immutable stETH; // Token to be staked
    IERC20 public immutable MOR;  // Reward token
    uint256 public constant LOCKUP_PERIOD = 7 days; // Lockup period for staked tokens
    uint256 public rewardRatePerSecond; // MOR emission rate per second per stETH token staked

    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their stake details

    uint256 public totalStaked; // Total amount of stETH staked in the contract

    // Events
    event StakeDeposited(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event StakeWithdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stETH, IERC20 _MOR, uint256 _rewardRatePerSecond) {
        stETH = _stETH;
        MOR = _MOR;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Stakes stETH tokens.
     * @param amount Amount of stETH tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        Stake storage userStake = stakes[msg.sender];

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Transfer stETH tokens from the user to the contract
        require(stETH.transferFrom(msg.sender, address(this), amount), "stETH transfer failed");

        // Update the user's stake and total staked amount
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;
        totalStaked += amount;

        emit StakeDeposited(msg.sender, amount);
    }

    /**
     * @dev Claims MOR rewards for the user.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 rewardAmount = userStake.rewardDebt;
        userStake.rewardDebt = 0;

        require(rewardAmount > 0, "No rewards available to claim");

        // Transfer MOR tokens to the user
        require(MOR.transfer(msg.sender, rewardAmount), "MOR transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Withdraws stETH tokens after the lockup period.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero tokens");

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");
        require(block.timestamp >= userStake.timestamp + LOCKUP_PERIOD, "Lockup period not yet over");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Update the user's stake and total staked amount
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer stETH tokens back to the user
        require(stETH.transfer(msg.sender, amount), "stETH transfer failed");

        emit StakeWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 reward = _calculateRewards(user);
            userStake.rewardDebt += reward;
            userStake.timestamp = block.timestamp; // Reset timestamp for reward calculation
        }
    }

    /**
     * @dev Calculates the rewards for a user based on their staked amount and duration.
     * @param user Address of the user.
     * @return rewardAmount Amount of MOR tokens to be rewarded.
     */
    function _calculateRewards(address user) internal view returns (uint256 rewardAmount) {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 stakingDuration = block.timestamp - userStake.timestamp;
            rewardAmount = (userStake.amount * stakingDuration * rewardRatePerSecond) / 1e18;
        }
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param user Address of the user.
     * @return rewardAmount Amount of MOR tokens pending as rewards.
     */
    function pendingRewards(address user) external view returns (uint256 rewardAmount) {
        Stake storage userStake = stakes[user];
        rewardAmount = userStake.rewardDebt + _calculateRewards(user);
    }
}
```
