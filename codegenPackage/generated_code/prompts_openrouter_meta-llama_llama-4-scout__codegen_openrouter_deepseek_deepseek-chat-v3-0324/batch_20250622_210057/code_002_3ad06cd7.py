"""
Generated Code Metadata:
========================
Original URL: https://arbius-en.pages.dev
Prompt: "Design a staking model for Arbius token that incorporates a continuous halving process and adjustment algorithm for task rewards, ensuring a decentralized and secure network."
Generated: DETERMINISTIC_3ad06cd713fea694
Batch ID: 20250622_210057
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

contract ArbiusStaking is Ownable, ReentrancyGuard {
    IERC20 public arbiusToken;
    
    // Staking parameters
    uint256 public constant INITIAL_REWARD = 1000 * 1e18; // 1000 tokens
    uint256 public constant HALVING_INTERVAL = 210000; // Blocks
    uint256 public constant ADJUSTMENT_INTERVAL = 10000; // Blocks
    
    // State variables
    uint256 public currentReward;
    uint256 public totalStaked;
    uint256 public lastHalvingBlock;
    uint256 public lastAdjustmentBlock;
    uint256 public rewardAdjustmentFactor = 1e18; // 1.0 in 18 decimals
    
    // User stakes
    struct Stake {
        uint256 amount;
        uint256 lastClaimBlock;
    }
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardAdjusted(uint256 newFactor);
    event RewardHalved(uint256 newReward);
    
    constructor(address _arbiusToken) {
        arbiusToken = IERC20(_arbiusToken);
        currentReward = INITIAL_REWARD;
        lastHalvingBlock = block.number;
        lastAdjustmentBlock = block.number;
    }
    
    // Stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to contract
        require(
            arbiusToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        
        // Update user stake
        if (stakes[msg.sender].amount > 0) {
            _claimReward();
        }
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastClaimBlock = block.number;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    // Unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");
        
        _claimReward();
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        // Transfer tokens back to user
        require(
            arbiusToken.transfer(msg.sender, amount),
            "Transfer failed"
        );
        
        emit Unstaked(msg.sender, amount);
    }
    
    // Claim rewards
    function claimReward() external nonReentrant {
        _claimReward();
    }
    
    // Internal function to claim rewards
    function _claimReward() internal {
        uint256 reward = calculateReward(msg.sender);
        if (reward == 0) {
            stakes[msg.sender].lastClaimBlock = block.number;
            return;
        }
        
        // Mint new tokens as reward
        require(
            arbiusToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );
        
        stakes[msg.sender].lastClaimBlock = block.number;
        emit RewardClaimed(msg.sender, reward);
        
        // Check for halving event
        _checkHalving();
        // Check for reward adjustment
        _checkAdjustment();
    }
    
    // Calculate reward for user
    function calculateReward(address user) public view returns (uint256) {
        if (stakes[user].amount == 0) return 0;
        
        uint256 blocksSinceLastClaim = block.number - stakes[user].lastClaimBlock;
        uint256 rewardPerBlock = (currentReward * rewardAdjustmentFactor) / 1e18;
        
        return (stakes[user].amount * blocksSinceLastClaim * rewardPerBlock) / totalStaked;
    }
    
    // Check for halving event
    function _checkHalving() internal {
        if (block.number - lastHalvingBlock >= HALVING_INTERVAL) {
            currentReward /= 2;
            lastHalvingBlock = block.number;
            emit RewardHalved(currentReward);
        }
    }
    
    // Check for reward adjustment
    function _checkAdjustment() internal {
        if (block.number - lastAdjustmentBlock >= ADJUSTMENT_INTERVAL) {
            // Simple adjustment algorithm: decrease reward if staking is high, increase if low
            uint256 targetStaking = arbiusToken.totalSupply() / 2; // Target 50% staked
            if (totalStaked > targetStaking) {
                rewardAdjustmentFactor = rewardAdjustmentFactor * 95 / 100; // Decrease by 5%
            } else {
                rewardAdjustmentFactor = rewardAdjustmentFactor * 105 / 100; // Increase by 5%
            }
            
            // Clamp between 0.1 and 10.0
            if (rewardAdjustmentFactor < 1e17) rewardAdjustmentFactor = 1e17;
            if (rewardAdjustmentFactor > 10e18) rewardAdjustmentFactor = 10e18;
            
            lastAdjustmentBlock = block.number;
            emit RewardAdjusted(rewardAdjustmentFactor);
        }
    }
    
    // Emergency function to recover tokens (only owner)
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
