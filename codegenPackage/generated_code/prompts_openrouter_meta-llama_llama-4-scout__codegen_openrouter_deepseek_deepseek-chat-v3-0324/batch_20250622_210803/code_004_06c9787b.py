"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-token.pages.dev
Prompt: Develop a simple smart contract in Solidity for staking Poodl Inu tokens on the Ethereum blockchain, considering the 30% allocation for the staking kennel.
Generated: DETERMINISTIC_06c9787b4f50fd7c
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PoodlInuStaking is Ownable, ReentrancyGuard {
    IERC20 public poodlInuToken;
    
    // Staking parameters
    uint256 public constant STAKING_ALLOCATION = 30; // 30% allocation
    uint256 public totalStaked;
    uint256 public stakingStartTime;
    uint256 public stakingEndTime;
    uint256 public rewardRate;
    
    // User staking data
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }
    
    mapping(address => Stake) public stakes;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    
    constructor(address _poodlInuToken, uint256 _stakingDurationDays, uint256 _rewardRate) {
        require(_poodlInuToken != address(0), "Invalid token address");
        poodlInuToken = IERC20(_poodlInuToken);
        stakingStartTime = block.timestamp;
        stakingEndTime = stakingStartTime + (_stakingDurationDays * 1 days);
        rewardRate = _rewardRate;
    }
    
    // Stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(block.timestamp < stakingEndTime, "Staking period has ended");
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 allocation = (amount * STAKING_ALLOCATION) / 100;
        uint256 stakableAmount = amount - allocation;
        
        require(
            poodlInuToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
        
        stakes[msg.sender].amount += stakableAmount;
        stakes[msg.sender].stakedAt = block.timestamp;
        totalStaked += stakableAmount;
        
        emit Staked(msg.sender, stakableAmount);
    }
    
    // Unstake tokens
    function unstake() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No staked tokens");
        
        uint256 amount = stakes[msg.sender].amount;
        uint256 reward = calculateReward(msg.sender);
        
        stakes[msg.sender].amount = 0;
        totalStaked -= amount;
        
        require(
            poodlInuToken.transfer(msg.sender, amount + reward),
            "Token transfer failed"
        );
        
        emit Unstaked(msg.sender, amount);
        emit RewardClaimed(msg.sender, reward);
    }
    
    // Calculate reward for staker
    function calculateReward(address staker) public view returns (uint256) {
        if (stakes[staker].amount == 0) return 0;
        
        uint256 stakingDuration = block.timestamp - stakes[staker].stakedAt;
        return (stakes[staker].amount * stakingDuration * rewardRate) / (100 * 1 days);
    }
    
    // Withdraw remaining tokens after staking period (owner only)
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > stakingEndTime, "Staking period not ended");
        uint256 balance = poodlInuToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        require(
            poodlInuToken.transfer(owner(), balance),
            "Token transfer failed"
        );
    }
    
    // Extend staking period (owner only)
    function extendStakingPeriod(uint256 additionalDays) external onlyOwner {
        require(additionalDays > 0, "Invalid duration");
        stakingEndTime += (additionalDays * 1 days);
    }
    
    // Update reward rate (owner only)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Invalid rate");
        rewardRate = newRate;
    }
}
```
