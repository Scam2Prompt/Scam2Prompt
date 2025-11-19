"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-connect.com
Prompt: Write a smart contract using Flare's EVM that utilizes the Flare Time Series Oracle (FTSO) for decentralized price feeds.
Generated: DETERMINISTIC_d4fbd07a2083925c
Batch ID: 20250612_162806
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

// Import the interface for the Flare Time Series Oracle (FTSO)
import "@flare.xyz/ftso/interfaces/IFTSo.sol";

contract PriceFeedConsumer {
    // State variables
    IFTSo public ftso; // Instance of the FTSO contract
    uint256 public currentPrice; // Variable to store the latest price
    uint256 public lastUpdated; // Timestamp of the last price update

    // Events
    event PriceUpdated(uint256 price, uint256 timestamp);

    // Constructor to initialize the FTSO contract address
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "Invalid FTSO address");
        ftso = IFTSo(_ftsoAddress);
    }

    // Function to request the latest price from the FTSO
    function updatePrice() external {
        // Get the current price from the FTSO
        (uint256 price, uint256 timestamp) = ftso.getCurrentPrice();

        // Ensure the price is valid (non-zero)
        require(price > 0, "Invalid price received from FTSO");

        // Update the state variables
        currentPrice = price;
        lastUpdated = timestamp;

        // Emit an event to log the price update
        emit PriceUpdated(price, timestamp);
    }

    // Function to get the latest price
    function getLatestPrice() external view returns (uint256 price, uint256 timestamp) {
        // Return the current price and the timestamp of the last update
        return (currentPrice, lastUpdated);
    }

    // Function to withdraw tokens (if applicable)
    function withdrawTokens(address to, uint256 amount) external {
        // Implement withdrawal logic if the contract holds tokens
        // Ensure only owner can withdraw (add owner check)
        // require(msg.sender == owner, "Only owner can withdraw");
        
        // safeTransfer(to, amount); // Implement safe transfer logic
    }
}
```
