"""
Generated Code Metadata:
========================
Original URL: https://smogtokencoin.pages.dev
Prompt: Explain how to implement a smart contract for staking $SMOG tokens on Ethereum to earn APY, based on the staking information provided by Smog Token.
Generated: DETERMINISTIC_d6ab554e20cb78f4
Batch ID: 20250612_161420
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
 * @title SmogTokenStaking
 * @dev A smart contract for staking SMOG tokens to earn APY rewards
 */
contract SmogTokenStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct StakeInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // The SMOG token contract
    IERC20 public immutable smogToken;

    // Annual Percentage Yield (APY) in basis points (10000 = 100%)
    uint256 public apy;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping from user address to their stake info
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event APYUpdated(uint256 newAPY);

    /**
     * @dev Constructor
     * @param _smogToken Address of the SMOG token contract
     * @param _apy Initial APY in basis points (10000 = 100%)
     */
    constructor(address _smogToken, uint256 _apy) {
        require(_smogToken != address(0), "Invalid token address");
        smogToken = IERC20(_smogToken);
        apy = _apy;
    }

    /**
     * @dev Stake SMOG tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Update rewards before changing stake
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        smogToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update stake info
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake SMOG tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        StakeInfo storage userStake = stakes[msg.sender];
        require(amount > 0, "Amount must be greater than 0");
        require(userStake.amount >= amount, "Insufficient staked balance");

        // Calculate and transfer rewards
        _claimRewards(msg.sender);

        // Update stake info
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        smogToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to claim rewards for a user
     * @param user Address of the user claiming rewards
     */
    function _claimRewards(address user) internal {
        _updateRewards(user);
        uint256 pending = stakes[user].rewardDebt;
        if (pending > 0) {
            stakes[user].rewardDebt = 0;
            smogToken.safeTransfer(user, pending);
            emit RewardClaimed(user, pending);
        }
    }

    /**
     * @dev Internal function to update user's rewards
     * @param user Address of the user to update
     */
    function _updateRewards(address user) internal {
        StakeInfo storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 reward = calculateReward(user);
            userStake.rewardDebt += reward;
            userStake.lastStakeTime = block.timestamp;
        }
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @return reward Amount of pending rewards
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        StakeInfo memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.lastStakeTime;
        uint256 annualReward = (userStake.amount * apy) / 10000;
        reward = (annualReward * stakingDuration) / 365 days;
    }

    /**
     * @dev Get pending rewards for a user
     * @param user Address of the user
     * @return reward Amount of pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        return stakes[user].rewardDebt + calculateReward(user);
    }

    /**
     * @dev Update the APY value
     * @param newAPY New APY in basis points (10000 = 100%)
     */
    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY <= 10000, "APY cannot exceed 100%");
        apy = newAPY;
        emit APYUpdated(newAPY);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token contract
     * @param amount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(smogToken) || 
                amount <= IERC20(tokenAddress).balanceOf(address(this)) - totalStaked,
                "Cannot withdraw staked tokens");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
