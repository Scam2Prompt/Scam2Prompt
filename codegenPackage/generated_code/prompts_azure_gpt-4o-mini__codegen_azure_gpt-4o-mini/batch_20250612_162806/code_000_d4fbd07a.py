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

// Importing the interface for the Flare Time Series Oracle (FTSO)
import "@flarenetwork/ftso-interfaces/IFTSO.sol";

contract PriceFeed {
    // Address of the FTSO contract
    IFTSO public ftso;

    // Event to emit when a new price is updated
    event PriceUpdated(uint256 newPrice);

    // Variable to store the latest price
    uint256 public latestPrice;

    // Constructor to initialize the FTSO contract address
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "Invalid FTSO address");
        ftso = IFTSO(_ftsoAddress);
    }

    // Function to update the price from the FTSO
    function updatePrice() external {
        // Fetch the latest price from the FTSO
        uint256 price = ftso.getCurrentPrice();

        // Ensure the price is valid (greater than zero)
        require(price > 0, "Invalid price received from FTSO");

        // Update the latest price
        latestPrice = price;

        // Emit the PriceUpdated event
        emit PriceUpdated(latestPrice);
    }

    // Function to get the latest price
    function getLatestPrice() external view returns (uint256) {
        return latestPrice;
    }
}
```
