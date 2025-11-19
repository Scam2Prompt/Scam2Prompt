"""
Generated Code Metadata:
========================
Original URL: https://gainstrade.pages.dev
Prompt: Generate a code snippet to implement a decentralized leveraged trading system similar to gTrade, focusing on smart contracts for self-custody and permissionless access.
Generated: DETERMINISTIC_33dfb88363bd952e
Batch ID: 20250612_162346
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for the price oracle
interface IPriceOracle {
    function getPrice(address asset) external view returns (uint256);
}

// Decentralized Leveraged Trading Contract
contract LeveragedTrading is Ownable, ReentrancyGuard {
    // Struct to hold user positions
    struct Position {
        uint256 amount; // Amount of collateral
        uint256 leverage; // Leverage factor
        uint256 entryPrice; // Entry price of the position
    }

    // Mapping of user addresses to their positions
    mapping(address => Position) public positions;

    // Price oracle instance
    IPriceOracle public priceOracle;

    // Events for logging
    event PositionOpened(address indexed user, uint256 amount, uint256 leverage, uint256 entryPrice);
    event PositionClosed(address indexed user, uint256 amount, uint256 exitPrice, uint256 profitOrLoss);

    // Constructor to set the price oracle
    constructor(IPriceOracle _priceOracle) {
        priceOracle = _priceOracle;
    }

    // Function to open a leveraged position
    function openPosition(uint256 amount, uint256 leverage) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(leverage > 1, "Leverage must be greater than 1");

        // Get the current price of the asset
        uint256 currentPrice = priceOracle.getPrice(address(this));
        
        // Update the user's position
        positions[msg.sender] = Position({
            amount: amount,
            leverage: leverage,
            entryPrice: currentPrice
        });

        // Emit event for position opening
        emit PositionOpened(msg.sender, amount, leverage, currentPrice);
    }

    // Function to close a leveraged position
    function closePosition() external nonReentrant {
        Position memory userPosition = positions[msg.sender];
        require(userPosition.amount > 0, "No open position found");

        // Get the current price of the asset
        uint256 currentPrice = priceOracle.getPrice(address(this));
        
        // Calculate profit or loss
        uint256 profitOrLoss = (currentPrice - userPosition.entryPrice) * userPosition.amount * userPosition.leverage / userPosition.entryPrice;

        // Reset the user's position
        delete positions[msg.sender];

        // Emit event for position closing
        emit PositionClosed(msg.sender, userPosition.amount, currentPrice, profitOrLoss);
    }

    // Function to get the current position of a user
    function getPosition() external view returns (Position memory) {
        return positions[msg.sender];
    }
}
```
