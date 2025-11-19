"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: Create an example of a dapp that leverages Flare's enshrined oracles for data integrity and security.
Generated: DETERMINISTIC_28424ba249216696
Batch ID: 20250612_161005
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

// Import Flare's Oracle contracts
import "@flarenetwork/flare-periphery-contracts/contracts/oracles/PriceSubmitter.sol";
import "@flarenetwork/flare-periphery-contracts/contracts/oracles/PriceProvider.sol";

/**
 * @title OracleDataConsumer
 * @dev A contract that demonstrates using Flare's enshrined oracles for data integrity
 */
contract OracleDataConsumer {
    // PriceSubmitter contract address
    address public priceSubmitterAddress;
    
    // PriceProvider contract address
    address public priceProviderAddress;
    
    // Event emitted when a price is received
    event PriceReceived(bytes32 indexed symbol, uint256 price, uint256 timestamp);
    
    // Mapping to store the latest prices
    mapping(bytes32 => uint256) public latestPrices;
    
    /**
     * @dev Constructor initializes the oracle contract addresses
     * @param _priceSubmitter Address of the PriceSubmitter contract
     * @param _priceProvider Address of the PriceProvider contract
     */
    constructor(address _priceSubmitter, address _priceProvider) {
        require(_priceSubmitter != address(0), "Invalid PriceSubmitter address");
        require(_priceProvider != address(0), "Invalid PriceProvider address");
        
        priceSubmitterAddress = _priceSubmitter;
        priceProviderAddress = _priceProvider;
    }
    
    /**
     * @dev Fetches the latest price for a given symbol from Flare's oracle
     * @param symbol The symbol to fetch price for (e.g., "BTC", "ETH")
     */
    function getLatestPrice(bytes32 symbol) public returns (uint256) {
        // Get the price from the PriceProvider contract
        (uint256 price, uint256 timestamp) = PriceProvider(priceProviderAddress).getPrice(symbol);
        
        require(price > 0, "Invalid price received");
        require(timestamp > 0, "Invalid timestamp received");
        
        // Update the latest price
        latestPrices[symbol] = price;
        
        // Emit event
        emit PriceReceived(symbol, price, timestamp);
        
        return price;
    }
    
    /**
     * @dev Example function that uses the oracle price for business logic
     * @param symbol The symbol to check price for
     * @param threshold The minimum acceptable price
     * @return bool Whether the price is above threshold
     */
    function isPriceAboveThreshold(bytes32 symbol, uint256 threshold) external returns (bool) {
        uint256 currentPrice = getLatestPrice(symbol);
        return currentPrice > threshold;
    }
    
    /**
     * @dev Example function that demonstrates submitting a price (for oracle nodes)
     * @param symbol The symbol to submit price for
     * @param price The price to submit
     * @param timestamp The timestamp of the price
     */
    function submitPrice(bytes32 symbol, uint256 price, uint256 timestamp) external {
        require(msg.sender == priceSubmitterAddress, "Only PriceSubmitter can call");
        
        // In a real scenario, additional validation would be performed here
        latestPrices[symbol] = price;
        emit PriceReceived(symbol, price, timestamp);
    }
}
```
