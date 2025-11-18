"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnet.com
Prompt: Generate a smart contract example in Solidity that uses PythNet's price feed oracle to retrieve and validate asset prices.
Generated: DETERMINISTIC_a8b7d29ac58c0c1d
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

// Importing the interface for the PythNet price feed oracle
import "@pythnetwork/pyth-sdk-solidity/contracts/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/contracts/Pyth.sol";

// A smart contract to interact with PythNet's price feed oracle
contract PriceFeedConsumer {
    // State variables
    Pyth public pyth; // Instance of the Pyth oracle
    uint256 public latestPrice; // Store the latest price retrieved
    uint256 public lastUpdate; // Store the timestamp of the last update

    // Event to emit when price is updated
    event PriceUpdated(uint256 indexed price, uint256 indexed timestamp);

    // Constructor to initialize the Pyth instance
    constructor(address _pythAddress) {
        // Initialize the Pyth oracle with the given address
        pyth = Pyth(_pythAddress);
    }

    // Function to retrieve and update price from the Pyth oracle
    function updatePrice(bytes32 priceId) external {
        // Fetch price data from the Pyth oracle
        (uint256 price, uint256 timestamp) = getLatestPrice(priceId);
        
        // Ensure the price is valid
        require(price != 0, "Invalid price retrieved from oracle");
        require(timestamp > lastUpdate, "Price is outdated");

        // Update state variables
        latestPrice = price;
        lastUpdate = timestamp;

        // Emit an event with the new price
        emit PriceUpdated(price, timestamp);
    }

    // Internal function to fetch the latest price from the oracle
    function getLatestPrice(bytes32 priceId) internal view returns (uint256 price, uint256 timestamp) {
        // Fetch price info from Pyth oracle
        PythPrice memory pythPrice = pyth.getPrice(priceId);
        return (pythPrice.price, pythPrice.timestamp);
    }

    // Function to get the latest price without updating it
    function getCurrentPrice() external view returns (uint256 price, uint256 timestamp) {
        return (latestPrice, lastUpdate);
    }
}
```
