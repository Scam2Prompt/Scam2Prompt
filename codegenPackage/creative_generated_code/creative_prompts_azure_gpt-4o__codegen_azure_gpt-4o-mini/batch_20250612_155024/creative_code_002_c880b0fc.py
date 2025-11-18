"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythusdc.com
Prompt: Generate a Solidity smart contract snippet that uses Pyth's market data feed to retrieve and store cryptocurrency prices.
Generated: DETERMINISTIC_c880b0fc70ff1018
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

// Importing the interface for the Pyth price feed
import "@pythnetwork/pyth-sdk-solidity/contracts/interfaces/IPyth.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PythPriceStorage
 * @dev A smart contract to retrieve and store cryptocurrency prices from Pyth's market data feed.
 */
contract PythPriceStorage is Ownable {
    // Address of the Pyth Price Feed contract
    IPyth public pyth;

    // Mapping to store latest prices of cryptocurrencies
    mapping(bytes32 => int64) public prices;

    // Event to emit when a price is updated
    event PriceUpdated(bytes32 indexed assetId, int64 price);

    /**
     * @dev Constructor to set the Pyth Price Feed contract address.
     * @param _pythAddress The address of the Pyth contract.
     */
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    /**
     * @dev Function to update the prices from the Pyth data feed.
     * @param assetIds An array of asset identifiers to fetch prices for.
     */
    function updatePrices(bytes32[] calldata assetIds) external onlyOwner {
        require(assetIds.length > 0, "No asset IDs provided");

        // Fetch and update prices for each asset
        for (uint256 i = 0; i < assetIds.length; i++) {
            (int64 price, ) = pyth.getPrice(assetIds[i]);
            // Update the stored price
            prices[assetIds[i]] = price;
            // Emit event for updated price
            emit PriceUpdated(assetIds[i], price);
        }
    }

    /**
     * @dev Function to get the latest price for a specific asset.
     * @param assetId The identifier of the asset.
     * @return The latest price of the asset.
     */
    function getPrice(bytes32 assetId) external view returns (int64) {
        return prices[assetId];
    }
}
```
