"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-connect.com
Prompt: Write a smart contract using Flare's EVM platform that integrates the Flare Time Series Oracle (FTSO) to fetch decentralized price data for a cryptocurrency trading application.
Generated: DETERMINISTIC_766f2c7a9c5b561b
Batch ID: 20250612_153848
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
 * @title FTSOPriceFetcher
 * @dev A smart contract to fetch decentralized price data from Flare Time Series Oracle (FTSO).
 *      This contract is designed for integration with a cryptocurrency trading application.
 */
contract FTSOPriceFetcher {
    // Address of the FTSO manager contract on Flare's EVM platform
    address public ftsoManager;

    // Event emitted when a price is fetched successfully
    event PriceFetched(string symbol, uint256 price, uint256 timestamp);

    // Modifier to ensure address inputs are not zero
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to set the FTSO manager address.
     * @param _ftsoManager Address of the FTSO manager contract.
     */
    constructor(address _ftsoManager) validAddress(_ftsoManager) {
        ftsoManager = _ftsoManager;
    }

    /**
     * @dev Interface to interact with the FTSO manager contract.
     */
    interface IFTSOManager {
        function getCurrentPrice(string calldata symbol)
            external
            view
            returns (uint256 price, uint256 timestamp);
    }

    /**
     * @dev Function to fetch the current price for a given symbol from FTSO.
     * @param symbol The symbol of the cryptocurrency (e.g., "BTC", "ETH").
     * @return price The current price of the cryptocurrency.
     * @return timestamp The timestamp of the price update.
     */
    function fetchPrice(string calldata symbol)
        external
        view
        returns (uint256 price, uint256 timestamp)
    {
        // Ensure the symbol is not empty
        require(bytes(symbol).length > 0, "Symbol cannot be empty");

        IFTSOManager ftso = IFTSOManager(ftsoManager);

        // Attempt to fetch the price from the FTSO manager
        try ftso.getCurrentPrice(symbol) returns (
            uint256 fetchedPrice,
            uint256 fetchedTimestamp
        ) {
            // Emit a success event
            emit PriceFetched(symbol, fetchedPrice, fetchedTimestamp);

            // Return the price and timestamp
            return (fetchedPrice, fetchedTimestamp);
        } catch {
            // Revert if fetching price fails
            revert("Failed to fetch price from FTSO");
        }
    }

    /**
     * @dev Function to update the FTSO manager address.
     * @param _ftsoManager The new FTSO manager address.
     */
    function updateFTSOManager(address _ftsoManager) external validAddress(_ftsoManager) {
        ftsoManager = _ftsoManager;
    }
}
```
