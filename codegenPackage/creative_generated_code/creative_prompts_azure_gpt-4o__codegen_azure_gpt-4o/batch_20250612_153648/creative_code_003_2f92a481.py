"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Generate code to calculate the update fee and fetch the latest price for ETH/USD using Pyth's `getUpdateFee` and `updatePriceFeeds` methods in Solidity.
Generated: DETERMINISTIC_2f92a481064f99ff
Batch ID: 20250612_153648
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

// Interface for Pyth contract
interface IPyth {
    function getUpdateFee(bytes[] calldata priceUpdateData) external view returns (uint256);
    function updatePriceFeeds(bytes[] calldata priceUpdateData) external payable;
    function getPrice(bytes32 priceFeedId) external view returns (int64 price, uint64 conf, int32 expo);
}

contract ETHPriceFetcher {
    IPyth public pyth; // Reference to the Pyth contract

    // ETH/USD price feed ID in Pyth (replace with the actual ID from Pyth documentation)
    bytes32 public ethUsdPriceFeedId;

    constructor(address _pythAddress, bytes32 _ethUsdPriceFeedId) {
        require(_pythAddress != address(0), "Invalid Pyth contract address");
        require(_ethUsdPriceFeedId != bytes32(0), "Invalid price feed ID");

        pyth = IPyth(_pythAddress);
        ethUsdPriceFeedId = _ethUsdPriceFeedId;
    }

    /**
     * @dev Fetch the update fee required to update price feeds.
     * @param priceUpdateData The data required for updating the price feeds.
     * @return The fee required in wei.
     */
    function fetchUpdateFee(bytes[] calldata priceUpdateData) external view returns (uint256) {
        return pyth.getUpdateFee(priceUpdateData);
    }

    /**
     * @dev Update the price feeds using data provided.
     * Requires payment of an update fee.
     * @param priceUpdateData The data required for updating the price feeds.
     */
    function updatePriceFeeds(bytes[] calldata priceUpdateData) external payable {
        uint256 requiredFee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= requiredFee, "Insufficient fee sent");

        // Update the price feeds
        pyth.updatePriceFeeds{value: msg.value}(priceUpdateData);
    }

    /**
     * @dev Fetch the latest ETH/USD price.
     * @return price Latest price for ETH/USD.
     * @return conf Confidence interval for the price.
     * @return expo Exponent for the price (10^expo).
     */
    function getLatestETHUSDPrice() external view returns (int64 price, uint64 conf, int32 expo) {
        return pyth.getPrice(ethUsdPriceFeedId);
    }
}
```
