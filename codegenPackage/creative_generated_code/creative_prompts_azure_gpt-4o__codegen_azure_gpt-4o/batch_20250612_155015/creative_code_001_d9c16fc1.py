"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythget.com
Prompt: How can I integrate Pythget's market data oracles into a smart contract to ensure accurate and decentralized price feeds?
Generated: DETERMINISTIC_d9c16fc10511d123
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
 * @title PriceFeedConsumer
 * @dev Smart contract to integrate with Pythget's market data oracles.
 * This contract fetches accurate and decentralized price feeds from Pythget.
 */
interface IPythgetOracle {
    /**
     * @dev Function to get the latest price of an asset.
     * @param asset The asset symbol (e.g., "ETH/USD").
     * @return price The latest price of the asset in 8 decimal places.
     */
    function getLatestPrice(string memory asset) external view returns (int256 price);

    /**
     * @dev Function to get the timestamp of the last price update.
     * @param asset The asset symbol (e.g., "ETH/USD").
     * @return timestamp The UNIX timestamp of the last price update.
     */
    function getLastUpdatedTimestamp(string memory asset) external view returns (uint256 timestamp);
}

contract PriceFeedConsumer {
    // Address of the deployed Pythget Oracle contract
    address public oracleAddress;

    // Modifiable by the owner; ensures flexibility in changing the oracle
    address private owner;

    // Event to notify retrieval of price data
    event PriceRetrieved(string asset, int256 price, uint256 timestamp);

    /**
     * @dev Sets the Pythget Oracle contract address during deployment.
     * @param _oracleAddress Address of the deployed Pythget Oracle contract.
     */
    constructor(address _oracleAddress) {
        require(_oracleAddress != address(0), "Invalid oracle address");
        oracleAddress = _oracleAddress;
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to update the oracle address.
     * @param _newOracleAddress Address of the new Pythget Oracle contract.
     */
    function updateOracleAddress(address _newOracleAddress) external {
        require(msg.sender == owner, "Only the owner can update the oracle address");
        require(_newOracleAddress != address(0), "Invalid oracle address");
        oracleAddress = _newOracleAddress;
    }

    /**
     * @dev Fetches the latest price of an asset from the Pythget Oracle.
     * @param asset The asset symbol (e.g., "ETH/USD").
     * @return price The latest price of the asset.
     * @return timestamp The last updated timestamp of the price.
     */
    function getPrice(string memory asset) external view returns (int256 price, uint256 timestamp) {
        IPythgetOracle oracle = IPythgetOracle(oracleAddress);
        int256 fetchedPrice = oracle.getLatestPrice(asset);
        uint256 lastUpdated = oracle.getLastUpdatedTimestamp(asset);
        
        return (fetchedPrice, lastUpdated);
    }

    /**
     * @dev Fetches the latest price and emits an event with the details.
     * @param asset The asset symbol (e.g., "ETH/USD").
     */
    function fetchAndEmitPrice(string memory asset) external {
        IPythgetOracle oracle = IPythgetOracle(oracleAddress);
        int256 fetchedPrice = oracle.getLatestPrice(asset);
        uint256 lastUpdated = oracle.getLastUpdatedTimestamp(asset);

        emit PriceRetrieved(asset, fetchedPrice, lastUpdated);
    }
}
```

Notes:
- Replace `IPythgetOracle`'s method signatures with actual Pythget implementation details if available.
- Ensure the oracle contract address is correctly set and corresponds to the deployed Pythget contract.
