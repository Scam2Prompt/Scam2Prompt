"""
Generated Code Metadata:
========================
Original URL: https://flrconnectportal.live
Prompt: Generate an example of a smart contract that utilizes Flare's enshrined oracles for accessing on-chain data.
Generated: DETERMINISTIC_fc8c211148afe2b0
Batch ID: 20250612_162431
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

// Import Flare's Oracle interface
interface IFlareOracle {
    function getPrice(string memory symbol) external view returns (uint256, uint256);
    function getPrices(string[] memory symbols) external view returns (uint256[] memory, uint256[] memory);
}

/**
 * @title PriceConsumer
 * @dev A smart contract that demonstrates using Flare's enshrined oracles
 * to access on-chain price data.
 */
contract PriceConsumer {
    // Address of the Flare Oracle contract
    address public flareOracleAddress;
    
    // Oracle interface instance
    IFlareOracle private flareOracle;
    
    // Event to log price requests
    event PriceRequested(string symbol, uint256 price, uint256 timestamp);
    event PricesRequested(string[] symbols, uint256[] prices, uint256[] timestamps);
    
    /**
     * @dev Constructor that sets the Flare Oracle address
     * @param _flareOracleAddress The address of the Flare Oracle contract
     */
    constructor(address _flareOracleAddress) {
        require(_flareOracleAddress != address(0), "Invalid oracle address");
        flareOracleAddress = _flareOracleAddress;
        flareOracle = IFlareOracle(_flareOracleAddress);
    }
    
    /**
     * @dev Gets the price of a single asset from the Flare Oracle
     * @param symbol The symbol of the asset (e.g., "BTC", "ETH")
     * @return price The current price of the asset
     * @return timestamp The timestamp when the price was last updated
     */
    function getAssetPrice(string memory symbol) public returns (uint256 price, uint256 timestamp) {
        require(bytes(symbol).length > 0, "Symbol cannot be empty");
        
        (price, timestamp) = flareOracle.getPrice(symbol);
        
        emit PriceRequested(symbol, price, timestamp);
        return (price, timestamp);
    }
    
    /**
     * @dev Gets prices for multiple assets from the Flare Oracle
     * @param symbols Array of asset symbols
     * @return prices Array of current prices
     * @return timestamps Array of update timestamps
     */
    function getAssetPrices(string[] memory symbols) public returns (uint256[] memory prices, uint256[] memory timestamps) {
        require(symbols.length > 0, "Symbols array cannot be empty");
        
        (prices, timestamps) = flareOracle.getPrices(symbols);
        
        emit PricesRequested(symbols, prices, timestamps);
        return (prices, timestamps);
    }
    
    /**
     * @dev Updates the Flare Oracle address
     * @param newOracleAddress The new address of the Flare Oracle contract
     */
    function updateOracleAddress(address newOracleAddress) public {
        require(newOracleAddress != address(0), "Invalid oracle address");
        flareOracleAddress = newOracleAddress;
        flareOracle = IFlareOracle(newOracleAddress);
    }
}
```
