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

// Import the ERC20 interface for the JESSE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract JessePresale is Ownable {
    // Token to be sold in the presale
    IERC20 public jesseToken;
    
    // Presale parameters
    uint256 public presalePrice; // Price of one JESSE token in BASE increments
    uint256 public totalTokens; // Total tokens available for presale
    uint256 public tokensSold; // Total tokens sold in the presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event PresalePriceUpdated(uint256 newPrice);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    // Modifier to ensure presale is active
    modifier presaleActive() {
        require(tokensSold < totalTokens, "Presale is over");
        _;
    }

    // Constructor to initialize the presale contract
    constructor(IERC20 _jesseToken, uint256 _presalePrice, uint256 _totalTokens) {
        jesseToken = _jesseToken;
        presalePrice = _presalePrice;
        totalTokens = _totalTokens;
        tokensSold = 0;
    }

    // Function to purchase JESSE tokens
    function purchaseTokens(uint256 _amount) external payable presaleActive {
        uint256 totalCost = _amount * presalePrice;
        
        // Ensure user sent enough ETH for the purchase
        require(msg.value >= totalCost, "Insufficient ETH sent");

        // Ensure we do not sell more tokens than available
        require(tokensSold + _amount <= totalTokens, "Not enough tokens available");

        // Transfer JESSE tokens to the buyer
        tokensSold += _amount;
        jesseToken.transfer(msg.sender, _amount);

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, _amount, totalCost);
        
        // Refund excess ETH sent, if any
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    // Function to update the presale price
    function updatePresalePrice(uint256 _newPrice) external onlyOwner {
        presalePrice = _newPrice;
        emit PresalePriceUpdated(_newPrice);
    }

    // Function to withdraw unsold tokens or ETH by the owner
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount <= jesseToken.balanceOf(address(this)), "Not enough tokens in contract");
        jesseToken.transfer(msg.sender, _amount);
        emit TokensWithdrawn(msg.sender, _amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(msg.sender).transfer(balance);
    }
}
```
