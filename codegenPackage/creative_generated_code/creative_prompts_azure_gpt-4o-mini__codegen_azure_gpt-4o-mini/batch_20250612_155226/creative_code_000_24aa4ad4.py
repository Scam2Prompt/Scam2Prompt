"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbidoge.pages.dev
Prompt: Generate a smart contract in Solidity for a meme token similar to Arbidoge, ensuring it has no taxes and a simple buy/sell mechanism.
Generated: DETERMINISTIC_24aa4ad4935082f2
Batch ID: 20250612_155226
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

/// @title MemeToken - A simple ERC20 token with no taxes and basic buy/sell functionality
contract MemeToken is ERC20, Ownable {
    // Event to emit when tokens are bought
    event TokensBought(address indexed buyer, uint256 amount);

    // Event to emit when tokens are sold
    event TokensSold(address indexed seller, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("MemeToken", "MEME") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint 1 million tokens
    }

    /// @notice Function to buy tokens
    /// @dev Tokens can be bought by sending Ether to the contract
    function buyTokens() external payable {
        require(msg.value > 0, "You need to send Ether to buy tokens");
        
        // Calculate the amount of tokens to mint based on a fixed rate
        uint256 tokensToBuy = msg.value * 100; // Example: 1 Ether = 100 tokens
        _transfer(owner(), msg.sender, tokensToBuy);

        // Emit the event for buying tokens
        emit TokensBought(msg.sender, tokensToBuy);
    }

    /// @notice Function to sell tokens back to the contract
    /// @dev Allows users to sell tokens for Ether
    /// @param amount The amount of tokens to sell
    function sellTokens(uint256 amount) external {
        require(amount > 0, "You need to sell at least 1 token");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Calculate the Ether to return to the seller based on a fixed rate
        uint256 etherAmount = amount / 100; // Example: 100 tokens = 1 Ether
        require(address(this).balance >= etherAmount, "Contract has insufficient Ether");

        // Transfer tokens from the seller to the contract
        _transfer(msg.sender, owner(), amount);

        // Transfer Ether to the seller
        payable(msg.sender).transfer(etherAmount);

        // Emit the event for selling tokens
        emit TokensSold(msg.sender, amount);
    }

    /// @notice Function to withdraw Ether from the contract
    /// @dev Only the owner can call this function
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available to withdraw");
        
        // Transfer the entire contract balance to the owner
        payable(owner()).transfer(balance);
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {
        // Allow the contract to receive Ether
    }
}
```
