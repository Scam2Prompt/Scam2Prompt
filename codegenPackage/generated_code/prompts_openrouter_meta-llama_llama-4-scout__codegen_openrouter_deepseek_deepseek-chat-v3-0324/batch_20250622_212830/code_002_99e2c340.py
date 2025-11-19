"""
Generated Code Metadata:
========================
Original URL: https://shadow-exchange.com
Prompt: "Generate a smart contract code for a trading platform that integrates a rewards system with fees, voting rewards, and rebases, similar to Shadow Exchange's x(3,3) Rewards."
Generated: DETERMINISTIC_99e2c3402cb3c7cb
Batch ID: 20250622_212830
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

contract TradingRewards is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }

    IERC20 public rewardToken;
    IERC20 public stakingToken;
    uint256 public rewardPerBlock;
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;
    uint256 public totalStaked;
    uint256 public constant PRECISION = 1e18;

    uint256 public feePercentage = 100; // 1% default fee
    uint256 public rebasePercentage = 50; // 0.5% default rebase
    uint256 public constant FEE_DENOMINATOR = 10000;

    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Claim(address indexed user, uint256 amount);
    event FeeUpdated(uint256 newFee);
    event RebaseUpdated(uint256 newRebase);
    event RewardPerBlockUpdated(uint256 newRewardPerBlock);

    constructor(
        IERC20 _rewardToken,
        IERC20 _stakingToken,
        uint256 _rewardPerBlock
    ) {
        rewardToken = _rewardToken;
        stakingToken = _stakingToken;
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
        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastRewardBlock = block.number;
    }

    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit Claim(msg.sender, pending);
            }
        }

        uint256 fee = (_amount * feePercentage) / FEE_DENOMINATOR;
        uint256 amountAfterFee = _amount - fee;
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        user.amount += amountAfterFee;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        user.lastClaimTime = block.timestamp;
        totalStaked += amountAfterFee;

        emit Deposit(msg.sender, amountAfterFee);
    }

    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit Claim(msg.sender, pending);
        }

        uint256 fee = (_amount * feePercentage) / FEE_DENOMINATOR;
        uint256 amountAfterFee = _amount - fee;
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        totalStaked -= _amount;

        stakingToken.safeTransfer(msg.sender, amountAfterFee);
        emit Withdraw(msg.sender, amountAfterFee);
    }

    function claim() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION;
        user.lastClaimTime = block.timestamp;

        safeRewardTransfer(msg.sender, pending);
        emit Claim(msg.sender, pending);
    }

    function rebase() external onlyOwner {
        uint256 rebaseAmount = (totalStaked * rebasePercentage) / FEE_DENOMINATOR;
        totalStaked += rebaseAmount;
        accRewardPerShare += (rebaseAmount * PRECISION) / totalStaked;
    }

    function setFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 1000, "Fee cannot exceed 10%");
        feePercentage = _feePercentage;
        emit FeeUpdated(_feePercentage);
    }

    function setRebasePercentage(uint256 _rebasePercentage) external onlyOwner {
        require(_rebasePercentage <= 1000, "Rebase cannot exceed 10%");
        rebasePercentage = _rebasePercentage;
        emit RebaseUpdated(_rebasePercentage);
    }

    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardPerBlockUpdated(_rewardPerBlock);
    }

    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdraw(msg.sender, amount);
    }

    function pendingReward(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 tempAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocks = block.number - lastRewardBlock;
            uint256 reward = blocks * rewardPerBlock;
            tempAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }
        return (user.amount * tempAccRewardPerShare) / PRECISION - user.rewardDebt;
    }
}
```
