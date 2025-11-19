"""
Generated Code Metadata:
========================
Original URL: https://token-dogecoin20.pages.dev
Prompt: Write a smart contract in Solidity for a staking system that distributes rewards over a period of two years, similar to Dogecoin20's staking mechanism.
Generated: DETERMINISTIC_a4cc9b002642bcc0
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public constant REWARD_DURATION = 730 days; // 2 years
    uint256 public constant TOTAL_REWARDS = 1000000 * 10**18; // Example: 1M tokens
    uint256 public rewardRate;
    uint256 public stakingStartTime;
    uint256 public stakingEndTime;

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = TOTAL_REWARDS / REWARD_DURATION;
    }

    function startStaking() external onlyOwner {
        require(stakingStartTime == 0, "Staking already started");
        stakingStartTime = block.timestamp;
        stakingEndTime = stakingStartTime + REWARD_DURATION;
    }

    function stake(uint256 amount) external nonReentrant {
        require(stakingStartTime != 0, "Staking not started yet");
        require(block.timestamp < stakingEndTime, "Staking period ended");
        require(amount > 0, "Cannot stake 0");

        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            stakedAt: block.timestamp,
            lastClaimed: block.timestamp
        });
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        require(amount > 0, "Cannot unstake 0");

        _claimRewards();

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        stakingToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No staked amount");
        _claimRewards();
    }

    function _claimRewards() private {
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            stakes[msg.sender].lastClaimed = block.timestamp;
            rewardToken.safeTransfer(msg.sender, rewards);
            emit RewardClaimed(msg.sender, rewards);
        }
    }

    function calculateRewards(address user) public view returns (uint256) {
        Stake memory stakeInfo = stakes[user];
        if (stakeInfo.amount == 0) return 0;

        uint256 endTime = block.timestamp > stakingEndTime ? stakingEndTime : block.timestamp;
        uint256 stakedDuration = endTime - stakeInfo.lastClaimed;
        uint256 rewards = (stakeInfo.amount * rewardRate * stakedDuration) / totalStaked;

        return rewards;
    }

    function withdrawRemainingRewards() external onlyOwner {
        require(block.timestamp > stakingEndTime, "Staking period not ended");
        uint256 balance = rewardToken.balanceOf(address(this));
        rewardToken.safeTransfer(owner(), balance);
    }
}
```
