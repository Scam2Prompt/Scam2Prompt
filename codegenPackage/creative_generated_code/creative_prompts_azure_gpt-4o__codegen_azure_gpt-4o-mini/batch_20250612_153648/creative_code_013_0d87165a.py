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
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IPyth {
    function getPrice(string memory assetId) external view returns (int256 price, uint256 timestamp);
}

contract PerpetualsTradingPlatform is Ownable {
    using SafeMath for uint256;

    // ERC20 token for trading (e.g., USDC)
    IERC20 public stablecoin;

    // Pyth Network price feed contract
    IPyth public pyth;

    // Struct to hold position data
    struct Position {
        uint256 size; // Size of the position
        uint256 entryPrice; // Entry price of the position
        bool isLong; // Is the position long or short
    }

    // Mapping of user addresses to their positions
    mapping(address => Position) public positions;

    // Events for trading actions
    event PositionOpened(address indexed user, uint256 size, uint256 entryPrice, bool isLong);
    event PositionClosed(address indexed user, uint256 size, uint256 exitPrice, bool isLong);

    // Constructor to set the stablecoin and Pyth contract addresses
    constructor(address _stablecoin, address _pyth) {
        stablecoin = IERC20(_stablecoin);
        pyth = IPyth(_pyth);
    }

    // Function to open a position
    function openPosition(uint256 size, bool isLong) external {
        require(size > 0, "Size must be greater than 0");

        // Get the current price from Pyth
        (int256 price, uint256 timestamp) = pyth.getPrice("assetId"); // Replace "assetId" with actual asset ID
        require(price > 0, "Invalid price received from Pyth");

        // Transfer stablecoin to the contract for margin
        stablecoin.transferFrom(msg.sender, address(this), size);

        // Update the user's position
        positions[msg.sender] = Position(size, uint256(price), isLong);
        emit PositionOpened(msg.sender, size, uint256(price), isLong);
    }

    // Function to close a position
    function closePosition() external {
        Position storage position = positions[msg.sender];
        require(position.size > 0, "No open position");

        // Get the current price from Pyth
        (int256 price, uint256 timestamp) = pyth.getPrice("assetId"); // Replace "assetId" with actual asset ID
        require(price > 0, "Invalid price received from Pyth");

        // Calculate profit/loss
        uint256 exitPrice = uint256(price);
        uint256 profitOrLoss = position.isLong ? exitPrice.sub(position.entryPrice) : position.entryPrice.sub(exitPrice);

        // Transfer the profit or loss to the user
        if (profitOrLoss > 0) {
            stablecoin.transfer(msg.sender, profitOrLoss);
        }

        // Emit position closed event
        emit PositionClosed(msg.sender, position.size, exitPrice, position.isLong);

        // Reset the position
        delete positions[msg.sender];
    }

    // Function to withdraw tokens from the contract (emergency use)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to accept ETH (if needed)
    receive() external payable {}

    // Function to set the Pyth price feed address in case of upgrades
    function setPythAddress(address _pyth) external onlyOwner {
        pyth = IPyth(_pyth);
    }
}
```
