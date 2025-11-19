"""
Generated Code Metadata:
========================
Original URL: https://pythnet.com
Prompt: Write a smart contract function in Solidity that uses PythNet's market data to trigger an event when an asset price crosses a specific threshold.
Generated: DETERMINISTIC_7c6752d053b29458
Batch ID: 20250612_155015
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
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract PriceThresholdAlert {
    IPyth public pyth;
    bytes32 public priceFeedId;
    uint256 public thresholdPrice;
    uint256 public priceScaleFactor = 10**8; // Adjust based on price feed decimals

    event ThresholdCrossed(
        bytes32 indexed priceFeedId,
        int64 currentPrice,
        uint256 thresholdPrice,
        uint256 timestamp
    );

    constructor(
        address _pythContract,
        bytes32 _priceFeedId,
        uint256 _thresholdPrice
    ) {
        pyth = IPyth(_pythContract);
        priceFeedId = _priceFeedId;
        thresholdPrice = _thresholdPrice;
    }

    function checkPriceThreshold(bytes[] calldata priceUpdateData) external payable {
        // Update price feed with the latest data
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeedId);

        // Scale the price to match threshold units
        uint256 currentPrice = uint64(price.price) * priceScaleFactor;

        // Check if price crossed the threshold
        if (currentPrice >= thresholdPrice) {
            emit ThresholdCrossed(
                priceFeedId,
                price.price,
                thresholdPrice,
                block.timestamp
            );
        }
    }

    // Allow contract to receive funds for price updates
    receive() external payable {}
}
```
