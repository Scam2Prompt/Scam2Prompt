"""
Generated Code Metadata:
========================
Original URL: https://bitcoinsbsc.pages.dev
Prompt: Develop a smart contract code to deploy a similar staking pool on BNB Smart Chain, inspired by the Bitcoin BSC project.
Generated: DETERMINISTIC_2ecc3266125177c3
Batch ID: 20250622_211350
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title StakingPool
 * @dev A smart contract for staking BSC tokens and earning rewards.
 * Inspired by Bitcoin BSC project, adapted for BNB Smart Chain.
 */
contract StakingPool is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;     // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastStakeTime; // Last stake time for lock period
    }

    // The staking token (BSC token)
    IERC20 public stakingToken;
    // The reward token (could be same as staking token)
    IERC20 public rewardToken;

    // Reward rate per block
    uint256 public rewardPerBlock;
    // Total staked amount
    uint256 public totalStaked;
    // Last block number where rewards were calculated
    uint256 public lastRewardBlock;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    // Staking lock period in seconds
    uint256 public lockPeriod;

    // Mapping from staker address to staker info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event LockPeriodUpdated(uint256 newLockPeriod);

    /**
     * @dev Constructor to initialize the staking pool
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardPerBlock Reward rate per block
     * @param _lockPeriod Staking lock period in seconds
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _lockPeriod
    ) {
        require(_stakingToken != address(0), "Staking token cannot be zero address");
        require(_rewardToken != address(0), "Reward token cannot be zero address");
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lockPeriod = _lockPeriod;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update the reward variables of the pool
     */
    function updatePool() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksPassed = block.number - lastRewardBlock;
        uint256 reward = blocksPassed * rewardPerBlock;

        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens into the pool
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");

        updatePool();

        Staker storage staker = stakers[msg.sender];

        if (staker.amount > 0) {
            uint256 pending = (staker.amount * accRewardPerShare) / 1e12 - staker.rewardDebt;
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        staker.amount += amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e12;
        staker.lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot withdraw 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient balance");
        require(block.timestamp >= staker.lastStakeTime + lockPeriod, "Tokens are locked");

        updatePool();

        uint256 pending = (staker.amount * accRewardPerShare) / 1e12 - staker.rewardDebt;
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
        }

        staker.amount -= amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e12;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimReward() external nonReentrant {
        updatePool();

        Staker storage staker = stakers[msg.sender];
        uint256 pending = (staker.amount * accRewardPerShare) / 1e12 - staker.rewardDebt;
        require(pending > 0, "No rewards to claim");

        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e12;
        safeTransferReward(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Safe transfer reward tokens
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function safeTransferReward(address to, uint256 amount) internal {
        uint256 balance = rewardToken.balanceOf(address(this));
        if (amount > balance) {
            rewardToken.safeTransfer(to, balance);
        } else {
            rewardToken.safeTransfer(to, amount);
        }
    }

    /**
     * @dev Update reward rate per block (owner only)
     * @param _rewardPerBlock New reward rate
     */
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardRateUpdated(_rewardPerBlock);
    }

    /**
     * @dev Update lock period (owner only)
     * @param _lockPeriod New lock period in seconds
     */
    function setLockPeriod(uint256 _lockPeriod) external onlyOwner {
        lockPeriod = _lockPeriod;
        emit LockPeriodUpdated(_lockPeriod);
    }

    /**
     * @dev Emergency withdraw tokens from the contract (owner only)
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).safeTransfer(msg.sender, amount);
    }

    /**
     * @dev View function to see pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards
     */
    function pendingReward(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksPassed = block.number - lastRewardBlock;
            uint256 reward = blocksPassed * rewardPerBlock;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        return (staker.amount * currentAccRewardPerShare) / 1e12 - staker.rewardDebt;
    }

    /**
     * @dev View function to check if user's tokens are locked
     * @param user Address of the user
     * @return True if tokens are locked, false otherwise
     */
    function isLocked(address user) external view returns (bool) {
        return block.timestamp < stakers[user].lastStakeTime + lockPeriod;
    }
}
```
