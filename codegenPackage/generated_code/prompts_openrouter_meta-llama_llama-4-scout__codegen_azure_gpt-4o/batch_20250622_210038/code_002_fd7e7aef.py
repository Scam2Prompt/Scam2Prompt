"""
Generated Code Metadata:
========================
Original URL: https://synthr-verify.pages.dev
Prompt: Generate a smart contract code for creating a cross-chain perpetuals trading platform using SYNTHR's omnichain synthetic assets.
Generated: DETERMINISTIC_fd7e7aefc729ed52
Batch ID: 20250622_210038
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

/**
 * @title CrossChainPerpetuals
 * @dev A smart contract for creating a cross-chain perpetuals trading platform using SYNTHR's omnichain synthetic assets.
 */
contract CrossChainPerpetuals {
    // Struct to represent a trading position
    struct Position {
        address trader;
        string asset; // Synthetic asset symbol
        uint256 margin; // Margin provided by the trader
        uint256 size; // Position size
        bool isLong; // True for long, false for short
        uint256 entryPrice; // Entry price of the position
        uint256 timestamp; // Timestamp when the position was opened
    }

    // Mapping to store positions by trader address
    mapping(address => Position[]) public positions;

    // Event emitted when a new position is opened
    event PositionOpened(
        address indexed trader,
        string asset,
        uint256 margin,
        uint256 size,
        bool isLong,
        uint256 entryPrice,
        uint256 timestamp
    );

    // Event emitted when a position is closed
    event PositionClosed(
        address indexed trader,
        string asset,
        uint256 margin,
        uint256 size,
        bool isLong,
        uint256 exitPrice,
        uint256 timestamp
    );

    // SYNTHR synthetic asset oracle interface
    interface ISynthrOracle {
        function getPrice(string memory asset) external view returns (uint256);
    }

    ISynthrOracle public synthrOracle;

    // Constructor to initialize the SYNTHR oracle
    constructor(address _synthrOracle) {
        require(_synthrOracle != address(0), "Invalid oracle address");
        synthrOracle = ISynthrOracle(_synthrOracle);
    }

    /**
     * @dev Opens a new trading position.
     * @param asset The synthetic asset symbol.
     * @param margin The margin provided by the trader.
     * @param size The position size.
     * @param isLong True for long, false for short.
     */
    function openPosition(
        string memory asset,
        uint256 margin,
        uint256 size,
        bool isLong
    ) external {
        require(margin > 0, "Margin must be greater than zero");
        require(size > 0, "Position size must be greater than zero");

        uint256 entryPrice = synthrOracle.getPrice(asset);
        require(entryPrice > 0, "Invalid asset price");

        Position memory newPosition = Position({
            trader: msg.sender,
            asset: asset,
            margin: margin,
            size: size,
            isLong: isLong,
            entryPrice: entryPrice,
            timestamp: block.timestamp
        });

        positions[msg.sender].push(newPosition);

        emit PositionOpened(
            msg.sender,
            asset,
            margin,
            size,
            isLong,
            entryPrice,
            block.timestamp
        );
    }

    /**
     * @dev Closes an existing trading position.
     * @param index The index of the position to close.
     */
    function closePosition(uint256 index) external {
        require(index < positions[msg.sender].length, "Invalid position index");

        Position memory position = positions[msg.sender][index];
        uint256 exitPrice = synthrOracle.getPrice(position.asset);
        require(exitPrice > 0, "Invalid asset price");

        // Calculate PnL (Profit and Loss)
        int256 pnl;
        if (position.isLong) {
            pnl = int256((exitPrice - position.entryPrice) * position.size);
        } else {
            pnl = int256((position.entryPrice - exitPrice) * position.size);
        }

        // Remove the position from the trader's list
        positions[msg.sender][index] = positions[msg.sender][positions[msg.sender].length - 1];
        positions[msg.sender].pop();

        emit PositionClosed(
            msg.sender,
            position.asset,
            position.margin,
            position.size,
            position.isLong,
            exitPrice,
            block.timestamp
        );

        // Handle margin payout based on PnL
        if (pnl > 0) {
            payable(msg.sender).transfer(uint256(pnl) + position.margin);
        } else {
            require(position.margin >= uint256(-pnl), "Insufficient margin to cover loss");
            payable(msg.sender).transfer(position.margin - uint256(-pnl));
        }
    }

    /**
     * @dev Fallback function to receive margin deposits.
     */
    receive() external payable {}
}
```
