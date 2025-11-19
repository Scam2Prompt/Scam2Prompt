"""
Generated Code Metadata:
========================
Original URL: https://dinamikaplus.ru
Prompt: Write a smart contract in Solidity to enable staking of BELT tokens and distribute rewards based on the mechanisms described in Belt Finance.
Generated: DETERMINISTIC_1845eac8f9ec3e5e
Batch ID: 20250612_155024
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

contract BeltStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Info of each user
    struct UserInfo {
        uint256 amount;     // How many BELT tokens the user has staked
        uint256 rewardDebt; // Reward debt (see explanation below)
        uint256 pendingRewards; // Pending rewards to be claimed
    }

    // The BELT token
    IERC20 public beltToken;
    // The reward token (could be BELT or another token)
    IERC20 public rewardToken;
    // Reward tokens distributed per block
    uint256 public rewardPerBlock;
    // Last block number that rewards distribution occurred
    uint256 public lastRewardBlock;
    // Accumulated rewards per share, times 1e18
    uint256 public accRewardPerShare;
    // Total amount staked
    uint256 public totalStaked;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPerBlockUpdated(uint256 oldReward, uint256 newReward);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        IERC20 _beltToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock
    ) {
        beltToken = _beltToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = _startBlock;
    }

    // Update reward variables of the pool
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocks = block.number - lastRewardBlock;
        uint256 reward = blocks * rewardPerBlock;
        accRewardPerShare += (reward * 1e18) / totalStaked;
        lastRewardBlock = block.number;
    }

    // Deposit BELT tokens to contract for reward allocation
    function deposit(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e18 - user.rewardDebt;
            if (pending > 0) {
                user.pendingRewards += pending;
            }
        }

        if (_amount > 0) {
            beltToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            totalStaked += _amount;
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e18;
        emit Deposit(msg.sender, _amount);
    }

    // Withdraw BELT tokens from contract
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw: amount exceeds balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e18 - user.rewardDebt;
        if (pending > 0) {
            user.pendingRewards += pending;
        }

        if (_amount > 0) {
            user.amount -= _amount;
            totalStaked -= _amount;
            beltToken.safeTransfer(msg.sender, _amount);
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e18;
        emit Withdraw(msg.sender, _amount);
    }

    // Claim pending rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e18 - user.rewardDebt;
        if (pending > 0 || user.pendingRewards > 0) {
            user.pendingRewards += pending;
            uint256 totalRewards = user.pendingRewards;
            user.pendingRewards = 0;

            if (totalRewards > 0) {
                safeRewardTransfer(msg.sender, totalRewards);
            }
            emit RewardClaimed(msg.sender, totalRewards);
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e18;
    }

    // Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    // Update reward per block (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        uint256 oldReward = rewardPerBlock;
        rewardPerBlock = _rewardPerBlock;
        emit RewardPerBlockUpdated(oldReward, _rewardPerBlock);
    }

    // Withdraw without caring about rewards. EMERGENCY ONLY
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;
        user.pendingRewards = 0;
        beltToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Recover any ERC20 tokens sent to the contract by mistake (except staking and reward tokens)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(beltToken) && tokenAddress != address(rewardToken), 
            "Cannot recover staking or reward tokens");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
