"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Write a smart contract in Solidity that integrates Pyth Network's data feeds to power a decentralized perpetuals trading platform on Arbitrum.
Generated: DETERMINISTIC_0d87165abf6a7e20
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Importing interfaces from OpenZeppelin and Pyth Network
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PerpetualTradingPlatform is Ownable, ReentrancyGuard {
    // Address of the Pyth Network price feed
    IPyth public pyth;

    // Struct to store user positions
    struct Position {
        uint256 size; // Position size in USD
        uint256 entryPrice; // Entry price of the asset
        bool isLong; // True for long position, false for short
    }

    // Mapping to store user positions by address
    mapping(address => Position) public positions;

    // Events for tracking important actions
    event PositionOpened(address indexed user, uint256 size, uint256 entryPrice, bool isLong);
    event PositionClosed(address indexed user, uint256 size, uint256 exitPrice, int256 pnl);

    // Constructor to initialize the contract with the Pyth price feed
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to open a position
    function openPosition(
        bytes32 priceFeedId, // Pyth price feed ID for specific asset
        uint256 usdSize,     // Position size in USD
        bool isLong          // True for long, false for short
    ) external payable nonReentrant {
        require(usdSize > 0, "Position size must be greater than zero");
        require(positions[msg.sender].size == 0, "Existing position must be closed first");

        // Fetch the asset's latest price from Pyth Network
        PythStructs.Price memory price = pyth.getPriceUnsafe(priceFeedId); // Assumes price feed exists
        require(price.price > 0, "Invalid price feed data");

        // Save the position details
        positions[msg.sender] = Position({
            size: usdSize,
            entryPrice: uint256(price.price),
            isLong: isLong
        });

        emit PositionOpened(msg.sender, usdSize, uint256(price.price), isLong);
    }

    // Function to close a position
    function closePosition(bytes32 priceFeedId) external nonReentrant {
        Position memory position = positions[msg.sender];
        require(position.size > 0, "No active position to close");

        // Fetch the asset's latest price from Pyth Network
        PythStructs.Price memory price = pyth.getPriceUnsafe(priceFeedId); // Assumes price feed exists
        require(price.price > 0, "Invalid price feed data");

        uint256 exitPrice = uint256(price.price);
        int256 pnl;

        // Calculate Profit and Loss (PnL)
        if (position.isLong) {
            pnl = int256(position.size) * (int256(exitPrice) - int256(position.entryPrice)) / int256(position.entryPrice);
        } else {
            pnl = int256(position.size) * (int256(position.entryPrice) - int256(exitPrice)) / int256(position.entryPrice);
        }

        // Remove the position
        delete positions[msg.sender];

        // Transfer funds back to the user based on PnL
        if (pnl > 0) {
            payable(msg.sender).transfer(uint256(pnl)); // Positive PnL
        }

        emit PositionClosed(msg.sender, position.size, exitPrice, pnl);
    }

    // Function to update Pyth price feeds (required for accuracy)
    function updatePriceFeeds(bytes[] calldata updateData) external payable {
        pyth.updatePriceFeeds{value: msg.value}(updateData);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
