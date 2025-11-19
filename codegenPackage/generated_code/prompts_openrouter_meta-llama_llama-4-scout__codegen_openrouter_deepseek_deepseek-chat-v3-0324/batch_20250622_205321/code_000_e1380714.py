"""
Generated Code Metadata:
========================
Original URL: https://paxful.bond
Prompt: What is Paxful Bond and how does it relate to DeFi on Ethereum?
Generated: DETERMINISTIC_e138071459e2c695
Batch ID: 20250622_205321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simple implementation of a Paxful Bond-like token on Ethereum
# using Solidity. It includes basic DeFi functionality like staking and rewards.

# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PaxfulBond
 * @dev A simple ERC20 token with DeFi staking functionality
 */
contract PaxfulBond is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant SECONDS_IN_YEAR = 31536000;
    
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardStartTimes;
    mapping(address => uint256) public accumulatedRewards;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    
    constructor() ERC20("Paxful Bond", "PXB") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Initial supply: 1M tokens
    }
    
    /**
     * @dev Stake tokens to earn rewards
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Calculate pending rewards before updating balance
        if (stakedBalances[msg.sender] > 0) {
            accumulatedRewards[msg.sender] += calculateReward(msg.sender);
        }
        
        _transfer(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        rewardStartTimes[msg.sender] = block.timestamp;
        
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake tokens and claim rewards
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        
        // Calculate and transfer rewards
        uint256 reward = calculateReward(msg.sender) + accumulatedRewards[msg.sender];
        if (reward > 0) {
            _mint(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
        
        // Reset accumulated rewards
        accumulatedRewards[msg.sender] = 0;
        
        // Transfer staked tokens back
        stakedBalances[msg.sender] -= amount;
        _transfer(address(this), msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Calculate current reward for a staker
     * @param staker The address of the staker
     * @return The calculated reward amount
     */
    function calculateReward(address staker) public view returns (uint256) {
        if (stakedBalances[staker] == 0) return 0;
        
        uint256 stakingDuration = block.timestamp - rewardStartTimes[staker];
        return (stakedBalances[staker] * REWARD_RATE * stakingDuration) / (SECONDS_IN_YEAR * 100);
    }
    
    /**
     * @dev Claim rewards without unstaking
     */
    function claimReward() external nonReentrant {
        uint256 reward = calculateReward(msg.sender) + accumulatedRewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        accumulatedRewards[msg.sender] = 0;
        rewardStartTimes[msg.sender] = block.timestamp;
        
        _mint(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }
}
```
