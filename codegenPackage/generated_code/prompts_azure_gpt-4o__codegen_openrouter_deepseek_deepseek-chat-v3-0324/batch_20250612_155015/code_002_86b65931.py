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

// Interface for Pyth price feed
interface IPyth {
    struct Price {
        // Price
        int64 price;
        // Confidence interval around the price
        uint64 conf;
        // Price exponent
        int32 expo;
        // Unix timestamp describing when the price was published
        uint publishTime;
    }

    // Get the price of a price feed with `id`
    function getPrice(bytes32 id) external view returns (Price memory price);
}

contract StockMarketOracle {
    IPyth public pyth;
    bytes32 public priceFeedId;

    // Events
    event PriceUpdated(int64 price, uint64 confidence, uint timestamp);

    constructor(address _pyth, bytes32 _priceFeedId) {
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }

    // Fetch the latest price from Pyth oracle
    function getLatestPrice() public view returns (int64, uint64, uint) {
        IPyth.Price memory priceData = pyth.getPrice(priceFeedId);
        return (priceData.price, priceData.conf, priceData.publishTime);
    }

    // Example function to use the price data
    function checkStockPrice() external {
        (int64 price, uint64 confidence, uint timestamp) = getLatestPrice();
        
        require(confidence < uint64(1e18), "Price confidence too low");
        require(timestamp >= block.timestamp - 3600, "Price too old");

        // Use the price data (e.g., for trading logic)
        emit PriceUpdated(price, confidence, timestamp);
    }
}
```
