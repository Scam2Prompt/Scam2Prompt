"""
Generated Code Metadata:
========================
Original URL: https://doge20claim.pages.dev
Prompt: Implement a staking system using a specific blockchain platform (e.g., Ethereum) that incorporates features like reward distribution, dynamic returns rates, and user staking pool management, inspired by Dogecoin20's model.
Generated: DETERMINISTIC_8cfb71169e188a5a
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingSystem is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    uint256 public totalStaked;
    uint256 public rewardRate = 10; // Base reward rate (10%)
    uint256 public rewardInterval = 1 days;
    uint256 public minStakeDuration = 7 days;
    uint256 public maxStakeDuration = 365 days;
    uint256 public dynamicRateFactor = 2; // Factor for dynamic rate calculation

    mapping(address => Stake) public stakes;
    mapping(uint256 => uint256) public durationMultipliers; // Maps duration to multiplier

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);

        // Initialize duration multipliers
        durationMultipliers[7 days] = 110; // 1.1x
        durationMultipliers[30 days] = 120; // 1.2x
        durationMultipliers[90 days] = 150; // 1.5x
        durationMultipliers[180 days] = 200; // 2x
        durationMultipliers[365 days] = 300; // 3x
    }

    function stake(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(duration >= minStakeDuration && duration <= maxStakeDuration, "Invalid duration");
        require(stakes[msg.sender].amount == 0, "Already staked");

        uint256 multiplier = durationMultipliers[duration];
        require(multiplier > 0, "Invalid duration selected");

        stakes[msg.sender] = Stake({
            amount: amount,
            stakedAt: block.timestamp,
            lastClaimed: block.timestamp
        });

        totalStaked += amount;

        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }

    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(block.timestamp >= userStake.stakedAt + minStakeDuration, "Minimum stake duration not reached");

        // Claim any pending rewards first
        _claimRewards();

        uint256 amount = userStake.amount;
        totalStaked -= amount;
        delete stakes[msg.sender];

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            userStake.lastClaimed = block.timestamp;
            require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 duration = block.timestamp - userStake.lastClaimed;
        if (duration < rewardInterval) return 0;

        uint256 intervals = duration / rewardInterval;
        uint256 effectiveRate = getDynamicRate(userStake.stakedAt);

        return (userStake.amount * effectiveRate * intervals) / (100 * 365);
    }

    function getDynamicRate(uint256 stakedAt) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - stakedAt;
        uint256 durationFactor = timeElapsed / rewardInterval;
        
        // The longer the stake, the higher the reward rate
        return rewardRate + (durationFactor * dynamicRateFactor);
    }

    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0 && newRate <= 100, "Invalid rate");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    function updateDurationMultiplier(uint256 duration, uint256 multiplier) external onlyOwner {
        require(duration >= minStakeDuration && duration <= maxStakeDuration, "Invalid duration");
        durationMultipliers[duration] = multiplier;
    }

    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(stakingToken) || totalStaked == 0, "Cannot withdraw staking tokens while staked");
        IERC20(token).transfer(owner(), amount);
    }
}
```
