"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultrax.io
Prompt: How can I implement a decentralized perpetual exchange for trading cryptocurrencies like BTC and ETH with up to 100x leverage using smart contracts?
Generated: DETERMINISTIC_e6ae4449e05e836e
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Creating a decentralized perpetual exchange with leverage is a complex task requiring expertise in blockchain development. Below is a simplified implementation of a smart contract that demonstrates core functionality such as margin trading and perpetual positions using Solidity (for Ethereum-compatible blockchains like Ethereum or Binance Smart Chain). This example doesn't include advanced features like oracle integration, liquidation mechanisms, and sophisticated risk management; those would need to be added in a production-ready deployment.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Decentralized Perpetual Exchange
 * @dev A simplified implementation for trading cryptocurrencies with leverage.
 */
contract PerpetualExchange {
    struct Position {
        uint256 collateral;         // Collateral amount in wei
        uint256 leverage;           // Leverage multiplier
        uint256 entryPrice;         // Entry price (in USD, scaled by 1e8)
        uint256 size;               // Position size in USD
        bool isLong;                // True if long position, false if short
    }

    mapping(address => Position) public positions;
    uint256 public constant MAX_LEVERAGE = 100; // Maximum leverage (100x)
    uint256 public constant LIQUIDATION_THRESHOLD = 75; // Collateral must be ≥ 75% of position size

    event PositionOpened(
        address indexed user,
        uint256 collateral,
        uint256 leverage,
        uint256 entryPrice,
        uint256 size,
        bool isLong
    );

    event PositionClosed(
        address indexed user,
        uint256 profitOrLoss
    );

    /**
     * @dev Open a leveraged position.
     * @param leverage The leverage multiplier (must be ≤ MAX_LEVERAGE).
     * @param entryPrice The price at which the position is opened (scaled by 1e8).
     * @param isLong True for a long position, false for a short position.
     */
    function openPosition(uint256 leverage, uint256 entryPrice, bool isLong) external payable {
        require(msg.value > 0, "Collateral must be greater than 0");
        require(leverage > 0 && leverage <= MAX_LEVERAGE, "Invalid leverage");

        uint256 positionSize = msg.value * leverage; // Position size in USD
        positions[msg.sender] = Position({
            collateral: msg.value,
            leverage: leverage,
            entryPrice: entryPrice,
            size: positionSize,
            isLong: isLong
        });

        emit PositionOpened(msg.sender, msg.value, leverage, entryPrice, positionSize, isLong);
    }

    /**
     * @dev Close an existing position and calculate profit/loss.
     * @param exitPrice The price at which the position is closed (scaled by 1e8).
     */
    function closePosition(uint256 exitPrice) external {
        Position storage position = positions[msg.sender];
        require(position.size > 0, "No open position");

        // Calculate profit or loss
        uint256 profitOrLoss = 0;
        if (position.isLong) {
            profitOrLoss = (position.size * (exitPrice - position.entryPrice)) / position.entryPrice;
        } else {
            profitOrLoss = (position.size * (position.entryPrice - exitPrice)) / position.entryPrice;
        }

        // Adjust collateral based on profit/loss
        uint256 adjustedCollateral = position.collateral + profitOrLoss;
        require(adjustedCollateral >= (position.size * LIQUIDATION_THRESHOLD) / 100, "Position liquidated");

        // Send adjusted collateral back to user
        payable(msg.sender).transfer(adjustedCollateral);

        // Clear position
        delete positions[msg.sender];

        emit PositionClosed(msg.sender, profitOrLoss);
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}

    /**
     * @dev Helper function to get the current position of a user.
     * @param user The address of the user.
     * @return The position details.
     */
    function getPosition(address user) external view returns (Position memory) {
        return positions[user];
    }
}
```

### Disclaimer:
- **Testing:** This example contract needs rigorous testing in testnets before use in production.
- **Oracle Integration:** You'll need to integrate price feeds—for example, Chainlink or custom oracles—to set accurate `entryPrice` and `exitPrice`.
- **Liquidation Mechanism:** Implement liquidation for positions failing the collateral threshold.
- **Security Audits:** Always audit smart contracts before deploying.
- **Gas Optimization:** Ensure the contract is optimized for gas costs.
