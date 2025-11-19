"""
Generated Code Metadata:
========================
Original URL: https://bogeonbase.pages.dev
Prompt: Develop a smart contract for staking $BOGE tokens on the Base blockchain. Include functionality for depositing tokens, calculating rewards, and withdrawing tokens.
Generated: DETERMINISTIC_5bd32c1053923cbd
Batch ID: 20250612_145619
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

contract BogeStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 depositTime;
    }

    // The BOGE token contract
    IERC20 public immutable bogeToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // Precision factor for reward calculation
    uint256 private constant PRECISION = 1e18;

    // Last time reward was calculated
    uint256 public lastUpdateTime;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Mapping of user addresses to their stake info
    mapping(address => Stake) public stakes;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _bogeToken, uint256 _rewardRate) {
        require(_bogeToken != address(0), "Invalid token address");
        bogeToken = IERC20(_bogeToken);
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    // Update reward variables
    modifier updateRewards() {
        _updateRewards();
        _;
    }

    // Internal function to update reward variables
    function _updateRewards() internal {
        if (totalStaked == 0) {
            lastUpdateTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        uint256 reward = timeElapsed * rewardRate;
        accRewardPerShare += (reward * PRECISION) / totalStaked;
        lastUpdateTime = block.timestamp;
    }

    // Deposit BOGE tokens to stake
    function deposit(uint256 amount) external nonReentrant updateRewards {
        require(amount > 0, "Amount must be greater than 0");

        Stake storage stake = stakes[msg.sender];
        if (stake.amount > 0) {
            uint256 pending = (stake.amount * accRewardPerShare) / PRECISION - stake.rewardDebt;
            if (pending > 0) {
                _safeTransferReward(msg.sender, pending);
            }
        }

        totalStaked += amount;
        stake.amount += amount;
        stake.rewardDebt = (stake.amount * accRewardPerShare) / PRECISION;
        stake.depositTime = block.timestamp;

        bogeToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Deposited(msg.sender, amount);
    }

    // Withdraw staked BOGE tokens
    function withdraw(uint256 amount) external nonReentrant updateRewards {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount >= amount, "Insufficient staked amount");
        require(amount > 0, "Amount must be greater than 0");

        uint256 pending = (stake.amount * accRewardPerShare) / PRECISION - stake.rewardDebt;
        if (pending > 0) {
            _safeTransferReward(msg.sender, pending);
        }

        totalStaked -= amount;
        stake.amount -= amount;
        stake.rewardDebt = (stake.amount * accRewardPerShare) / PRECISION;

        bogeToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Claim accumulated rewards
    function claimRewards() external nonReentrant updateRewards {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount > 0, "No staked amount");

        uint256 pending = (stake.amount * accRewardPerShare) / PRECISION - stake.rewardDebt;
        require(pending > 0, "No rewards to claim");

        stake.rewardDebt = (stake.amount * accRewardPerShare) / PRECISION;
        _safeTransferReward(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    // Internal function to safely transfer rewards
    function _safeTransferReward(address to, uint256 amount) internal {
        uint256 balance = bogeToken.balanceOf(address(this));
        if (amount > balance) {
            bogeToken.safeTransfer(to, balance);
        } else {
            bogeToken.safeTransfer(to, amount);
        }
    }

    // View function to check pending rewards for a user
    function pendingRewards(address user) external view returns (uint256) {
        Stake storage stake = stakes[user];
        if (stake.amount == 0) return 0;

        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 reward = timeElapsed * rewardRate;
            currentAccRewardPerShare += (reward * PRECISION) / totalStaked;
        }

        return (stake.amount * currentAccRewardPerShare) / PRECISION - stake.rewardDebt;
    }

    // Owner function to update reward rate
    function setRewardRate(uint256 newRate) external onlyOwner {
        _updateRewards();
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    // Owner function to recover ERC20 tokens (except BOGE)
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(bogeToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
