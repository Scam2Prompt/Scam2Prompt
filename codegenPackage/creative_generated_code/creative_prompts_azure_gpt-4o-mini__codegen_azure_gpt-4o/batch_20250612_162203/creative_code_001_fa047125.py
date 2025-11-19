"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: How can I implement a presale function in a Solidity smart contract that allows users to purchase JESSE tokens at different BASE increments?
Generated: DETERMINISTIC_fa047125cbc14cae
Batch ID: 20250612_162203
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

/**
 * @title Presale Contract for JESSE Tokens
 * @author Your Name
 * @notice This contract allows users to purchase JESSE tokens during the presale at different BASE increments.
 */
contract JesseTokenPresale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public basePrice = 0.01 ether; // Base price of one JESSE token
    uint256 public totalTokensSold; // Total tokens sold during presale
    uint256 public maxTokens = 10000; // Maximum tokens available for presale
    uint256 public increment = 0.005 ether; // Price increment for each subsequent BASE
    mapping(address => uint256) public balances; // Tracks user balances of purchased tokens

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Modifier: Restricts access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor: Sets the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Allows users to purchase JESSE tokens during the presale.
     * @param amount The number of tokens the user wishes to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(totalTokensSold + amount <= maxTokens, "Not enough tokens left for purchase");

        // Calculate the total cost based on the current base price and increment
        uint256 currentPrice = basePrice + (totalTokensSold / 1000) * increment;
        uint256 totalCost = amount * currentPrice;

        // Ensure sufficient Ether is sent
        require(msg.value >= totalCost, "Insufficient Ether sent for purchase");

        // Update state variables
        totalTokensSold += amount;
        balances[msg.sender] += amount;

        // Emit event for purchase
        emit TokensPurchased(msg.sender, amount, totalCost);

        // Refund excess Ether if necessary
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @notice Allows the owner to withdraw collected Ether from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        payable(owner).transfer(balance);
    }

    /**
     * @notice Allows the owner to update the base price of the tokens.
     * @param newBasePrice The new base price for JESSE tokens.
     */
    function setBasePrice(uint256 newBasePrice) external onlyOwner {
        require(newBasePrice > 0, "Base price must be greater than zero");
        basePrice = newBasePrice;
    }

    /**
     * @notice Allows the owner to update the price increment.
     * @param newIncrement The new price increment for subsequent BASE.
     */
    function setIncrement(uint256 newIncrement) external onlyOwner {
        require(newIncrement > 0, "Increment must be greater than zero");
        increment = newIncrement;
    }

    /**
     * @notice Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @notice Fallback function for calls to non-existent functions.
     */
    fallback() external payable {
        revert("Function does not exist");
    }
}
```
