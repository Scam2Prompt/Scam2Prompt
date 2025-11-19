"""
Generated Code Metadata:
========================
Original URL: https://presale-bybet0x5d.pages.dev
Prompt: Design a staking system for a cryptocurrency token, inspired by Bybet's staking mechanism, which offers up to 1000% APY and allows users to claim their share of the GGR sharing.
Generated: DETERMINISTIC_b46f8778e6886fe7
Batch ID: 20250622_210856
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
        uint256 startTime;
        uint256 lastClaimTime;
        uint256 claimedRewards;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    uint256 public totalRewardsDistributed;
    uint256 public constant APY = 1000; // 1000% APY
    uint256 public constant SECONDS_IN_YEAR = 31536000;
    uint256 public constant GGR_SHARING_PERCENT = 20; // 20% of GGR shared

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event GGRShared(uint256 amount);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            _claimRewards();
        }

        userStake.amount += amount;
        userStake.startTime = block.timestamp;
        userStake.lastClaimTime = block.timestamp;

        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        _claimRewards();
        
        userStake.amount -= amount;
        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            uint256 ggrShare = (reward * GGR_SHARING_PERCENT) / 100;
            uint256 userReward = reward - ggrShare;

            userStake.claimedRewards += userReward;
            userStake.lastClaimTime = block.timestamp;

            require(rewardToken.transfer(msg.sender, userReward), "Reward transfer failed");
            require(rewardToken.transfer(owner(), ggrShare), "GGR transfer failed");

            totalRewardsDistributed += reward;
            emit RewardClaimed(msg.sender, userReward);
            emit GGRShared(ggrShare);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimTime;
        uint256 reward = (userStake.amount * APY * timeElapsed) / (SECONDS_IN_YEAR * 100);
        return reward;
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardToken.transfer(owner(), balance), "Emergency withdraw failed");
    }

    function updateRewardToken(address _rewardToken) external onlyOwner {
        rewardToken = IERC20(_rewardToken);
    }
}
```
