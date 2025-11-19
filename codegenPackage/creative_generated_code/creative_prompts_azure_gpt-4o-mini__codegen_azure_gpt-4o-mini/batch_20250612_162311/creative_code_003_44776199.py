"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcloud.com
Prompt: Generate a sample smart contract that utilizes Pyth Cloud's price feed oracles for real-time asset pricing.
Generated: DETERMINISTIC_447761993ab5502a
Batch ID: 20250612_162311
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

// Importing necessary interfaces from Pyth's price feed oracle
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PythPriceFeed {
    // Address of the Pyth contract on the specific network
    IPyth public pyth;

    // Mapping to store the latest prices for various assets
    mapping(bytes32 => PriceInfo) public prices;

    // Struct to hold price information
    struct PriceInfo {
        uint256 price; // The latest price of the asset
        uint256 updateTime; // Timestamp of the last price update
    }

    // Event to notify when a price is updated
    event PriceUpdated(bytes32 assetId, uint256 price, uint256 updateTime);

    // Constructor to initialize the Pyth contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth Address");
        pyth = IPyth(_pythAddress);
    }

    // Function to update the price for a given asset
    function updatePrice(bytes32 assetId) external {
        // Fetch price data from Pyth's oracle
        (int64 price, uint64 updateTime, uint64 publishTime) = pyth.getPrice(assetId);
        
        // Check if the price is valid
        require(price > 0, "Invalid price received");
        
        // Update the prices mapping
        prices[assetId] = PriceInfo({
            price: uint256(price),
            updateTime: uint256(updateTime)
        });

        // Emit an event indicating the price update
        emit PriceUpdated(assetId, uint256(price), uint256(updateTime));
    }

    // Function to retrieve the latest price for a given asset
    function getPrice(bytes32 assetId) external view returns (uint256 price, uint256 updateTime) {
        PriceInfo memory priceInfo = prices[assetId];
        require(priceInfo.price > 0, "Price not available for this asset");
        return (priceInfo.price, priceInfo.updateTime);
    }
}
```
