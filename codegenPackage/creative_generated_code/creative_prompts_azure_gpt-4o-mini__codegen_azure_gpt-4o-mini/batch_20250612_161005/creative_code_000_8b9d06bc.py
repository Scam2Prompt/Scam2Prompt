"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Write a smart contract that utilizes the Flare Time Series Oracle to fetch decentralized price feeds for a DeFi application.
Generated: DETERMINISTIC_8b9d06bc47e7599b
Batch ID: 20250612_161005
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

// Import the interface for the Flare Time Series Oracle
import "@flarenetwork/flr-oracle/contracts/interfaces/IPriceOracle.sol";

contract DeFiPriceFeed {
    // The address of the Flare Time Series Oracle
    address private oracleAddress;
    IPriceOracle private priceOracle;

    // Mapping to store the price feeds for different assets
    mapping(string => uint256) public assetPrices;

    // Event for logging price updates
    event PriceUpdated(string asset, uint256 price);

    // Constructor to initialize the oracle address
    constructor(address _oracleAddress) {
        require(_oracleAddress != address(0), "Invalid oracle address");
        oracleAddress = _oracleAddress;
        priceOracle = IPriceOracle(oracleAddress);
    }

    // Function to update the price for a specific asset
    function updateAssetPrice(string memory asset) public {
        // Fetch the latest price from the Flare Time Series Oracle
        uint256 price = priceOracle.getLatestPrice(asset);
        require(price > 0, "Invalid price fetched");

        // Update the mapping with the new price
        assetPrices[asset] = price;

        // Emit an event to log the price update
        emit PriceUpdated(asset, price);
    }

    // Function to retrieve the current price for a specific asset
    function getAssetPrice(string memory asset) public view returns (uint256) {
        uint256 price = assetPrices[asset];
        require(price > 0, "Price not available for this asset");
        return price;
    }

    // Function to get the price directly from the oracle (for external calls)
    function fetchPriceFromOracle(string memory asset) public view returns (uint256) {
        uint256 price = priceOracle.getLatestPrice(asset);
        require(price > 0, "Invalid price fetched from oracle");
        return price;
    }

    // Optional: Function to change the oracle address (if required)
    function setOracleAddress(address _oracleAddress) external {
        require(_oracleAddress != address(0), "Invalid oracle address");
        oracleAddress = _oracleAddress;
        priceOracle = IPriceOracle(oracleAddress);
    }
}
```
