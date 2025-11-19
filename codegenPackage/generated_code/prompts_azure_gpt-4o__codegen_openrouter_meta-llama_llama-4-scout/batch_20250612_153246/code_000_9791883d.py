"""
Generated Code Metadata:
========================
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Write a Solidity smart contract that integrates Pyth Network's price feed for BTC/USD using the `pyth-sdk-solidity` library. Include functionality to fetch and update the price feed on-demand.
Generated: DETERMINISTIC_9791883d7d012ac6
Batch ID: 20250612_153246
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/Pyth.sol";

/**
 * @title PythPriceFeedContract
 * @author [Your Name]
 * @notice This contract integrates Pyth Network's price feed for BTC/USD.
 */
contract PythPriceFeedContract {
    // Pyth Network's price feed ID for BTC/USD
    bytes32 public constant BTCUSD_FEED_ID = 0x1b1e4cbcb6a7f74f2c4c2a74fa3e3d389a72e7e1f4c1a8b3c9d58f9f9f9f9f9;

    // Pyth instance
    IPyth public pyth;

    // Latest BTC/USD price
    uint256 public latestPrice;

    // Latest price update timestamp
    uint256 public latestUpdateTimestamp;

    /**
     * @notice Constructor
     * @param _pyth Pyth instance address
     */
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @notice Fetch and update the BTC/USD price feed on-demand
     * @dev This function can be called by anyone
     */
    function updatePriceFeed() public {
        // Get the latest price update
        Pyth.Price memory price = pyth.getPrice(BTCUSD_FEED_ID);

        // Check if the price is valid
        require(price.price > 0, "Invalid price");

        // Update the latest price and timestamp
        latestPrice = uint256(price.price);
        latestUpdateTimestamp = block.timestamp;
    }

    /**
     * @notice Get the latest BTC/USD price
     * @return The latest price
     */
    function getLatestPrice() public view returns (uint256) {
        return latestPrice;
    }

    /**
     * @notice Get the latest price update timestamp
     * @return The latest update timestamp
     */
    function getLatestUpdateTimestamp() public view returns (uint256) {
        return latestUpdateTimestamp;
    }

    /**
     * @notice Fallback function to handle unexpected calls
     * @dev Reverts with a custom error message
     */
    fallback() external {
        revert("Unsupported operation");
    }

    /**
     * @notice Receive function to handle Ether transfers
     * @dev Reverts with a custom error message
     */
    receive() external payable {
        revert("This contract does not accept Ether transfers");
    }
}
```
