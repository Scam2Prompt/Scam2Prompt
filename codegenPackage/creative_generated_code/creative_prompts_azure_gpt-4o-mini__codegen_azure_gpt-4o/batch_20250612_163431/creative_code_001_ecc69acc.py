"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-staking.pages.dev
Prompt: Write a code example for a Solidity contract that utilizes Pyth's pull oracle to fetch the latest BTC/USD price.
Generated: DETERMINISTIC_ecc69acc4895b010
Batch ID: 20250612_163431
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

// Importing the necessary interface for interacting with the Pyth oracle
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract BTCPriceFetcher {
    // Address of the Pyth oracle on the deployed network
    IPyth public pythOracle;
    
    // Pyth price feed ID for BTC/USD
    // Replace this with the actual price feed ID from Pyth documentation for your network.
    bytes32 public constant BTC_USD_PRICE_ID = 0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;

    // Event to log the fetched BTC/USD price
    event BTCPriceUpdated(int price, uint64 timestamp);

    constructor(address _pythOracleAddress) {
        // Initialize the Pyth oracle contract instance
        require(_pythOracleAddress != address(0), "Pyth oracle address cannot be zero");
        pythOracle = IPyth(_pythOracleAddress);
    }

    /**
     * @dev Fetches the latest price of BTC/USD from the Pyth pull oracle.
     * Emits an event with the price and timestamp.
     */
    function fetchBTCPrice() external {
        // Fetch the latest price data from Pyth for the BTC/USD feed
        IPyth.Price memory priceData = pythOracle.getPrice(BTC_USD_PRICE_ID);

        // Check if the price feed is valid
        require(priceData.price != 0, "Price feed is invalid or not available");
        require(priceData.conf >= 0, "Price confidence interval is invalid");

        // Emit an event with the fetched price and its timestamp
        emit BTCPriceUpdated(priceData.price, priceData.publishTime);
    }

    /**
     * @dev Allows querying the current BTC/USD price without emitting an event.
     * @return price The BTC/USD price.
     * @return timestamp The timestamp of the price update.
     */
    function getBTCPrice() external view returns (int price, uint64 timestamp) {
        // Fetch the latest price data from Pyth for the BTC/USD feed
        IPyth.Price memory priceData = pythOracle.getPrice(BTC_USD_PRICE_ID);

        // Return the fetched price and its timestamp
        return (priceData.price, priceData.publishTime);
    }
}
```

This code assumes that the Pyth SDK for Solidity (`pyth-sdk-solidity`) has been properly installed and configured in your project. Replace the placeholder `BTC_USD_PRICE_ID` value with the actual price feed ID from Pyth's documentation for the specific network you're targeting.
