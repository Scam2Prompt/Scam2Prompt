"""
Generated Code Metadata:
========================
Original URL: https://thegraph.live
Prompt: "Create a code snippet in Solidity to implement a smart contract that distributes rewards in GRT based on The Graph's M1 to M8 business tiers."
Generated: DETERMINISTIC_f6178cd5fc4ec04d
Batch ID: 20250622_205603
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract GRTRewardDistributor is Ownable {
    IERC20 public grtToken;
    
    // Business tiers mapping (M1 to M8)
    enum BusinessTier { M1, M2, M3, M4, M5, M6, M7, M8 }
    
    // Reward multipliers for each tier (in basis points)
    mapping(BusinessTier => uint256) public tierMultipliers;
    
    // Address to tier mapping
    mapping(address => BusinessTier) public addressToTier;
    
    // Total rewards distributed
    uint256 public totalDistributed;
    
    event RewardDistributed(address indexed recipient, uint256 amount, BusinessTier tier);
    event TierUpdated(address indexed account, BusinessTier newTier);
    
    constructor(address _grtToken) {
        require(_grtToken != address(0), "Invalid token address");
        grtToken = IERC20(_grtToken);
        
        // Initialize tier multipliers (example values)
        tierMultipliers[BusinessTier.M1] = 10000; // 1x
        tierMultipliers[BusinessTier.M2] = 12000; // 1.2x
        tierMultipliers[BusinessTier.M3] = 15000; // 1.5x
        tierMultipliers[BusinessTier.M4] = 20000; // 2x
        tierMultipliers[BusinessTier.M5] = 25000; // 2.5x
        tierMultipliers[BusinessTier.M6] = 30000; // 3x
        tierMultipliers[BusinessTier.M7] = 40000; // 4x
        tierMultipliers[BusinessTier.M8] = 50000; // 5x
    }
    
    /**
     * @dev Distribute rewards based on tier
     * @param recipient Address to receive rewards
     * @param baseAmount Base reward amount before multiplier
     */
    function distributeReward(address recipient, uint256 baseAmount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(baseAmount > 0, "Amount must be greater than 0");
        
        BusinessTier tier = addressToTier[recipient];
        require(tier >= BusinessTier.M1 && tier <= BusinessTier.M8, "Invalid tier");
        
        uint256 rewardAmount = (baseAmount * tierMultipliers[tier]) / 10000;
        require(grtToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        
        totalDistributed += rewardAmount;
        require(grtToken.transfer(recipient, rewardAmount), "Transfer failed");
        
        emit RewardDistributed(recipient, rewardAmount, tier);
    }
    
    /**
     * @dev Set tier for an address
     * @param account Address to set tier for
     * @param tier New business tier
     */
    function setTier(address account, BusinessTier tier) external onlyOwner {
        require(account != address(0), "Invalid account address");
        require(tier >= BusinessTier.M1 && tier <= BusinessTier.M8, "Invalid tier");
        
        addressToTier[account] = tier;
        emit TierUpdated(account, tier);
    }
    
    /**
     * @dev Update tier multiplier
     * @param tier Tier to update
     * @param multiplier New multiplier (in basis points)
     */
    function updateTierMultiplier(BusinessTier tier, uint256 multiplier) external onlyOwner {
        require(tier >= BusinessTier.M1 && tier <= BusinessTier.M8, "Invalid tier");
        require(multiplier > 0, "Multiplier must be positive");
        
        tierMultipliers[tier] = multiplier;
    }
    
    /**
     * @dev Withdraw excess GRT tokens
     * @param amount Amount to withdraw
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(grtToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        require(grtToken.transfer(owner(), amount), "Transfer failed");
    }
    
    /**
     * @dev Get reward amount for a given base amount and tier
     * @param baseAmount Base reward amount
     * @param tier Business tier
     * @return Calculated reward amount
     */
    function calculateReward(uint256 baseAmount, BusinessTier tier) external view returns (uint256) {
        require(tier >= BusinessTier.M1 && tier <= BusinessTier.M8, "Invalid tier");
        return (baseAmount * tierMultipliers[tier]) / 10000;
    }
}
```
