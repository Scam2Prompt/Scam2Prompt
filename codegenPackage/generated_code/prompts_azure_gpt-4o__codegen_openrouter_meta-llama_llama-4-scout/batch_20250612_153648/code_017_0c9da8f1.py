"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: Write a Solidity contract that retrieves and verifies the accuracy of Pyth Network's price data using first-party sources.
Generated: DETERMINISTIC_0c9da8f182bc1118
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

import "@pythnetwork/pyth-contracts/src/Pyth.sol";
import "@pythnetwork/pyth-contracts/src/PythStructs.sol";

/**
 * @title PythPriceVerifier
 * @author [Your Name]
 * @notice A contract to retrieve and verify Pyth Network's price data.
 */
contract PythPriceVerifier {
    // Pyth contract instance
    Pyth public pyth;

    /**
     * @param _pyth Pyth contract address
     */
    constructor(address _pyth) {
        pyth = Pyth(_pyth);
    }

    /**
     * @notice Retrieve the latest price data for a given price feed ID.
     * @param _priceFeedId Price feed ID (e.g. 0x...)
     * @return The latest price data
     */
    function getLatestPrice(bytes32 _priceFeedId) public view returns (PythStructs.Price) {
        PythStructs.Price memory price = pyth.getPrice(_priceFeedId);
        return price;
    }

    /**
     * @notice Verify the accuracy of the price data by checking its freshness.
     * @param _priceFeedId Price feed ID (e.g. 0x...)
     * @param _maxAge Maximum allowed age of the price data in seconds
     * @return True if the price data is fresh, false otherwise
     */
    function isPriceFresh(bytes32 _priceFeedId, uint64 _maxAge) public view returns (bool) {
        PythStructs.Price memory price = getLatestPrice(_priceFeedId);
        uint64 age = block.timestamp - price.publishTime;
        return age <= _maxAge;
    }

    /**
     * @notice Retrieve and verify the latest price data for a given price feed ID.
     * @param _priceFeedId Price feed ID (e.g. 0x...)
     * @param _maxAge Maximum allowed age of the price data in seconds
     * @return The latest price data if it's fresh, otherwise revert
     */
    function getFreshPrice(bytes32 _priceFeedId, uint64 _maxAge) public view returns (PythStructs.Price) {
        PythStructs.Price memory price = getLatestPrice(_priceFeedId);
        require(isPriceFresh(_priceFeedId, _maxAge), "Price is stale");
        return price;
    }
}
```
