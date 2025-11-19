"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Write a smart contract in Solidity that enables staking, unstaking, and reward distribution for a token, with features like emergency withdrawal and reward tracking.
Generated: DETERMINISTIC_2c4a40fe13fec1da
Batch ID: 20250622_205929
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

contract StakingContract is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public totalStaked;
    bool public stakingPaused;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastRewardClaimedAt;
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdrawn(address indexed user, uint256 amount);
    event StakingPaused(bool paused);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        stakingPaused = false;
    }

    modifier whenNotPaused() {
        require(!stakingPaused, "Staking is paused");
        _;
    }

    function stake(uint256 amount) external nonReentrant whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            _claimRewards();
        }

        userStake.amount += amount;
        userStake.stakedAt = block.timestamp;
        userStake.lastRewardClaimedAt = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        require(amount > 0, "Amount must be greater than 0");

        _claimRewards();

        userStake.amount -= amount;
        totalStaked -= amount;

        require(
            stakingToken.transfer(msg.sender, amount),
            "Transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount == 0) return;

        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            require(
                rewardToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            emit RewardClaimed(msg.sender, reward);
        }
        userStake.lastRewardClaimedAt = block.timestamp;
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastRewardClaimedAt;
        uint256 reward = (userStake.amount * REWARD_RATE * timeElapsed) / 
                        (REWARD_INTERVAL * 100);
        return reward;
    }

    function emergencyWithdraw() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        uint256 amount = userStake.amount;
        totalStaked -= amount;
        userStake.amount = 0;
        userStake.stakedAt = 0;
        userStake.lastRewardClaimedAt = 0;

        require(
            stakingToken.transfer(msg.sender, amount),
            "Transfer failed"
        );

        emit EmergencyWithdrawn(msg.sender, amount);
    }

    function toggleStakingPause() external onlyOwner {
        stakingPaused = !stakingPaused;
        emit StakingPaused(stakingPaused);
    }

    function withdrawRewardTokens(uint256 amount) external onlyOwner {
        require(
            rewardToken.transfer(owner(), amount),
            "Transfer failed"
        );
    }

    function getStakeInfo(address user) external view returns (uint256, uint256, uint256) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.stakedAt, userStake.lastRewardClaimedAt);
    }
}
```
