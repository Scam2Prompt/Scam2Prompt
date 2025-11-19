"""
Generated Code Metadata:
========================
Original URL: https://nettensor-5u5.pages.dev
Prompt: Create a smart contract in Solidity that interacts with Net Tensor's App Chain and utilizes $NAO tokens for staking and claiming rewards.
Generated: DETERMINISTIC_6bbc158d498d412c
Batch ID: 20250612_152527
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

contract NAOStaking is Ownable, ReentrancyGuard {
    IERC20 public naoToken;
    
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }
    
    uint256 public constant REWARD_RATE = 10; // 10% annual reward
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public totalStaked;
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    constructor(address _naoToken) {
        require(_naoToken != address(0), "Invalid token address");
        naoToken = IERC20(_naoToken);
    }
    
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(naoToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");
        
        if (stakes[msg.sender].amount > 0) {
            claimRewards();
        }
        
        naoToken.transferFrom(msg.sender, address(this), _amount);
        
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + _amount,
            startTime: block.timestamp,
            rewardDebt: stakes[msg.sender].rewardDebt + calculatePendingRewards(msg.sender)
        });
        
        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }
    
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");
        
        claimRewards();
        
        stakes[msg.sender].amount -= _amount;
        totalStaked -= _amount;
        
        naoToken.transfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _amount);
    }
    
    function claimRewards() public nonReentrant {
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        if (pendingRewards > 0) {
            stakes[msg.sender].rewardDebt = 0;
            stakes[msg.sender].startTime = block.timestamp;
            
            naoToken.transfer(msg.sender, pendingRewards);
            emit RewardsClaimed(msg.sender, pendingRewards);
        }
    }
    
    function calculatePendingRewards(address _user) public view returns (uint256) {
        if (stakes[_user].amount == 0) return 0;
        
        uint256 stakedTime = block.timestamp - stakes[_user].startTime;
        uint256 annualReward = (stakes[_user].amount * REWARD_RATE) / 100;
        uint256 pendingRewards = (annualReward * stakedTime) / REWARD_INTERVAL;
        
        return pendingRewards + stakes[_user].rewardDebt;
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = naoToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        naoToken.transfer(owner(), balance);
    }
    
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Rate must be greater than 0");
        REWARD_RATE = _newRate;
    }
}
```
