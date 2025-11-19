"""
Generated Code Metadata:
========================
Original URL: https://scottytheais.web.app
Prompt: Write a smart contract in Solidity to automate staking $SCOTTY tokens and calculate APY rewards as outlined in the Scotty AI platform.
Generated: DETERMINISTIC_c798ddbfb00d3836
Batch ID: 20250612_152656
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

contract ScottyStaking is Ownable, ReentrancyGuard {
    IERC20 public scottyToken;
    
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lastClaimTime;
        uint256 rewardDebt;
    }
    
    uint256 public constant APY = 15; // 15% APY
    uint256 public constant SECONDS_IN_YEAR = 31536000;
    uint256 public totalStaked;
    uint256 public rewardPool;
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPoolFunded(uint256 amount);
    
    constructor(address _scottyToken) {
        require(_scottyToken != address(0), "Invalid token address");
        scottyToken = IERC20(_scottyToken);
    }
    
    function fundRewardPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        rewardPool += amount;
        emit RewardPoolFunded(amount);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }
        
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            startTime: block.timestamp,
            lastClaimTime: block.timestamp,
            rewardDebt: stakes[msg.sender].rewardDebt
        });
        
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }
    
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        _claimRewards();
        
        userStake.amount -= amount;
        totalStaked -= amount;
        
        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }
    
    function claimRewards() external nonReentrant {
        _claimRewards();
    }
    
    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount == 0) return;
        
        uint256 reward = calculateReward(msg.sender);
        if (reward == 0) return;
        
        require(rewardPool >= reward, "Insufficient reward pool");
        
        userStake.lastClaimTime = block.timestamp;
        rewardPool -= reward;
        
        require(scottyToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }
    
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;
        
        uint256 timeElapsed = block.timestamp - userStake.lastClaimTime;
        uint256 rewardPerYear = (userStake.amount * APY) / 100;
        uint256 reward = (rewardPerYear * timeElapsed) / SECONDS_IN_YEAR;
        
        return reward;
    }
    
    function getStakeInfo(address user) external view returns (uint256, uint256, uint256) {
        Stake memory userStake = stakes[user];
        return (
            userStake.amount,
            userStake.startTime,
            calculateReward(user)
        );
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = scottyToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(scottyToken.transfer(owner(), balance), "Transfer failed");
    }
}
```
