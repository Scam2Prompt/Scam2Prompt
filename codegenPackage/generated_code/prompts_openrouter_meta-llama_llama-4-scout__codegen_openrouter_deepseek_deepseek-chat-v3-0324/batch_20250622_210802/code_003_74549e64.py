"""
Generated Code Metadata:
========================
Original URL: https://playgorund.pages.dev
Prompt: Design a simple smart contract using Solidity to distribute $BEYOND tokens to users based on their contribution level on the Beyond Blitz platform.
Generated: DETERMINISTIC_74549e646f357cca
Batch ID: 20250622_210802
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title BeyondTokenDistribution
 * @dev A smart contract for distributing $BEYOND tokens based on user contribution levels
 */
contract BeyondTokenDistribution is ERC20, Ownable, Pausable {
    // Contribution levels and corresponding token amounts
    enum ContributionLevel { NOVICE, CONTRIBUTOR, HERO, LEGEND }
    mapping(ContributionLevel => uint256) public levelToReward;
    
    // Track claimed rewards
    mapping(address => bool) public hasClaimed;
    
    // Events
    event TokensDistributed(address indexed recipient, ContributionLevel level, uint256 amount);
    event RewardLevelUpdated(ContributionLevel level, uint256 newAmount);
    
    /**
     * @dev Constructor that initializes the token and sets reward amounts
     */
    constructor() ERC20("BEYOND", "BEYOND") {
        // Initial reward amounts (in wei)
        levelToReward[ContributionLevel.NOVICE] = 1000 * 10**decimals();
        levelToReward[ContributionLevel.CONTRIBUTOR] = 5000 * 10**decimals();
        levelToReward[ContributionLevel.HERO] = 25000 * 10**decimals();
        levelToReward[ContributionLevel.LEGEND] = 100000 * 10**decimals();
        
        // Mint initial supply to contract owner
        _mint(msg.sender, 10000000 * 10**decimals());
    }
    
    /**
     * @dev Claim tokens based on contribution level
     * @param level The user's contribution level
     */
    function claimTokens(ContributionLevel level) external whenNotPaused {
        require(!hasClaimed[msg.sender], "BeyondToken: Tokens already claimed");
        require(address(this).balance >= levelToReward[level], "BeyondToken: Insufficient contract balance");
        
        uint256 rewardAmount = levelToReward[level];
        hasClaimed[msg.sender] = true;
        
        _transfer(owner(), msg.sender, rewardAmount);
        emit TokensDistributed(msg.sender, level, rewardAmount);
    }
    
    /**
     * @dev Update reward amount for a specific level (owner only)
     * @param level The contribution level to update
     * @param amount The new reward amount
     */
    function updateRewardAmount(ContributionLevel level, uint256 amount) external onlyOwner {
        require(amount > 0, "BeyondToken: Reward amount must be positive");
        levelToReward[level] = amount;
        emit RewardLevelUpdated(level, amount);
    }
    
    /**
     * @dev Pause token distribution (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause token distribution (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Withdraw excess tokens from contract (owner only)
     * @param amount The amount to withdraw
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "BeyondToken: Insufficient balance");
        _transfer(address(this), owner(), amount);
    }
}
```
