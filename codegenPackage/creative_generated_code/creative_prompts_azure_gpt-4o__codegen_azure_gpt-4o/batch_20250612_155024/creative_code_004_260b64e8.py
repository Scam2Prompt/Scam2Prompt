"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythgame.com
Prompt: Write code to validate and update market data in a smart contract using Pyth Network's oracle services.
Generated: DETERMINISTIC_260b64e895135bf5
Batch ID: 20250612_155024
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
 * @title MarketDataUpdater
 * @dev A smart contract that validates and updates market data using Pyth Network's oracle services.
 */
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract MarketDataUpdater {
    // Pyth Network oracle contract address
    address public pythOracleAddress;

    // Data structure to store market data
    struct MarketData {
        int64 price;            // Price of the asset (e.g., stock or commodity)
        uint64 publishTime;     // Timestamp when the price was published
    }

    // Mapping to store market data by asset symbol
    mapping(string => MarketData) public marketData;

    // Events
    event MarketDataUpdated(string indexed assetSymbol, int64 price, uint64 publishTime);

    // Modifier to ensure the oracle address is set
    modifier oracleIsSet() {
        require(pythOracleAddress != address(0), "Pyth oracle address is not set");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the Pyth oracle address.
     * @param _pythOracleAddress Address of the Pyth oracle contract.
     */
    constructor(address _pythOracleAddress) {
        require(_pythOracleAddress != address(0), "Invalid Pyth oracle address");
        pythOracleAddress = _pythOracleAddress;
    }

    /**
     * @dev Function to update the Pyth oracle address.
     * @param _pythOracleAddress New address of the Pyth oracle contract.
     */
    function updateOracleAddress(address _pythOracleAddress) external {
        require(_pythOracleAddress != address(0), "Invalid Pyth oracle address");
        pythOracleAddress = _pythOracleAddress;
    }

    /**
     * @dev Function to validate and update market data for a given asset symbol.
     * @param assetSymbol Symbol of the asset to update market data for (e.g., "BTC/USD").
     * @param priceFeedId Feed ID for the asset on Pyth Network.
     */
    function updateMarketData(string memory assetSymbol, bytes32 priceFeedId)
        external
        oracleIsSet
    {
        IPyth pyth = IPyth(pythOracleAddress);

        // Validate and get the price data from the Pyth oracle
        (int64 price, uint64 publishTime) = pyth.getPriceUnsafe(priceFeedId);

        require(price > 0, "Invalid price data");
        require(publishTime > 0, "Invalid publish time");

        // Update the market data mapping
        marketData[assetSymbol] = MarketData({price: price, publishTime: publishTime});

        // Emit an event for the update
        emit MarketDataUpdated(assetSymbol, price, publishTime);
    }

    /**
     * @dev Function to retrieve market data for a given asset symbol.
     * @param assetSymbol Symbol of the asset to retrieve market data for.
     * @return price Current price of the asset.
     * @return publishTime Timestamp when the price was published.
     */
    function getMarketData(string memory assetSymbol)
        external
        view
        returns (int64 price, uint64 publishTime)
    {
        MarketData memory data = marketData[assetSymbol];
        return (data.price, data.publishTime);
    }
}
```

This code assumes the availability of the Pyth Network's `IPyth` interface library (`pyth-sdk-solidity`) and uses its `getPriceUnsafe` method to fetch price data. Make sure that the appropriate Pyth library is installed and properly referenced in your project.
