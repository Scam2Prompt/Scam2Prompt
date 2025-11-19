"""
Generated Code Metadata:
========================
Original URL: https://upshift.fi
Prompt: Write a smart contract in Solidity that incorporates Upshift Finance's rewards boost mechanism (e.g., 1.25x upUSDC PT Boost) for users who participate in voting.
Generated: DETERMINISTIC_a5820648d9acdd11
Batch ID: 20250612_153954
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

contract VotingRewardsBoost is Ownable, ReentrancyGuard {
    IERC20 public immutable rewardToken;
    IERC20 public immutable stakingToken;

    // Reward boost parameters
    uint256 public constant BASE_REWARD_RATE = 1 ether; // 1x base reward
    uint256 public constant BOOSTED_REWARD_RATE = 1.25 ether; // 1.25x boosted reward
    uint256 public constant VOTE_THRESHOLD = 1; // Minimum votes required for boost

    // User data
    struct UserInfo {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 pendingRewards;
        uint256 votesCast;
        bool isBoostActive;
    }

    mapping(address => UserInfo) public userInfo;

    // Contract state
    uint256 public totalStaked;
    uint256 public accRewardPerShare;
    uint256 public lastRewardUpdate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event Voted(address indexed user, uint256 votes);
    event BoostActivated(address indexed user);

    constructor(address _rewardToken, address _stakingToken) {
        require(_rewardToken != address(0), "Invalid reward token");
        require(_stakingToken != address(0), "Invalid staking token");
        
        rewardToken = IERC20(_rewardToken);
        stakingToken = IERC20(_stakingToken);
        lastRewardUpdate = block.timestamp;
    }

    // Update reward variables
    function updateRewards() public {
        if (block.timestamp <= lastRewardUpdate) return;

        if (totalStaked > 0) {
            uint256 reward = calculatePendingRewards();
            accRewardPerShare += (reward * 1e18) / totalStaked;
        }

        lastRewardUpdate = block.timestamp;
    }

    // Calculate pending rewards since last update
    function calculatePendingRewards() public view returns (uint256) {
        // In a real implementation, this would calculate actual rewards
        // For demo purposes, we return a fixed amount
        return 1000 * 1e18; // Example: 1000 tokens per second
    }

    // Stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        updateRewards();

        if (user.amountStaked > 0) {
            uint256 pending = (user.amountStaked * accRewardPerShare) / 1e18 - user.rewardDebt;
            if (pending > 0) {
                user.pendingRewards += pending;
            }
        }

        stakingToken.transferFrom(msg.sender, address(this), _amount);
        user.amountStaked += _amount;
        user.rewardDebt = (user.amountStaked * accRewardPerShare) / 1e18;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amountStaked >= _amount, "Insufficient staked amount");

        updateRewards();

        uint256 pending = (user.amountStaked * accRewardPerShare) / 1e18 - user.rewardDebt;
        if (pending > 0) {
            user.pendingRewards += pending;
        }

        user.amountStaked -= _amount;
        user.rewardDebt = (user.amountStaked * accRewardPerShare) / 1e18;
        totalStaked -= _amount;

        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Cast a vote and check for boost eligibility
    function vote() external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amountStaked > 0, "Must stake to vote");

        user.votesCast += 1;
        
        if (user.votesCast >= VOTE_THRESHOLD && !user.isBoostActive) {
            user.isBoostActive = true;
            emit BoostActivated(msg.sender);
        }

        emit Voted(msg.sender, user.votesCast);
    }

    // Claim rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updateRewards();

        uint256 pending = (user.amountStaked * accRewardPerShare) / 1e18 - user.rewardDebt;
        if (pending > 0) {
            user.pendingRewards += pending;
        }

        uint256 rewardAmount = user.pendingRewards;
        if (user.isBoostActive) {
            rewardAmount = (rewardAmount * BOOSTED_REWARD_RATE) / 1e18;
        } else {
            rewardAmount = (rewardAmount * BASE_REWARD_RATE) / 1e18;
        }

        require(rewardAmount > 0, "No rewards to claim");
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");

        user.pendingRewards = 0;
        user.rewardDebt = (user.amountStaked * accRewardPerShare) / 1e18;

        rewardToken.transfer(msg.sender, rewardAmount);
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amountStaked;
        
        require(amount > 0, "Nothing to withdraw");
        
        totalStaked -= amount;
        user.amountStaked = 0;
        user.rewardDebt = 0;
        user.pendingRewards = 0;
        user.isBoostActive = false;

        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Admin function to withdraw excess tokens
    function adminWithdraw(uint256 _amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient balance");
        rewardToken.transfer(owner(), _amount);
    }
}
```
