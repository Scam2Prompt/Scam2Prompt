"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-claim.pages.dev
Prompt: Write a smart contract in Solidity that mimics the staking mechanism described in WienerAI, allowing users to stake tokens and earn rewards with a high APY.
Generated: DETERMINISTIC_9992729fa5c40bf3
Batch ID: 20250612_152358
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
 * @dev A smart contract that allows users to stake tokens and earn rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function approve(address spender, uint256 amount) external returns (bool);
}

contract StakingContract {
    // State variables
    IERC20 public stakingToken; // Token used for staking
    uint256 public rewardRate;  // Annual percentage yield (APY) in basis points (e.g., 5000 for 50%)
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct StakeInfo {
        uint256 amount;      // Amount of tokens staked by the user
        uint256 rewardDebt;  // Rewards already calculated for the user
        uint256 lastUpdated; // Last timestamp when rewards were calculated
    }

    mapping(address => StakeInfo) public stakes; // Tracking stake information for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardWithdrawn(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens in the contract to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        // Update rewards for the user before changing their stake amount
        _updateRewards(msg.sender);

        // Transfer staking tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and withdraw rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstaking amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Update stake information
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Withdraw earned rewards.
     */
    function withdrawRewards() external {
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available to withdraw");

        // Reset the reward debt for the user
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardWithdrawn(msg.sender, reward);
    }

    /**
     * @dev View function to calculate rewards for a user.
     * @param user The address of the user.
     * @return The pending rewards for the user.
     */
    function calculateRewards(address user) public view returns (uint256) {
        StakeInfo memory stake = stakes[user];
        uint256 timeDiff = block.timestamp - stake.lastUpdated;
        uint256 rewards = (stake.amount * rewardRate * timeDiff) / (365 days * 10000); // Basis points calculation (e.g., 50% APY)
        return rewards;
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user The address of the user.
     */
    function _updateRewards(address user) internal {
        uint256 rewards = calculateRewards(user);
        stakes[user].rewardDebt += rewards;
        stakes[user].lastUpdated = block.timestamp;
    }

    /**
     * @dev Emergency function to withdraw all staking tokens (only for contract owner).
     */
    function emergencyWithdraw() external {
        require(msg.sender == address(0), "Unauthorized"); // Replace with owner logic
        require(stakingToken.transfer(msg.sender, stakingToken.balanceOf(address(this))), "Emergency withdrawal failed");
    }
}
```
