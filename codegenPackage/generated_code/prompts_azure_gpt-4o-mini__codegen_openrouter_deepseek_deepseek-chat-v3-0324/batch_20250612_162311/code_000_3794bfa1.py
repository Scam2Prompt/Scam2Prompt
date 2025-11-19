"""
Generated Code Metadata:
========================
Original URL: https://pythnet.com
Prompt: How can I implement price feed oracles for smart contracts using the data provided by Pyth Network?
Generated: DETERMINISTIC_3794bfa18ff81383
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

// Import Pyth Network interfaces
interface IPyth {
    struct Price {
        // Price
        int64 price;
        // Confidence interval around the price
        uint64 conf;
        // Price exponent
        int32 expo;
        // Unix timestamp describing when the price was published
        uint publishTime;
    }

    // Get the price of a price feed with `id`
    function getPrice(bytes32 id) external view returns (Price memory price);

    // Get the latest update data for price feeds
    function getUpdateFee(bytes[] calldata updateData) external view returns (uint feeAmount);

    // Update the price feeds (needs to be paid)
    function updatePriceFeeds(bytes[] calldata updateData) external payable;
}

contract PythOracleConsumer {
    IPyth public pyth;
    bytes32 public priceFeedId;

    event PriceUpdated(int64 price, uint64 conf, uint publishTime);

    constructor(address _pyth, bytes32 _priceFeedId) {
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }

    // Get the latest price from Pyth Network
    function getLatestPrice() public view returns (int64, uint64, uint) {
        IPyth.Price memory priceData = pyth.getPrice(priceFeedId);
        return (priceData.price, priceData.conf, priceData.publishTime);
    }

    // Update the price feed with the latest data (caller must pay the fee)
    function updatePriceFeed(bytes[] calldata updateData) external payable {
        // Get the required fee for the update
        uint fee = pyth.getUpdateFee(updateData);
        require(msg.value >= fee, "Insufficient fee");

        // Update the price feed
        pyth.updatePriceFeeds{value: fee}(updateData);

        // Refund any excess fee
        if (msg.value > fee) {
            payable(msg.sender).transfer(msg.value - fee);
        }

        // Emit the latest price
        (int64 price, uint64 conf, uint publishTime) = getLatestPrice();
        emit PriceUpdated(price, conf, publishTime);
    }

    // Helper function to convert price to a human-readable format
    function getNormalizedPrice() public view returns (uint) {
        (int64 price, , int32 expo) = pyth.getPrice(priceFeedId);
        return uint(int(price)) * (10 ** uint(int(-expo)));
    }

    // Allow contract to receive ETH refunds
    receive() external payable {}
}
```
