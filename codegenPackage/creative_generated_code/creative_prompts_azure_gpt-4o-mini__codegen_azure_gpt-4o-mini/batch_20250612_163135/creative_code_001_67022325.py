"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap-finance.medium.com
Prompt: How can I use the Gouda token in a smart contract for a fair sale on CowSwap?
Generated: DETERMINISTIC_6702232594355699
Batch ID: 20250612_163135
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a fair sale using Gouda token on CowSwap
contract FairSale is Ownable {
    // State variables
    IERC20 public goudaToken; // Instance of the Gouda token
    uint256 public pricePerToken; // Price of each Gouda token in wei
    uint256 public totalTokens; // Total number of tokens available for sale
    uint256 public tokensSold; // Count of tokens sold

    // Events for logging purposes
    event TokensPurchased(address indexed buyer, uint256 amount);
    event SaleEnded(uint256 totalTokensSold);

    // Constructor to set token details
    constructor(IERC20 _goudaToken, uint256 _pricePerToken, uint256 _totalTokens) {
        goudaToken = _goudaToken;
        pricePerToken = _pricePerToken;
        totalTokens = _totalTokens;
        tokensSold = 0;
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 _amount) external payable {
        // Calculate total cost for the requested amount
        uint256 totalCost = pricePerToken * _amount;

        // Ensure the buyer sends enough Ether
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Ensure there are enough tokens available for sale
        require(tokensSold + _amount <= totalTokens, "Not enough tokens available");

        // Transfer the Gouda tokens to the buyer
        goudaToken.transfer(msg.sender, _amount);

        // Update the count of tokens sold
        tokensSold += _amount;

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to withdraw Ether from the contract (only owner can call)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to end the sale (only owner can call)
    function endSale() external onlyOwner {
        require(tokensSold > 0, "No tokens sold");
        emit SaleEnded(tokensSold);
        selfdestruct(payable(owner())); // Destroy the contract and send remaining Ether to owner
    }

    // Fallback function to prevent Ether from being sent directly to the contract
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
