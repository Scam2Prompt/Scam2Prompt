"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogleonidas.pages.dev
Prompt: Provide a code example for a smart contract that manages the presale of DOG tokens, including the cap and total supply.
Generated: DETERMINISTIC_906bb1450870aeb2
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGTokenPresale
 * @dev Smart contract for managing the presale of DOG tokens
 */
contract DOGTokenPresale is Ownable {
    // The DOG token contract
    ERC20 public dogToken;

    // Total supply of DOG tokens for sale
    uint256 public totalSupply;
    
    // Cap for the presale
    uint256 public cap;

    // Amount of DOG tokens sold
    uint256 public tokensSold;

    // Mapping to track the amount of DOG tokens purchased by each address
    mapping(address => uint256) public contributions;

    // Event to emit when tokens are sold
    event TokensPurchased(address indexed buyer, uint256 amount);
    
    /**
     * @dev Constructor to initialize the presale contract
     * @param _dogToken The address of the DOG token contract
     * @param _totalSupply Total supply of DOG tokens for the presale
     * @param _cap The cap for the presale
     */
    constructor(ERC20 _dogToken, uint256 _totalSupply, uint256 _cap) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(_cap > 0, "Cap must be greater than zero");
        
        dogToken = _dogToken;
        totalSupply = _totalSupply;
        cap = _cap;
        tokensSold = 0;
    }

    /**
     * @dev Function to purchase DOG tokens during the presale
     * @param amount Amount of DOG tokens to purchase
     */
    function buyTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(tokensSold + amount <= totalSupply, "Not enough tokens available for sale");
        require(tokensSold + amount <= cap, "Purchase exceeds presale cap");
        
        // Update state
        tokensSold += amount;
        contributions[msg.sender] += amount;

        // Transfer DOG tokens to the buyer
        dogToken.transfer(msg.sender, amount);
        
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw unsold tokens by the owner after presale ends
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = totalSupply - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens available");

        // Transfer unsold tokens back to owner
        dogToken.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Function to get the amount of tokens purchased by an address
     * @param buyer The address of the buyer
     * @return The amount of DOG tokens purchased by the buyer
     */
    function getContribution(address buyer) external view returns (uint256) {
        return contributions[buyer];
    }
}
```
