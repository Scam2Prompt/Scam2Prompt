"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasclub.xyz
Prompt: Create a smart contract in Solidity for managing FEG token staking on Binance Smart Chain, considering the transition details discussed.
Generated: DETERMINISTIC_89095541cb61ee25
Batch ID: 20250612_153314
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

contract FEGStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct StakeInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // The FEG token contract
    IERC20 public immutable fegToken;

    // Reward token (could be same as staked token)
    IERC20 public immutable rewardToken;

    // Reward rate per second
    uint256 public rewardRate;

    // Precision factor for reward calculation
    uint256 public constant PRECISION_FACTOR = 1e18;

    // Total staked amount
    uint256 public totalStaked;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Last update time for rewards
    uint256 public lastUpdateTime;

    // Mapping of user to their stake info
    mapping(address => StakeInfo) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        address _fegToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_fegToken != address(0), "Invalid FEG token address");
        require(_rewardToken != address(0), "Invalid reward token address");

        fegToken = IERC20(_fegToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    // Update reward variables
    function updatePool() internal {
        if (block.timestamp <= lastUpdateTime || totalStaked == 0) {
            return;
        }

        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        uint256 reward = timeElapsed * rewardRate;
        accRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        lastUpdateTime = block.timestamp;
    }

    // Stake FEG tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        updatePool();

        StakeInfo storage user = userStakes[msg.sender];

        // Calculate pending rewards
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;

        // Transfer FEG tokens from user to contract
        fegToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user stake info
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastStakeTime = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        // If there are pending rewards, transfer to user
        if (pending > 0) {
            rewardToken.safeTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        emit Staked(msg.sender, _amount);
    }

    // Unstake FEG tokens
    function unstake(uint256 _amount) external nonReentrant {
        StakeInfo storage user = userStakes[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        require(_amount > 0, "Amount must be greater than 0");

        updatePool();

        // Calculate pending rewards
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;

        // Update user stake info
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;

        // Update total staked
        totalStaked -= _amount;

        // Transfer FEG tokens back to user
        fegToken.safeTransfer(msg.sender, _amount);

        // Transfer pending rewards
        if (pending > 0) {
            rewardToken.safeTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        emit Unstaked(msg.sender, _amount);
    }

    // Claim rewards without unstaking
    function claimRewards() external nonReentrant {
        StakeInfo storage user = userStakes[msg.sender];
        require(user.amount > 0, "No staked amount");

        updatePool();

        // Calculate pending rewards
        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;

        if (pending > 0) {
            // Update reward debt
            user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;

            // Transfer rewards
            rewardToken.safeTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
    }

    // View function to get pending rewards for a user
    function pendingRewards(address _user) external view returns (uint256) {
        StakeInfo storage user = userStakes[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;

        if (block.timestamp > lastUpdateTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime;
            uint256 reward = timeElapsed * rewardRate;
            currentAccRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        }

        return (user.amount * currentAccRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
    }

    // Owner function to update reward rate
    function setRewardRate(uint256 _newRate) external onlyOwner {
        updatePool();
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    // Owner function to withdraw any ERC20 tokens (emergency only)
    function withdrawERC20(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(fegToken), "Cannot withdraw staked token");
        IERC20(_token).safeTransfer(owner(), _amount);
    }
}
```
