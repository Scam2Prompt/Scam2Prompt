"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: Generate code to calculate the update fee and fetch the latest price for ETH/USD using Pyth's `getUpdateFee` and `updatePriceFeeds` methods in Solidity.
Generated: DETERMINISTIC_2f92a481064f99ff
Batch ID: 20250612_153648
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

contract PythPriceUpdater {
    IPyth public pyth;
    bytes32 public priceFeedId;

    constructor(address _pyth, bytes32 _priceFeedId) {
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }

    /**
     * @dev Calculates the required fee to update the price feed
     * @param updateData The update data to be sent to Pyth
     * @return updateFee The required fee in wei
     */
    function calculateUpdateFee(bytes[] calldata updateData) external view returns (uint256) {
        return pyth.getUpdateFee(updateData);
    }

    /**
     * @dev Updates the price feed and returns the latest price information
     * @param updateData The update data to be sent to Pyth
     * @return price The latest price information
     */
    function updateAndFetchPrice(bytes[] calldata updateData) external payable returns (PythStructs.Price memory) {
        // Update the price feed with the provided data
        pyth.updatePriceFeeds{value: msg.value}(updateData);

        // Get the latest price information
        return pyth.getPrice(priceFeedId);
    }

    /**
     * @dev Fetches the latest price information without updating
     * @return price The latest price information
     */
    function fetchLatestPrice() external view returns (PythStructs.Price memory) {
        return pyth.getPrice(priceFeedId);
    }

    /**
     * @dev Allows the contract to receive ETH refunds from Pyth
     */
    receive() external payable {}
}
```
