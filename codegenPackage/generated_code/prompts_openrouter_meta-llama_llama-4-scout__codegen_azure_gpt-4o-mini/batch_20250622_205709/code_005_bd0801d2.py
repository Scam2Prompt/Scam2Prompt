"""
Generated Code Metadata:
========================
Original URL: https://app-shibabudz.web.app
Prompt: Write a function in Solidity to create a smart contract for buying and selling BUDZ tokens.
Generated: DETERMINISTIC_bd0801d2bae2b4e7
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

// Importing the OpenZeppelin ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BUDZToken is an ERC20 token that allows users to buy and sell BUDZ tokens
contract BUDZToken is ERC20, Ownable {
    // Event emitted when tokens are bought
    event TokensBought(address indexed buyer, uint256 amount, uint256 cost);
    
    // Event emitted when tokens are sold
    event TokensSold(address indexed seller, uint256 amount, uint256 revenue);

    // Price of one BUDZ token in wei
    uint256 public tokenPrice;

    // Constructor to initialize the token with a name, symbol, and initial price
    constructor(string memory name, string memory symbol, uint256 initialPrice) 
        ERC20(name, symbol) 
    {
        // Set the initial price of the token
        tokenPrice = initialPrice;
    }

    // Function to buy BUDZ tokens
    function buyTokens(uint256 amount) external payable {
        // Calculate the total cost of the tokens
        uint256 cost = amount * tokenPrice;

        // Ensure the sender has sent enough Ether
        require(msg.value >= cost, "Insufficient Ether sent");

        // Ensure the contract has enough tokens to sell
        require(balanceOf(owner()) >= amount, "Not enough tokens available");

        // Transfer tokens from the owner to the buyer
        _transfer(owner(), msg.sender, amount);

        // Emit the TokensBought event
        emit TokensBought(msg.sender, amount, cost);

        // Refund any excess Ether sent
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    // Function to sell BUDZ tokens
    function sellTokens(uint256 amount) external {
        // Ensure the seller has enough tokens to sell
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Calculate the revenue from the sale
        uint256 revenue = amount * tokenPrice;

        // Transfer tokens from the seller to the owner
        _transfer(msg.sender, owner(), amount);

        // Transfer the revenue to the seller
        payable(msg.sender).transfer(revenue);

        // Emit the TokensSold event
        emit TokensSold(msg.sender, amount, revenue);
    }

    // Function to set a new token price (only owner can call this)
    function setTokenPrice(uint256 newPrice) external onlyOwner {
        tokenPrice = newPrice;
    }

    // Function to withdraw Ether from the contract (only owner can call this)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
