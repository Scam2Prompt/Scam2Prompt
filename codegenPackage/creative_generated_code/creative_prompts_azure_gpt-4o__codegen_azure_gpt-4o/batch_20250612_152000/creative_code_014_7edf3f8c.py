"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity contract that uses Pyth's `updatePriceFeeds` method to fetch and store price data for multiple assets, including BTC/USD, ETH/USD, and PYTH/USD.
Generated: DETERMINISTIC_7edf3f8c4a6d5b09
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

// Importing Pyth's interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract AssetPriceManager {
    // Address of the Pyth contract (to be provided for the respective network)
    address public pythContractAddress;

    // Mapping to store the latest price of each asset feed
    mapping(bytes32 => int64) public latestPrices;

    // Mapping to store the latest timestamp of each asset feed
    mapping(bytes32 => uint64) public latestTimestamps;

    // Event emitted when price feeds are updated
    event PriceUpdated(bytes32 priceId, int64 price, uint64 timestamp);

    // Constructor to initialize the Pyth contract address
    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pythContractAddress = _pythContractAddress;
    }

    /**
     * @notice Updates price feeds for the provided asset IDs using the Pyth contract
     * @dev The asset IDs must match the IDs used in the Pyth network.
     * @param priceIds Array of asset price IDs
     * @param updateData Pyth update data (passed directly from off-chain sources)
     */
    function updatePriceFeeds(bytes32[] memory priceIds, bytes memory updateData) external {
        // Reference to the Pyth contract instance
        IPyth pyth = IPyth(pythContractAddress);

        // Update all price feeds using the provided update data
        pyth.updatePriceFeeds(updateData);

        // Retrieve and store the latest price and timestamp for each asset ID
        for (uint256 i = 0; i < priceIds.length; i++) {
            bytes32 priceId = priceIds[i];

            // Fetch price information from Pyth
            (int64 price, , uint64 timestamp) = pyth.getPriceUnsafe(priceId);

            // Store the price and timestamp in the contract state
            latestPrices[priceId] = price;
            latestTimestamps[priceId] = timestamp;

            // Emit an event for the updated price
            emit PriceUpdated(priceId, price, timestamp);
        }
    }

    /**
     * @notice Retrieves the latest price and timestamp for a given asset ID
     * @param priceId The asset price ID
     * @return price Latest price of the asset
     * @return timestamp Latest timestamp of the price update
     */
    function getLatestPrice(bytes32 priceId) external view returns (int64 price, uint64 timestamp) {
        price = latestPrices[priceId];
        timestamp = latestTimestamps[priceId];
    }
}
```
