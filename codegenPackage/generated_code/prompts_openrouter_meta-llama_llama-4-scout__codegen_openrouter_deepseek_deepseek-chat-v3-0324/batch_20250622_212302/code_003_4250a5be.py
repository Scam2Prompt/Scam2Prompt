"""
Generated Code Metadata:
========================
Original URL: https://thenafl.org
Prompt: Design a smart contract that utilizes THENA FI's ve3,3 tokenomics model for incentivizing liquidity providers.
Generated: DETERMINISTIC_4250a5be9e8a8a00
Batch ID: 20250622_212302
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

contract Ve33Incentives is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Struct to store user information
    struct UserInfo {
        uint256 amount;     // How many LP tokens the user has provided
        uint256 rewardDebt; // Reward debt (see explanation below)
        uint256 unlockTime; // When the user can withdraw their tokens
    }

    // The reward token
    IERC20 public rewardToken;
    // The LP token
    IERC20 public lpToken;
    // Reward tokens created per block
    uint256 public rewardPerBlock;
    // Total locked up rewards
    uint256 public totalLockedRewards;
    // The block number when reward distribution starts
    uint256 public startBlock;
    // The block number when reward distribution ends
    uint256 public endBlock;
    // Total allocation points (must be the sum of all allocation points in all pools)
    uint256 public totalAllocPoint = 0;
    // Accumulated rewards per share, times 1e12
    uint256 public accRewardPerShare;
    // Last block number that rewards were calculated
    uint256 public lastRewardBlock;
    // Lock duration in blocks
    uint256 public lockDuration;
    // Info of each user that stakes LP tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        IERC20 _rewardToken,
        IERC20 _lpToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _lockDuration,
        uint256 _totalAllocPoint
    ) {
        rewardToken = _rewardToken;
        lpToken = _lpToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        lockDuration = _lockDuration;
        totalAllocPoint = _totalAllocPoint;
        lastRewardBlock = startBlock;
        endBlock = _startBlock.add(_lockDuration);
    }

    // View function to see pending rewards on frontend
    function pendingReward(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 _accRewardPerShare = accRewardPerShare;
        uint256 lpSupply = lpToken.balanceOf(address(this));
        
        if (block.number > lastRewardBlock && lpSupply != 0) {
            uint256 multiplier = _getMultiplier(lastRewardBlock, block.number);
            uint256 reward = multiplier.mul(rewardPerBlock).div(totalAllocPoint);
            _accRewardPerShare = _accRewardPerShare.add(reward.mul(1e12).div(lpSupply));
        }
        
        return user.amount.mul(_accRewardPerShare).div(1e12).sub(user.rewardDebt);
    }

    // Update reward variables
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }
        
        uint256 lpSupply = lpToken.balanceOf(address(this));
        if (lpSupply == 0) {
            lastRewardBlock = block.number;
            return;
        }
        
        uint256 multiplier = _getMultiplier(lastRewardBlock, block.number);
        uint256 reward = multiplier.mul(rewardPerBlock).div(totalAllocPoint);
        
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e12).div(lpSupply));
        lastRewardBlock = block.number;
    }

    // Deposit LP tokens to earn rewards
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];
        updatePool();
        
        if (user.amount > 0) {
            uint256 pending = user.amount.mul(accRewardPerShare).div(1e12).sub(user.rewardDebt);
            if (pending > 0) {
                _safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        lpToken.safeTransferFrom(address(msg.sender), address(this), _amount);
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e12);
        user.unlockTime = block.number.add(lockDuration);
        
        emit Deposit(msg.sender, _amount);
    }

    // Withdraw LP tokens and collect rewards
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw: not enough balance");
        require(block.number >= user.unlockTime, "Tokens are still locked");
        
        updatePool();
        
        uint256 pending = user.amount.mul(accRewardPerShare).div(1e12).sub(user.rewardDebt);
        if (pending > 0) {
            _safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e12);
        lpToken.safeTransfer(address(msg.sender), _amount);
        
        emit Withdraw(msg.sender, _amount);
    }

    // Withdraw without caring about rewards (EMERGENCY ONLY)
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;
        lpToken.safeTransfer(address(msg.sender), amount);
        
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
    function _safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    // Return reward multiplier over the given _from to _to block
    function _getMultiplier(uint256 _from, uint256 _to) internal view returns (uint256) {
        if (_to <= endBlock) {
            return _to.sub(_from);
        } else if (_from >= endBlock) {
            return 0;
        } else {
            return endBlock.sub(_from);
        }
    }
}
```
