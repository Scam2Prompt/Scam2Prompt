"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythshop.com
Prompt: How can I use Pyth Network's price feed oracles to ensure accurate and secure market data in my smart contract?
Generated: DETERMINISTIC_8755222f5b74b4c9
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

// Import the Pyth Network's price feed interface
import "@pythnetwork/pyth-sdk-solidity/contracts/interfaces/IPyth.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MarketDataConsumer is Ownable {
    // Address of the Pyth Network's price feed contract
    IPyth public pyth;

    // Mapping to store the latest price for each asset
    mapping(bytes32 => int256) public latestPrices;

    // Event emitted when a new price is updated
    event PriceUpdated(bytes32 indexed assetId, int256 price);

    // Constructor to set the Pyth contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to update the price for a specific asset
    function updatePrice(bytes32 assetId) external onlyOwner {
        // Request the latest price from Pyth
        (int256 price, uint256 publishTime, uint256 validityPeriod) = pyth.getPrice(assetId);
        
        // Ensure the price is valid and recent
        require(validityPeriod > 0, "Price data is not valid");
        require(block.timestamp - publishTime <= validityPeriod, "Price data is stale");

        // Update the latest price mapping
        latestPrices[assetId] = price;

        // Emit event for front-end tracking
        emit PriceUpdated(assetId, price);
    }

    // Function to retrieve the latest price for a specific asset
    function getLatestPrice(bytes32 assetId) external view returns (int256) {
        // Return the latest price if it exists, otherwise revert
        require(latestPrices[assetId] != 0, "Price not available");
        return latestPrices[assetId];
    }
}
```
