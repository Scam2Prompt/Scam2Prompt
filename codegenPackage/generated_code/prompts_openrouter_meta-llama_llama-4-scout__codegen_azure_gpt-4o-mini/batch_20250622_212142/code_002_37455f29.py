"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: "Generate a smart contract code on Flare Network that uses the Flare Time Series Oracle (FTSO) for decentralized price and data feeds."
Generated: DETERMINISTIC_37455f2997b3d372
Batch ID: 20250622_212142
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
import "@flarenetwork/ftso-contracts/contracts/interfaces/IFTSO.sol";

// Smart contract to utilize the Flare Time Series Oracle for price feeds
contract PriceConsumer {
    // Address of the FTSO contract
    IFTSO public ftso;

    // Event to emit when a new price is fetched
    event PriceUpdated(uint256 price);

    // Constructor to initialize the FTSO contract address
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "Invalid FTSO address");
        ftso = IFTSO(_ftsoAddress);
    }

    // Function to fetch the latest price from the FTSO
    function getLatestPrice() external returns (uint256) {
        // Fetching the latest price from the FTSO
        uint256 price = ftso.getCurrentPrice();
        
        // Emitting the price update event
        emit PriceUpdated(price);
        
        return price;
    }

    // Function to fetch the price with error handling
    function safeGetLatestPrice() external returns (uint256) {
        // Attempt to fetch the latest price
        try ftso.getCurrentPrice() returns (uint256 price) {
            emit PriceUpdated(price);
            return price;
        } catch {
            // Handle the error gracefully
            revert("Failed to fetch the latest price from FTSO");
        }
    }
}
```
