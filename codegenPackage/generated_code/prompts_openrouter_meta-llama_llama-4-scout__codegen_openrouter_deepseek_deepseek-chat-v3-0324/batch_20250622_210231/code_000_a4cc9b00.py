"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-def.pages.dev
Prompt: Write a smart contract in Solidity for a staking system that distributes rewards over a period of two years, similar to Dogecoin20's staking mechanism.
Generated: DETERMINISTIC_a4cc9b002642bcc0
Batch ID: 20250622_210231
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

contract StakingRewards is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lastClaimTime;
        uint256 totalRewardsClaimed;
    }

    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardsToken;

    uint256 public constant REWARD_DURATION = 730 days; // 2 years
    uint256 public constant REWARD_RATE_PER_SECOND = 1 ether / (30 days * 24 hours * 60 minutes * 60 seconds); // Example rate
    uint256 public totalStaked;
    uint256 public totalRewardsDistributed;

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _stakingToken, address _rewardsToken) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        
        Stake storage userStake = stakes[msg.sender];
        
        // Claim any pending rewards before staking
        if (userStake.amount > 0) {
            _claimRewards();
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        
        userStake.amount += amount;
        userStake.startTime = block.timestamp;
        userStake.lastClaimTime = block.timestamp;
        
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        // Claim any pending rewards before unstaking
        _claimRewards();
        
        userStake.amount -= amount;
        totalStaked -= amount;
        
        stakingToken.safeTransfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to claim rewards");
        
        uint256 reward = calculateRewards(msg.sender);
        if (reward > 0) {
            userStake.lastClaimTime = block.timestamp;
            userStake.totalRewardsClaimed += reward;
            totalRewardsDistributed += reward;
            
            rewardsToken.safeTransfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;
        
        uint256 endTime = userStake.startTime + REWARD_DURATION;
        uint256 currentTime = block.timestamp < endTime ? block.timestamp : endTime;
        
        uint256 timeSinceLastClaim = currentTime - userStake.lastClaimTime;
        return userStake.amount * timeSinceLastClaim * REWARD_RATE_PER_SECOND;
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardsToken.balanceOf(address(this));
        rewardsToken.safeTransfer(owner(), balance);
    }
}
```
