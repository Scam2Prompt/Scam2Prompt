"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Write a Solidity smart contract that integrates the Pyth Network's price feed to retrieve the BTC/USD price using the `IPyth` interface and `PythStructs`.
Generated: DETERMINISTIC_8cb5ac22d1b4eb94
Batch ID: 20250612_153648
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

// Import the Pyth Network interface and structures
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

/// @title Pyth Price Feed Consumer
/// @notice A smart contract to fetch BTC/USD prices using the Pyth Network
contract PythPriceFeedConsumer {
    // Address of the deployed Pyth contract
    IPyth public pyth;

    // Pyth price feed ID for BTC/USD
    bytes32 public btcUsdPriceId;

    /// @notice Emitted when the price is fetched successfully
    /// @param price The latest BTC/USD price
    /// @param timestamp The timestamp of the price update
    event PriceFetched(int64 price, uint64 timestamp);

    /// @notice Constructor to set the Pyth contract address and BTC/USD price ID
    /// @param _pythContract Address of the deployed Pyth contract
    /// @param _btcUsdPriceId Pyth price ID for BTC/USD
    constructor(address _pythContract, bytes32 _btcUsdPriceId) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        require(_btcUsdPriceId != bytes32(0), "Invalid price ID");

        pyth = IPyth(_pythContract);
        btcUsdPriceId = _btcUsdPriceId;
    }

    /// @notice Fetch the latest BTC/USD price using the Pyth Network
    /// @dev Ensure the calling address has sufficient gas to execute the function
    /// @return price The latest BTC/USD price as an integer
    /// @return timestamp The timestamp of the price update
    function getLatestBtcUsdPrice()
        external
        view
        returns (int64 price, uint64 timestamp)
    {
        // Get the price feed information
        PythStructs.Price memory priceFeed = pyth.getPrice(btcUsdPriceId);

        // Emit an event for transparency
        emit PriceFetched(priceFeed.price, priceFeed.publishTime);

        // Return the price and timestamp
        return (priceFeed.price, priceFeed.publishTime);
    }

    /// @notice Fetch the BTC/USD price and verify if it is up-to-date
    /// @dev Custom verification logic can be added to ensure price validity
    /// @param maxAge Seconds since the last price update for validity
    /// @return price The latest BTC/USD price if valid
    /// @return isValid Whether the price is up-to-date
    function getVerifiedBtcUsdPrice(uint64 maxAge)
        external
        view
        returns (int64 price, bool isValid)
    {
        // Get the price feed information
        PythStructs.Price memory priceFeed = pyth.getPrice(btcUsdPriceId);

        // Verify the price age
        uint64 currentTime = uint64(block.timestamp);
        bool valid = (currentTime - priceFeed.publishTime) <= maxAge;

        // Return the price and validity
        return (priceFeed.price, valid);
    }
}
```
