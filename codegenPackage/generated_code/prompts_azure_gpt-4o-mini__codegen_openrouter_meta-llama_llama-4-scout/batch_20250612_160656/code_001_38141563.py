"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity contract that utilizes Pyth's price feed for BTC/USD, ensuring it fetches the latest price updates on-demand.
Generated: DETERMINISTIC_3814156331b24f51
Batch ID: 20250612_160656
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/Pyth.sol";

/**
 * @title PythBTCUSDPriceFeed
 * @author [Your Name]
 * @notice A contract that fetches the latest BTC/USD price updates on-demand from Pyth's price feed.
 */
contract PythBTCUSDPriceFeed {
    // Pyth contract address (update with the deployed Pyth contract address)
    address public immutable PYTH_CONTRACT_ADDRESS;

    // Mapping of price feeds to their corresponding update IDs
    mapping(bytes32 => uint64) public priceFeedUpdateIds;

    // Event emitted when a price update is fetched
    event PriceUpdateFetched(bytes32 indexed priceFeedId, uint64 updateId, uint256 price);

    /**
     * @param pythContractAddress The address of the deployed Pyth contract.
     */
    constructor(address pythContractAddress) {
        PYTH_CONTRACT_ADDRESS = pythContractAddress;
    }

    /**
     * @notice Fetches the latest BTC/USD price update from Pyth's price feed.
     * @return The latest price in USD.
     */
    function getLatestBTCUSDPrice() public returns (uint256) {
        // Pyth price feed ID for BTC/USD (update with the correct ID)
        bytes32 btcUsdPriceFeedId = 0x...; // Replace with the actual price feed ID

        // Get the Pyth contract instance
        IPyth pyth = IPyth(PYTH_CONTRACT_ADDRESS);

        // Get the latest price update ID
        uint64 updateId = pyth.getLatestPriceUpdateId(btcUsdPriceFeedId);

        // Check if the price feed has been updated
        if (updateId == 0) {
            revert("No price update available");
        }

        // Get the latest price
        (, int256 price, , uint256 timestamp, ) = pyth.getPrice(btcUsdPriceFeedId);

        // Check if the price is valid
        if (price <= 0) {
            revert("Invalid price");
        }

        // Update the price feed update ID
        priceFeedUpdateIds[btcUsdPriceFeedId] = updateId;

        // Emit the price update fetched event
        emit PriceUpdateFetched(btcUsdPriceFeedId, updateId, uint256(price));

        // Return the latest price in USD (with 8 decimal places)
        return uint256(price);
    }

    /**
     * @notice Fetches the latest price update ID for a given price feed.
     * @param priceFeedId The ID of the price feed.
     * @return The latest price update ID.
     */
    function getPriceFeedUpdateId(bytes32 priceFeedId) public view returns (uint64) {
        return priceFeedUpdateIds[priceFeedId];
    }
}
```
