"""
Generated Code Metadata:
========================
Original URL: https://pythcloud.com
Prompt: How can I implement a price feed oracle for smart contracts using the data provided by Pyth Cloud?
Generated: DETERMINISTIC_ce452ba48fd5c97b
Batch ID: 20250612_162311
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
 * @title PythPriceFeedOracle
 * @dev A contract that provides price feed data from Pyth Network to smart contracts
 */
contract PythPriceFeedOracle {
    IPyth public pyth;
    bytes32 public priceFeedId;
    uint public lastUpdatedTimestamp;
    uint public validTimePeriod;

    event PriceUpdated(int64 price, uint publishTime);

    /**
     * @dev Constructor to initialize the Pyth contract and price feed ID
     * @param _pyth The address of the Pyth contract
     * @param _priceFeedId The ID of the price feed to track
     * @param _validTimePeriod The time period (in seconds) for which a price is considered valid
     */
    constructor(address _pyth, bytes32 _priceFeedId, uint _validTimePeriod) {
        require(_pyth != address(0), "Invalid Pyth address");
        require(_priceFeedId != bytes32(0), "Invalid price feed ID");
        require(_validTimePeriod > 0, "Valid time period must be positive");

        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
        validTimePeriod = _validTimePeriod;
    }

    /**
     * @dev Updates the price feed with the latest data from Pyth
     * @param updateData The Pyth price update data
     * @param updateFee The fee required to update the price (will be refunded if unused)
     */
    function updatePrice(bytes[] calldata updateData, uint updateFee) external payable {
        require(updateData.length > 0, "No update data provided");
        require(msg.value >= updateFee, "Insufficient fee sent");

        // Update the price data
        uint refundAmount = msg.value - updateFee;
        pyth.updatePriceFeeds{value: updateFee}(updateData);

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeedId);
        lastUpdatedTimestamp = price.publishTime;

        emit PriceUpdated(price.price, price.publishTime);

        // Refund any excess payment
        if (refundAmount > 0) {
            payable(msg.sender).transfer(refundAmount);
        }
    }

    /**
     * @dev Returns the latest price and its validity status
     * @return price The current price
     * @return isValid Whether the price is valid (not too old)
     */
    function getPrice() external view returns (int64 price, bool isValid) {
        PythStructs.Price memory currentPrice = pyth.getPrice(priceFeedId);
        price = currentPrice.price;
        isValid = (block.timestamp - currentPrice.publishTime) <= validTimePeriod;
    }

    /**
     * @dev Returns the latest price with additional metadata
     * @return price The current price
     * @return confidence The confidence interval of the price
     * @return publishTime The timestamp when the price was published
     * @return isValid Whether the price is valid (not too old)
     */
    function getPriceWithMetadata() external view returns (
        int64 price,
        uint64 confidence,
        uint64 publishTime,
        bool isValid
    ) {
        PythStructs.Price memory currentPrice = pyth.getPrice(priceFeedId);
        price = currentPrice.price;
        confidence = currentPrice.conf;
        publishTime = currentPrice.publishTime;
        isValid = (block.timestamp - publishTime) <= validTimePeriod;
    }

    /**
     * @dev Updates the valid time period for price freshness
     * @param _validTimePeriod The new valid time period in seconds
     */
    function setValidTimePeriod(uint _validTimePeriod) external {
        require(_validTimePeriod > 0, "Valid time period must be positive");
        validTimePeriod = _validTimePeriod;
    }
}
```
