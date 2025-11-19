"""
Generated Code Metadata:
========================
Original URL: https://hehe-verse.pages.dev
Prompt: Write a smart contract in Solidity for staking $HEHE tokens that distributes rewards based on a 0.05% fee from each trade within the HEHE ecosystem.
Generated: DETERMINISTIC_52427a9da49fe60d
Batch ID: 20250612_153420
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

contract HEHEStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by user
        uint256 rewardDebt; // Reward debt for accounting
    }

    // The HEHE token
    IERC20 public immutable heheToken;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Total amount staked
    uint256 public totalStaked;

    // Last reward balance
    uint256 public lastRewardBalance;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardAdded(uint256 amount);

    constructor(IERC20 _heheToken) {
        heheToken = _heheToken;
    }

    // Add rewards to the staking contract (called from fee collection)
    function addReward(uint256 amount) external onlyOwner {
        heheToken.safeTransferFrom(msg.sender, address(this), amount);
        _updateRewards();
        emit RewardAdded(amount);
    }

    // Update reward variables
    function _updateRewards() internal {
        uint256 currentBalance = heheToken.balanceOf(address(this));
        uint256 rewardBalance = currentBalance - totalStaked;

        if (rewardBalance > 0 && totalStaked > 0) {
            accRewardPerShare += (rewardBalance * 1e12) / totalStaked;
            lastRewardBalance = rewardBalance;
        }
    }

    // Deposit HEHE tokens for staking
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        _updateRewards();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                heheToken.safeTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        heheToken.safeTransferFrom(msg.sender, address(this), amount);
        user.amount += amount;
        totalStaked += amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        emit Deposit(msg.sender, amount);
    }

    // Withdraw staked HEHE tokens
    function withdraw(uint256 amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Withdraw amount exceeds balance");

        _updateRewards();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            heheToken.safeTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= amount;
        totalStaked -= amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        heheToken.safeTransfer(msg.sender, amount);
        emit Withdraw(msg.sender, amount);
    }

    // Claim pending rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        _updateRewards();

        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        heheToken.safeTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // View function to see pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentBalance = heheToken.balanceOf(address(this));
        uint256 tempAccRewardPerShare = accRewardPerShare;

        if (currentBalance > totalStaked && totalStaked != 0) {
            uint256 rewardBalance = currentBalance - totalStaked;
            tempAccRewardPerShare += (rewardBalance * 1e12) / totalStaked;
        }

        return (user.amount * tempAccRewardPerShare) / 1e12 - user.rewardDebt;
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;

        heheToken.safeTransfer(msg.sender, amount);
        emit Withdraw(msg.sender, amount);
    }
}
```
