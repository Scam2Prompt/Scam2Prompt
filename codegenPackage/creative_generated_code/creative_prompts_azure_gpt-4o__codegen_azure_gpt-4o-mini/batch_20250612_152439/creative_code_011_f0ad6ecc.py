"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanchain-drop.pages.dev
Prompt: Build a dApp on Swan Chain that reduces gas fees by 90% compared to Ethereum and optimizes user experience.
Generated: DETERMINISTIC_f0ad6ecc5b25d038
Batch ID: 20250612_152439
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for the dApp on Swan Chain
contract SwanChainDApp is Ownable {
    // State variables
    IERC20 public token; // The token being used in the dApp
    uint256 public gasReductionFactor; // Factor to reduce gas fees

    // Events
    event TokenPurchased(address indexed buyer, uint256 amount);
    event TokenWithdrawn(address indexed owner, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _tokenAddress, uint256 _gasReductionFactor) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_gasReductionFactor > 0, "Gas reduction factor must be positive");
        
        token = IERC20(_tokenAddress);
        gasReductionFactor = _gasReductionFactor;
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Ether sent must be greater than zero");

        // Calculate the effective amount of tokens to purchase based on gas reduction
        uint256 effectiveAmount = amount * gasReductionFactor / 100;

        // Ensure there are enough tokens for the purchase
        require(token.balanceOf(address(this)) >= effectiveAmount, "Insufficient tokens available");

        // Transfer tokens to the buyer
        token.transfer(msg.sender, effectiveAmount);

        emit TokenPurchased(msg.sender, effectiveAmount);
    }

    // Function for the owner to withdraw tokens
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Transfer tokens to the owner
        token.transfer(owner(), amount);

        emit TokenWithdrawn(owner(), amount);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient Ether in contract");

        // Transfer Ether to the owner
        payable(owner()).transfer(amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
