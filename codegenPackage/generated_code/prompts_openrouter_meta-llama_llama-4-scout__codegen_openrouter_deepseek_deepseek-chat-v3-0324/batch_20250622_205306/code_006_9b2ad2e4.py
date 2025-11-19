"""
Generated Code Metadata:
========================
Original URL: https://dappssync.pages.dev
Prompt: Implement a staking system for a Dapp, handling issues such as staking problems, locked accounts, and trading wallet issues, using a secure and decentralized protocol.
Generated: DETERMINISTIC_9b2ad2e42ba2187a
Batch ID: 20250622_205306
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Secure Staking Contract
 * @dev Implements a decentralized staking system with security features
 */
contract StakingSystem is ReentrancyGuard, Ownable {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastRewardCalculated;
        bool isActive;
    }

    mapping(address => Stake) public stakes;
    mapping(address => bool) public lockedAccounts;

    uint256 public stakingDuration = 30 days;
    uint256 public rewardRate = 10; // 10% annual reward
    uint256 public totalStaked;
    uint256 public minimumStakeAmount = 100 * 10**18; // 100 tokens

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event AccountLocked(address indexed user);
    event AccountUnlocked(address indexed user);

    /**
     * @dev Constructor initializes the staking and reward tokens
     * @param _stakingToken Address of the token to be staked
     * @param _rewardToken Address of the reward token
     */
    constructor(address _stakingToken, address _rewardToken) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(!lockedAccounts[msg.sender], "Account is locked");
        require(amount >= minimumStakeAmount, "Amount below minimum stake");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(stakingToken.allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");

        if (stakes[msg.sender].isActive) {
            _calculateReward(msg.sender);
            stakes[msg.sender].amount += amount;
        } else {
            stakes[msg.sender] = Stake({
                amount: amount,
                stakedAt: block.timestamp,
                lastRewardCalculated: block.timestamp,
                isActive: true
            });
        }

        totalStaked += amount;
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(!lockedAccounts[msg.sender], "Account is locked");
        require(stakes[msg.sender].isActive, "No active stake");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        require(block.timestamp >= stakes[msg.sender].stakedAt + stakingDuration, "Staking period not completed");

        _calculateReward(msg.sender);
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        if (stakes[msg.sender].amount == 0) {
            stakes[msg.sender].isActive = false;
        }

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimReward() external nonReentrant {
        require(!lockedAccounts[msg.sender], "Account is locked");
        require(stakes[msg.sender].isActive, "No active stake");

        uint256 reward = _calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        require(rewardToken.balanceOf(address(this)) >= reward, "Insufficient reward tokens");

        stakes[msg.sender].lastRewardCalculated = block.timestamp;
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
        
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate reward for a staker
     * @param staker Address of the staker
     * @return reward Calculated reward amount
     */
    function _calculateReward(address staker) internal returns (uint256 reward) {
        Stake storage userStake = stakes[staker];
        if (!userStake.isActive) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastRewardCalculated;
        reward = (userStake.amount * rewardRate * timeElapsed) / (365 days * 100);
        return reward;
    }

    /**
     * @dev Lock an account (admin only)
     * @param account Address to lock
     */
    function lockAccount(address account) external onlyOwner {
        require(!lockedAccounts[account], "Account already locked");
        lockedAccounts[account] = true;
        emit AccountLocked(account);
    }

    /**
     * @dev Unlock an account (admin only)
     * @param account Address to unlock
     */
    function unlockAccount(address account) external onlyOwner {
        require(lockedAccounts[account], "Account not locked");
        lockedAccounts[account] = false;
        emit AccountUnlocked(account);
    }

    /**
     * @dev Update staking duration (admin only)
     * @param newDuration New staking duration in seconds
     */
    function updateStakingDuration(uint256 newDuration) external onlyOwner {
        require(newDuration > 0, "Duration must be positive");
        stakingDuration = newDuration;
    }

    /**
     * @dev Update reward rate (admin only)
     * @param newRate New reward rate (percentage)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    /**
     * @dev Update minimum stake amount (admin only)
     * @param newAmount New minimum stake amount
     */
    function updateMinimumStake(uint256 newAmount) external onlyOwner {
        minimumStakeAmount = newAmount;
    }

    /**
     * @dev Emergency withdraw tokens from contract (admin only)
     * @param tokenAddress Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
