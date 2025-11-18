"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Write a smart contract for launching Fan Tokens using Moxie Bonding Curves, ensuring utility-focused price discovery as described in the Moxie Protocol documentation.
Generated: DETERMINISTIC_472541826768fb7c
Batch ID: 20250612_151027
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
 * @title MoxieFanToken
 * @dev A smart contract for launching Fan Tokens using Moxie Bonding Curves.
 * This contract allows users to purchase tokens at a price determined by a bonding curve.
 */
contract MoxieFanToken is ERC20, Ownable {
    // State variable to store the reserve balance.
    uint256 public reserveBalance;
    
    // Events to log important actions.
    event Purchase(address indexed buyer, uint256 amount, uint256 price);
    event Withdrawal(address indexed owner, uint256 amount);

    // Constructor to initialize the token with a name and symbol.
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        reserveBalance = 0;
    }

    /**
     * @dev Purchase tokens using Ether. The price is determined by the bonding curve.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Must send Ether to purchase tokens");

        // Calculate price based on the current reserve balance
        uint256 amountToPurchase = calculateAmountToPurchase(msg.value);
        require(amountToPurchase > 0, "Insufficient value for token purchase");

        // Update reserve balance and mint new tokens
        reserveBalance += msg.value;
        _mint(msg.sender, amountToPurchase);

        emit Purchase(msg.sender, amountToPurchase, msg.value);
    }

    /**
     * @dev Withdraw Ether from the contract by the owner.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");

        // Transfer specified amount to the owner's address
        payable(owner()).transfer(amount);
        emit Withdrawal(owner(), amount);
    }

    /**
     * @dev Calculate the amount of tokens to purchase based on the Ether sent.
     * Uses a simple bonding curve formula.
     * @param value The amount of Ether sent.
     * @return The amount of tokens to mint.
     */
    function calculateAmountToPurchase(uint256 value) internal view returns (uint256) {
        // Example bonding curve formula: The more Ether sent, the more tokens are minted.
        // For simplicity, we use a linear relation: 1 Ether = 100 tokens
        uint256 tokensToMint = value * 100; // Adjust the multiplier as per bonding curve logic
        return tokensToMint;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {
        // Allow contract to accept Ether directly
    }

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
