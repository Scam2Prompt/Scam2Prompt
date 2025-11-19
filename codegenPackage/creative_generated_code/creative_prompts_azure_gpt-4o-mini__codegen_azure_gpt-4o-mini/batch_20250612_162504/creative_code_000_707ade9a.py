"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-sale1.vercel.app
Prompt: How can I implement a token sale feature that allows users to select a wallet and specify the amount of BeyBlade (BBD) tokens to purchase at a price of 0.0500 SOL?
Generated: DETERMINISTIC_707ade9adaff67d1
Batch ID: 20250612_162504
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BeyBladeTokenSale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    IERC20 public bbdToken;
    
    // Price of one BBD token in SOL
    uint256 public tokenPriceInSOL = 0.0500 ether;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Modifier to check if the sale is ongoing
    modifier saleActive() {
        require(bbdToken.balanceOf(address(this)) > 0, "Sale is inactive or tokens sold out");
        _;
    }

    // Constructor to initialize the token sale contract
    constructor(IERC20 _bbdToken) {
        require(address(_bbdToken) != address(0), "Invalid token address");
        bbdToken = _bbdToken;
    }

    // Function to purchase BBD tokens
    function purchaseTokens(uint256 tokenAmount) external payable saleActive {
        // Calculate the total cost
        uint256 totalCost = tokenAmount.mul(tokenPriceInSOL);
        
        // Ensure the sent Ether is equal to the total cost
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Check if the contract has enough tokens for the purchase
        require(bbdToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens available");

        // Transfer tokens to the buyer
        bbdToken.transfer(msg.sender, tokenAmount);

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, tokenAmount, totalCost);

        // Refund any excess Ether sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value.sub(totalCost));
        }
    }

    // Function to withdraw collected Ether to the owner's address
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to allow the owner to update the token price
    function updateTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero");
        tokenPriceInSOL = newPrice;
    }

    // Function to withdraw unsold tokens after the sale
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 remainingTokens = bbdToken.balanceOf(address(this));
        require(remainingTokens > 0, "No unsold tokens to withdraw");
        bbdToken.transfer(owner(), remainingTokens);
    }
}
```
