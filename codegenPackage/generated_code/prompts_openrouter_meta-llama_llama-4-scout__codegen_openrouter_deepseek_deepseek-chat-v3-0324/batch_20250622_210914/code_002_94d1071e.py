"""
Generated Code Metadata:
========================
Original URL: https://bonkrewards-6st.pages.dev
Prompt: Generate a smart contract code in Solidity to implement a similar rewards system with dynamic multipliers based on lock duration.
Generated: DETERMINISTIC_94d1071e8b6f8e1b
Batch ID: 20250622_210914
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

contract RewardSystem is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    IERC20 public stakingToken;

    struct Stake {
        uint256 amount;
        uint256 lockDuration;
        uint256 timestamp;
        uint256 claimedRewards;
    }

    mapping(address => Stake[]) public userStakes;
    mapping(uint256 => uint256) public lockDurationMultiplier; // lock duration in days => multiplier (percentage)

    uint256 public constant MAX_LOCK_DURATION = 365 days;
    uint256 public constant MIN_LOCK_DURATION = 7 days;
    uint256 public constant BASE_REWARD_RATE = 10; // 10% APY

    event Staked(address indexed user, uint256 amount, uint256 lockDuration);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);

        // Initialize multipliers (example values)
        lockDurationMultiplier[7 days] = 100;    // 1x
        lockDurationMultiplier[30 days] = 150;   // 1.5x
        lockDurationMultiplier[90 days] = 200;   // 2x
        lockDurationMultiplier[180 days] = 300;  // 3x
        lockDurationMultiplier[365 days] = 500;  // 5x
    }

    function stake(uint256 amount, uint256 lockDuration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            lockDuration >= MIN_LOCK_DURATION && lockDuration <= MAX_LOCK_DURATION,
            "Invalid lock duration"
        );
        require(
            lockDurationMultiplier[lockDuration] > 0,
            "No multiplier set for this duration"
        );

        stakingToken.transferFrom(msg.sender, address(this), amount);

        userStakes[msg.sender].push(Stake({
            amount: amount,
            lockDuration: lockDuration,
            timestamp: block.timestamp,
            claimedRewards: 0
        }));

        emit Staked(msg.sender, amount, lockDuration);
    }

    function calculateRewards(address user, uint256 stakeIndex) public view returns (uint256) {
        Stake memory stakeInfo = userStakes[user][stakeIndex];
        if (block.timestamp <= stakeInfo.timestamp) return 0;

        uint256 timeElapsed = block.timestamp - stakeInfo.timestamp;
        if (timeElapsed > stakeInfo.lockDuration) {
            timeElapsed = stakeInfo.lockDuration;
        }

        uint256 multiplier = lockDurationMultiplier[stakeInfo.lockDuration];
        uint256 effectiveRate = (BASE_REWARD_RATE * multiplier) / 100;
        
        return (stakeInfo.amount * effectiveRate * timeElapsed) / (365 days * 100);
    }

    function claimRewards(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");

        Stake storage stakeInfo = userStakes[msg.sender][stakeIndex];
        uint256 rewards = calculateRewards(msg.sender, stakeIndex) - stakeInfo.claimedRewards;
        require(rewards > 0, "No rewards to claim");

        stakeInfo.claimedRewards += rewards;
        rewardToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    function unstake(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");

        Stake memory stakeInfo = userStakes[msg.sender][stakeIndex];
        require(
            block.timestamp >= stakeInfo.timestamp + stakeInfo.lockDuration,
            "Lock period not ended"
        );

        // Claim any remaining rewards first
        uint256 rewards = calculateRewards(msg.sender, stakeIndex) - stakeInfo.claimedRewards;
        if (rewards > 0) {
            rewardToken.transfer(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        // Remove the stake
        _removeStake(msg.sender, stakeIndex);

        // Return staked tokens
        stakingToken.transfer(msg.sender, stakeInfo.amount);
        emit Unstaked(msg.sender, stakeInfo.amount);
    }

    function _removeStake(address user, uint256 stakeIndex) private {
        uint256 lastIndex = userStakes[user].length - 1;
        if (stakeIndex != lastIndex) {
            userStakes[user][stakeIndex] = userStakes[user][lastIndex];
        }
        userStakes[user].pop();
    }

    function setLockDurationMultiplier(uint256 duration, uint256 multiplier) external onlyOwner {
        require(duration >= MIN_LOCK_DURATION && duration <= MAX_LOCK_DURATION, "Invalid duration");
        lockDurationMultiplier[duration] = multiplier;
    }

    function emergencyWithdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    function getUserStakesCount(address user) external view returns (uint256) {
        return userStakes[user].length;
    }

    function getTotalStaked(address user) external view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < userStakes[user].length; i++) {
            total += userStakes[user][i].amount;
        }
        return total;
    }
}
```
