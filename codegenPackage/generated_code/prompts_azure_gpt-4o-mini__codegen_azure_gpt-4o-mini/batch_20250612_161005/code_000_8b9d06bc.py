"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: Write a smart contract that utilizes the Flare Time Series Oracle to fetch decentralized price feeds for a DeFi application.
Generated: DETERMINISTIC_8b9d06bc47e7599b
Batch ID: 20250612_161005
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

// Importing the interface for the Flare Time Series Oracle
import "@flare.xyz/flare-oracle/contracts/interfaces/IFlareOracle.sol";

contract DeFiPriceFeed {
    // State variable to store the address of the Flare Oracle
    IFlareOracle public flareOracle;

    // Event to emit when a price is fetched
    event PriceFetched(uint256 price);

    // Constructor to initialize the Flare Oracle address
    constructor(address _flareOracleAddress) {
        require(_flareOracleAddress != address(0), "Invalid Oracle Address");
        flareOracle = IFlareOracle(_flareOracleAddress);
    }

    // Function to fetch the price of an asset
    function getPrice(string memory assetSymbol) public returns (uint256) {
        // Fetching the price from the Flare Oracle
        (uint256 price, uint256 timestamp) = flareOracle.getLatestPrice(assetSymbol);
        
        // Check if the price is valid
        require(price > 0, "Invalid price fetched");

        // Emit the price fetched event
        emit PriceFetched(price);

        return price;
    }

    // Function to fetch the price with a timestamp
    function getPriceWithTimestamp(string memory assetSymbol) public returns (uint256, uint256) {
        // Fetching the price and timestamp from the Flare Oracle
        (uint256 price, uint256 timestamp) = flareOracle.getLatestPrice(assetSymbol);
        
        // Check if the price is valid
        require(price > 0, "Invalid price fetched");

        // Emit the price fetched event
        emit PriceFetched(price);

        return (price, timestamp);
    }
}
```
