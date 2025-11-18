"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Write a Solidity smart contract that integrates Pyth Network's price feed for BTC/USD using the `pyth-sdk-solidity` library. Include functionality to fetch and update the price feed on-demand.
Generated: DETERMINISTIC_9791883d7d012ac6
Batch ID: 20250612_153246
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

// Import the Pyth SDK for Solidity
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract BTCUSDPriceFeed {
    // Address of the Pyth contract on the respective network
    IPyth public pyth; 
    
    // Store the price ID for BTC/USD (this will be specific to the Pyth network deployment)
    bytes32 public priceFeedId;

    // Event for logging price updates
    event PriceUpdated(int64 price, uint64 publishTime);

    // Constructor to initialize the Pyth contract and BTC/USD price feed ID
    constructor(address _pythContract, bytes32 _priceFeedId) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        require(_priceFeedId != bytes32(0), "Invalid price feed ID");

        pyth = IPyth(_pythContract);
        priceFeedId = _priceFeedId;
    }

    /**
     * @notice Fetch the latest BTC/USD price from the Pyth price feed.
     * @dev Requires the caller to provide the update data (to ensure the price is up-to-date).
     * @param updateData The update data fetched from the off-chain Pyth network API.
     */
    function updatePrice(bytes[] calldata updateData) external payable {
        // Update the price feed using Pyth's updatePriceFeeds function
        pyth.updatePriceFeeds{value: msg.value}(updateData);

        // Fetch the latest price info for the BTC/USD pair
        PythStructs.Price memory priceData = pyth.getPrice(priceFeedId);

        // Emit the updated price and its publish time
        emit PriceUpdated(priceData.price, priceData.publishTime);
    }

    /**
     * @notice Retrieves the latest BTC/USD price without updating the feed.
     * @return price The latest BTC/USD price.
     * @return publishTime The timestamp of when the price was published.
     */
    function getLatestPrice() external view returns (int64 price, uint64 publishTime) {
        PythStructs.Price memory priceData = pyth.getPriceNoOlderThan(priceFeedId, 60); // Allow max 60 seconds old price
        return (priceData.price, priceData.publishTime);
    }

    /**
     * @notice Receive function to allow the contract to accept ETH for Pyth fees.
     */
    receive() external payable {}

    /**
     * @notice Fallback function to allow the contract to accept ETH.
     */
    fallback() external payable {}
}
```

Make sure to replace `@pythnetwork/pyth-sdk-solidity/IPyth.sol` with the actual import path for the Pyth library based on your project setup, and use the appropriate `priceFeedId` for the BTC/USD pair in the Pyth network deployment you're targeting.
