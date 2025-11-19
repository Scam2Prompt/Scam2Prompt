"""
Generated Code Metadata:
========================
Original URL: https://nodeapp-serverlaunch.com
Prompt: "Design a smart contract for a decentralized leveraged trading platform that utilizes oracle architecture for real-time asset prices."
Generated: DETERMINISTIC_5936aff5eec5e480
Batch ID: 20250622_204914
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the interface for the oracle contract
interface IPriceOracle {
    function getPrice(address _asset) external view returns (uint256);
}

// Define the smart contract for the decentralized leveraged trading platform
contract LeveragedTradingPlatform is Ownable {
    using SafeMath for uint256;

    // Mapping of assets to their respective prices
    mapping(address => uint256) public assetPrices;

    // Mapping of users to their respective positions
    mapping(address => mapping(address => Position)) public userPositions;

    // Mapping of assets to their respective oracle contracts
    mapping(address => IPriceOracle) public assetOracles;

    // Event emitted when a new position is opened
    event NewPosition(address indexed user, address indexed asset, uint256 leverage, uint256 positionSize);

    // Event emitted when a position is closed
    event ClosePosition(address indexed user, address indexed asset, uint256 profitLoss);

    // Struct to represent a user's position
    struct Position {
        address asset;
        uint256 leverage;
        uint256 positionSize;
        uint256 entryPrice;
    }

    // Function to set the oracle contract for an asset
    function setAssetOracle(address _asset, address _oracle) public onlyOwner {
        require(_oracle != address(0), "Oracle address cannot be zero");
        assetOracles[_asset] = IPriceOracle(_oracle);
    }

    // Function to get the price of an asset from the oracle contract
    function getAssetPrice(address _asset) public view returns (uint256) {
        require(assetOracles[_asset] != IPriceOracle(address(0)), "Oracle contract not set for asset");
        return assetOracles[_asset].getPrice(_asset);
    }

    // Function to open a new position
    function openPosition(address _asset, uint256 _leverage, uint256 _positionSize) public {
        require(_leverage > 0, "Leverage must be greater than zero");
        require(_positionSize > 0, "Position size must be greater than zero");

        // Get the current price of the asset
        uint256 currentPrice = getAssetPrice(_asset);

        // Calculate the entry price of the position
        uint256 entryPrice = currentPrice;

        // Create a new position for the user
        userPositions[msg.sender][_asset] = Position(_asset, _leverage, _positionSize, entryPrice);

        // Emit an event to indicate a new position has been opened
        emit NewPosition(msg.sender, _asset, _leverage, _positionSize);
    }

    // Function to close a position
    function closePosition(address _asset) public {
        require(userPositions[msg.sender][_asset].positionSize > 0, "User does not have an open position");

        // Get the current price of the asset
        uint256 currentPrice = getAssetPrice(_asset);

        // Calculate the profit/loss of the position
        uint256 entryPrice = userPositions[msg.sender][_asset].entryPrice;
        uint256 positionSize = userPositions[msg.sender][_asset].positionSize;
        uint256 leverage = userPositions[msg.sender][_asset].leverage;
        uint256 profitLoss = currentPrice.sub(entryPrice).mul(positionSize).mul(leverage);

        // Update the user's balance
        IERC20(_asset).transfer(msg.sender, profitLoss);

        // Delete the user's position
        delete userPositions[msg.sender][_asset];

        // Emit an event to indicate a position has been closed
        emit ClosePosition(msg.sender, _asset, profitLoss);
    }

    // Function to liquidate a position
    function liquidatePosition(address _user, address _asset) public onlyOwner {
        require(userPositions[_user][_asset].positionSize > 0, "User does not have an open position");

        // Get the current price of the asset
        uint256 currentPrice = getAssetPrice(_asset);

        // Calculate the profit/loss of the position
        uint256 entryPrice = userPositions[_user][_asset].entryPrice;
        uint256 positionSize = userPositions[_user][_asset].positionSize;
        uint256 leverage = userPositions[_user][_asset].leverage;
        uint256 profitLoss = currentPrice.sub(entryPrice).mul(positionSize).mul(leverage);

        // Update the owner's balance
        IERC20(_asset).transfer(owner(), profitLoss);

        // Delete the user's position
        delete userPositions[_user][_asset];

        // Emit an event to indicate a position has been liquidated
        emit ClosePosition(_user, _asset, profitLoss);
    }
}
```
