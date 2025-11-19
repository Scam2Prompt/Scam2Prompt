"""
Generated Code Metadata:
========================
Original URL: https://kodiak-finance.org
Prompt: Write a Solidity smart contract that incorporates security protocols similar to Kodiak Finance's approach to protecting investors’ assets during yield farming activities.
Generated: DETERMINISTIC_2907d3521a3b6135
Batch ID: 20250612_155106
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title SecureYieldFarming
 * @dev A secure yield farming contract with investor protection mechanisms
 */
contract SecureYieldFarming is Ownable, ReentrancyGuard, Pausable {
    using SafeERC20 for IERC20;

    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastDepositTime;
    }

    // The reward token
    IERC20 public rewardToken;
    // The staking token
    IERC20 public stakingToken;
    // Reward tokens created per block
    uint256 public rewardPerBlock;
    // Start block when rewards start accumulating
    uint256 public startBlock;
    // Last block when rewards were calculated
    uint256 public lastRewardBlock;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    // Total staked amount
    uint256 public totalStaked;
    // Emergency withdrawal fee (basis points)
    uint256 public emergencyWithdrawFee = 500; // 5%
    // Lockup period for deposits (in blocks)
    uint256 public lockupPeriod = 5760; // ~24 hours assuming 15s block time
    // Maximum deposit amount per user
    uint256 public maxDepositAmount = 100000 ether;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event SetEmergencyWithdrawFee(uint256 fee);
    event SetLockupPeriod(uint256 period);
    event SetMaxDepositAmount(uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardPerBlock Reward tokens created per block
     * @param _startBlock Start block when rewards start accumulating
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock
    ) {
        require(address(_stakingToken) != address(0), "Invalid staking token");
        require(address(_rewardToken) != address(0), "Invalid reward token");
        require(_rewardPerBlock > 0, "Invalid reward per block");
        require(_startBlock > block.number, "Start block must be in future");

        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        lastRewardBlock = _startBlock;
    }

    /**
     * @dev Update reward variables
     */
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 reward = blocksSinceLastReward * rewardPerBlock;

        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Deposit staking tokens
     * @param _amount Amount to deposit
     */
    function deposit(uint256 _amount) external nonReentrant whenNotPaused {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            userInfo[msg.sender].amount + _amount <= maxDepositAmount,
            "Exceeds max deposit amount"
        );

        updatePool();

        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) /
                1e12 -
                user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.lastDepositTime = block.timestamp;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked += _amount;

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staking tokens and claim rewards
     * @param _amount Amount to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        require(
            block.timestamp >= user.lastDepositTime + lockupPeriod,
            "Funds are locked"
        );

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) /
            1e12 -
            user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked -= _amount;

        stakingToken.safeTransfer(msg.sender, _amount);
        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Emergency withdraw without rewards (with penalty)
     */
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        uint256 feeAmount = (amount * emergencyWithdrawFee) / 10000;
        uint256 withdrawAmount = amount - feeAmount;

        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, withdrawAmount);
        stakingToken.safeTransfer(owner(), feeAmount);

        emit EmergencyWithdraw(msg.sender, withdrawAmount);
    }

    /**
     * @dev Safe reward transfer function
     * @param _to Address to transfer to
     * @param _amount Amount to transfer
     */
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (_amount > rewardBalance) {
            rewardToken.safeTransfer(_to, rewardBalance);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No staked amount");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) /
            1e12 -
            user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeRewardTransfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    // Admin functions

    /**
     * @dev Set emergency withdrawal fee
     * @param _fee Fee in basis points (1 = 0.01%)
     */
    function setEmergencyWithdrawFee(uint256 _fee) external onlyOwner {
        require(_fee <= 2000, "Fee too high"); // Max 20%
        emergencyWithdrawFee = _fee;
        emit SetEmergencyWithdrawFee(_fee);
    }

    /**
     * @dev Set lockup period
     * @param _period Lockup period in blocks
     */
    function setLockupPeriod(uint256 _period) external onlyOwner {
        lockupPeriod = _period;
        emit SetLockupPeriod(_period);
    }

    /**
     * @dev Set maximum deposit amount per user
     * @param _amount Maximum amount
     */
    function setMaxDepositAmount(uint256 _amount) external onlyOwner {
        maxDepositAmount = _amount;
        emit SetMaxDepositAmount(_amount);
    }

    /**
     * @dev Pause the contract
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract
     */
    function unpause() external onlyOwner
