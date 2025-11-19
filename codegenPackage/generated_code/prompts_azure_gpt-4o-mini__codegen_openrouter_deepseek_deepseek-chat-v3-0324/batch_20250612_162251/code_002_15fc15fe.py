"""
Generated Code Metadata:
========================
Original URL: https://pythcash.com
Prompt: What are the best practices for utilizing price feed oracles in smart contracts as outlined on pythcash.com?
Generated: DETERMINISTIC_15fc15fe26c9da99
Batch ID: 20250612_162251
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
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

/**
 * @title PriceFeedConsumer
 * @dev A contract that consumes price feeds from Pyth Network oracle
 */
contract PriceFeedConsumer {
    IPyth public pyth;

    // Mapping to store price feed IDs for different assets
    mapping(string => bytes32) public priceFeedIds;

    // Event to log price updates
    event PriceUpdated(string asset, int64 price, uint64 confidence, uint64 publishTime);

    /**
     * @dev Constructor to initialize the Pyth contract address
     * @param _pyth The address of the Pyth contract
     */
    constructor(address _pyth) {
        require(_pyth != address(0), "Invalid Pyth address");
        pyth = IPyth(_pyth);
    }

    /**
     * @dev Add a price feed ID for an asset
     * @param asset The symbol of the asset (e.g., "BTC/USD")
     * @param priceId The Pyth price feed ID for the asset
     */
    function addPriceFeed(string memory asset, bytes32 priceId) external {
        require(priceId != bytes32(0), "Invalid price ID");
        priceFeedIds[asset] = priceId;
    }

    /**
     * @dev Get the latest price for an asset
     * @param asset The symbol of the asset
     * @return price The current price
     * @return confidence The confidence interval of the price
     * @return publishTime The timestamp when the price was published
     */
    function getLatestPrice(
        string memory asset
    ) public view returns (int64, uint64, uint64) {
        bytes32 priceId = priceFeedIds[asset];
        require(priceId != bytes32(0), "Price feed not found");

        PythStructs.Price memory price = pyth.getPriceUnsafe(priceId);
        return (price.price, price.conf, price.publishTime);
    }

    /**
     * @dev Update the price feed with a signed price update data
     * @param updateData The signed price update data from Pyth
     * @param asset The asset symbol to update
     */
    function updatePriceFeed(
        bytes[] calldata updateData,
        string memory asset
    ) external payable {
        bytes32 priceId = priceFeedIds[asset];
        require(priceId != bytes32(0), "Price feed not found");

        // Pay the required fee to update the price
        uint fee = pyth.getUpdateFee(updateData);
        require(msg.value >= fee, "Insufficient fee");

        // Update the price data
        pyth.updatePriceFeeds{value: fee}(updateData);

        // Get the latest price and emit event
        (int64 price, uint64 confidence, uint64 publishTime) = getLatestPrice(asset);
        emit PriceUpdated(asset, price, confidence, publishTime);

        // Refund any excess payment
        if (msg.value > fee) {
            payable(msg.sender).transfer(msg.value - fee);
        }
    }

    /**
     * @dev Emergency function to withdraw any stuck ETH
     */
    function withdraw() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
