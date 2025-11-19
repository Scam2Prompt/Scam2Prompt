"""
Generated Code Metadata:
========================
Original URL: https://astertex.com
Prompt: "Generate a smart contract code for staking BNB, USDT, BTC, and CAKE on Aster DEX to earn up to 30%+ APY, using Solidity or Vyper."
Generated: DETERMINISTIC_b634a26412d01cbd
Batch ID: 20250622_212748
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

contract AsterStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct StakeInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    struct PoolInfo {
        IERC20 stakeToken;
        uint256 allocPoint;
        uint256 lastRewardBlock;
        uint256 accRewardPerShare;
        uint256 totalStaked;
        uint256 lockDuration;
        uint256 rewardRate;
    }

    IERC20 public rewardToken;
    PoolInfo[] public poolInfo;
    mapping(uint256 => mapping(address => StakeInfo)) public userInfo;

    uint256 public totalAllocPoint = 0;
    uint256 public startBlock;
    uint256 public rewardPerBlock;

    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(
        IERC20 _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock
    ) {
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
    }

    function addPool(
        IERC20 _stakeToken,
        uint256 _allocPoint,
        uint256 _lockDuration,
        uint256 _rewardRate,
        bool _withUpdate
    ) public onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }
        uint256 lastRewardBlock = block.number > startBlock ? block.number : startBlock;
        totalAllocPoint += _allocPoint;
        poolInfo.push(
            PoolInfo({
                stakeToken: _stakeToken,
                allocPoint: _allocPoint,
                lastRewardBlock: lastRewardBlock,
                accRewardPerShare: 0,
                totalStaked: 0,
                lockDuration: _lockDuration,
                rewardRate: _rewardRate
            })
        );
    }

    function setPool(
        uint256 _pid,
        uint256 _allocPoint,
        uint256 _lockDuration,
        uint256 _rewardRate,
        bool _withUpdate
    ) public onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }
        totalAllocPoint = totalAllocPoint - poolInfo[_pid].allocPoint + _allocPoint;
        poolInfo[_pid].allocPoint = _allocPoint;
        poolInfo[_pid].lockDuration = _lockDuration;
        poolInfo[_pid].rewardRate = _rewardRate;
    }

    function massUpdatePools() public {
        uint256 length = poolInfo.length;
        for (uint256 pid = 0; pid < length; ++pid) {
            updatePool(pid);
        }
    }

    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.number <= pool.lastRewardBlock) {
            return;
        }
        if (pool.totalStaked == 0) {
            pool.lastRewardBlock = block.number;
            return;
        }
        uint256 multiplier = block.number - pool.lastRewardBlock;
        uint256 reward = (multiplier * rewardPerBlock * pool.allocPoint) / totalAllocPoint;
        pool.accRewardPerShare += (reward * 1e12) / pool.totalStaked;
        pool.lastRewardBlock = block.number;
    }

    function pendingReward(uint256 _pid, address _user) public view returns (uint256) {
        PoolInfo storage pool = poolInfo[_pid];
        StakeInfo storage user = userInfo[_pid][_user];
        uint256 accRewardPerShare = pool.accRewardPerShare;
        if (block.number > pool.lastRewardBlock && pool.totalStaked != 0) {
            uint256 multiplier = block.number - pool.lastRewardBlock;
            uint256 reward = (multiplier * rewardPerBlock * pool.allocPoint) / totalAllocPoint;
            accRewardPerShare += (reward * 1e12) / pool.totalStaked;
        }
        return ((user.amount * accRewardPerShare) / 1e12) - user.rewardDebt;
    }

    function deposit(uint256 _pid, uint256 _amount) public nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        StakeInfo storage user = userInfo[_pid][msg.sender];
        updatePool(_pid);
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        if (_amount > 0) {
            pool.stakeToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            pool.totalStaked += _amount;
            user.lastStakeTime = block.timestamp;
        }
        
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        emit Deposit(msg.sender, _pid, _amount);
    }

    function withdraw(uint256 _pid, uint256 _amount) public nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        StakeInfo storage user = userInfo[_pid][msg.sender];
        require(user.amount >= _amount, "Withdraw: amount exceeds balance");
        require(block.timestamp >= user.lastStakeTime + pool.lockDuration, "Tokens are locked");
        
        updatePool(_pid);
        
        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        if (_amount > 0) {
            user.amount -= _amount;
            pool.totalStaked -= _amount;
            pool.stakeToken.safeTransfer(msg.sender, _amount);
        }
        
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        emit Withdraw(msg.sender, _pid, _amount);
    }

    function emergencyWithdraw(uint256 _pid) public nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        StakeInfo storage user = userInfo[_pid][msg.sender];
        uint256 amount = user.amount;
        
        user.amount = 0;
        user.rewardDebt = 0;
        pool.totalStaked -= amount;
        
        pool.stakeToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, _pid, amount);
    }

    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.transfer(_to, rewardBal);
        } else {
            rewardToken.transfer(_to, _amount);
        }
    }

    function setRewardPerBlock(uint256 _rewardPerBlock) public onlyOwner {
        massUpdatePools();
        rewardPerBlock = _rewardPerBlock;
    }

    function recoverWrongTokens(address _tokenAddress, uint256 _tokenAmount) external onlyOwner {
        IERC20(_tokenAddress).transfer(msg.sender, _tokenAmount);
    }
}
```
sender, _tokenAmount);
    }
}
```
Debt = 0;
        pool.totalStaked -= amount;
        pool.stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, _pid, amount);
    }

    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    function setFeeAddress(address _feeAddress) public {
        require(msg.sender == feeAddress, "setFeeAddress: FORBIDDEN");
        feeAddress = _feeAddress;
        emit SetFeeAddress(msg.sender, _feeAddress);
    }

    function setRewardPerBlock(uint256
