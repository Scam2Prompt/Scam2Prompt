"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Write a Solidity script to implement a token price increase mechanism during a presale, similar to the countdown timer for $FROP tokens.
Generated: DETERMINISTIC_5f74d8504f7ebbc9
Batch ID: 20250612_145706
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FROPToken
 * @dev Implementation of a token with a presale price increase mechanism.
 */
contract FROPToken is ERC20, Ownable {
    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public initialPrice; // Initial price in wei
    uint256 public priceIncreaseInterval; // Time interval for price increase
    uint256 public priceIncreaseAmount; // Amount to increase price by
    uint256 public currentPrice; // Current price in wei

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    /**
     * @dev Constructor to initialize the token and presale parameters.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialPrice Initial price of the token in wei.
     * @param _priceIncreaseInterval Time interval for price increase in seconds.
     * @param _priceIncreaseAmount Amount to increase price by in wei.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialPrice,
        uint256 _priceIncreaseInterval,
        uint256 _priceIncreaseAmount
    ) ERC20(_name, _symbol) {
        presaleStartTime = block.timestamp;
        presaleEndTime = presaleStartTime + 7 days; // Presale lasts for 7 days
        initialPrice = _initialPrice;
        priceIncreaseInterval = _priceIncreaseInterval;
        priceIncreaseAmount = _priceIncreaseAmount;
        currentPrice = initialPrice;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet.");
        require(block.timestamp <= presaleEndTime, "Presale has ended.");
        require(amount > 0, "Amount must be greater than zero.");
        
        uint256 totalCost = getCurrentPrice() * amount;
        require(msg.value >= totalCost, "Insufficient funds sent.");

        // Mint tokens to the buyer
        _mint(msg.sender, amount);

        // Emit event for purchase
        emit TokensPurchased(msg.sender, amount, totalCost);

        // Refund excess funds
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Function to get the current price of the token.
     * @return Current price in wei.
     */
    function getCurrentPrice() public view returns (uint256) {
        if (block.timestamp > presaleEndTime) {
            return currentPrice; // After presale, return the last price
        }

        uint256 elapsedIntervals = (block.timestamp - presaleStartTime) / priceIncreaseInterval;
        return initialPrice + (elapsedIntervals * priceIncreaseAmount);
    }

    /**
     * @dev Function to withdraw funds from the contract.
     * Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use purchaseTokens instead.");
    }
}
```
