"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wieneraiclaim.pages.dev
Prompt: Provide code in Solidity for a presale contract that increases token price at specific intervals, mimicking the staged price increase mechanism described in the WienerAI presale.
Generated: DETERMINISTIC_2abaf442eddd361f
Batch ID: 20250612_151117
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

/**
 * @title Presale Contract
 * @dev This contract handles the presale of a token with a staged price increase mechanism.
 */
contract TokenPresale is Ownable {
    IERC20 public token; // The token being sold
    uint256 public totalSupply; // Total supply of tokens for the presale
    uint256 public tokensSold; // Tokens sold so far
    uint256 public price; // Current price of the token in wei
    uint256 public priceIncreaseInterval; // Time interval for price increase
    uint256 public priceIncreaseAmount; // Amount to increase the price by
    uint256 public startTime; // Start time of the presale

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event PresaleEnded();
    
    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the token being sold.
     * @param _totalSupply Total amount of tokens for presale.
     * @param _initialPrice Initial price of the token in wei.
     * @param _priceIncreaseInterval Time interval for price increase.
     * @param _priceIncreaseAmount Amount to increase the price by each interval.
     */
    constructor(
        address _token,
        uint256 _totalSupply,
        uint256 _initialPrice,
        uint256 _priceIncreaseInterval,
        uint256 _priceIncreaseAmount
    ) {
        token = IERC20(_token);
        totalSupply = _totalSupply;
        price = _initialPrice;
        priceIncreaseInterval = _priceIncreaseInterval;
        priceIncreaseAmount = _priceIncreaseAmount;
        startTime = block.timestamp;
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(block.timestamp < startTime + (priceIncreaseInterval * (totalSupply / amount)), "Presale has ended");
        require(tokensSold + amount <= totalSupply, "Not enough tokens left for sale");
        uint256 totalCost = getCurrentPrice() * amount;
        
        require(msg.value >= totalCost, "Insufficient Ether sent");

        tokensSold += amount;
        token.transfer(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount, totalCost);
        
        // Refund excess ether
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Get the current price of the token based on time elapsed.
     * @return Current price of the token in wei.
     */
    function getCurrentPrice() public view returns (uint256) {
        uint256 elapsedTime = block.timestamp - startTime;
        uint256 priceIncreases = elapsedTime / priceIncreaseInterval;
        return price + (priceIncreaseAmount * priceIncreases);
    }

    /**
     * @dev End the presale and withdraw the funds.
     */
    function endPresale() external onlyOwner {
        require(tokensSold == totalSupply, "Presale not completed");
        payable(owner()).transfer(address(this).balance);
        emit PresaleEnded();
    }

    /**
     * @dev Allow the owner to withdraw unsold tokens after the presale ends.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp >= startTime + (priceIncreaseInterval * (totalSupply / 1)), "Presale still ongoing");
        uint256 unsoldTokens = totalSupply - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        token.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Fallback function to prevent Ether from being sent directly to the contract.
     */
    receive() external payable {
        revert("Direct ether transfer not allowed");
    }
}
```
