"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Write a smart contract in Solidity that uses Pyth's price feed IDs to retrieve the price of multiple assets, such as BTC/USD and ETH/USD.
Generated: DETERMINISTIC_8515b206234a82cb
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

// Import the Pyth interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract AssetPriceFetcher {
    // Address of the deployed Pyth contract (update with the correct address for your network)
    address public immutable PYTH_CONTRACT;

    // Store the price feed IDs for BTC/USD and ETH/USD
    bytes32 public immutable BTC_USD_FEED_ID;
    bytes32 public immutable ETH_USD_FEED_ID;

    // Event emitted when prices are fetched
    event PricesFetched(int64 btcPrice, int64 ethPrice);

    /**
     * @dev Constructor to initialize the contract with Pyth address and price feed IDs.
     * @param pythContract Address of the deployed Pyth contract.
     * @param btcUsdFeedId Price feed ID for BTC/USD.
     * @param ethUsdFeedId Price feed ID for ETH/USD.
     */
    constructor(address pythContract, bytes32 btcUsdFeedId, bytes32 ethUsdFeedId) {
        require(pythContract != address(0), "Invalid Pyth contract address");
        require(btcUsdFeedId != bytes32(0), "Invalid BTC/USD feed ID");
        require(ethUsdFeedId != bytes32(0), "Invalid ETH/USD feed ID");

        PYTH_CONTRACT = pythContract;
        BTC_USD_FEED_ID = btcUsdFeedId;
        ETH_USD_FEED_ID = ethUsdFeedId;
    }

    /**
     * @dev Fetches the latest prices for BTC/USD and ETH/USD from Pyth.
     * @return btcPrice The latest BTC/USD price.
     * @return ethPrice The latest ETH/USD price.
     */
    function fetchPrices() external view returns (int64 btcPrice, int64 ethPrice) {
        IPyth pyth = IPyth(PYTH_CONTRACT);

        // Fetch the price data for BTC/USD
        IPyth.Price memory btcPriceData = pyth.getPrice(BTC_USD_FEED_ID);

        // Fetch the price data for ETH/USD
        IPyth.Price memory ethPriceData = pyth.getPrice(ETH_USD_FEED_ID);

        // Extract the actual price values from the data
        btcPrice = btcPriceData.price;
        ethPrice = ethPriceData.price;

        // Emit the event with the fetched prices
        emit PricesFetched(btcPrice, ethPrice);
    }

    /**
     * @dev Fetches prices and handles errors gracefully.
     * This function fetches the latest BTC/USD and ETH/USD prices and ensures
     * that the Pyth contract call does not revert due to stale or unavailable data.
     * @return btcPrice The latest BTC/USD price, or 0 if data is unavailable.
     * @return ethPrice The latest ETH/USD price, or 0 if data is unavailable.
     */
    function safeFetchPrices() external view returns (int64 btcPrice, int64 ethPrice) {
        IPyth pyth = IPyth(PYTH_CONTRACT);

        try pyth.getPrice(BTC_USD_FEED_ID) returns (IPyth.Price memory btcPriceData) {
            btcPrice = btcPriceData.price;
        } catch {
            btcPrice = 0; // Fallback to 0 if data is unavailable or an error occurs
        }

        try pyth.getPrice(ETH_USD_FEED_ID) returns (IPyth.Price memory ethPriceData) {
            ethPrice = ethPriceData.price;
        } catch {
            ethPrice = 0; // Fallback to 0 if data is unavailable or an error occurs
        }

        emit PricesFetched(btcPrice, ethPrice);
    }
}
```

For this smart contract to operate, you will need the `IPyth` interface, which is part of the Pyth SDK. Ensure you import it correctly into your project and deploy the contract to the appropriate blockchain network supporting Pyth price feeds.
