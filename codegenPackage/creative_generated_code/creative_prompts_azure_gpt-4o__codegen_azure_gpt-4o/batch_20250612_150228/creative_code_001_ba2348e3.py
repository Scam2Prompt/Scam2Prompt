"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-im.pages.dev
Prompt: Generate Solidity code for a staking contract that allows users to stake $QUBE tokens and earn rewards from the 5% sell tax reward pool, as described on the InQubeta platform.
Generated: DETERMINISTIC_ba2348e3eb0c86e2
Batch ID: 20250612_150228
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
 * @title InQubeta Staking Contract
 * @notice Allows users to stake $QUBE tokens and earn rewards from the sell tax reward pool.
 * @dev Users can stake, unstake, and claim rewards. Owner can manage reward distribution.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QUBEStaking is Ownable {
    // $QUBE token interface
    IERC20 public qubeToken;

    // Reward pool balance (funded by the 5% sell tax)
    uint256 public rewardPool;

    // Total staked tokens across all users
    uint256 public totalStaked;

    // Struct to track user staking details
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Rewards owed to the user
        uint256 lastUpdated; // Timestamp of the last staking update
    }

    // Mapping to track staking information per user
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardPoolFunded(uint256 amount);

    /**
     * @dev Constructor to initialize the $QUBE token address.
     * @param _qubeToken Address of the $QUBE token contract.
     */
    constructor(IERC20 _qubeToken) {
        qubeToken = _qubeToken;
    }

    /**
     * @notice Stake $QUBE tokens to earn rewards.
     * @param _amount Amount of $QUBE tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        StakeInfo storage userStake = stakes[msg.sender];

        // Calculate pending rewards for the user before updating the stake
        uint256 pendingReward = _calculateReward(msg.sender);
        userStake.rewardDebt += pendingReward;

        // Transfer tokens from the user to the contract
        qubeToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking information
        userStake.amount += _amount;
        userStake.lastUpdated = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $QUBE tokens.
     * @param _amount Amount of $QUBE tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate pending rewards before updating the stake
        uint256 pendingReward = _calculateReward(msg.sender);
        userStake.rewardDebt += pendingReward;

        // Update staking information
        userStake.amount -= _amount;
        userStake.lastUpdated = block.timestamp;

        totalStaked -= _amount;

        // Transfer tokens back to the user
        qubeToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards earned from the reward pool.
     */
    function claimReward() external {
        StakeInfo storage userStake = stakes[msg.sender];

        // Calculate the total reward for the user
        uint256 reward = _calculateReward(msg.sender) + userStake.rewardDebt;

        require(reward > 0, "No rewards available to claim");

        // Reset reward debt and last updated timestamp
        userStake.rewardDebt = 0;
        userStake.lastUpdated = block.timestamp;

        // Transfer the reward from the pool to the user
        require(rewardPool >= reward, "Insufficient reward pool balance");
        rewardPool -= reward;
        qubeToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Fund the reward pool (only callable by the owner).
     * @param _amount Amount of $QUBE tokens to add to the reward pool.
     */
    function fundRewardPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Funding amount must be greater than zero");

        // Transfer tokens from the owner to the reward pool
        qubeToken.transferFrom(msg.sender, address(this), _amount);

        rewardPool += _amount;

        emit RewardPoolFunded(_amount);
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        StakeInfo storage userStake = stakes[_user];

        // Reward calculation logic (example: proportional to staked tokens vs total staked)
        if (totalStaked == 0 || userStake.amount == 0) {
            return 0;
        }

        uint256 userShare = (userStake.amount * 1e18) / totalStaked;
        uint256 elapsedTime = block.timestamp - userStake.lastUpdated;

        // Example reward rate: 5% of the reward pool distributed per year
        uint256 yearlyRewardRate = rewardPool / 100; // 5% reward pool
        uint256 reward = (userShare * yearlyRewardRate * elapsedTime) / (365 days * 1e18);

        return reward;
    }
}
```
