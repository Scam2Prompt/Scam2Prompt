"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Write a smart contract using Flare's EVM that utilizes the Flare Time Series Oracle (FTSO) for decentralized price feeds.
Generated: DETERMINISTIC_d4fbd07a2083925c
Batch ID: 20250612_162806
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
 * @title PriceFeedConsumer
 * @dev A smart contract that interacts with Flare's Time Series Oracle (FTSO) to fetch decentralized price feeds.
 */
contract PriceFeedConsumer {
    // Address of the FTSO contract
    address public ftsoAddress;

    // Event emitted when the price is successfully fetched
    event PriceFetched(string indexed symbol, uint256 price, uint256 timestamp);

    /**
     * @dev Constructor to initialize the FTSO address.
     * @param _ftsoAddress The address of the Flare Time Series Oracle contract.
     */
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "FTSO address cannot be zero");
        ftsoAddress = _ftsoAddress;
    }

    /**
     * @dev Fetches the latest price for a given symbol from the FTSO.
     * @param symbol The symbol for which the price is requested (e.g., "BTC/USD").
     * @return price The latest price for the given symbol.
     * @return timestamp The timestamp of the price data.
     */
    function getLatestPrice(string memory symbol) public returns (uint256 price, uint256 timestamp) {
        // Interface for the FTSO contract
        IFTSO ftso = IFTSO(ftsoAddress);

        // Fetch the price and timestamp from the FTSO
        (price, timestamp) = ftso.getCurrentPrice(symbol);

        // Emit an event for logging purposes
        emit PriceFetched(symbol, price, timestamp);

        return (price, timestamp);
    }

    /**
     * @dev Updates the FTSO address. Can be used for contract upgrades or changes.
     * @param _newFtsoAddress The new address of the Flare Time Series Oracle contract.
     */
    function updateFtsoAddress(address _newFtsoAddress) external {
        require(_newFtsoAddress != address(0), "FTSO address cannot be zero");
        ftsoAddress = _newFtsoAddress;
    }
}

/**
 * @dev Interface for the Flare Time Series Oracle (FTSO).
 * This interface defines the methods that the FTSO contract exposes.
 */
interface IFTSO {
    /**
     * @dev Returns the current price and timestamp for a given symbol.
     * @param symbol The symbol for which the price is requested (e.g., "BTC/USD").
     * @return price The latest price for the given symbol.
     * @return timestamp The timestamp of the price data.
     */
    function getCurrentPrice(string memory symbol) external view returns (uint256 price, uint256 timestamp);
}
```
