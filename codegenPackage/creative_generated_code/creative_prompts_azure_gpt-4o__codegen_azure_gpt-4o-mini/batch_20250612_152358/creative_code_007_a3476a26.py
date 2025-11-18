"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milady-dfk.pages.dev
Prompt: Generate a Solidity contract for a token sale mechanism that includes stepped raises and fixed-price pools, similar to the Milady Cult presale structure.
Generated: DETERMINISTIC_a3476a2614ba538b
Batch ID: 20250612_152358
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

/**
 * @title TokenSale
 * @dev A simple token sale contract with stepped raises and fixed-price pools.
 */
contract TokenSale is Ownable {
    using SafeMath for uint256;

    IERC20 public token; // The token being sold
    uint256 public startTime; // Start time of the sale
    uint256 public endTime; // End time of the sale
    uint256 public totalTokens; // Total tokens for sale
    uint256 public tokensSold; // Amount of tokens sold
    uint256 public price; // Price of the token in wei
    uint256 public raiseStep; // Amount to raise after each step
    uint256 public stepDuration; // Duration of each step in seconds
    uint256 public lastRaiseTime; // Time of last raise

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PriceUpdated(uint256 newPrice);

    /**
     * @dev Initializes the token sale contract.
     * @param _token The address of the token being sold.
     * @param _totalTokens The total amount of tokens for sale.
     * @param _startTime The start time of the sale.
     * @param _endTime The end time of the sale.
     * @param _initialPrice The initial price of the token in wei.
     * @param _raiseStep The amount to raise the price after each step.
     * @param _stepDuration The duration of each step in seconds.
     */
    constructor(
        IERC20 _token,
        uint256 _totalTokens,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _initialPrice,
        uint256 _raiseStep,
        uint256 _stepDuration
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        require(_startTime < _endTime, "Start time must be before end time");
        require(_initialPrice > 0, "Initial price must be greater than 0");
        require(_raiseStep > 0, "Raise step must be greater than 0");
        require(_stepDuration > 0, "Step duration must be greater than 0");

        token = _token;
        totalTokens = _totalTokens;
        startTime = _startTime;
        endTime = _endTime;
        price = _initialPrice;
        raiseStep = _raiseStep;
        stepDuration = _stepDuration;
        lastRaiseTime = _startTime;
    }

    /**
     * @dev Purchase tokens during the sale.
     * @param amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(block.timestamp >= startTime, "Sale has not started yet");
        require(block.timestamp <= endTime, "Sale has ended");
        require(amount > 0, "Amount must be greater than 0");
        require(tokensSold.add(amount) <= totalTokens, "Not enough tokens available");
        require(msg.value == amount.mul(price), "Incorrect Ether value sent");

        // Update tokens sold
        tokensSold = tokensSold.add(amount);

        // Emit event for purchased tokens
        emit TokensPurchased(msg.sender, amount);

        // Transfer tokens to buyer
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Handle price adjustment
        adjustPrice();
    }

    /**
     * @dev Adjust the token price based on time elapsed.
     */
    function adjustPrice() internal {
        if (block.timestamp >= lastRaiseTime.add(stepDuration)) {
            price = price.add(raiseStep);
            lastRaiseTime = block.timestamp;
            emit PriceUpdated(price);
        }
    }

    /**
     * @dev Allows owner to withdraw Ether from the contract.
     */
    function withdrawEther() external onlyOwner {
        require(address(this).balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Allows owner to withdraw unsold tokens after sale ends.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > endTime, "Sale has not ended yet");
        uint256 unsoldTokens = totalTokens.sub(tokensSold);
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfer.
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
