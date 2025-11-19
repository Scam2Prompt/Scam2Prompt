"""
Generated Code Metadata:
========================
Original URL: https://scottytheaidapp.pages.dev
Prompt: Write a Solidity function to allow users to withdraw their staked $SCOTTY tokens while maintaining accurate tracking of their rewards and pool percentage.
Generated: DETERMINISTIC_001c6949eeedf382
Batch ID: 20250612_153526
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

contract ScottyStaking is ReentrancyGuard, Ownable {
    IERC20 public scottyToken;
    
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastRewardCalculationTime;
    }
    
    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    
    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    
    constructor(address _scottyToken) {
        scottyToken = IERC20(_scottyToken);
    }
    
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
    
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }
    
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (block.timestamp - lastUpdateTime) * rewardRate * 1e18 / totalStaked
        );
    }
    
    function earned(address account) public view returns (uint256) {
        return (
            stakes[account].amount * (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18
        ) + rewards[account];
    }
    
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastRewardCalculationTime = block.timestamp;
        totalStaked += amount;
        
        require(
            scottyToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        
        emit Staked(msg.sender, amount);
    }
    
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");
        
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            require(
                scottyToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            emit RewardPaid(msg.sender, reward);
        }
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        require(
            scottyToken.transfer(msg.sender, amount),
            "Withdrawal transfer failed"
        );
        
        emit Withdrawn(msg.sender, amount);
    }
    
    function getStake(address account) external view returns (uint256) {
        return stakes[account].amount;
    }
    
    function getPoolPercentage(address account) external view returns (uint256) {
        if (totalStaked == 0) return 0;
        return (stakes[account].amount * 10000) / totalStaked; // Returns basis points (1/100th of a percent)
    }
}
```
