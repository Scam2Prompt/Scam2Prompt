"""
Generated Code Metadata:
========================
Original URL: https://pythshop.com
Prompt: How can I use Pyth Network's price feed oracles to ensure accurate and secure market data in my smart contract?
Generated: DETERMINISTIC_8755222f5b74b4c9
Batch ID: 20250612_155024
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

// Importing the Pyth Network's price feed interface
import "@pythnetwork/pyth-sdk-solidity/contracts/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/contracts/Pyth.sol";

contract PriceFeedConsumer {
    // Pyth price feed contract address
    Pyth public pyth;

    // Mapping to store the latest price for each asset
    mapping(bytes32 => int64) public latestPrices;

    // Event to emit when a new price is updated
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    // Constructor to initialize the Pyth contract
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = Pyth(_pythAddress);
    }

    // Function to update the price for a specific asset
    function updatePrice(bytes32 assetId) external {
        // Fetch the latest price data from Pyth
        Pyth.Price memory priceData = pyth.getPrice(assetId);
        
        // Check if the price data is valid
        require(priceData.valid, "Price data is not valid");
        
        // Update the latest price mapping
        latestPrices[assetId] = priceData.price;

        // Emit an event for the updated price
        emit PriceUpdated(assetId, priceData.price);
    }

    // Function to get the latest price for a specific asset
    function getLatestPrice(bytes32 assetId) external view returns (int64) {
        // Return the latest price for the asset
        return latestPrices[assetId];
    }
}
```

Make sure to replace the Pyth contract address with the actual deployed address of the Pyth Network's price feed contract when deploying this smart contract.
