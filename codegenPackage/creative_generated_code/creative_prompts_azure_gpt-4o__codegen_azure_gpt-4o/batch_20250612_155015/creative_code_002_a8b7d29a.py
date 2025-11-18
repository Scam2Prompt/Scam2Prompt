"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnet.com
Prompt: Generate a smart contract example in Solidity that uses PythNet's price feed oracle to retrieve and validate asset prices.
Generated: DETERMINISTIC_a8b7d29ac58c0c1d
Batch ID: 20250612_155015
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

// Import the PythNet interface for interacting with its price feed oracle
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PythPriceFeed {
    // Address of the PythNet oracle contract (update with the correct address in your deployment environment)
    IPyth public pythOracle;
    uint public priceUpdateThreshold; // Threshold in seconds for considering a price update valid

    // Constructor to set the Pyth oracle contract address and price update threshold
    constructor(address _pythOracleAddress, uint _priceUpdateThreshold) {
        require(_pythOracleAddress != address(0), "Invalid Pyth oracle address");
        require(_priceUpdateThreshold > 0, "Price update threshold must be greater than zero");

        pythOracle = IPyth(_pythOracleAddress);
        priceUpdateThreshold = _priceUpdateThreshold;
    }

    /**
     * @dev Retrieves the price of an asset and validates its freshness.
     * @param priceId The unique price identifier for the asset from PythNet.
     * @return price The current price of the asset in its base currency.
     * @return isValid Whether the price update is considered valid.
     */
    function getAssetPrice(bytes32 priceId) external view returns (int price, bool isValid) {
        try pythOracle.getPriceUnsafe(priceId) returns (IPyth.Price memory pythPrice) {
            // Check if the price is valid based on the update age
            uint lastUpdateAge = block.timestamp - pythPrice.publishTime;

            if (lastUpdateAge <= priceUpdateThreshold) {
                price = pythPrice.price; // Asset price in its base currency
                isValid = true; // Price is considered valid
            } else {
                price = 0; // Invalid price
                isValid = false; // Update threshold exceeded
            }
        } catch {
            // If there's an error interacting with PythNet, handle gracefully
            price = 0; // Invalid price
            isValid = false; // Unable to validate price
        }
    }

    /**
     * @dev Allows the owner to update the price update threshold.
     * @param _priceUpdateThreshold New threshold in seconds.
     */
    function updatePriceUpdateThreshold(uint _priceUpdateThreshold) external {
        require(_priceUpdateThreshold > 0, "Price update threshold must be greater than zero");
        priceUpdateThreshold = _priceUpdateThreshold;
    }
}
```
