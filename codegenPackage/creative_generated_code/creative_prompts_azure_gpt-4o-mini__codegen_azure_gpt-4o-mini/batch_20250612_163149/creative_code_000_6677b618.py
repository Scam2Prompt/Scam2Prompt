"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Write a smart contract using the Flare blockchain that utilizes the Flare Time Series Oracle (FTSO) for decentralized price feeds.
Generated: DETERMINISTIC_6677b618f73717fa
Batch ID: 20250612_163149
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

// Importing the interface for the Flare Time Series Oracle (FTSO)
import "@flarenetwork/flare-oracle/contracts/IFTSO.sol";

// Smart contract for interacting with the Flare Time Series Oracle (FTSO)
contract PriceFeedConsumer {
    
    // State variable to hold the FTSO contract address
    IFTSO public ftso;

    // Event to be emitted when a new price is fetched
    event PriceUpdated(uint256 price);

    // Constructor to set the FTSO contract address
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "Invalid FTSO address");
        ftso = IFTSO(_ftsoAddress);
    }

    // Function to fetch the current price from the FTSO
    function getCurrentPrice() external returns (uint256) {
        // Fetching the price from the FTSO
        uint256 price = ftso.getCurrentPrice();
        
        // Emitting event after price retrieval
        emit PriceUpdated(price);
        
        return price;
    }

    // Function to fetch the price with error handling
    function safeGetCurrentPrice() external returns (uint256) {
        // Attempt to fetch the price with a try-catch for error handling
        try ftso.getCurrentPrice() returns (uint256 price) {
            emit PriceUpdated(price);
            return price;
        } catch {
            // If fetching fails, revert with a custom error message
            revert("Failed to fetch price from FTSO");
        }
    }

    // Function to update FTSO address if needed
    function updateFTSOAddress(address _newFTSOAddress) external {
        require(_newFTSOAddress != address(0), "Invalid new FTSO address");
        // Updating the FTSO address
        ftso = IFTSO(_newFTSOAddress);
    }
}
```
