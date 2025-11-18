"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity smart contract that integrates the Pyth Network's price feed oracle to fetch the BTC/USD price using the `IPyth` interface and `getPrice` method.
Generated: DETERMINISTIC_4c5cc00f900d8200
Batch ID: 20250612_152000
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

// Interface for the Pyth Network's IPyth price feed
interface IPyth {
    function getPrice(uint64 priceId) external view returns (int64 price, uint64 conf, uint64 publishTime);
}

contract BTCPriceFetcher {
    // Address of the Pyth Network's price feed contract
    IPyth public pyth;
    // Price ID for BTC/USD from Pyth Network
    uint64 public constant BTC_USD_PRICE_ID = 0x12345678; // Replace with the actual price ID

    // Event to log the fetched BTC/USD price
    event PriceFetched(int64 price, uint64 confidence, uint64 publishTime);

    // Constructor to initialize the Pyth contract address
    constructor(address _pythAddress) {
        // Ensure the provided address is not zero
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to fetch the current BTC/USD price
    function fetchBTCPrice() external {
        // Fetch the price, confidence interval, and publish time from Pyth
        (int64 price, uint64 confidence, uint64 publishTime) = pyth.getPrice(BTC_USD_PRICE_ID);

        // Ensure the price is not negative (indicating an error)
        require(price >= 0, "Invalid price fetched");

        // Emit the price fetched event
        emit PriceFetched(price, confidence, publishTime);
    }
}
```
