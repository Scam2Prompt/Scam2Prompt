"""
Generated Code Metadata:
========================
Original URL: https://cruas.ru
Prompt: Create a Solidity smart contract that mimics the liquidity pool mechanism of Velodrome Finance, including token rewards for liquidity providers.
Generated: DETERMINISTIC_baf390242b70fe76
Batch ID: 20250612_154820
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract VelodromeLiquidityPool is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Struct to represent a liquidity provider's stake
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // The tokens in the liquidity pool
    IERC20 public tokenA;
    IERC20 public tokenB;
    IERC20 public rewardToken;

    // The LP token representing shares in the pool
    IERC20 public lpToken;

    // Reward variables
    uint256 public rewardPerBlock;
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;

    // Total LP tokens staked
    uint256 public totalStaked;

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        IERC20 _tokenA,
        IERC20 _tokenB,
        IERC20 _rewardToken,
        IERC20 _lpToken,
        uint256 _rewardPerBlock
    ) {
        require(address(_tokenA) != address(0), "TokenA cannot be zero address");
        require(address(_tokenB) != address(0), "TokenB cannot be zero address");
        require(address(_rewardToken) != address(0), "Reward token cannot be zero address");
        require(address(_lpToken) != address(0), "LP token cannot be zero address");

        tokenA = _tokenA;
        tokenB = _tokenB;
        rewardToken = _rewardToken;
        lpToken = _lpToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
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

        uint256 blocksPassed = block.number.sub(lastRewardBlock);
        uint256 reward = blocksPassed.mul(rewardPerBlock);
        
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e12).div(totalStaked));
        lastRewardBlock = block.number;
    }

    // Deposit LP tokens to earn rewards
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        updatePool();

        Stake storage stake = stakes[msg.sender];
        if (stake.amount > 0) {
            uint256 pending = stake.amount.mul(accRewardPerShare).div(1e12).sub(stake.rewardDebt);
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        lpToken.safeTransferFrom(msg.sender, address(this), _amount);
        stake.amount = stake.amount.add(_amount);
        stake.rewardDebt = stake.amount.mul(accRewardPerShare).div(1e12);
        totalStaked = totalStaked.add(_amount);

        emit Deposited(msg.sender, _amount);
    }

    // Withdraw LP tokens and claim rewards
    function withdraw(uint256 _amount) external nonReentrant {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount >= _amount, "Withdraw amount exceeds stake");

        updatePool();

        uint256 pending = stake.amount.mul(accRewardPerShare).div(1e12).sub(stake.rewardDebt);
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        stake.amount = stake.amount.sub(_amount);
        stake.rewardDebt = stake.amount.mul(accRewardPerShare).div(1e12);
        totalStaked = totalStaked.sub(_amount);

        lpToken.safeTransfer(msg.sender, _amount);
        emit Withdrawn(msg.sender, _amount);
    }

    // Claim pending rewards
    function claimRewards() external nonReentrant {
        updatePool();

        Stake storage stake = stakes[msg.sender];
        uint256 pending = stake.amount.mul(accRewardPerShare).div(1e12).sub(stake.rewardDebt);
        require(pending > 0, "No rewards to claim");

        stake.rewardDebt = stake.amount.mul(accRewardPerShare).div(1e12);
        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // Update reward rate (only callable by owner in a real implementation)
    function updateRewardRate(uint256 _rewardPerBlock) external {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardRateUpdated(_rewardPerBlock);
    }

    // View function to see pending rewards
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage stake = stakes[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksPassed = block.number.sub(lastRewardBlock);
            uint256 reward = blocksPassed.mul(rewardPerBlock);
            currentAccRewardPerShare = currentAccRewardPerShare.add(reward.mul(1e12).div(totalStaked));
        }
        
        return stake.amount.mul(currentAccRewardPerShare).div(1e12).sub(stake.rewardDebt);
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
}
```
