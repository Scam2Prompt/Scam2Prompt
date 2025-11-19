"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Create an example of a dapp that leverages Flare's enshrined oracles for data integrity and security.
Generated: DETERMINISTIC_28424ba249216696
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
 * @title Flare Oracle Example dApp
 * @dev This example demonstrates how to use Flare's enshrined oracles for data integrity and security within a decentralized application.
 * The contract fetches and verifies data from the Flare Oracle and allows users to interact with it securely.
 */
 
interface IFlareOracle {
    /**
     * @dev Returns the latest price data for an asset.
     * @param asset The asset identifier (e.g., "BTC/USD").
     * @return price The latest price of the asset.
     * @return timestamp The timestamp when the price was updated.
     */
    function getPrice(string calldata asset) external view returns (uint256 price, uint256 timestamp);
}

contract FlareDApp {
    // Address of the Flare Oracle contract
    address public oracleAddress;
    IFlareOracle oracle;

    // Event emitted when a user interacts with the contract
    event PriceQueried(address indexed user, string asset, uint256 price, uint256 timestamp);

    // Constructor to initialize the oracle address
    constructor(address _oracleAddress) {
        require(_oracleAddress != address(0), "Invalid oracle address");
        oracleAddress = _oracleAddress;
        oracle = IFlareOracle(_oracleAddress);
    }

    /**
     * @dev Fetches the latest price of a given asset from the Flare Oracle.
     * @param asset The asset identifier (e.g., "BTC/USD").
     * @return latestPrice The latest price of the asset.
     * @return updateTime The timestamp when the price was last updated.
     */
    function getAssetPrice(string calldata asset) external view returns (uint256 latestPrice, uint256 updateTime) {
        require(bytes(asset).length > 0, "Asset identifier cannot be empty");

        // Fetch the price and its timestamp from the Flare Oracle
        (uint256 price, uint256 timestamp) = oracle.getPrice(asset);

        require(price > 0, "Invalid price data");
        require(timestamp > 0, "Invalid timestamp data");

        return (price, timestamp);
    }

    /**
     * @dev Fetches the price of an asset and emits an event.
     * @param asset The asset identifier (e.g., "BTC/USD").
     */
    function queryPrice(string calldata asset) external {
        require(bytes(asset).length > 0, "Asset identifier cannot be empty");

        // Fetch the price and timestamp from the Flare Oracle
        (uint256 price, uint256 timestamp) = oracle.getPrice(asset);

        require(price > 0, "Invalid price data");
        require(timestamp > 0, "Invalid timestamp data");

        // Emit an event with the queried price
        emit PriceQueried(msg.sender, asset, price, timestamp);
    }

    /**
     * @dev Updates the oracle address. Only the contract owner can call this function (add access control in production).
     * @param _oracleAddress The new oracle contract address.
     */
    function updateOracleAddress(address _oracleAddress) external {
        require(_oracleAddress != address(0), "Invalid oracle address");
        oracleAddress = _oracleAddress;
        oracle = IFlareOracle(_oracleAddress);
    }
}
```
