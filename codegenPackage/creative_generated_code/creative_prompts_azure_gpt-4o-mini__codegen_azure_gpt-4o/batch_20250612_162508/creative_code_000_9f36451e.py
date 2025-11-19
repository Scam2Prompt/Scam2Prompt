"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellydrop.web.app
Prompt: How can I implement a staking utility for a token similar to $Jelly in a decentralized application?
Generated: DETERMINISTIC_9f36451ef093529c
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenStaking
 * @dev A staking contract for ERC20 tokens allowing users to stake tokens and earn rewards.
 * This contract is suitable for tokens with functionality similar to $Jelly.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenStaking is Ownable {
    // ERC20 token that will be staked
    IERC20 public stakingToken;

    // Reward rate per second (adjust based on your needs)
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to their staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to their reward debt
    mapping(address => uint256) public rewardDebt;

    // Last time rewards were calculated globally
    uint256 public lastRewardTime;

    // Accumulated rewards per token, scaled to prevent precision issues
    uint256 public accRewardsPerToken;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Updates the reward variables globally.
     */
    function _updateRewards() internal {
        if (totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate;

        accRewardsPerToken += (reward * 1e18) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     */
    function pendingRewards(address user) public view returns (uint256) {
        uint256 userStaked = stakedBalances[user];
        uint256 userRewardDebt = rewardDebt[user];

        uint256 _accRewardsPerToken = accRewardsPerToken;
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardRate;
            _accRewardsPerToken += (reward * 1e18) / totalStaked;
        }

        return ((userStaked * _accRewardsPerToken) / 1e18) - userRewardDebt;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        _updateRewards();

        stakingToken.transferFrom(msg.sender, address(this), amount);

        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        rewardDebt[msg.sender] = (stakedBalances[msg.sender] * accRewardsPerToken) / 1e18;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient balance");

        _updateRewards();

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        rewardDebt[msg.sender] = (stakedBalances[msg.sender] * accRewardsPerToken) / 1e18;

        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their rewards.
     */
    function claimRewards() external {
        _updateRewards();

        uint256 reward = pendingRewards(msg.sender);
        require(reward > 0, "No rewards available");

        rewardDebt[msg.sender] = (stakedBalances[msg.sender] * accRewardsPerToken) / 1e18;

        stakingToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _rewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        _updateRewards();
        rewardRate = _rewardRate;
    }
}
```
