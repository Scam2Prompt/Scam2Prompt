"""
Generated Code Metadata:
========================
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Write a smart contract using Solidity that integrates with Berachain's Proof-of-Liquidity consensus mechanism to reward liquidity providers with non-purchasable staking tokens.
Generated: DETERMINISTIC_5a2ffb89a07a161d
Batch ID: 20250612_152249
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
 * @title LiquidityRewardContract
 * @dev A smart contract that rewards liquidity providers with non-purchasable staking tokens
 *      based on Berachain's Proof-of-Liquidity consensus mechanism.
 */
contract LiquidityRewardContract is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user's liquidity information
    struct UserInfo {
        uint256 amount;         // How many LP tokens the user has provided
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastRewardTime; // Last time user claimed rewards
    }

    // The staking token (non-purchasable)
    IERC20 public immutable stakingToken;
    // The LP token to be staked
    IERC20 public immutable lpToken;
    // Reward rate per second
    uint256 public rewardRate;
    // Last time reward distribution was updated
    uint256 public lastUpdateTime;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    // Total LP tokens staked
    uint256 public totalStaked;

    // Info of each user that stakes LP tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token (non-purchasable)
     * @param _lpToken Address of the LP token to be staked
     * @param _rewardRate Initial reward rate per second
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _lpToken,
        uint256 _rewardRate
    ) {
        require(address(_stakingToken) != address(0), "Invalid staking token");
        require(address(_lpToken) != address(0), "Invalid LP token");
        stakingToken = _stakingToken;
        lpToken = _lpToken;
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Update the reward variables
     */
    function updateReward() internal {
        if (totalStaked == 0) {
            lastUpdateTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        uint256 reward = timeElapsed * rewardRate;
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Deposit LP tokens to earn rewards
     * @param amount Amount of LP tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        updateReward();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeStakingTokenTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        lpToken.safeTransferFrom(msg.sender, address(this), amount);
        user.amount += amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastRewardTime = block.timestamp;
        totalStaked += amount;

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraw LP tokens and claim rewards
     * @param amount Amount of LP tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Withdraw amount exceeds balance");

        updateReward();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeStakingTokenTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastRewardTime = block.timestamp;
        totalStaked -= amount;

        lpToken.safeTransfer(msg.sender, amount);
        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimReward() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updateReward();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lastRewardTime = block.timestamp;

        safeStakingTokenTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Safe transfer function for staking token
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function safeStakingTokenTransfer(address to, uint256 amount) internal {
        uint256 balance = stakingToken.balanceOf(address(this));
        if (amount > balance) {
            stakingToken.safeTransfer(to, balance);
        } else {
            stakingToken.safeTransfer(to, amount);
        }
    }

    /**
     * @dev Update the reward rate (only callable by owner)
     * @param newRate New reward rate per second
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        updateReward();
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev View function to see pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards for user
     */
    function pendingReward(address user) external view returns (uint256) {
        UserInfo storage _user = userInfo[user];
        uint256 _accRewardPerShare = accRewardPerShare;
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 reward = timeElapsed * rewardRate;
            _accRewardPerShare += (reward * 1e12) / totalStaked;
        }
        return (_user.amount * _accRewardPerShare) / 1e12 - _user.rewardDebt;
    }
}
```
