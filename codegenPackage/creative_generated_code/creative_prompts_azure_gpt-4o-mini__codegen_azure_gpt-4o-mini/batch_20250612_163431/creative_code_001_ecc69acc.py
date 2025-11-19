"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-staking.pages.dev
Prompt: Write a code example for a Solidity contract that utilizes Pyth's pull oracle to fetch the latest BTC/USD price.
Generated: DETERMINISTIC_ecc69acc4895b010
Batch ID: 20250612_163431
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

// Importing the Pyth contract interface
import "@pythnetwork/pyth-sdk-solidity/contracts/interfaces/IPyth.sol";

// Define a contract to fetch BTC/USD price using Pyth's pull oracle
contract BTCPriceFetcher {
    // Declare state variables
    IPyth public pyth; // Pyth interface to interact with the oracle
    bytes32 public btcPriceId; // The price id for BTC/USD

    // Event to emit the latest BTC price
    event PriceUpdated(int64 price);

    // Constructor to initialize the Pyth oracle and BTC price ID
    constructor(address _pythAddress, bytes32 _btcPriceId) {
        pyth = IPyth(_pythAddress); // Initialize Pyth contract address
        btcPriceId = _btcPriceId;   // Set the BTC/USD price ID
    }

    // Function to fetch the latest BTC/USD price
    function updatePrice() external {
        // Fetch the price data from Pyth
        (int64 price, , , ) = pyth.getPrice(btcPriceId);
        
        // Check if the price is valid
        require(price > 0, "Invalid price received");

        // Emit the updated price
        emit PriceUpdated(price);
    }

    // Function to retrieve the latest price without updating
    function getLatestPrice() external view returns (int64) {
        (int64 price, , , ) = pyth.getPrice(btcPriceId);
        
        // Ensure the price is valid
        require(price > 0, "Invalid price received");

        return price; // Return the latest BTC/USD price
    }
}
```

**Note:** Ensure you have the correct Pyth SDK version installed in your project to use this contract.
