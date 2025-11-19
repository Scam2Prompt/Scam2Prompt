"""
Generated Code Metadata:
========================
Original URL: https://pepeu.pages.dev
Prompt: Generate Solidity code for a smart contract that facilitates double staking rewards for $PEPU tokens on Pepe Unchained.
Generated: DETERMINISTIC_26ae8e8553ed9edb
Batch ID: 20250612_153447
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PepeUnchainedDoubleStakingRewards
 * @author [Your Name]
 * @notice Smart contract for double staking rewards for $PEPU tokens on Pepe Unchained.
 */
contract PepeUnchainedDoubleStakingRewards is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token contract instance
    IERC20 public pepuToken;

    // Reward token contract instance
    IERC20 public rewardToken;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Accrued reward per share
    uint256 public accRewardPerShare;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Reward rate per second
    uint256 public rewardRate;

    // Last reward update timestamp
    uint256 public lastRewardUpdate;

    // Reward distribution start timestamp
    uint256 public rewardStartTimestamp;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for PepeUnchainedDoubleStakingRewards contract.
     * @param _pepuToken Address of $PEPU token contract.
     * @param _rewardToken Address of reward token contract.
     * @param _rewardRate Reward rate per second.
     * @param _rewardStartTimestamp Reward distribution start timestamp.
     */
    constructor(
        address _pepuToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardStartTimestamp
    ) public {
        pepuToken = IERC20(_pepuToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        rewardStartTimestamp = _rewardStartTimestamp;
        lastRewardUpdate = block.timestamp;
    }

    /**
     * @notice Stake $PEPU tokens to earn double rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid stake amount");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStakingBalance = totalStakingBalance.add(amount);

        // Transfer tokens from user to contract
        pepuToken.safeTransferFrom(msg.sender, address(this), amount);

        // Emit stake event
        emit Staked(msg.sender, amount);

        // Update reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake $PEPU tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStakingBalance = totalStakingBalance.sub(amount);

        // Transfer tokens from contract to user
        pepuToken.safeTransfer(msg.sender, amount);

        // Emit unstake event
        emit Unstaked(msg.sender, amount);

        // Update reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update reward debt for user.
     * @param user User address.
     */
    function updateRewardDebt(address user) internal {
        // Update accrued reward per share
        uint256 currentReward = getCurrentReward();
        accRewardPerShare = accRewardPerShare.add(currentReward);

        // Update user's reward debt
        rewardDebt[user] = stakingBalances[user].mul(accRewardPerShare).div(1e18);
    }

    /**
     * @notice Get current reward.
     * @return Current reward.
     */
    function getCurrentReward() public view returns (uint256) {
        if (block.timestamp < rewardStartTimestamp) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp.sub(lastRewardUpdate);
        lastRewardUpdate = block.timestamp;

        return timeElapsed.mul(rewardRate);
    }

    /**
     * @notice Get user's pending rewards.
     * @param user User address.
     * @return Pending rewards.
     */
    function getPendingRewards(address user) public view returns (uint256) {
        uint256 currentReward = getCurrentReward();
        uint256 userRewardDebt = rewardDebt[user];
        uint256 userStakingBalance = stakingBalances[user];

        return userStakingBalance.mul(accRewardPerShare.add(currentReward)).div(1e18).sub(userRewardDebt);
    }

    /**
     * @notice Claim pending rewards.
     */
    function claimRewards() public nonReentrant {
        uint256 pendingRewards = getPendingRewards(msg.sender);

        require(pendingRewards > 0, "No pending rewards");

        // Update user's reward debt
        rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);

        // Transfer rewards to user
        rewardToken.safeTransfer(msg.sender, pendingRewards);

        // Emit rewards distributed event
        emit RewardsDistributed(msg.sender, pendingRewards);
    }
}
```
