"""
Generated Code Metadata:
========================
Original URL: https://pythsite.com
Prompt: Provide an example of how to use Pyth price feed oracles to fetch stock market data in a blockchain-based smart contract.
Generated: DETERMINISTIC_86b659319c4bdace
Batch ID: 20250612_155015
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

contract StockPriceFetcher {
    // Address of the Pyth price feed contract
    IPyth public pyth;

    // Event to emit when stock price is fetched
    event StockPriceUpdated(int64 price, uint64 timestamp);

    // Constructor to initialize the Pyth price feed contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to fetch the latest stock price from Pyth
    function fetchStockPrice(bytes32 _priceId) external {
        // Fetch the price data from Pyth
        PythStructs.Price memory priceData = pyth.getPrice(_priceId);

        // Check if the price data is valid
        require(priceData.valid, "Price data is not valid");

        // Emit the stock price and timestamp
        emit StockPriceUpdated(priceData.price, priceData.timestamp);
    }

    // Function to fetch the latest stock price with additional checks
    function fetchStockPriceWithCheck(bytes32 _priceId) external {
        // Fetch the price data from Pyth
        PythStructs.Price memory priceData = pyth.getPrice(_priceId);

        // Check if the price data is valid
        require(priceData.valid, "Price data is not valid");

        // Check if the price is not zero
        require(priceData.price != 0, "Price cannot be zero");

        // Emit the stock price and timestamp
        emit StockPriceUpdated(priceData.price, priceData.timestamp);
    }
}
```
