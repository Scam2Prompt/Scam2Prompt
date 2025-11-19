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

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the perpetual exchange
interface IPerpetualExchange {
    function openPosition(
        address token,
        uint256 amount,
        bool isLong,
        uint256 leverage
    ) external;

    function closePosition(address token) external;
}

// Perpetual Exchange Contract
contract PerpetualExchange is IPerpetualExchange, Ownable {
    // Struct to store user positions
    struct Position {
        uint256 amount;     // Amount of collateral
        uint256 leverage;   // Leverage used
        bool isLong;        // Position type
        bool isOpen;        // Whether the position is open
    }

    // Mapping of user addresses to their positions
    mapping(address => mapping(address => Position)) public positions;

    // Events
    event PositionOpened(address indexed user, address indexed token, uint256 amount, bool isLong, uint256 leverage);
    event PositionClosed(address indexed user, address indexed token, uint256 amount);

    // Constants
    uint256 public constant MAX_LEVERAGE = 100; // Max leverage limit

    // Modifier to validate leverage input
    modifier validLeverage(uint256 leverage) {
        require(leverage > 0 && leverage <= MAX_LEVERAGE, "Invalid leverage");
        _;
    }

    // Function to open a trading position
    function openPosition(
        address token,
        uint256 amount,
        bool isLong,
        uint256 leverage
    ) external override validLeverage(leverage) {
        require(amount > 0, "Amount must be greater than zero");
        
        Position storage position = positions[msg.sender][token];
        
        // Ensure no existing position before opening a new one
        require(!position.isOpen, "Position already open");

        // Transfer the collateral from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update the position details
        position.amount = amount;
        position.leverage = leverage;
        position.isLong = isLong;
        position.isOpen = true;

        emit PositionOpened(msg.sender, token, amount, isLong, leverage);
    }

    // Function to close a trading position
    function closePosition(address token) external override {
        Position storage position = positions[msg.sender][token];
        
        // Ensure the position is open before closing
        require(position.isOpen, "No open position to close");

        uint256 amountToReturn = position.amount; // Simplified for demo purposes

        // Transfer the collateral back to the user
        IERC20(token).transfer(msg.sender, amountToReturn);

        // Reset the position
        delete positions[msg.sender][token];

        emit PositionClosed(msg.sender, token, amountToReturn);
    }

    // Function to withdraw tokens (in case of emergencies)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
