"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarenetdrops.com
Prompt: Provide a step-by-step guide for integrating Flare's enshrined oracles into a decentralized application (dApp) built on an EVM-compatible blockchain.
Generated: DETERMINISTIC_379114ed6dc544cf
Batch ID: 20250612_154752
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
 * @title Flare Oracle Integration Example
 * @dev Demonstrates how to integrate Flare's enshrined oracle into a dApp on an EVM-compatible blockchain.
 * This contract fetches price data from the Flare oracle and uses the data in a decentralized application.
 */

interface IFlareOracle {
    /**
     * @dev Interface for Flare's enshrined oracle.
     * @param token Symbol or identifier of the asset to query.
     * @return price The latest price of the asset retrieved from Flare's oracle.
     */
    function getPrice(string memory token) external view returns (uint256 price);
}

contract FlareOracleIntegration {
    // Address of the Flare oracle contract
    address public flareOracleAddress;

    // Mapping to store prices of various tokens
    mapping(string => uint256) public tokenPrices;

    // Event emitted when a token's price is updated
    event TokenPriceUpdated(string token, uint256 price);

    /**
     * @dev Contract constructor.
     * Sets the address of the Flare oracle to interact with.
     * @param _flareOracleAddress The address of the Flare oracle contract.
     */
    constructor(address _flareOracleAddress) {
        require(_flareOracleAddress != address(0), "Invalid oracle address");
        flareOracleAddress = _flareOracleAddress;
    }

    /**
     * @dev Fetches the latest price of the specified token from the Flare oracle.
     * @param token Symbol or identifier of the token (e.g., "BTC", "ETH").
     */
    function updateTokenPrice(string memory token) external {
        // Interface instance for the Flare oracle
        IFlareOracle flareOracle = IFlareOracle(flareOracleAddress);

        // Fetch the price using Flare oracle's getPrice function
        uint256 price = flareOracle.getPrice(token);

        // Update the local mapping with the fetched price
        tokenPrices[token] = price;

        // Emit an event to log the price update
        emit TokenPriceUpdated(token, price);
    }

    /**
     * @dev Retrieves the stored price of a token.
     * @param token Symbol or identifier of the token.
     * @return price The latest price of the token in the local storage.
     */
    function getStoredTokenPrice(string memory token) external view returns (uint256) {
        return tokenPrices[token];
    }
}
```
