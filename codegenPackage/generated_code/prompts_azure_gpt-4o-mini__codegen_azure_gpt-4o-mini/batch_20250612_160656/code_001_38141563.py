"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity contract that utilizes Pyth's price feed for BTC/USD, ensuring it fetches the latest price updates on-demand.
Generated: DETERMINISTIC_3814156331b24f51
Batch ID: 20250612_160656
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

// Importing the interface for the Pyth price feed
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract BTCPriceFetcher {
    // Address of the Pyth price feed contract
    IPyth public pyth;

    // Event to emit when the price is fetched
    event PriceUpdated(int64 price, uint64 timestamp);

    // Constructor to initialize the Pyth price feed contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to fetch the latest BTC/USD price
    function getBTCPrice() external returns (int64 price, uint64 timestamp) {
        // Fetching the price data from Pyth
        PythStructs.Price memory btcPrice = pyth.getPrice("BTC/USD");

        // Check if the price is valid
        require(btcPrice.valid, "Price data is not valid");

        // Emit the price update event
        emit PriceUpdated(btcPrice.price, btcPrice.timestamp);

        // Return the price and timestamp
        return (btcPrice.price, btcPrice.timestamp);
    }
}
```
