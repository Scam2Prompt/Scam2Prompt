"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Write a Solidity function to implement a token burn mechanism for Bitcoin ETF Token, reducing the token supply as milestones are reached.
Generated: DETERMINISTIC_c3a917525456c055
Batch ID: 20250622_205709
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

/**
 * @title BitcoinETFTToken
 * @dev Implementation of a Bitcoin ETF Token with a burn mechanism.
 */
contract BitcoinETFTToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Milestone threshold for burning tokens
    uint256 public milestoneThreshold;

    // Constructor to initialize the token with a name, symbol, and initial supply
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _milestoneThreshold) 
        ERC20(name, symbol) 
    {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        require(_milestoneThreshold > 0, "Milestone threshold must be greater than zero");
        
        _mint(msg.sender, initialSupply);
        milestoneThreshold = _milestoneThreshold;
    }

    /**
     * @dev Function to burn tokens when a milestone is reached.
     * @param amount The amount of tokens to burn.
     */
    function burnTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= balanceOf(msg.sender), "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
        
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Function to check if a milestone has been reached.
     * @return bool indicating if the milestone has been reached.
     */
    function isMilestoneReached() public view returns (bool) {
        return totalSupply() <= milestoneThreshold;
    }

    /**
     * @dev Function to set a new milestone threshold.
     * @param newThreshold The new milestone threshold.
     */
    function setMilestoneThreshold(uint256 newThreshold) external onlyOwner {
        require(newThreshold > 0, "New threshold must be greater than zero");
        milestoneThreshold = newThreshold;
    }
}
```
