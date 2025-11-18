"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write a Solidity script to implement a token price increase mechanism during a presale, similar to the countdown timer for $FROP tokens.
Generated: DETERMINISTIC_5f74d8504f7ebbc9
Batch ID: 20250612_145706
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
 * @title PresaleToken
 * @dev A contract for managing a token presale with a price increase mechanism.
 */
contract PresaleToken is Ownable {
    // State variables
    IERC20 public token; // The ERC20 token being sold
    uint256 public presaleStart; // Presale start timestamp
    uint256 public presaleEnd; // Presale end timestamp
    uint256 public priceIncreaseInterval; // Interval at which the price increases
    uint256 public initialPrice; // Initial token price in wei
    uint256 public currentPrice; // Current token price in wei
    uint256 public totalTokensSold; // Total tokens sold during presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event PriceUpdated(uint256 newPrice);

    // Constructor to set the presale parameters
    constructor(
        IERC20 _token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _priceIncreaseInterval,
        uint256 _initialPrice
    ) {
        require(address(_token) != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale time");
        require(_initialPrice > 0, "Initial price must be greater than 0");

        token = _token;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        priceIncreaseInterval = _priceIncreaseInterval;
        initialPrice = _initialPrice;
        currentPrice = _initialPrice;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 _amount) external payable {
        require(block.timestamp >= presaleStart, "Presale has not started");
        require(block.timestamp <= presaleEnd, "Presale has ended");
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value >= getTotalCost(_amount), "Insufficient funds sent");

        uint256 tokensAvailable = getAvailableTokens();
        require(tokensAvailable >= _amount, "Not enough tokens available");

        totalTokensSold += _amount;

        // Transfer the tokens to the buyer
        token.transfer(msg.sender, _amount);

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, _amount, getTotalCost(_amount));

        // Refund any excess ETH sent
        if (msg.value > getTotalCost(_amount)) {
            payable(msg.sender).transfer(msg.value - getTotalCost(_amount));
        }

        // Update the token price if necessary
        updatePrice();
    }

    // Function to get the total cost of purchasing a given amount of tokens
    function getTotalCost(uint256 _amount) public view returns (uint256) {
        return _amount * currentPrice;
    }

    // Function to get the available tokens for sale (to be defined)
    function getAvailableTokens() public view returns (uint256) {
        // Placeholder logic for available tokens
        return token.balanceOf(address(this));
    }

    // Function to update the token price based on the presale timing
    function updatePrice() internal {
        uint256 timeElapsed = block.timestamp - presaleStart;
        uint256 intervalsPassed = timeElapsed / priceIncreaseInterval;

        // Calculate new price based on intervals passed
        uint256 newPrice = initialPrice + (intervalsPassed * (initialPrice / 10)); // Example: increase by 10% per interval

        // Ensure the price does not decrease
        if (newPrice > currentPrice) {
            currentPrice = newPrice;
            emit PriceUpdated(currentPrice);
        }
    }

    // Function to withdraw ETH from the contract (only owner can call)
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    // Function to allow the owner to update presale parameters if needed
    function updatePresaleParams(uint256 _presaleStart, uint256 _presaleEnd) external onlyOwner {
        require(_presaleStart < _presaleEnd, "Invalid presale time");
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }
}
```
