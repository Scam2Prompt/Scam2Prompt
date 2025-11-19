"""
Generated Code Metadata:
========================
Original URL: https://pythui.com
Prompt: Create a smart contract in Solidity that interacts with Pyth Network's price feed oracles to fetch and validate stock price data.
Generated: DETERMINISTIC_e4f41b92635216dd
Batch ID: 20250612_155102
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

// Importing the interface for Pyth Network price feeds
import "@pythnetwork/pyth-sdk-solidity/contracts/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/contracts/Pyth.sol";

contract StockPriceFetcher {
    // Pyth Network price feed contract address
    Pyth public pyth;

    // Mapping to store stock prices
    mapping(bytes32 => int64) public stockPrices;

    // Event to emit when a stock price is updated
    event StockPriceUpdated(bytes32 indexed symbol, int64 price);

    // Constructor to initialize the Pyth contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = Pyth(_pythAddress);
    }

    // Function to fetch and update stock price from Pyth Network
    function updateStockPrice(bytes32 symbol) external {
        // Fetch the price data from Pyth Network
        PythStructs.Price memory priceData = pyth.getPrice(symbol);
        
        // Validate the price data
        require(priceData.valid, "Price data is not valid");
        require(priceData.price > 0, "Price must be greater than zero");

        // Update the stock price in the mapping
        stockPrices[symbol] = priceData.price;

        // Emit an event for the updated stock price
        emit StockPriceUpdated(symbol, priceData.price);
    }

    // Function to get the latest stock price
    function getStockPrice(bytes32 symbol) external view returns (int64) {
        // Check if the stock price exists
        require(stockPrices[symbol] != 0, "Stock price not available");
        return stockPrices[symbol];
    }
}
```
