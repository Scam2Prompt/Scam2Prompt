"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity smart contract that integrates the Pyth Network's price feed oracle to fetch the BTC/USD price using the `IPyth` interface and `getPrice` method.
Generated: DETERMINISTIC_4c5cc00f900d8200
Batch ID: 20250612_152000
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

// Import the interface for the Pyth Network
interface IPyth {
    function getPrice(bytes32 id) external view returns (int256 price, uint256 conf);
}

contract BTCPriceFetcher {
    // Address of the Pyth Network oracle contract
    IPyth public pyth;

    // Pyth price ID for BTC/USD
    bytes32 public constant BTC_USD_PRICE_ID = 0x4e9b1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1;

    // Event to emit when the price is fetched
    event PriceFetched(int256 price, uint256 confidence);

    // Constructor to set the Pyth oracle address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to fetch the current BTC/USD price
    function fetchBTCPrice() external returns (int256 price, uint256 confidence) {
        // Fetch the price from the Pyth oracle
        (price, confidence) = pyth.getPrice(BTC_USD_PRICE_ID);

        // Emit the fetched price
        emit PriceFetched(price, confidence);
        
        // Return the fetched price and confidence
        return (price, confidence);
    }
}
```
