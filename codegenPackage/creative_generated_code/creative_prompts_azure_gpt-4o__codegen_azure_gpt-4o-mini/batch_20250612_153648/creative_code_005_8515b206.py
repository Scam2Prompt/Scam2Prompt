"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Write a smart contract in Solidity that uses Pyth's price feed IDs to retrieve the price of multiple assets, such as BTC/USD and ETH/USD.
Generated: DETERMINISTIC_8515b206234a82cb
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

// Import the Pyth price feed interface
interface IPyth {
    function getPrice(string memory priceId) external view returns (int64, uint64);
}

/**
 * @title PythPriceFeed
 * @dev A smart contract to retrieve prices from Pyth's price feeds for multiple assets.
 */
contract PythPriceFeed {
    // Instance of the Pyth price feed contract
    IPyth public pythContract;

    // Event to emit when prices are retrieved
    event PricesRetrieved(string priceId, int64 price, uint64 confidence);

    /**
     * @dev Constructor to set the Pyth contract address.
     * @param _pythContract The address of the Pyth price feed contract.
     */
    constructor(address _pythContract) {
        pythContract = IPyth(_pythContract);
    }

    /**
     * @dev Fetch the price of an asset given its price ID.
     * @param priceId The price ID for the asset (e.g., BTC/USD, ETH/USD).
     * @return price The latest price of the asset in int64 format.
     * @return confidence The confidence interval for the price.
     */
    function getPrice(string memory priceId) public view returns (int64 price, uint64 confidence) {
        (price, confidence) = pythContract.getPrice(priceId);
        require(price != 0, "Invalid price returned");
        require(confidence != 0, "Invalid confidence returned");

        emit PricesRetrieved(priceId, price, confidence);
    }

    /**
     * @dev Fetch prices for multiple assets in a single call.
     * @param priceIds An array of price IDs for the assets.
     * @return prices An array of prices corresponding to the input price IDs.
     * @return confidences An array of confidence values corresponding to the input price IDs.
     */
    function getMultiplePrices(string[] memory priceIds) public view returns (int64[] memory prices, uint64[] memory confidences) {
        uint256 length = priceIds.length;
        prices = new int64[](length);
        confidences = new uint64[](length);

        for (uint256 i = 0; i < length; i++) {
            (prices[i], confidences[i]) = getPrice(priceIds[i]);
        }
    }
}
```
