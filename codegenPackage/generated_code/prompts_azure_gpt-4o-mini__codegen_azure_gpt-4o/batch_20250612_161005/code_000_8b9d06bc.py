"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: Write a smart contract that utilizes the Flare Time Series Oracle to fetch decentralized price feeds for a DeFi application.
Generated: DETERMINISTIC_8b9d06bc47e7599b
Batch ID: 20250612_161005
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

/**
 * @title DeFiPriceFeed
 * @dev A smart contract that utilizes the Flare Time Series Oracle (FTSO) to fetch decentralized price feeds.
 */
contract DeFiPriceFeed {
    // Address of the Flare Time Series Oracle (FTSO)
    address public ftsoAddress;

    // Mapping to store the latest price data for different assets
    mapping(string => uint256) public assetPrices;

    // Event emitted when a price is updated
    event PriceUpdated(string asset, uint256 price);

    /**
     * @dev Constructor to initialize the FTSO address.
     * @param _ftsoAddress Address of the Flare Time Series Oracle.
     */
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "FTSO address cannot be zero");
        ftsoAddress = _ftsoAddress;
    }

    /**
     * @dev Fetches the latest price for a given asset from the FTSO.
     * @param asset Symbol of the asset (e.g., "BTC", "ETH").
     */
    function fetchPrice(string memory asset) external {
        require(bytes(asset).length > 0, "Asset symbol cannot be empty");

        // Interface to interact with the FTSO
        IFTSO ftso = IFTSO(ftsoAddress);

        // Fetch the latest price from the FTSO
        (uint256 price, uint256 timestamp) = ftso.getCurrentPrice(asset);

        // Ensure the price is valid
        require(price > 0, "Invalid price fetched from FTSO");

        // Update the asset price in the contract
        assetPrices[asset] = price;

        // Emit the PriceUpdated event
        emit PriceUpdated(asset, price);
    }

    /**
     * @dev Retrieves the latest price for a given asset stored in the contract.
     * @param asset Symbol of the asset (e.g., "BTC", "ETH").
     * @return price Latest price of the asset.
     */
    function getPrice(string memory asset) external view returns (uint256 price) {
        require(bytes(asset).length > 0, "Asset symbol cannot be empty");
        price = assetPrices[asset];
        require(price > 0, "Price not available for the asset");
    }
}

/**
 * @dev Interface for the Flare Time Series Oracle (FTSO).
 */
interface IFTSO {
    /**
     * @dev Returns the current price and timestamp for a given asset.
     * @param asset Symbol of the asset (e.g., "BTC", "ETH").
     * @return price Current price of the asset.
     * @return timestamp Timestamp of the price data.
     */
    function getCurrentPrice(string memory asset) external view returns (uint256 price, uint256 timestamp);
}
```
