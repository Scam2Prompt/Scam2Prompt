"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity contract that utilizes Pyth's price feed for BTC/USD, ensuring it fetches the latest price updates on-demand.
Generated: DETERMINISTIC_3814156331b24f51
Batch ID: 20250612_160656
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

// Importing the interface for Pyth's price feed
import "@pythnetwork/pyth-sdk-solidity/PriceFeed.sol";

contract BTCPriceFetcher {
    // Address of the Pyth BTC/USD price feed on the Solana network (make sure to replace it with the correct one)
    address public constant BTC_USD_PRICE_FEED = 0x...; // Replace with actual Pyth BTC/USD Price Feed address

    // Variable to hold the latest BTC price
    int256 public latestBTCPrice;

    // Event to emit when the BTC price is updated
    event BTCPriceUpdated(int256 price);

    // Function to fetch the latest BTC price from Pyth's price feed
    function fetchLatestBTCPrice() external {
        // Fetch the price feed
        PriceFeed priceFeed = PriceFeed(BTC_USD_PRICE_FEED);
        
        // Get the latest price
        (int256 price, ) = priceFeed.getLatestPrice();

        // Check for valid price data
        require(price > 0, "Invalid price received from Pyth");

        // Update the latest BTC price
        latestBTCPrice = price;

        // Emit an event with the updated price
        emit BTCPriceUpdated(price);
    }

    // Function to get the latest BTC price
    function getLatestBTCPrice() external view returns (int256) {
        return latestBTCPrice;
    }
}
```
