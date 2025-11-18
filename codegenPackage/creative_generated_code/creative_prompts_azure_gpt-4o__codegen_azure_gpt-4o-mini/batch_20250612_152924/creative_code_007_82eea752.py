"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Write a Solidity contract that includes an event to log each SHROOM token purchase, including the buyer's address, ETH amount, and token quantity.
Generated: DETERMINISTIC_82eea752cf2daaab
Batch ID: 20250612_152924
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

// Import OpenZeppelin's ERC20 interface for creating SHROOM tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// SHROOM Token Purchase Contract
contract ShroomPurchase is Ownable {
    // Declare the SHROOM token interface
    IERC20 public shroomToken;

    // Event to log each SHROOM token purchase
    event ShroomPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenQuantity);

    // Constructor to initialize the SHROOM token address
    constructor(address _shroomTokenAddress) {
        require(_shroomTokenAddress != address(0), "Invalid token address");
        shroomToken = IERC20(_shroomTokenAddress);
    }

    // Function to purchase SHROOM tokens
    function purchaseShroomTokens(uint256 tokenQuantity) external payable {
        require(tokenQuantity > 0, "Token quantity must be greater than zero");
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Assuming a fixed price of 1 ETH for 100 SHROOM tokens
        uint256 pricePerToken = 1 ether / 100;
        uint256 totalCost = pricePerToken * tokenQuantity;

        // Ensure the buyer has sent enough ETH
        require(msg.value >= totalCost, "Insufficient ETH sent");

        // Transfer SHROOM tokens to the buyer
        uint256 totalTokens = tokenQuantity * 1 ether; // Scale to handle decimals
        require(shroomToken.balanceOf(address(this)) >= totalTokens, "Not enough tokens in contract");

        // Transfer the tokens
        shroomToken.transfer(msg.sender, totalTokens);

        // Emit the purchase event
        emit ShroomPurchased(msg.sender, msg.value, tokenQuantity);

        // Refund any excess ETH sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    // Function to withdraw ETH from the contract, only callable by the owner
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw SHROOM tokens from the contract, only callable by the owner
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(shroomToken.balanceOf(address(this)) >= amount, "Insufficient token balance");
        shroomToken.transfer(owner(), amount);
    }

    // Fallback function to prevent accidental ETH deposits
    receive() external payable {
        revert("Direct ETH deposits not allowed");
    }
}
```
