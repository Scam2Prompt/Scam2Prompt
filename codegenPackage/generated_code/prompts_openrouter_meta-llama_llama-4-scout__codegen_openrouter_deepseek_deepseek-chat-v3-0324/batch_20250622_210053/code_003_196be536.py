"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Design a simple use case for RedStone's Core (Pull) oracle model, describing how a dApp can utilize this model for low-latency data updates.
Generated: DETERMINISTIC_196be53681dd15a7
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import RedStone's Core (Pull) model interface
import "@redstone-finance/evm-connector/contracts/data-services/PullBasedDataService.sol";

/**
 * @title PriceFeed
 * @dev A simple dApp that uses RedStone's Pull oracle model to get price updates
 */
contract PriceFeed {
    // RedStone data service instance
    PullBasedDataService public dataService;
    
    // Supported token symbols
    string public constant ETH = "ETH";
    string public constant BTC = "BTC";
    
    // Events
    event PriceUpdated(string symbol, uint256 price, uint256 timestamp);
    
    /**
     * @dev Initialize with RedStone data service address
     * @param _dataServiceAddress Address of RedStone's PullBasedDataService
     */
    constructor(address _dataServiceAddress) {
        dataService = PullBasedDataService(_dataServiceAddress);
    }
    
    /**
     * @dev Get the latest price for a token
     * @param symbol Token symbol (e.g., "ETH", "BTC")
     * @return price The current price of the token
     * @return timestamp The timestamp of the price update
     */
    function getLatestPrice(string memory symbol) public returns (uint256 price, uint256 timestamp) {
        // Validate input
        require(
            keccak256(bytes(symbol)) == keccak256(bytes(ETH)) || 
            keccak256(bytes(symbol)) == keccak256(bytes(BTC)),
            "Unsupported token symbol"
        );
        
        // Get price data from RedStone oracle
        (price, timestamp) = dataService.getLatestPrice(symbol);
        
        // Emit event
        emit PriceUpdated(symbol, price, timestamp);
        
        return (price, timestamp);
    }
    
    /**
     * @dev Get prices for multiple tokens in a single call
     * @param symbols Array of token symbols
     * @return prices Array of prices
     * @return timestamps Array of timestamps
     */
    function getLatestPrices(string[] memory symbols) public returns (uint256[] memory prices, uint256[] memory timestamps) {
        require(symbols.length > 0, "Empty symbols array");
        
        prices = new uint256[](symbols.length);
        timestamps = new uint256[](symbols.length);
        
        for (uint256 i = 0; i < symbols.length; i++) {
            (prices[i], timestamps[i]) = getLatestPrice(symbols[i]);
        }
        
        return (prices, timestamps);
    }
}
```
