"""
Generated Code Metadata:
========================
Original URL: https://pythcall.com
Prompt: Generate code for a smart contract that utilizes Pyth Network's price feed oracles to retrieve and process cryptocurrency price data.
Generated: DETERMINISTIC_8f9f84c2a0dbf9e3
Batch ID: 20250612_155024
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract PythPriceConsumer {
    IPyth public pyth;
    bytes32 public priceFeedId;
    
    // Events
    event PriceUpdated(int64 price, uint64 publishTime);
    event PriceFeedIdUpdated(bytes32 newPriceFeedId);
    
    // Errors
    error InvalidPriceFeed();
    error PriceUpdateFailed();
    error StalePrice();
    
    /**
     * @dev Constructor initializes the Pyth contract and price feed ID
     * @param _pyth The address of the Pyth oracle contract
     * @param _priceFeedId The ID of the price feed to track
     */
    constructor(address _pyth, bytes32 _priceFeedId) {
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }
    
    /**
     * @dev Updates the price feed ID
     * @param newPriceFeedId The new price feed ID to use
     */
    function updatePriceFeedId(bytes32 newPriceFeedId) external {
        if (newPriceFeedId == bytes32(0)) {
            revert InvalidPriceFeed();
        }
        priceFeedId = newPriceFeedId;
        emit PriceFeedIdUpdated(newPriceFeedId);
    }
    
    /**
     * @dev Fetches the latest price from Pyth network
     * @param maxAge Maximum acceptable age of the price in seconds
     * @return price The current price
     * @return publishTime When the price was published
     */
    function getLatestPrice(uint64 maxAge) public returns (int64, uint64) {
        // Get the update fee for the price feed
        bytes[] memory updateData = new bytes[](1);
        updateData[0] = pyth.createPriceFeedUpdateData(priceFeedId);
        
        // Update the price data (this requires paying a fee)
        try pyth.updatePriceFeeds{value: msg.value}(updateData) {
            // Fetch the latest price after update
            PythStructs.Price memory priceData = pyth.getPrice(priceFeedId);
            
            // Check if price is stale
            if (block.timestamp - priceData.publishTime > maxAge) {
                revert StalePrice();
            }
            
            emit PriceUpdated(priceData.price, priceData.publishTime);
            return (priceData.price, priceData.publishTime);
        } catch {
            revert PriceUpdateFailed();
        }
    }
    
    /**
     * @dev Returns the latest price without updating it
     * @param maxAge Maximum acceptable age of the price in seconds
     * @return price The current price
     * @return publishTime When the price was published
     */
    function getPriceNoUpdate(uint64 maxAge) public view returns (int64, uint64) {
        PythStructs.Price memory priceData = pyth.getPrice(priceFeedId);
        
        if (block.timestamp - priceData.publishTime > maxAge) {
            revert StalePrice();
        }
        
        return (priceData.price, priceData.publishTime);
    }
    
    // Allow contract to receive ETH for update fees
    receive() external payable {}
}
```
