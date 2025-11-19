"""
Generated Code Metadata:
========================
Original URL: https://nibiru.cash
Prompt: Generate a smart contract for a simple token sale using Nibiru's blockchain, assuming it supports smart contracts similar to Ethereum.
Generated: DETERMINISTIC_180ed235005ed161
Batch ID: 20250622_205627
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenSale contract for managing a simple token sale
contract TokenSale is Ownable {
    // State variables
    IERC20 public token; // The token being sold
    uint256 public rate; // Number of token units per wei
    uint256 public weiRaised; // Amount of wei raised
    uint256 public saleEndTime; // End time of the sale

    // Events
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event SaleEnded(uint256 totalWeiRaised);

    // Constructor to initialize the token sale
    constructor(IERC20 _token, uint256 _rate, uint256 _duration) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_rate > 0, "Rate must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        token = _token;
        rate = _rate;
        saleEndTime = block.timestamp + _duration; // Set sale end time
    }

    // Function to purchase tokens
    function buyTokens() external payable {
        require(block.timestamp < saleEndTime, "Token sale has ended");
        require(msg.value > 0, "Must send ether to purchase tokens");

        // Calculate the number of tokens to be purchased
        uint256 tokens = msg.value * rate;
        weiRaised += msg.value;

        // Transfer tokens to the purchaser
        require(token.balanceOf(address(this)) >= tokens, "Not enough tokens in the reserve");
        token.transfer(msg.sender, tokens);

        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    // Function to end the sale and withdraw funds
    function endSale() external onlyOwner {
        require(block.timestamp >= saleEndTime, "Sale has not ended yet");

        // Transfer remaining tokens back to the owner
        uint256 remainingTokens = token.balanceOf(address(this));
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }

        // Transfer raised funds to the owner
        payable(owner()).transfer(address(this).balance);

        emit SaleEnded(weiRaised);
    }

    // Function to withdraw accidentally sent tokens
    function withdrawTokens(IERC20 _token) external onlyOwner {
        require(address(_token) != address(token), "Cannot withdraw sale token");
        uint256 balance = _token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        _token.transfer(owner(), balance);
    }

    // Fallback function to accept ether
    receive() external payable {
        buyTokens();
    }
}
```
