"""
Generated Code Metadata:
========================
Original URL: https://muzikoin.pages.dev
Prompt: Write a smart contract in Solidity for a music token sale platform like MuziKoin, incorporating blockchain technology for transparent and secure transactions.
Generated: DETERMINISTIC_fef3a07a95c80737
Batch ID: 20250622_204857
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

/**
 * @title MusicTokenSale
 * @dev A smart contract for a music token sale platform, enabling transparent and secure transactions.
 */
contract MusicTokenSale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public totalTokensSold; // Total tokens sold
    mapping(address => uint256) public balances; // Tracks token balances of buyers

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);
    event TokenPriceUpdated(uint256 oldPrice, uint256 newPrice);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenPrice Price of one token in wei.
     */
    constructor(uint256 _tokenPrice) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        owner = msg.sender;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to purchase tokens.
     * The buyer sends Ether to the contract, and tokens are credited to their balance.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Ether sent must be greater than zero");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = msg.value / tokenPrice;
        require(tokensToPurchase > 0, "Insufficient Ether to purchase tokens");

        // Update state variables
        balances[msg.sender] += tokensToPurchase;
        totalTokensSold += tokensToPurchase;

        // Emit event
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function for the owner to withdraw Ether from the contract.
     * @param _amount Amount of Ether to withdraw in wei.
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient contract balance");

        // Transfer Ether to the owner
        payable(owner).transfer(_amount);

        // Emit event
        emit TokensWithdrawn(owner, _amount);
    }

    /**
     * @dev Function for the owner to update the token price.
     * @param _newPrice New price of one token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero");

        // Emit event before updating the price
        emit TokenPriceUpdated(tokenPrice, _newPrice);

        // Update token price
        tokenPrice = _newPrice;
    }

    /**
     * @dev Function to get the contract's Ether balance.
     * @return The Ether balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to get the token balance of a specific address.
     * @param _address Address to query the token balance.
     * @return The token balance of the specified address.
     */
    function getTokenBalance(address _address) external view returns (uint256) {
        return balances[_address];
    }
}
```
