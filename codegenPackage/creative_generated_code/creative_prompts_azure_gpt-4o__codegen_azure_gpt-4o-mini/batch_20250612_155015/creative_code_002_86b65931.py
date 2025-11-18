"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythsite.com
Prompt: Provide an example of how to use Pyth price feed oracles to fetch stock market data in a blockchain-based smart contract.
Generated: DETERMINISTIC_86b659319c4bdace
Batch ID: 20250612_155015
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

// Importing the interface for the Pyth price feed
import "@pythnetwork/pyth-sdk-solidity/contracts/interfaces/IPyth.sol";

contract StockPriceConsumer {
    // State variables
    IPyth public pyth; // Instance of the Pyth contract
    bytes32 public stockPriceFeedId; // Identifier for the stock price feed
    int64 public latestPrice; // Variable to store the latest stock price

    // Event to emit when a new price is fetched
    event PriceUpdated(int64 price);

    // Constructor to initialize the Pyth price feed
    constructor(address _pythAddress, bytes32 _stockPriceFeedId) {
        pyth = IPyth(_pythAddress);
        stockPriceFeedId = _stockPriceFeedId;
    }

    // Function to fetch the latest stock price from Pyth
    function updateStockPrice() external {
        // Fetch the price data from Pyth
        (int64 price, uint64 timestamp) = pyth.getPriceUnsafe(stockPriceFeedId);

        // Ensure the price is not negative and timestamp is valid
        require(price >= 0, "Price must be non-negative");
        require(timestamp != 0, "Invalid timestamp");

        // Update the latest price
        latestPrice = price;

        // Emit the price update event
        emit PriceUpdated(latestPrice);
    }

    // Function to get the latest stock price
    function getLatestPrice() external view returns (int64) {
        return latestPrice;
    }
}
```
