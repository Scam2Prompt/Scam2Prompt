"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythbtc.com
Prompt: Demonstrate how to configure a smart contract to use Pyth price feed oracles for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_1fc6c012431fa2a4
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

// Importing the Pyth price feed interface
import "@pythnetwork/pyth-contracts/PriceFeed.sol";

// Define the contract
contract DeFiPriceFeed {
    // State variable to hold the price feed contract address
    PriceFeed public priceFeed;

    // Event to emit when the price is updated
    event PriceUpdated(int64 price, uint64 publishTime);

    // Constructor to set the Pyth price feed contract address
    constructor(address _priceFeedAddress) {
        require(_priceFeedAddress != address(0), "Invalid price feed address");
        priceFeed = PriceFeed(_priceFeedAddress);
    }

    // Function to fetch the latest price from the Pyth oracle
    function getLatestPrice() public returns (int64, uint64) {
        // Fetching price info from the Pyth price feed
        (int64 price, uint64 publishTime) = priceFeed.getCurrentPrice();

        // Emit an event with the updated price
        emit PriceUpdated(price, publishTime);

        // Return the price and publish time
        return (price, publishTime);
    }

    // Function to check if the price is updated recently
    function isPriceStale(uint64 maxStaleDuration) public view returns (bool) {
        ( , uint64 publishTime) = priceFeed.getCurrentPrice();
        
        // Comparing current time with the publish time to determine staleness
        return (block.timestamp > publishTime + maxStaleDuration);
    }
}
```

**Note:** Ensure that you have the Pyth price feed contracts imported correctly and that your development environment is set up to compile and deploy Solidity contracts.
