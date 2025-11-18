"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Write a Solidity contract that retrieves and verifies the accuracy of Pyth Network's price data using first-party sources.
Generated: DETERMINISTIC_0c9da8f182bc1118
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

interface IPyth {
    function getPrice(string memory id) external view returns (int256 price, uint256 timestamp);
}

contract PythPriceVerifier {
    // Address of the Pyth contract on the relevant network
    IPyth public pyth;

    // Event to emit when a price is fetched
    event PriceFetched(string indexed id, int256 price, uint256 timestamp);

    // Constructor to set the Pyth contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to retrieve and verify price data from Pyth Network
    function fetchPrice(string memory id) external returns (int256 price, uint256 timestamp) {
        // Fetch the price and timestamp from the Pyth contract
        (price, timestamp) = pyth.getPrice(id);

        // Verify that the price is valid (not zero) and the timestamp is recent
        require(price != 0, "Invalid price fetched");
        require(timestamp >= block.timestamp - 1 hours, "Price data is stale");

        // Emit event for fetched price
        emit PriceFetched(id, price, timestamp);
    }
}
```
