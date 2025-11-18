"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Write a smart contract that uses Pyth price feeds to calculate expiry prices for options contracts in a DeFi application on Ethereum.
Generated: DETERMINISTIC_e0bec934e5846536
Batch ID: 20250612_152000
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

/**
 * @title OptionsExpiryPriceCalculator
 * @dev A smart contract to calculate expiry prices for options contracts using Pyth price feeds.
 */
interface IPyth {
    function getPrice(bytes32 priceFeedId) external view returns (int64 price, uint64 timestamp, uint64 conf);
}

contract OptionsExpiryPriceCalculator {
    // Address of the Pyth price feed contract
    address public pythPriceFeedAddress;

    // Mapping to store expiry prices for specific options contracts
    mapping(bytes32 => int64) public expiryPrices;

    // Event emitted when an expiry price is calculated and stored
    event ExpiryPriceCalculated(bytes32 indexed optionId, int64 price, uint64 timestamp);

    /**
     * @dev Constructor to initialize the Pyth price feed address.
     * @param _pythPriceFeedAddress Address of the Pyth price feed contract.
     */
    constructor(address _pythPriceFeedAddress) {
        require(_pythPriceFeedAddress != address(0), "Pyth price feed address cannot be zero");
        pythPriceFeedAddress = _pythPriceFeedAddress;
    }

    /**
     * @dev Calculates and stores the expiry price for a given options contract.
     * @param optionId The unique ID of the options contract.
     * @param priceFeedId The Pyth price feed ID to fetch the asset price.
     */
    function calculateExpiryPrice(bytes32 optionId, bytes32 priceFeedId) external {
        require(optionId != bytes32(0), "Option ID cannot be zero");
        require(priceFeedId != bytes32(0), "Price feed ID cannot be zero");

        // Fetch the price data from the Pyth price feed
        (int64 price, uint64 timestamp, ) = IPyth(pythPriceFeedAddress).getPrice(priceFeedId);

        // Ensure the price and timestamp are valid
        require(price > 0, "Invalid price returned by Pyth");
        require(timestamp > 0, "Invalid timestamp returned by Pyth");

        // Store the price for the given option ID
        expiryPrices[optionId] = price;

        // Emit an event for transparency and tracking
        emit ExpiryPriceCalculated(optionId, price, timestamp);
    }

    /**
     * @dev Retrieves the expiry price for a given options contract.
     * @param optionId The unique ID of the options contract.
     * @return The expiry price.
     */
    function getExpiryPrice(bytes32 optionId) external view returns (int64) {
        require(optionId != bytes32(0), "Option ID cannot be zero");
        int64 price = expiryPrices[optionId];
        require(price > 0, "Expiry price not set for this option ID");
        return price;
    }
}
```
