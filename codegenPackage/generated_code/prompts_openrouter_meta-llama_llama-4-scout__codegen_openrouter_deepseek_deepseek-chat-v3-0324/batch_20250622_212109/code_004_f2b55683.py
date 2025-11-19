"""
Generated Code Metadata:
========================
Original URL: https://stekecoredao.org
Prompt: Design a staking strategy for a decentralized finance (DeFi) application on CoreDAO, taking into account the 7.88% reward rate for stCORE and the role of CoreDAO in DeFi and Web3.
Generated: DETERMINISTIC_f2b556837e9ebb08
Batch ID: 20250622_212109
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CoreDAOStakingStrategy
 * @dev A staking contract for stCORE tokens with a 7.88% annual reward rate
 * Features:
 * - Stake stCORE tokens
 * - Claim rewards
 * - Withdraw staked tokens
 * - Compound rewards
 * - Admin functions for emergency stops and reward rate updates
 */
contract CoreDAOStakingStrategy is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // stCORE token interface
    IERC20 public stCORE;

    // Staking parameters
    uint256 public constant SECONDS_IN_YEAR = 31536000; // 365 days
    uint256 public rewardRate = 788; // 7.88% in basis points (1 = 0.01%)
    uint256 public totalStaked;
    bool public isActive = true;

    // User staking data
    struct Stake {
        uint256 amount;
        uint256 lastUpdateTime;
        uint256 rewardDebt;
    }
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyStop(bool isActive);

    /**
     * @dev Initialize the staking contract with stCORE token address
     * @param _stCORE Address of the stCORE token contract
     */
    constructor(address _stCORE) {
        require(_stCORE != address(0), "Invalid token address");
        stCORE = IERC20(_stCORE);
    }

    /**
     * @dev Stake stCORE tokens to earn rewards
     * @param amount Amount of stCORE to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(isActive, "Staking is currently paused");
        require(amount > 0, "Amount must be greater than 0");

        // Update existing rewards before new stake
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        stCORE.safeTransferFrom(msg.sender, address(this), amount);

        // Update staking data
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastUpdateTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked stCORE tokens
     * @param amount Amount of stCORE to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");

        // Update rewards before withdrawal
        _updateRewards(msg.sender);

        // Update staking data
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stCORE.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = userStake.rewardDebt;
        require(rewards > 0, "No rewards to claim");

        userStake.rewardDebt = 0;
        stCORE.safeTransfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Compound rewards by adding them to the staked balance
     */
    function compoundRewards() external nonReentrant {
        _updateRewards(msg.sender);
        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = userStake.rewardDebt;
        require(rewards > 0, "No rewards to compound");

        userStake.rewardDebt = 0;
        userStake.amount += rewards;
        totalStaked += rewards;
        userStake.lastUpdateTime = block.timestamp;

        emit Staked(msg.sender, rewards);
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdateTime;
        uint256 annualReward = (userStake.amount * rewardRate) / 10000;
        uint256 pending = (annualReward * timeElapsed) / SECONDS_IN_YEAR;
        return pending + userStake.rewardDebt;
    }

    /**
     * @dev Internal function to update user rewards
     * @param user Address of the user
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            userStake.lastUpdateTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - userStake.lastUpdateTime;
        uint256 annualReward = (userStake.amount * rewardRate) / 10000;
        uint256 pending = (annualReward * timeElapsed) / SECONDS_IN_YEAR;

        userStake.rewardDebt += pending;
        userStake.lastUpdateTime = block.timestamp;
    }

    // Admin functions

    /**
     * @dev Update the reward rate (only owner)
     * @param newRate New reward rate in basis points (1 = 0.01%)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 10000, "Rate cannot exceed 100%");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Toggle staking activity (only owner)
     * @param _isActive New staking status
     */
    function setActive(bool _isActive) external onlyOwner {
        isActive = _isActive;
        emit EmergencyStop(!_isActive);
    }

    /**
     * @dev Emergency withdraw all stCORE tokens (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stCORE.balanceOf(address(this));
        stCORE.safeTransfer(owner(), balance);
    }
}
```
