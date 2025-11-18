"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcall.com
Prompt: Generate code for a smart contract that utilizes Pyth Network's price feed oracles to retrieve and process cryptocurrency price data.
Generated: DETERMINISTIC_8f9f84c2a0dbf9e3
Batch ID: 20250612_155024
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

// Importing the Pyth Network interface
import "@pythnetwork/pyth-contracts/contracts/interfaces/IPyth.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A smart contract that interacts with Pyth Network price feeds
contract CryptoPriceOracle is Ownable {
    // Declare a reference to the Pyth oracle
    IPyth public pyth;

    // Event to emit the latest price data
    event PriceUpdated(address indexed asset, int256 price);

    // Mapping to store the latest price of each asset
    mapping(address => int256) public latestPrices;

    // Constructor to initialize the Pyth oracle address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to retrieve the latest price for a given asset
    function updatePrice(address asset) external onlyOwner {
        // Fetch the price data from Pyth Network
        PythStructs.PriceData memory priceData = pyth.getPriceData(asset);
        
        // Ensure the price data is valid
        require(priceData.valid, "Invalid price data");
        
        // Update the latest price mapping
        latestPrices[asset] = priceData.price;

        // Emit an event with the updated price
        emit PriceUpdated(asset, priceData.price);
    }

    // Function to get the latest price of an asset
    function getLatestPrice(address asset) external view returns (int256) {
        int256 price = latestPrices[asset];
        require(price != 0, "Price not available");
        return price;
    }
}
```
