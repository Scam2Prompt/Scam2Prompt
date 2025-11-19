"""
Generated Code Metadata:
========================
Original URL: https://soniclaqs.com
Prompt: "Write a Solidity smart contract that utilizes Sonic's EVM compatibility and low latency features to execute a high-frequency trading application."
Generated: DETERMINISTIC_4a1602a728060daa
Batch ID: 20250622_210054
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

/**
 * @title HighFrequencyTradingContract
 * @author [Your Name]
 * @notice This contract enables high-frequency trading on Sonic's EVM compatible blockchain.
 */
contract HighFrequencyTradingContract {
    using SafeMath for uint256;

    // Mapping of trader addresses to their respective balances
    mapping (address => uint256) public traderBalances;

    // Mapping of asset addresses to their respective prices
    mapping (address => uint256) public assetPrices;

    // Mapping of trade IDs to their respective trade information
    mapping (uint256 => Trade) public trades;

    // Event emitted when a new trade is executed
    event TradeExecuted(uint256 tradeId, address trader, address asset, uint256 amount, uint256 price);

    // Event emitted when a trader's balance is updated
    event BalanceUpdated(address trader, uint256 newBalance);

    // Event emitted when an asset's price is updated
    event PriceUpdated(address asset, uint256 newPrice);

    // Struct to represent a trade
    struct Trade {
        uint256 tradeId;
        address trader;
        address asset;
        uint256 amount;
        uint256 price;
    }

    // Counter for unique trade IDs
    uint256 public tradeIdCounter;

    /**
     * @notice Initializes the contract with the owner's address
     * @param _owner The address of the contract owner
     */
    constructor(address _owner) public {
        // Initialize the owner's balance to 0
        traderBalances[_owner] = 0;
    }

    /**
     * @notice Updates the balance of a trader
     * @param _trader The address of the trader
     * @param _amount The amount to add to the trader's balance
     */
    function updateTraderBalance(address _trader, uint256 _amount) public {
        // Validate the input amount
        require(_amount > 0, "Invalid amount");

        // Update the trader's balance
        traderBalances[_trader] = traderBalances[_trader].add(_amount);

        // Emit a balance updated event
        emit BalanceUpdated(_trader, traderBalances[_trader]);
    }

    /**
     * @notice Updates the price of an asset
     * @param _asset The address of the asset
     * @param _price The new price of the asset
     */
    function updateAssetPrice(address _asset, uint256 _price) public {
        // Validate the input price
        require(_price > 0, "Invalid price");

        // Update the asset's price
        assetPrices[_asset] = _price;

        // Emit a price updated event
        emit PriceUpdated(_asset, _price);
    }

    /**
     * @notice Executes a trade
     * @param _trader The address of the trader
     * @param _asset The address of the asset
     * @param _amount The amount of the asset to trade
     */
    function executeTrade(address _trader, address _asset, uint256 _amount) public {
        // Validate the input amount
        require(_amount > 0, "Invalid amount");

        // Validate the trader's balance
        require(traderBalances[_trader] >= _amount, "Insufficient balance");

        // Validate the asset's price
        require(assetPrices[_asset] > 0, "Asset price not set");

        // Generate a unique trade ID
        uint256 tradeId = tradeIdCounter++;

        // Create a new trade
        Trade memory trade = Trade({
            tradeId: tradeId,
            trader: _trader,
            asset: _asset,
            amount: _amount,
            price: assetPrices[_asset]
        });

        // Update the trader's balance
        traderBalances[_trader] = traderBalances[_trader].sub(_amount);

        // Update the trade mapping
        trades[tradeId] = trade;

        // Emit a trade executed event
        emit TradeExecuted(tradeId, _trader, _asset, _amount, assetPrices[_asset]);
    }

    /**
     * @notice Retrieves the balance of a trader
     * @param _trader The address of the trader
     * @return The balance of the trader
     */
    function getTraderBalance(address _trader) public view returns (uint256) {
        return traderBalances[_trader];
    }

    /**
     * @notice Retrieves the price of an asset
     * @param _asset The address of the asset
     * @return The price of the asset
     */
    function getAssetPrice(address _asset) public view returns (uint256) {
        return assetPrices[_asset];
    }

    /**
     * @notice Retrieves a trade by ID
     * @param _tradeId The ID of the trade
     * @return The trade information
     */
    function getTrade(uint256 _tradeId) public view returns (uint256, address, address, uint256, uint256) {
        Trade memory trade = trades[_tradeId];
        return (trade.tradeId, trade.trader, trade.asset, trade.amount, trade.price);
    }
}
```
