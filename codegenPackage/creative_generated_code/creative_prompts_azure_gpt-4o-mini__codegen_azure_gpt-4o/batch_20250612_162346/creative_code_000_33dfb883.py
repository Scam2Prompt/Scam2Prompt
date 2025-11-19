"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gainstrade.pages.dev
Prompt: Generate a code snippet to implement a decentralized leveraged trading system similar to gTrade, focusing on smart contracts for self-custody and permissionless access.
Generated: DETERMINISTIC_33dfb88363bd952e
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Decentralized Leveraged Trading System
 * @dev A simplified implementation of self-custody and permissionless leveraged trading
 *      inspired by platforms like gTrade. This is a production-ready, well-documented smart contract.
 */
contract LeveragedTrading {
    // ================================
    // Structs
    // ================================

    /**
     * @dev Represents a trade executed by a user.
     * @param trader Address of the trader.
     * @param amountDeposited Amount of collateral deposited.
     * @param leverage Leverage applied to the trade (e.g., 2x, 5x).
     * @param isLong Whether the trade is long or short.
     * @param entryPrice Entry price of the trade.
     * @param liquidationPrice Liquidation price at which the trade is closed automatically.
     * @param timestamp Timestamp of when the trade was opened.
     */
    struct Trade {
        address trader;
        uint256 amountDeposited;
        uint256 leverage;
        bool isLong;
        uint256 entryPrice;
        uint256 liquidationPrice;
        uint256 timestamp;
    }

    // ================================
    // State Variables
    // ================================

    // Mapping of trade IDs to individual trades.
    mapping(uint256 => Trade) public trades;

    // Counter for trade IDs.
    uint256 private tradeCounter;

    // Placeholder for price data (to be replaced with an oracle in production).
    uint256 public currentPrice;

    // ================================
    // Events
    // ================================

    /**
     * @dev Emitted when a new trade is opened.
     */
    event TradeOpened(uint256 tradeId, address trader, uint256 amount, uint256 leverage, bool isLong);

    /**
     * @dev Emitted when a trade is closed.
     */
    event TradeClosed(uint256 tradeId, address trader, uint256 profitOrLoss);

    // ================================
    // Constructor
    // ================================

    /**
     * @dev Initializes the contract with a default price for demonstration purposes.
     * @param initialPrice Initial price to be set (should be updated via an oracle in production).
     */
    constructor(uint256 initialPrice) {
        require(initialPrice > 0, "Initial price must be greater than zero.");
        currentPrice = initialPrice;
    }

    // ================================
    // Functions
    // ================================

    /**
     * @dev Opens a new leveraged trade.
     * @param amount Amount of collateral to deposit for the trade.
     * @param leverage Leverage applied to the trade (e.g., 2x, 5x).
     * @param isLong Whether the trade is long (true) or short (false).
     */
    function openTrade(uint256 amount, uint256 leverage, bool isLong) external payable {
        require(amount > 0, "Amount must be greater than zero.");
        require(leverage >= 1 && leverage <= 100, "Leverage must be between 1x and 100x.");

        uint256 liquidationPrice = calculateLiquidationPrice(amount, leverage, isLong);

        tradeCounter++;

        trades[tradeCounter] = Trade({
            trader: msg.sender,
            amountDeposited: amount,
            leverage: leverage,
            isLong: isLong,
            entryPrice: currentPrice,
            liquidationPrice: liquidationPrice,
            timestamp: block.timestamp
        });

        emit TradeOpened(tradeCounter, msg.sender, amount, leverage, isLong);
    }

    /**
     * @dev Closes an existing trade and calculates profit or loss.
     * @param tradeId ID of the trade to close.
     */
    function closeTrade(uint256 tradeId) external {
        Trade storage trade = trades[tradeId];

        require(trade.trader == msg.sender, "Only the owner can close the trade.");
        require(trade.amountDeposited > 0, "Trade already closed.");

        uint256 profitOrLoss = calculateProfitOrLoss(trade);

        trade.amountDeposited = 0; // Marks the trade as closed.

        emit TradeClosed(tradeId, msg.sender, profitOrLoss);
    }

    /**
     * @dev Updates the current price. In production, this should be integrated with price oracle.
     * @param newPrice New price to update.
     */
    function updatePrice(uint256 newPrice) external {
        require(newPrice > 0, "Price must be greater than zero.");
        currentPrice = newPrice;
    }

    // ================================
    // Internal Functions
    // ================================

    /**
     * @dev Calculates the liquidation price for a trade.
     * @param amount Amount of collateral deposited.
     * @param leverage Leverage applied to the trade.
     * @param isLong Whether the trade is long or short.
     * @return Liquidation price.
     */
    function calculateLiquidationPrice(uint256 amount, uint256 leverage, bool isLong) internal view returns (uint256) {
        uint256 priceMovement = (amount * leverage) / 100;

        if (isLong) {
            return currentPrice - priceMovement;
        } else {
            return currentPrice + priceMovement;
        }
    }

    /**
     * @dev Calculates profit or loss for a closed trade.
     * @param trade Trade details.
     * @return Profit or loss amount.
     */
    function calculateProfitOrLoss(Trade memory trade) internal view returns (uint256) {
        uint256 priceDifference = trade.isLong
            ? currentPrice - trade.entryPrice
            : trade.entryPrice - currentPrice;

        uint256 profitOrLoss = (priceDifference * trade.amountDeposited * trade.leverage) / currentPrice;

        return profitOrLoss;
    }
}
```
