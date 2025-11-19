"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnet.com
Prompt: How do I use Pyth Network's price feed data in a Solidity smart contract?
Generated: DETERMINISTIC_002e4ea96f6e7b04
Batch ID: 20250612_162311
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

// Importing the interface for the Pyth price feed
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Pyth Network price feed
interface IPyth {
    function getPrice(bytes32 priceId) external view returns (int64 price, uint64 conf);
}

contract PriceFeedConsumer is Ownable {
    // Pyth price feed contract address
    IPyth public pyth;

    // Mapping to store price data
    mapping(bytes32 => int64) public prices;

    // Event to log price updates
    event PriceUpdated(bytes32 indexed priceId, int64 price);

    // Constructor to set the Pyth price feed address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    // Function to update price for a given priceId
    function updatePrice(bytes32 priceId) external onlyOwner {
        // Fetch price from Pyth network
        (int64 price, uint64 conf) = pyth.getPrice(priceId);

        // Check for valid price
        require(price > 0, "Invalid price received");

        // Update the price mapping
        prices[priceId] = price;

        // Emit price update event
        emit PriceUpdated(priceId, price);
    }

    // Function to retrieve the price for a given priceId
    function getPrice(bytes32 priceId) external view returns (int64) {
        // Return the price from the mapping
        return prices[priceId];
    }
}
```
