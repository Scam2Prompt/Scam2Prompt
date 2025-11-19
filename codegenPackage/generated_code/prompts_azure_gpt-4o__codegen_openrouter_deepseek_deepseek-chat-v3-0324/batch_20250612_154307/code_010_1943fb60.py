"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity contract that implements a reward distribution mechanism for $STARS holders, ensuring higher rewards for larger token holdings, as described in the Crypto All-Stars tokenomics.
Generated: DETERMINISTIC_1943fb6032be838e
Batch ID: 20250612_154307
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

contract StarsRewardDistributor is Ownable, ReentrancyGuard {
    IERC20 public starsToken;
    IERC20 public rewardToken;
    
    uint256 public totalDistributedRewards;
    uint256 public lastDistributionTime;
    uint256 public distributionInterval;
    uint256 public rewardPerInterval;
    
    mapping(address => uint256) public lastClaimTime;
    mapping(address => uint256) public pendingRewards;
    
    event RewardsDistributed(address indexed user, uint256 amount);
    event DistributionParametersUpdated(uint256 interval, uint256 reward);
    
    constructor(
        address _starsToken,
        address _rewardToken,
        uint256 _distributionInterval,
        uint256 _rewardPerInterval
    ) {
        require(_starsToken != address(0), "Invalid STARS token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_distributionInterval > 0, "Interval must be > 0");
        
        starsToken = IERC20(_starsToken);
        rewardToken = IERC20(_rewardToken);
        distributionInterval = _distributionInterval;
        rewardPerInterval = _rewardPerInterval;
        lastDistributionTime = block.timestamp;
    }
    
    function updateDistributionParameters(uint256 _interval, uint256 _reward) external onlyOwner {
        require(_interval > 0, "Interval must be > 0");
        distributionInterval = _interval;
        rewardPerInterval = _reward;
        emit DistributionParametersUpdated(_interval, _reward);
    }
    
    function calculateRewards(address user) public view returns (uint256) {
        if (starsToken.balanceOf(user) == 0) return 0;
        
        uint256 totalSupply = starsToken.totalSupply();
        uint256 userShare = (starsToken.balanceOf(user) * 1e18) / totalSupply;
        uint256 intervalsPassed = (block.timestamp - lastDistributionTime) / distributionInterval;
        
        if (intervalsPassed == 0) return pendingRewards[user];
        
        uint256 totalRewards = intervalsPassed * rewardPerInterval;
        uint256 userReward = (totalRewards * userShare) / 1e18;
        
        return pendingRewards[user] + userReward;
    }
    
    function distributeRewards() external nonReentrant {
        require(block.timestamp >= lastDistributionTime + distributionInterval, "Distribution interval not reached");
        
        uint256 intervalsPassed = (block.timestamp - lastDistributionTime) / distributionInterval;
        uint256 totalRewards = intervalsPassed * rewardPerInterval;
        
        require(rewardToken.balanceOf(address(this)) >= totalRewards, "Insufficient reward tokens");
        
        lastDistributionTime += intervalsPassed * distributionInterval;
        totalDistributedRewards += totalRewards;
        
        uint256 totalSupply = starsToken.totalSupply();
        require(totalSupply > 0, "No tokens staked");
        
        // Distribute rewards proportionally to all holders
        // Actual claims will be calculated when users claim
    }
    
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");
        
        pendingRewards[msg.sender] = 0;
        lastClaimTime[msg.sender] = block.timestamp;
        
        require(rewardToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");
        emit RewardsDistributed(msg.sender, rewardAmount);
    }
    
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(starsToken), "Cannot withdraw STARS tokens");
        IERC20(token).transfer(owner(), amount);
    }
}
```
