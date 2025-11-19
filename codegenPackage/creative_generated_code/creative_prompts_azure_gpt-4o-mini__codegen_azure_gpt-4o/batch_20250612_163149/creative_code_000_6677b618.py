"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Write a smart contract using the Flare blockchain that utilizes the Flare Time Series Oracle (FTSO) for decentralized price feeds.
Generated: DETERMINISTIC_6677b618f73717fa
Batch ID: 20250612_163149
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
 * @title PriceConsumer
 * @dev A smart contract that interacts with the Flare Time Series Oracle (FTSO)
 *      to retrieve decentralized price feeds.
 */
contract PriceConsumer {

    // Address of the Flare Time Series Oracle (FTSO) provider
    IFTSO immutable ftsoProvider;

    // Event to log price updates
    event PriceUpdated(string indexed assetSymbol, uint256 price, uint256 timestamp);

    /**
     * @dev Interface for interacting with the Flare Time Series Oracle (FTSO).
     */
    interface IFTSO {
        function getCurrentPrice(string memory symbol) external view returns (uint256 price, uint256 timestamp);
    }

    /**
     * @dev Constructor to initialize the contract with the FTSO provider address.
     * @param _ftsoProvider The address of the deployed FTSO contract.
     */
    constructor(address _ftsoProvider) {
        require(_ftsoProvider != address(0), "FTSO provider address cannot be zero");
        ftsoProvider = IFTSO(_ftsoProvider);
    }

    /**
     * @dev Fetch current price for a given asset symbol from the FTSO.
     * @param assetSymbol The symbol of the asset (e.g., "BTC", "ETH").
     * @return price The current price of the asset in USD.
     * @return timestamp The timestamp of when the price was fetched.
     */
    function getPrice(string memory assetSymbol) external view returns (uint256 price, uint256 timestamp) {
        require(bytes(assetSymbol).length > 0, "Asset symbol cannot be empty");

        // Fetch current price from the FTSO
        (price, timestamp) = ftsoProvider.getCurrentPrice(assetSymbol);
        require(price > 0, "Price must be greater than zero");

        return (price, timestamp);
    }

    /**
     * @dev Fetch current price and emit an event for a given asset symbol.
     * @param assetSymbol The symbol of the asset (e.g., "BTC", "ETH").
     */
    function fetchAndLogPrice(string memory assetSymbol) external {
        require(bytes(assetSymbol).length > 0, "Asset symbol cannot be empty");

        // Fetch current price from the FTSO
        (uint256 price, uint256 timestamp) = ftsoProvider.getCurrentPrice(assetSymbol);
        require(price > 0, "Price must be greater than zero");

        // Emit an event with the price information
        emit PriceUpdated(assetSymbol, price, timestamp);
    }
}
```
