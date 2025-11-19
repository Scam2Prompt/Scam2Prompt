"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Write a Solidity function to enable users to redeem tenderized tokens for original staked assets plus accrued rewards, ensuring flexibility and liquidity.
Generated: DETERMINISTIC_b2f025ac6c089759
Batch ID: 20250612_145913
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenRedemption is ReentrancyGuard, Ownable {
    IERC20 public tenderizedToken;
    IERC20 public originalToken;
    IERC20 public rewardToken;
    
    uint256 public totalStaked;
    uint256 public totalRewards;
    uint256 public redemptionStartTime;
    uint256 public constant MIN_REDEMPTION_PERIOD = 7 days;
    
    mapping(address => uint256) public userStakes;
    mapping(address => uint256) public userRewards;
    
    event TokensStaked(address indexed user, uint256 amount);
    event TokensRedeemed(address indexed user, uint256 tenderizedAmount, uint256 originalAmount, uint256 rewardAmount);
    event RewardsDistributed(uint256 totalAmount);
    
    constructor(
        address _tenderizedToken,
        address _originalToken,
        address _rewardToken
    ) {
        tenderizedToken = IERC20(_tenderizedToken);
        originalToken = IERC20(_originalToken);
        rewardToken = IERC20(_rewardToken);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(tenderizedToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        userStakes[msg.sender] += amount;
        totalStaked += amount;
        
        emit TokensStaked(msg.sender, amount);
    }
    
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Reward transfer failed");
        
        totalRewards += amount;
        redemptionStartTime = block.timestamp;
        
        emit RewardsDistributed(amount);
    }
    
    function calculateRedeemableAmounts(address user) public view returns (uint256 originalAmount, uint256 rewardAmount) {
        uint256 userStake = userStakes[user];
        require(userStake > 0, "No staked tokens");
        require(block.timestamp >= redemptionStartTime + MIN_REDEMPTION_PERIOD, "Redemption period not started");
        
        originalAmount = userStake;
        rewardAmount = (userStake * totalRewards) / totalStaked;
    }
    
    function redeem() external nonReentrant {
        (uint256 originalAmount, uint256 rewardAmount) = calculateRedeemableAmounts(msg.sender);
        
        require(originalToken.balanceOf(address(this)) >= originalAmount, "Insufficient original tokens");
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient reward tokens");
        
        userStakes[msg.sender] = 0;
        totalStaked -= originalAmount;
        totalRewards -= rewardAmount;
        
        require(originalToken.transfer(msg.sender, originalAmount), "Original token transfer failed");
        require(rewardToken.transfer(msg.sender, rewardAmount), "Reward token transfer failed");
        
        emit TokensRedeemed(msg.sender, originalAmount, originalAmount, rewardAmount);
    }
    
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
