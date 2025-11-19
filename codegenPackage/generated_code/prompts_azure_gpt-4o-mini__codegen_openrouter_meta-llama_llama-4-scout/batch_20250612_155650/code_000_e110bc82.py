"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate a smart contract for staking the $GGG token as described in the Good Games Guild documentation.
Generated: DETERMINISTIC_e110bc82f7fd5c4f
Batch ID: 20250612_155650
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
 * @title GGG Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $GGG tokens and earn rewards.
 */
contract GGGStakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // $GGG token contract
    IERC20 public gggToken;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Reward per share
    uint256 public rewardPerShare;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward distribution interval (in seconds)
    uint256 public rewardDistributionInterval;

    // Last reward distribution timestamp
    uint256 public lastRewardDistributionTimestamp;

    // Reward amount per interval
    uint256 public rewardAmountPerInterval;

    /**
     * @notice Constructor
     * @param _gggToken $GGG token contract address
     * @param _rewardDistributionInterval Reward distribution interval (in seconds)
     * @param _rewardAmountPerInterval Reward amount per interval
     */
    constructor(
        address _gggToken,
        uint256 _rewardDistributionInterval,
        uint256 _rewardAmountPerInterval
    ) public {
        gggToken = IERC20(_gggToken);
        rewardDistributionInterval = _rewardDistributionInterval;
        rewardAmountPerInterval = _rewardAmountPerInterval;
        lastRewardDistributionTimestamp = block.timestamp;
    }

    /**
     * @notice Stake $GGG tokens
     * @param _amount Amount of $GGG tokens to stake
     */
    function stake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Transfer $GGG tokens to the contract
        gggToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake $GGG tokens
     * @param _amount Amount of $GGG tokens to unstake
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer $GGG tokens to the user
        gggToken.safeTransfer(msg.sender, _amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update user's reward debt
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        // Calculate accumulated reward per share
        accRewardPerShare = accRewardPerShare.add(
            rewardPerShare.add(
                rewardAmountPerInterval.mul(
                    block.timestamp.sub(lastRewardDistributionTimestamp)
                ).div(totalStakingBalance)
            )
        );

        // Update user's reward debt
        rewardDebt[_user] = stakingBalances[_user].mul(accRewardPerShare).div(1e18);
    }

    /**
     * @notice Distribute rewards
     */
    function distributeRewards() public nonReentrant {
        // Check if reward distribution interval has passed
        require(
            block.timestamp.sub(lastRewardDistributionTimestamp) >= rewardDistributionInterval,
            "Reward distribution interval has not passed"
        );

        // Update accumulated reward per share
        accRewardPerShare = accRewardPerShare.add(
            rewardAmountPerInterval.mul(
                block.timestamp.sub(lastRewardDistributionTimestamp)
            ).div(totalStakingBalance)
        );

        // Update last reward distribution timestamp
        lastRewardDistributionTimestamp = block.timestamp;

        // Update reward per share
        rewardPerShare = accRewardPerShare;
    }

    /**
     * @notice Get user's staking balance and reward debt
     * @param _user User address
     * @return staking balance and reward debt
     */
    function getUserInfo(address _user) public view returns (uint256, uint256) {
        return (stakingBalances[_user], rewardDebt[_user]);
    }
}
```
