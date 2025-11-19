"""
Generated Code Metadata:
========================
Original URL: https://bafybeiapzu7x4dr6cvx3pfwbbamnaqgtc5tl5c7l4o4yngnf3goy6wwixq.ipfs.dweb.link
Prompt: How can I implement fixed yield staking using PRYZM's Layer 1 Yield Hub?
Generated: DETERMINISTIC_bf9414678fa9d20e
Batch ID: 20250612_160853
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

contract FixedYieldStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct StakingInfo {
        uint256 amount;
        uint256 startTime;
        uint256 endTime;
        uint256 claimedAmount;
        bool isActive;
    }

    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardToken;
    uint256 public fixedAPY; // APY in basis points (10000 = 100%)
    uint256 public stakingDuration; // in seconds
    uint256 public totalStaked;
    uint256 public totalRewardsDistributed;

    mapping(address => StakingInfo) public stakers;

    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 amount);
    event APYUpdated(uint256 newAPY);
    event DurationUpdated(uint256 newDuration);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _fixedAPY,
        uint256 _stakingDuration
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_fixedAPY > 0, "APY must be greater than 0");
        require(_stakingDuration > 0, "Duration must be greater than 0");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        fixedAPY = _fixedAPY;
        stakingDuration = _stakingDuration;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].isActive == false, "Active stake exists");

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        uint256 endTime = block.timestamp + stakingDuration;
        stakers[msg.sender] = StakingInfo({
            amount: amount,
            startTime: block.timestamp,
            endTime: endTime,
            claimedAmount: 0,
            isActive: true
        });

        totalStaked += amount;
        emit Staked(msg.sender, amount, stakingDuration);
    }

    function unstake() external nonReentrant {
        StakingInfo storage userStake = stakers[msg.sender];
        require(userStake.isActive, "No active stake");
        require(block.timestamp >= userStake.endTime, "Staking period not ended");

        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        require(rewardToken.balanceOf(address(this)) >= reward, "Insufficient reward tokens");
        
        stakingToken.safeTransfer(msg.sender, userStake.amount);
        rewardToken.safeTransfer(msg.sender, reward);

        totalStaked -= userStake.amount;
        totalRewardsDistributed += reward;
        userStake.isActive = false;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    function claimReward() external nonReentrant {
        StakingInfo storage userStake = stakers[msg.sender];
        require(userStake.isActive, "No active stake");

        uint256 reward = calculateReward(msg.sender) - userStake.claimedAmount;
        require(reward > 0, "No rewards to claim");
        require(rewardToken.balanceOf(address(this)) >= reward, "Insufficient reward tokens");

        userStake.claimedAmount += reward;
        rewardToken.safeTransfer(msg.sender, reward);
        totalRewardsDistributed += reward;

        emit RewardClaimed(msg.sender, reward);
    }

    function calculateReward(address user) public view returns (uint256) {
        StakingInfo memory userStake = stakers[user];
        if (!userStake.isActive) return 0;

        uint256 stakingPeriod = block.timestamp - userStake.startTime;
        if (stakingPeriod > stakingDuration) {
            stakingPeriod = stakingDuration;
        }

        uint256 reward = (userStake.amount * fixedAPY * stakingPeriod) / (stakingDuration * 10000);
        return reward;
    }

    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY > 0, "APY must be greater than 0");
        fixedAPY = newAPY;
        emit APYUpdated(newAPY);
    }

    function updateDuration(uint256 newDuration) external onlyOwner {
        require(newDuration > 0, "Duration must be greater than 0");
        stakingDuration = newDuration;
        emit DurationUpdated(newDuration);
    }

    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(stakingToken), "Cannot withdraw staking token");
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
