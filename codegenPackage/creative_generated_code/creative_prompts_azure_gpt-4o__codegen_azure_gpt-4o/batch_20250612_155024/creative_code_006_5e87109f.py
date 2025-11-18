"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythusdc.com
Prompt: Provide an example of a smart contract that uses Pyth's price feed oracle to trigger an event when the price of an asset crosses a certain threshold.
Generated: DETERMINISTIC_5e87109f13d706d0
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

// Import the Pyth interface for interacting with the price feed oracle
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract AssetPriceMonitor {
    // Address of the Pyth price feed oracle
    IPyth public pythOracle;

    // Asset price threshold
    int public priceThreshold;

    // Event to trigger when the price crosses the threshold
    event PriceThresholdCrossed(int price, int threshold);

    // Constructor to initialize the Pyth oracle and price threshold
    constructor(address _pythOracle, int _priceThreshold) {
        require(_pythOracle != address(0), "Invalid Pyth oracle address");
        pythOracle = IPyth(_pythOracle);
        priceThreshold = _priceThreshold;
    }

    /**
     * @dev Update the price threshold
     * @param _newThreshold The new price threshold
     */
    function updatePriceThreshold(int _newThreshold) external {
        priceThreshold = _newThreshold;
    }

    /**
     * @dev Check the asset price and trigger the event if it crosses the threshold
     * @param priceFeedId The unique ID of the price feed for the asset
     * @param updateData Data to update the Pyth price feed
     */
    function checkPrice(bytes32 priceFeedId, bytes calldata updateData) external payable {
        // Update the Pyth price feed with the provided data
        pythOracle.updatePriceFeeds{value: msg.value}(updateData);

        // Retrieve the latest price for the asset
        IPyth.Price memory priceData = pythOracle.getPrice(priceFeedId);

        // Ensure the price is not stale or invalid
        require(priceData.price != 0, "Invalid price data");

        // Check if the price crosses the threshold
        if (priceData.price > priceThreshold || priceData.price < priceThreshold) {
            // Emit the event with the current price and threshold
            emit PriceThresholdCrossed(priceData.price, priceThreshold);
        }
    }

    /**
     * @dev Fallback function to receive ETH for fee payments to the Pyth oracle
     */
    receive() external payable {}
}
```
