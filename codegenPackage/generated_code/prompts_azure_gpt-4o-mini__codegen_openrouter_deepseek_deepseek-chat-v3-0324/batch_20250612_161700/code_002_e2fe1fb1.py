"""
Generated Code Metadata:
========================
Original URL: https://basedbrett-in.web.app
Prompt: Create a Solidity contract that allows staking and unstaking of BASE’d BRETT tokens on the Base Chain.
Generated: DETERMINISTIC_e2fe1fb108a5ccd8
Batch ID: 20250612_161700
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

/**
 * @title BRETT Staking Contract
 * @dev Allows users to stake and unstake BRETT tokens and earn rewards
 */
contract BrettStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // The BRETT token contract
    IERC20 public immutable brettToken;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of user addresses to their staking info
    mapping(address => Staker) public stakers;

    // Total amount of BRETT tokens staked
    uint256 public totalStaked;

    // Reward rate (tokens per second per token staked)
    uint256 public rewardRate;

    // Last time the reward was calculated
    uint256 public lastRewardTime;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor
     * @param _brettToken Address of the BRETT token contract
     * @param _rewardRate Initial reward rate (tokens per second per token staked)
     */
    constructor(address _brettToken, uint256 _rewardRate) {
        require(_brettToken != address(0), "Invalid token address");
        brettToken = IERC20(_brettToken);
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Update the reward variables
     */
    function updateReward() internal {
        if (block.timestamp <= lastRewardTime) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate * totalStaked;
        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Stake BRETT tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        updateReward();

        Staker storage staker = stakers[msg.sender];

        if (staker.amountStaked > 0) {
            uint256 pending = (staker.amountStaked * accRewardPerShare) / 1e12 - staker.rewardDebt;
            if (pending > 0) {
                safeTransferReward(msg.sender, pending);
            }
        }

        brettToken.safeTransferFrom(msg.sender, address(this), amount);
        staker.amountStaked += amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e12;
        staker.lastStakedTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake BRETT tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than 0");
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        updateReward();

        uint256 pending = (staker.amountStaked * accRewardPerShare) / 1e12 - staker.rewardDebt;
        if (pending > 0) {
            safeTransferReward(msg.sender, pending);
        }

        staker.amountStaked -= amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e12;
        totalStaked -= amount;

        brettToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimReward() external nonReentrant {
        updateReward();

        Staker storage staker = stakers[msg.sender];
        uint256 pending = (staker.amountStaked * accRewardPerShare) / 1e12 - staker.rewardDebt;
        require(pending > 0, "No rewards to claim");

        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e12;
        safeTransferReward(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Safe transfer reward tokens
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function safeTransferReward(address to, uint256 amount) internal {
        uint256 balance = brettToken.balanceOf(address(this));
        if (amount > balance) {
            brettToken.safeTransfer(to, balance);
        } else {
            brettToken.safeTransfer(to, amount);
        }
    }

    /**
     * @dev Update the reward rate
     * @param newRate New reward rate (tokens per second per token staked)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        updateReward();
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev View function to check pending rewards for a user
     * @param user Address of the user
     * @return Pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardRate * totalStaked;
            currentAccRewardPerShare += (reward * 1e12) / totalStaked;
        }
        
        return (staker.amountStaked * currentAccRewardPerShare) / 1e12 - staker.rewardDebt;
    }

    /**
     * @dev Emergency withdraw all staked tokens without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amountStaked;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;

        brettToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }
}
```
