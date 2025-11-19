"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Illustrate how to implement a staking mechanism for $YETIO tokens in a Solidity smart contract based on Yeti Ouro's tokenomics.
Generated: DETERMINISTIC_0d27b8a41f6d5c5b
Batch ID: 20250612_161059
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
 * @title YetiStaking
 * @dev A contract that allows users to stake $YETIO tokens and earn rewards
 */
contract YetiStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTimestamp;
    }

    // The $YETIO token contract
    IERC20 public yetiToken;

    // Reward token (could be same as staking token)
    IERC20 public rewardToken;

    // Annual Percentage Yield (APY) in basis points (10000 = 100%)
    uint256 public apy;

    // Total staked tokens
    uint256 public totalStaked;

    // Precision factor for reward calculation
    uint256 private constant PRECISION = 1e18;

    // Mapping of user addresses to their staking info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event APYUpdated(uint256 newAPY);

    /**
     * @dev Constructor
     * @param _yetiToken Address of the $YETIO token
     * @param _rewardToken Address of the reward token
     * @param _apy Annual Percentage Yield in basis points
     */
    constructor(
        address _yetiToken,
        address _rewardToken,
        uint256 _apy
    ) {
        require(_yetiToken != address(0), "Invalid token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_apy > 0, "APY must be greater than 0");

        yetiToken = IERC20(_yetiToken);
        rewardToken = IERC20(_rewardToken);
        apy = _apy;
    }

    /**
     * @dev Stake $YETIO tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];

        // Claim any pending rewards before staking more
        if (staker.amountStaked > 0) {
            _claimRewards(msg.sender);
        }

        // Transfer tokens from user to contract
        yetiToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staking info
        staker.amountStaked += amount;
        staker.lastStakedTimestamp = block.timestamp;
        staker.rewardDebt = _calculateRewardDebt(staker.amountStaked);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $YETIO tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Claim any pending rewards before unstaking
        _claimRewards(msg.sender);

        // Update staking info
        staker.amountStaked -= amount;
        staker.rewardDebt = _calculateRewardDebt(staker.amountStaked);
        totalStaked -= amount;

        // Transfer tokens back to user
        yetiToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].amountStaked > 0, "No staked tokens");
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to claim rewards
     * @param user Address of the user claiming rewards
     */
    function _claimRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 pendingRewards = _calculatePendingRewards(user);

        if (pendingRewards > 0) {
            uint256 contractBalance = rewardToken.balanceOf(address(this));
            require(contractBalance >= pendingRewards, "Insufficient reward tokens");

            staker.rewardDebt = _calculateRewardDebt(staker.amountStaked);
            staker.lastStakedTimestamp = block.timestamp;

            rewardToken.safeTransfer(user, pendingRewards);
            emit RewardClaimed(user, pendingRewards);
        }
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @return Amount of pending rewards
     */
    function _calculatePendingRewards(address user) internal view returns (uint256) {
        Staker memory staker = stakers[user];
        if (staker.amountStaked == 0) return 0;

        uint256 currentRewardDebt = _calculateRewardDebt(staker.amountStaked);
        return currentRewardDebt - staker.rewardDebt;
    }

    /**
     * @dev Calculate reward debt for a given staked amount
     * @param amount Staked amount
     * @return Reward debt
     */
    function _calculateRewardDebt(uint256 amount) internal view returns (uint256) {
        if (amount == 0) return 0;
        return (amount * apy * (block.timestamp - stakers[msg.sender].lastStakedTimestamp)) / (365 days * 10000);
    }

    /**
     * @dev Update APY (only owner)
     * @param newAPY New APY in basis points
     */
    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY > 0, "APY must be greater than 0");
        apy = newAPY;
        emit APYUpdated(newAPY);
    }

    /**
     * @dev Withdraw excess reward tokens (only owner)
     * @param amount Amount to withdraw
     */
    function withdrawExcessRewards(uint256 amount) external onlyOwner {
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        uint256 requiredBalance = _calculateTotalPendingRewards();
        
        require(contractBalance > requiredBalance, "No excess rewards to withdraw");
        require(contractBalance - requiredBalance >= amount, "Withdrawal amount too high");

        rewardToken.safeTransfer(owner(), amount);
    }

    /**
     * @dev Calculate total pending rewards for all stakers
     * @return Total pending rewards
     */
    function _calculateTotalPendingRewards() internal view returns (uint256) {
        // This is a simplified implementation
        // In production, you might want to track this separately
        return (totalStaked * apy * (block.timestamp)) / (365 days * 10000);
    }

    /**
     * @dev View function to get pending rewards for a user
     * @param user Address of the user
     * @return Amount of pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        return _calculatePendingRewards(user);
    }

    /**
     * @dev View function to get staking info for a user
     * @param user Address of the user
     * @return amountStaked Amount of tokens staked
     * @return pendingReward Amount of pending rewards
     * @return lastStakedTimestamp Last staking timestamp
     */
    function getUserInfo(address user) external view returns (
        uint256 amountStaked,
        uint256 pendingReward,
        uint256 lastStakedTimestamp
    ) {
        Staker memory staker = stakers[user];
        return (
            staker.amountStaked,
            _calculatePendingRewards(user),
            staker.lastStakedTimestamp
        );
    }
}
```
