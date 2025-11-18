"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that enables decentralized leveraged trading for crypto, forex, and commodities, similar to the functionality described on the gTrade platform. Ensure the contract supports self-custody and permissionless access.
Generated: DETERMINISTIC_29d66fba11217f22
Batch ID: 20250612_152827
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

/**
 * @title Decentralized Leveraged Trading Smart Contract
 * @notice This contract allows permissionless and self-custody leveraged trading for crypto, forex, and commodities.
 * It supports opening positions with leverage, closing positions, and manages collateral.
 * @dev This contract assumes external price feeds and a liquidation mechanism implemented off-chain.
 */
contract LeveragedTrading {
    // Struct representing a trading position
    struct Position {
        address user;      // User who opened the position
        uint256 collateral; // Amount of collateral provided
        uint256 leverage;   // Leverage factor (e.g., 5x, 10x)
        uint256 entryPrice; // Entry price of the asset
        bool isLong;        // True for long, false for short
        bool isOpen;        // Position status
    }

    // Mapping of user positions (user address => position ID => Position)
    mapping(address => mapping(uint256 => Position)) public positions;

    // Mapping to track the next position ID for each user
    mapping(address => uint256) public nextPositionId;

    // Event emitted when a position is opened
    event PositionOpened(
        address indexed user,
        uint256 positionId,
        uint256 collateral,
        uint256 leverage,
        uint256 entryPrice,
        bool isLong
    );

    // Event emitted when a position is closed
    event PositionClosed(
        address indexed user,
        uint256 positionId,
        uint256 exitPrice,
        uint256 pnl // Profit or Loss
    );

    // Error for invalid parameters
    error InvalidParameters(string message);

    // Error for unauthorized actions
    error Unauthorized(string message);

    /**
     * @notice Opens a leveraged trading position.
     * @param collateral The amount of collateral provided (in wei).
     * @param leverage The leverage factor (e.g., 5x, 10x).
     * @param entryPrice The current price of the asset (from an external price feed).
     * @param isLong True for long position, false for short.
     */
    function openPosition(
        uint256 collateral,
        uint256 leverage,
        uint256 entryPrice,
        bool isLong
    ) external payable {
        // Validate inputs
        if (collateral == 0 || leverage < 1 || entryPrice == 0) {
            revert InvalidParameters("Collateral, leverage, or entry price is invalid");
        }
        if (msg.value != collateral) {
            revert InvalidParameters("Collateral mismatch with sent value");
        }

        // Create the position
        uint256 positionId = nextPositionId[msg.sender];
        positions[msg.sender][positionId] = Position({
            user: msg.sender,
            collateral: collateral,
            leverage: leverage,
            entryPrice: entryPrice,
            isLong: isLong,
            isOpen: true
        });
        nextPositionId[msg.sender]++;

        // Emit the open position event
        emit PositionOpened(msg.sender, positionId, collateral, leverage, entryPrice, isLong);
    }

    /**
     * @notice Closes an existing position and calculates Profit or Loss (PnL).
     * @param positionId The ID of the position to close.
     * @param exitPrice The current price of the asset (from an external price feed).
     */
    function closePosition(uint256 positionId, uint256 exitPrice) external {
        // Validate position ownership and ensure it is open
        Position storage position = positions[msg.sender][positionId];
        if (position.user != msg.sender) {
            revert Unauthorized("User does not own this position");
        }
        if (!position.isOpen) {
            revert InvalidParameters("Position is already closed");
        }

        // Calculate PnL
        uint256 pnl;
        uint256 leveragedAmount = position.collateral * position.leverage;
        if (position.isLong) {
            // Long position: PnL = (Exit Price - Entry Price) * Leveraged Amount / Entry Price
            pnl = (exitPrice > position.entryPrice)
                ? ((exitPrice - position.entryPrice) * leveragedAmount) / position.entryPrice
                : ((position.entryPrice - exitPrice) * leveragedAmount) / position.entryPrice;
        } else {
            // Short position: PnL = (Entry Price - Exit Price) * Leveraged Amount / Entry Price
            pnl = (position.entryPrice > exitPrice)
                ? ((position.entryPrice - exitPrice) * leveragedAmount) / position.entryPrice
                : ((exitPrice - position.entryPrice) * leveragedAmount) / position.entryPrice;
        }

        // Update position status
        position.isOpen = false;

        // Transfer collateral and PnL to user
        uint256 payout = position.collateral + pnl;
        if (payout > address(this).balance) {
            revert InvalidParameters("Contract has insufficient funds");
        }
        payable(msg.sender).transfer(payout);

        // Emit the close position event
        emit PositionClosed(msg.sender, positionId, exitPrice, pnl);
    }

    /**
     * @notice Receives funds for collateralization purposes.
     */
    receive() external payable {}

    /**
     * @notice Withdraws contract funds (admin only).
     * @dev This is a placeholder. In production, access control must be implemented to restrict this functionality.
     */
    function withdrawFunds(uint256 amount) external {
        // Access control must be implemented in production-ready code
        payable(msg.sender).transfer(amount);
    }
}
```
