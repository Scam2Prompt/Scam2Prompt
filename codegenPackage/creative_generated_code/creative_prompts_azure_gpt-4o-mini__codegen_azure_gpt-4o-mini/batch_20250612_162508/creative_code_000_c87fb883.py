"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: How can I integrate Pyth's real-time price feeds into my smart contract on EVM using the provided API documentation?
Generated: DETERMINISTIC_c87fb8833b78b2eb
Batch ID: 20250612_162508
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

// Importing necessary interfaces for interacting with external price feeds.
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// Define a contract to integrate Pyth's real-time price feeds
contract PythPriceFeed is Ownable {
    // Address of the Pyth price feed contract
    AggregatorV3Interface internal priceFeed;

    // Event to emit when the price is updated
    event PriceUpdated(int256 price);

    // Constructor to initialize the price feed contract
    constructor(address _priceFeedAddress) {
        require(_priceFeedAddress != address(0), "Invalid price feed address");
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    // Function to set a new price feed address, only callable by the owner
    function setPriceFeedAddress(address _newPriceFeedAddress) external onlyOwner {
        require(_newPriceFeedAddress != address(0), "Invalid price feed address");
        priceFeed = AggregatorV3Interface(_newPriceFeedAddress);
    }

    // Function to fetch the latest price from the Pyth price feed
    function getLatestPrice() external returns (int256) {
        // Fetching the latest price data
        (
            , // Timestamp is not needed
            int256 price,
            , // Answered at is not needed
            , // The round ID is not needed
            // The round ID is not needed
        ) = priceFeed.latestRoundData();

        // Emit the price updated event
        emit PriceUpdated(price);
        
        // Return the latest price
        return price;
    }

    // Function to get price feed details
    function getPriceFeedDetails() external view returns (uint80, int256, uint256, uint256, uint80) {
        return priceFeed.latestRoundData();
    }
}
```

This smart contract integrates with Pyth's price feeds via Chainlink's AggregatorV3Interface and allows the owner to update the price feed address. It includes error handling and emits events when the price is fetched.
