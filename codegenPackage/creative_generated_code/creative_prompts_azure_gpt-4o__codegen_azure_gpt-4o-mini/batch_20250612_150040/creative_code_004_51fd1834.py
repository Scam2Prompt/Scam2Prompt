"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Provide a step-by-step guide to integrate a high-to-low pricing mechanism into a decentralized application (dApp) for token sales, inspired by Fjord Foundry's methodology.
Generated: DETERMINISTIC_51fd183429b05c9a
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenSale
 * @dev A contract that implements a high-to-low pricing mechanism for token sales in a decentralized application (dApp).
 */
contract TokenSale is Ownable {
    IERC20 public token;  // The token being sold
    uint256 public saleStart;  // Sale start time
    uint256 public saleEnd;    // Sale end time
    uint256 public initialPrice;  // Initial price for the first token
    uint256 public priceDecrease;  // Price decrease per sold token
    uint256 public totalTokens;  // Total tokens available for sale
    uint256 public tokensSold;    // Tokens sold so far

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    /**
     * @dev Constructor to initialize the token sale parameters.
     * @param _token Address of the ERC20 token being sold.
     * @param _initialPrice Initial price of the token in wei.
     * @param _priceDecrease Price decrease per token sold in wei.
     * @param _totalTokens Total number of tokens for sale.
     * @param _saleDuration Duration of the sale in seconds.
     */
    constructor(
        address _token,
        uint256 _initialPrice,
        uint256 _priceDecrease,
        uint256 _totalTokens,
        uint256 _saleDuration
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_initialPrice > 0, "Initial price must be greater than zero");
        require(_priceDecrease > 0, "Price decrease must be greater than zero");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        token = IERC20(_token);
        initialPrice = _initialPrice;
        priceDecrease = _priceDecrease;
        totalTokens = _totalTokens;
        saleStart = block.timestamp;
        saleEnd = saleStart + _saleDuration;
    }

    /**
     * @dev Function to purchase tokens.
     * @param _amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(block.timestamp >= saleStart, "Sale has not started yet");
        require(block.timestamp <= saleEnd, "Sale has already ended");
        require(tokensSold + _amount <= totalTokens, "Not enough tokens available");

        uint256 cost = getCurrentPrice() * _amount;
        require(msg.value >= cost, "Insufficient Ether sent");

        tokensSold += _amount;

        // Transfer tokens from contract to buyer
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, _amount, cost);

        // Refund any excess Ether
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Function to get the current price of the token.
     * @return The current price in wei.
     */
    function getCurrentPrice() public view returns (uint256) {
        // Calculate the price based on tokens sold
        uint256 price = initialPrice - (priceDecrease * tokensSold);
        return price > 0 ? price : 0;  // Ensure the price does not go below zero
    }

    /**
     * @dev Function to withdraw the funds collected from the token sale.
     * Only the owner can withdraw.
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > saleEnd, "Sale not finished yet");

        // Withdraw the collected Ether to the owner
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
