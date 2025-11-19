"""
Generated Code Metadata:
========================
Original URL: https://sosphon.xyz
Prompt: Generate a smart contract code to automate the reward system for $SOPH stakers, ensuring sustainable yields and decentralization of the Sophon network.
Generated: DETERMINISTIC_38a60b9159568c38
Batch ID: 20250622_212813
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

contract SophonStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for yield calculation
        uint256 lastClaim;  // Timestamp of last reward claim
    }

    // Staking token (SOPH)
    IERC20 public immutable stakingToken;

    // Reward token (SOPH)
    IERC20 public immutable rewardToken;

    // Reward variables
    uint256 public rewardPerSecond;  // Reward tokens distributed per second
    uint256 public lastRewardTime;   // Last time reward distribution was calculated
    uint256 public accRewardPerShare; // Accumulated rewards per share, times 1e18

    // Staking parameters
    uint256 public totalStaked;      // Total tokens staked
    uint256 public constant MIN_STAKE = 1 ether; // Minimum stake amount
    uint256 public constant MAX_STAKE = 100000 ether; // Maximum stake amount
    uint256 public constant LOCK_PERIOD = 30 days; // Minimum staking period

    // Staking pool info
    mapping(address => UserInfo) public userInfo;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerSecond
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerSecond = _rewardPerSecond;
        lastRewardTime = block.timestamp;
    }

    // Update reward variables
    function updatePool() public {
        if (block.timestamp <= lastRewardTime) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardPerSecond;

        accRewardPerShare += (reward * 1e18) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    // Stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount >= MIN_STAKE, "Amount below minimum stake");
        require(_amount <= MAX_STAKE, "Amount exceeds maximum stake");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e18 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e18;
        user.lastClaim = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp >= user.lastClaim + LOCK_PERIOD, "Tokens are still locked");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e18 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e18;
        totalStaked -= _amount;

        stakingToken.safeTransfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / 1e18 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        safeRewardTransfer(msg.sender, pending);
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e18;
        user.lastClaim = block.timestamp;

        emit RewardClaimed(msg.sender, pending);
    }

    // Safe reward transfer function
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    // Update reward rate (only owner)
    function setRewardRate(uint256 _rewardPerSecond) external onlyOwner {
        updatePool();
        rewardPerSecond = _rewardPerSecond;
        emit RewardRateUpdated(_rewardPerSecond);
    }

    // Emergency withdraw (without rewards)
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        require(tokenAddress != address(rewardToken), "Cannot withdraw reward token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
