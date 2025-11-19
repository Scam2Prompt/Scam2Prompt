"""
Generated Code Metadata:
========================
Original URL: https://mercury-dusky-pi.vercel.app
Prompt: Design a function in Solidity to interact with a perpetual trading contract on a decentralized exchange, inspired by the "Perpetual Degen and Earn" feature on this platform.
Generated: DETERMINISTIC_a0429e5a5f2a1967
Batch ID: 20250622_211011
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

// Interface for the perpetual trading contract
interface IPerpetualTrading {
    function openPosition(uint256 amount, bool isLong) external returns (uint256 positionId);
    function closePosition(uint256 positionId) external returns (uint256 profitLoss);
    function getPosition(uint256 positionId) external view returns (uint256 amount, bool isLong, uint256 entryPrice);
}

// Main contract to interact with the perpetual trading contract
contract PerpetualTrader {
    IPerpetualTrading public perpetualTradingContract;

    // Event emitted when a position is opened
    event PositionOpened(uint256 indexed positionId, uint256 amount, bool isLong);
    
    // Event emitted when a position is closed
    event PositionClosed(uint256 indexed positionId, uint256 profitLoss);

    // Constructor to set the perpetual trading contract address
    constructor(address _perpetualTradingContract) {
        require(_perpetualTradingContract != address(0), "Invalid contract address");
        perpetualTradingContract = IPerpetualTrading(_perpetualTradingContract);
    }

    // Function to open a trading position
    function openTradingPosition(uint256 amount, bool isLong) external returns (uint256) {
        require(amount > 0, "Amount must be greater than zero");

        // Call the perpetual trading contract to open a position
        uint256 positionId = perpetualTradingContract.openPosition(amount, isLong);
        
        // Emit an event for the opened position
        emit PositionOpened(positionId, amount, isLong);
        
        return positionId;
    }

    // Function to close a trading position
    function closeTradingPosition(uint256 positionId) external returns (uint256) {
        // Call the perpetual trading contract to close the position
        uint256 profitLoss = perpetualTradingContract.closePosition(positionId);
        
        // Emit an event for the closed position
        emit PositionClosed(positionId, profitLoss);
        
        return profitLoss;
    }

    // Function to get details of a trading position
    function getTradingPosition(uint256 positionId) external view returns (uint256 amount, bool isLong, uint256 entryPrice) {
        // Retrieve position details from the perpetual trading contract
        (amount, isLong, entryPrice) = perpetualTradingContract.getPosition(positionId);
    }
}
```
