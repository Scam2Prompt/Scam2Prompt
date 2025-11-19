"""
Generated Code Metadata:
========================
Original URL: https://bafybeidfgwggshi5syqnklufswynx2u6rumuvgp4jl6n4lbqsolbeshdga.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that integrates the governance mechanism of the $USUAL token, ensuring rewards distribution based on TVL-derived profits as described in the Usual protocol.
Generated: DETERMINISTIC_36b02b57fb9a8906
Batch ID: 20250612_152358
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

contract UsualGovernance is Ownable, ReentrancyGuard {
    IERC20 public usualToken;
    
    struct RewardPeriod {
        uint256 startTime;
        uint256 endTime;
        uint256 totalRewards;
        uint256 totalStaked;
        bool isActive;
    }
    
    struct UserStake {
        uint256 amount;
        uint256 lastClaimedPeriod;
    }
    
    mapping(address => UserStake) public userStakes;
    RewardPeriod[] public rewardPeriods;
    
    uint256 public currentPeriodId;
    uint256 public minStakeDuration = 7 days;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPeriodCreated(uint256 periodId, uint256 startTime, uint256 endTime, uint256 totalRewards);
    
    constructor(address _usualToken) {
        require(_usualToken != address(0), "Invalid token address");
        usualToken = IERC20(_usualToken);
    }
    
    function createRewardPeriod(uint256 _startTime, uint256 _endTime, uint256 _totalRewards) external onlyOwner {
        require(_startTime >= block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_totalRewards > 0, "Rewards must be greater than zero");
        
        rewardPeriods.push(RewardPeriod({
            startTime: _startTime,
            endTime: _endTime,
            totalRewards: _totalRewards,
            totalStaked: 0,
            isActive: true
        }));
        
        emit RewardPeriodCreated(rewardPeriods.length - 1, _startTime, _endTime, _totalRewards);
    }
    
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        UserStake storage userStake = userStakes[msg.sender];
        if (userStake.amount > 0) {
            _claimRewards();
        }
        
        usualToken.transferFrom(msg.sender, address(this), _amount);
        userStake.amount += _amount;
        
        if (rewardPeriods.length > 0 && rewardPeriods[currentPeriodId].isActive) {
            rewardPeriods[currentPeriodId].totalStaked += _amount;
        }
        
        emit Staked(msg.sender, _amount);
    }
    
    function unstake(uint256 _amount) external nonReentrant {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");
        
        _claimRewards();
        
        userStake.amount -= _amount;
        usualToken.transfer(msg.sender, _amount);
        
        if (rewardPeriods.length > 0 && rewardPeriods[currentPeriodId].isActive) {
            rewardPeriods[currentPeriodId].totalStaked -= _amount;
        }
        
        emit Unstaked(msg.sender, _amount);
    }
    
    function claimRewards() external nonReentrant {
        _claimRewards();
    }
    
    function _claimRewards() private {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");
        
        uint256 totalRewards;
        for (uint256 i = userStake.lastClaimedPeriod; i < rewardPeriods.length; i++) {
            RewardPeriod storage period = rewardPeriods[i];
            
            if (!period.isActive || period.totalStaked == 0) continue;
            
            uint256 userShare = (userStake.amount * period.totalRewards) / period.totalStaked;
            totalRewards += userShare;
        }
        
        if (totalRewards > 0) {
            usualToken.transfer(msg.sender, totalRewards);
            emit RewardClaimed(msg.sender, totalRewards);
        }
        
        userStake.lastClaimedPeriod = rewardPeriods.length;
    }
    
    function updateCurrentPeriod(uint256 _periodId) external onlyOwner {
        require(_periodId < rewardPeriods.length, "Invalid period ID");
        currentPeriodId = _periodId;
    }
    
    function setMinStakeDuration(uint256 _duration) external onlyOwner {
        minStakeDuration = _duration;
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = usualToken.balanceOf(address(this));
        usualToken.transfer(owner(), balance);
    }
    
    function getPendingRewards(address _user) external view returns (uint256) {
        UserStake storage userStake = userStakes[_user];
        if (userStake.amount == 0) return 0;
        
        uint256 totalRewards;
        for (uint256 i = userStake.lastClaimedPeriod; i < rewardPeriods.length; i++) {
            RewardPeriod storage period = rewardPeriods[i];
            
            if (!period.isActive || period.totalStaked == 0) continue;
            
            uint256 userShare = (userStake.amount * period.totalRewards) / period.totalStaked;
            totalRewards += userShare;
        }
        
        return totalRewards;
    }
    
    function getActivePeriods() external view returns (RewardPeriod[] memory) {
        uint256 activeCount;
        for (uint256 i = 0; i < rewardPeriods.length; i++) {
            if (rewardPeriods[i].isActive) {
                activeCount++;
            }
        }
        
        RewardPeriod[] memory activePeriods = new RewardPeriod[](activeCount);
        uint256 index;
        for (uint256 i = 0; i < rewardPeriods.length; i++) {
            if (rewardPeriods[i].isActive) {
                activePeriods[index] = rewardPeriods[i];
                index++;
            }
        }
        
        return activePeriods;
    }
}
```
