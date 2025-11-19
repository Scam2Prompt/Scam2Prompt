"""
Generated Code Metadata:
========================
Original URL: https://staking-shakryfi.pages.dev
Prompt: Explain how to use the $msSHARK, $asSHARK, and $isSHARK LP tokens to represent user weights in a staking pool and prevent unauthorized withdrawals.
Generated: DETERMINISTIC_29d66c15e50cb688
Batch ID: 20250622_210803
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

contract SharkStakingPool is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lockedUntil;
    }

    IERC20 public msSHARK;
    IERC20 public asSHARK;
    IERC20 public isSHARK;
    IERC20 public rewardToken;

    uint256 public totalStaked;
    uint256 public accRewardPerShare;
    uint256 public lastRewardBlock;
    uint256 public rewardPerBlock;

    mapping(address => UserInfo) public userInfo;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        IERC20 _msSHARK,
        IERC20 _asSHARK,
        IERC20 _isSHARK,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock
    ) {
        msSHARK = _msSHARK;
        asSHARK = _asSHARK;
        isSHARK = _isSHARK;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

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
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    function stake(uint256 _msAmount, uint256 _asAmount, uint256 _isAmount) external nonReentrant {
        require(_msAmount > 0 || _asAmount > 0 || _isAmount > 0, "Must stake at least one token");
        updatePool();

        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                rewardToken.safeTransfer(msg.sender, pending);
                emit RewardPaid(msg.sender, pending);
            }
        }

        uint256 totalAmount = _msAmount + _asAmount + _isAmount;
        if (_msAmount > 0) {
            msSHARK.safeTransferFrom(msg.sender, address(this), _msAmount);
        }
        if (_asAmount > 0) {
            asSHARK.safeTransferFrom(msg.sender, address(this), _asAmount);
        }
        if (_isAmount > 0) {
            isSHARK.safeTransferFrom(msg.sender, address(this), _isAmount);
        }

        user.amount += totalAmount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.lockedUntil = block.timestamp + 30 days; // Lock for 30 days
        totalStaked += totalAmount;

        emit Staked(msg.sender, totalAmount);
    }

    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        require(block.timestamp >= user.lockedUntil, "Tokens are still locked");

        updatePool();
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            rewardToken.safeTransfer(msg.sender, pending);
            emit RewardPaid(msg.sender, pending);
        }

        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        totalStaked -= _amount;

        // Withdraw proportional amounts of each token
        uint256 msAmount = (_amount * msSHARK.balanceOf(address(this))) / totalStaked;
        uint256 asAmount = (_amount * asSHARK.balanceOf(address(this))) / totalStaked;
        uint256 isAmount = (_amount * isSHARK.balanceOf(address(this))) / totalStaked;

        if (msAmount > 0) {
            msSHARK.safeTransfer(msg.sender, msAmount);
        }
        if (asAmount > 0) {
            asSHARK.safeTransfer(msg.sender, asAmount);
        }
        if (isAmount > 0) {
            isSHARK.safeTransfer(msg.sender, isAmount);
        }

        emit Withdrawn(msg.sender, _amount);
    }

    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        user.amount = 0;
        user.rewardDebt = 0;
        user.lockedUntil = 0;
        totalStaked -= amount;

        // Withdraw proportional amounts of each token
        uint256 msAmount = (amount * msSHARK.balanceOf(address(this))) / totalStaked;
        uint256 asAmount = (amount * asSHARK.balanceOf(address(this))) / totalStaked;
        uint256 isAmount = (amount * isSHARK.balanceOf(address(this))) / totalStaked;

        if (msAmount > 0) {
            msSHARK.safeTransfer(msg.sender, msAmount);
        }
        if (asAmount > 0) {
            asSHARK.safeTransfer(msg.sender, asAmount);
        }
        if (isAmount > 0) {
            isSHARK.safeTransfer(msg.sender, isAmount);
        }

        emit EmergencyWithdraw(msg.sender, amount);
    }

    function pendingReward(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocks = block.number - lastRewardBlock;
            uint256 reward = blocks * rewardPerBlock;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        return (user.amount * currentAccRewardPerShare) / 1e12 - user.rewardDebt;
    }

    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
    }

    function recoverTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != msSHARK && token != asSHARK && token != isSHARK, "Cannot withdraw staking tokens");
        token.safeTransfer(owner(), amount);
    }
}
```
