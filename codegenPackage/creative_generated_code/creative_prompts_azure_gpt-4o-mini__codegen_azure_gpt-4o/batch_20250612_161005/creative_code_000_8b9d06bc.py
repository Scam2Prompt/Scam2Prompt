"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Write a smart contract that utilizes the Flare Time Series Oracle to fetch decentralized price feeds for a DeFi application.
Generated: DETERMINISTIC_8b9d06bc47e7599b
Batch ID: 20250612_161005
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
 * @title PriceFeedConsumer
 * @dev This contract interacts with the Flare Time Series Oracle (FTSO) to fetch decentralized price feeds.
 */
contract PriceFeedConsumer {
    // Address of the Flare Time Series Oracle
    address public ftsoOracleAddress;

    // Event emitted when a price is successfully fetched
    event PriceFetched(string indexed assetSymbol, uint256 price);

    // Event emitted when an error occurs during price fetching
    event ErrorFetchingPrice(string indexed assetSymbol, string reason);

    /**
     * @dev Constructor for setting the FTSO Oracle address.
     * @param _ftsoOracleAddress The address of the Flare Time Series Oracle.
     */
    constructor(address _ftsoOracleAddress) {
        require(_ftsoOracleAddress != address(0), "FTSO Oracle address cannot be zero.");
        ftsoOracleAddress = _ftsoOracleAddress;
    }

    /**
     * @dev Fetches the price of a given asset symbol from the Flare Time Series Oracle.
     * @param assetSymbol The symbol of the asset to fetch the price for (e.g., "BTC", "ETH").
     * @return The latest price for the asset.
     */
    function getPrice(string memory assetSymbol) public returns (uint256) {
        require(bytes(assetSymbol).length > 0, "Asset symbol cannot be empty.");

        try IFTSO(ftsoOracleAddress).getCurrentPrice(assetSymbol) returns (uint256 price) {
            emit PriceFetched(assetSymbol, price); // Emit event for successful price fetch
            return price; // Return the fetched price
        } catch Error(string memory reason) {
            emit ErrorFetchingPrice(assetSymbol, reason); // Emit event for error
            revert(reason); // Revert the transaction with the error reason
        } catch {
            emit ErrorFetchingPrice(assetSymbol, "Unknown error occurred."); // Emit generic error event
            revert("Unknown error occurred."); // Revert transaction with generic error
        }
    }
}

/**
 * @dev Interface for the Flare Time Series Oracle (FTSO).
 * This is used to interact with the FTSO contract to fetch price feeds.
 */
interface IFTSO {
    /**
     * @dev Fetches the current price for a given asset symbol.
     * @param assetSymbol The symbol of the asset (e.g., "BTC", "ETH").
     * @return The latest price of the asset.
     */
    function getCurrentPrice(string memory assetSymbol) external view returns (uint256);
}
```
