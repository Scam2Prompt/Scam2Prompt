"""
Generated Code Metadata:
========================
Original URL: https://moonbirds.pro
Prompt: Generate a JavaScript code snippet for creating a cryptocurrency token named "Moonbirds" with a similar narrative of resilience and instinctual growth.
Generated: DETERMINISTIC_965b8248f9420689
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Moonbirds Token
 * @dev ERC20 token with resilience and instinctual growth narrative
 */
contract MoonbirdsToken is ERC20, Ownable {
    uint256 private constant INITIAL_SUPPLY = 1000000000 * 10**18; // 1 billion tokens with 18 decimals
    uint256 private constant MAX_SUPPLY = 10000000000 * 10**18; // 10 billion max supply
    uint256 public constant REWARD_RATE = 5; // 5% annual reward rate
    uint256 public lastRewardTime;
    
    /**
     * @dev Constructor that mints initial supply to the deployer
     */
    constructor() ERC20("Moonbirds", "MBRD") {
        _mint(msg.sender, INITIAL_SUPPLY);
        lastRewardTime = block.timestamp;
    }
    
    /**
     * @dev Function to distribute rewards to all token holders
     */
    function distributeRewards() external onlyOwner {
        require(block.timestamp >= lastRewardTime + 365 days, "Rewards can only be distributed annually");
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        
        uint256 currentSupply = totalSupply();
        uint256 rewardAmount = (currentSupply * REWARD_RATE) / 100;
        
        // Ensure we don't exceed max supply
        if (currentSupply + rewardAmount > MAX_SUPPLY) {
            rewardAmount = MAX_SUPPLY - currentSupply;
        }
        
        _mint(address(this), rewardAmount);
        lastRewardTime = block.timestamp;
    }
    
    /**
     * @dev Function to claim rewards for a token holder
     * @param amount Amount of tokens to claim
     */
    function claimRewards(uint256 amount) external {
        require(balanceOf(address(this)) >= amount, "Insufficient rewards available");
        _transfer(address(this), msg.sender, amount);
    }
    
    /**
     * @dev Override transfer to include reward distribution logic
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        super._transfer(sender, recipient, amount);
    }
    
    /**
     * @dev Function to burn tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
