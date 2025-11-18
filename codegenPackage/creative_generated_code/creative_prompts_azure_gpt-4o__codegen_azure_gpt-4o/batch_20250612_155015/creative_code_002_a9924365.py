"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pytheth.com
Prompt: Generate code to connect a smart contract to Pytheth's market data oracles for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_a9924365e9ef52d1
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

/**
 * @title OracleConnector
 * @dev A smart contract that connects to Pyth's market data oracles to fetch price data
 * for decentralized finance (DeFi) applications.
 */
contract OracleConnector {
    // Address of the Pyth oracle contract
    address public pythOracleAddress;

    // Mapping to store the price feeds from the oracle
    mapping(bytes32 => int256) public priceFeeds;

    // Event emitted when a price feed is updated
    event PriceUpdated(bytes32 indexed priceId, int256 price);

    /**
     * @dev Constructor to set the Pyth oracle contract address.
     * @param _pythOracleAddress The address of the deployed Pyth oracle contract.
     */
    constructor(address _pythOracleAddress) {
        require(_pythOracleAddress != address(0), "Invalid oracle address");
        pythOracleAddress = _pythOracleAddress;
    }

    /**
     * @dev External function to update the price of a specific asset from the oracle.
     * @param priceId The unique identifier for the price feed (e.g., BTC/USD).
     */
    function updatePrice(bytes32 priceId) external {
        // Call the Pyth oracle contract to fetch the latest price data
        // Note: Interface for the Pyth oracle contract must be defined elsewhere
        int256 price = IPythOracle(pythOracleAddress).getPrice(priceId);

        // Save the price data in the contract's storage
        priceFeeds[priceId] = price;

        // Emit the PriceUpdated event
        emit PriceUpdated(priceId, price);
    }

    /**
     * @dev External view function to get the latest cached price of an asset.
     * @param priceId The unique identifier for the price feed (e.g., BTC/USD).
     * @return The latest price of the requested asset.
     */
    function getLatestPrice(bytes32 priceId) external view returns (int256) {
        require(priceFeeds[priceId] != 0, "Price not available");
        return priceFeeds[priceId];
    }
}

/**
 * @dev Interface for the Pyth oracle contract.
 * This should match the oracle's contract ABI.
 */
interface IPythOracle {
    function getPrice(bytes32 priceId) external view returns (int256);
}
```

This Solidity code connects to Pyth's market data oracles by using an interface (`IPythOracle`) provided for the oracle contract. It fetches price data for specific assets and caches it in the contract storage. It adheres to best practices, including input validation, error handling, and event logging.
