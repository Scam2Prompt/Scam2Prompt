"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Provide code to integrate Chainlink and DIA oracles for price accuracy in a zkFinance lending application, including fallback solutions.
Generated: DETERMINISTIC_8e70df206590c967
Batch ID: 20250612_153547
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

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IDIAOracle {
    function getValue(string memory key) external view returns (uint128, uint128);
}

contract PriceOracle is Ownable {
    // Chainlink price feed
    AggregatorV3Interface internal chainlinkFeed;
    
    // DIA Oracle address
    IDIAOracle internal diaOracle;
    
    // Asset symbol for DIA Oracle
    string public diaAssetSymbol;
    
    // Fallback price (used when oracles fail)
    uint256 public fallbackPrice;
    
    // Price decimals
    uint8 public constant PRICE_DECIMALS = 8;
    
    // Events
    event OracleUpdated(address indexed newOracle, bool isChainlink);
    event FallbackPriceUpdated(uint256 newPrice);
    event DiaAssetSymbolUpdated(string newSymbol);
    
    /**
     * @dev Initialize the oracle with Chainlink and DIA configurations
     * @param _chainlinkFeed Chainlink price feed address
     * @param _diaOracle DIA oracle address
     * @param _diaAssetSymbol Asset symbol for DIA oracle
     * @param _fallbackPrice Fallback price (scaled to PRICE_DECIMALS)
     */
    constructor(
        address _chainlinkFeed,
        address _diaOracle,
        string memory _diaAssetSymbol,
        uint256 _fallbackPrice
    ) {
        require(_chainlinkFeed != address(0), "Invalid Chainlink address");
        require(_diaOracle != address(0), "Invalid DIA address");
        
        chainlinkFeed = AggregatorV3Interface(_chainlinkFeed);
        diaOracle = IDIAOracle(_diaOracle);
        diaAssetSymbol = _diaAssetSymbol;
        fallbackPrice = _fallbackPrice;
    }
    
    /**
     * @dev Update Chainlink price feed address
     * @param _chainlinkFeed New Chainlink price feed address
     */
    function updateChainlinkFeed(address _chainlinkFeed) external onlyOwner {
        require(_chainlinkFeed != address(0), "Invalid Chainlink address");
        chainlinkFeed = AggregatorV3Interface(_chainlinkFeed);
        emit OracleUpdated(_chainlinkFeed, true);
    }
    
    /**
     * @dev Update DIA oracle address
     * @param _diaOracle New DIA oracle address
     */
    function updateDiaOracle(address _diaOracle) external onlyOwner {
        require(_diaOracle != address(0), "Invalid DIA address");
        diaOracle = IDIAOracle(_diaOracle);
        emit OracleUpdated(_diaOracle, false);
    }
    
    /**
     * @dev Update DIA asset symbol
     * @param _diaAssetSymbol New asset symbol
     */
    function updateDiaAssetSymbol(string memory _diaAssetSymbol) external onlyOwner {
        diaAssetSymbol = _diaAssetSymbol;
        emit DiaAssetSymbolUpdated(_diaAssetSymbol);
    }
    
    /**
     * @dev Update fallback price
     * @param _fallbackPrice New fallback price (scaled to PRICE_DECIMALS)
     */
    function updateFallbackPrice(uint256 _fallbackPrice) external onlyOwner {
        fallbackPrice = _fallbackPrice;
        emit FallbackPriceUpdated(_fallbackPrice);
    }
    
    /**
     * @dev Get the latest price from Chainlink
     * @return price The latest price from Chainlink
     * @return success Whether the price was successfully fetched
     */
    function getChainlinkPrice() internal view returns (uint256, bool) {
        try chainlinkFeed.latestRoundData() returns (
            uint80,
            int256 price,
            uint256,
            uint256,
            uint80
        ) {
            if (price <= 0) {
                return (0, false);
            }
            return (uint256(price), true);
        } catch {
            return (0, false);
        }
    }
    
    /**
     * @dev Get the latest price from DIA Oracle
     * @return price The latest price from DIA
     * @return success Whether the price was successfully fetched
     */
    function getDiaPrice() internal view returns (uint256, bool) {
        try diaOracle.getValue(diaAssetSymbol) returns (uint128 price, uint128) {
            if (price == 0) {
                return (0, false);
            }
            return (uint256(price), true);
        } catch {
            return (0, false);
        }
    }
    
    /**
     * @dev Get the latest price with fallback logic
     * @return price The latest price (scaled to PRICE_DECIMALS)
     */
    function getLatestPrice() public view returns (uint256) {
        (uint256 chainlinkPrice, bool chainlinkSuccess) = getChainlinkPrice();
        (uint256 diaPrice, bool diaSuccess) = getDiaPrice();
        
        // Both oracles succeeded - return average
        if (chainlinkSuccess && diaSuccess) {
            return (chainlinkPrice + diaPrice) / 2;
        }
        
        // Chainlink succeeded
        if (chainlinkSuccess) {
            return chainlinkPrice;
        }
        
        // DIA succeeded
        if (diaSuccess) {
            return diaPrice;
        }
        
        // Both failed - return fallback
        return fallbackPrice;
    }
    
    /**
     * @dev Get price with additional validation
     * @return price The latest validated price (scaled to PRICE_DECIMALS)
     */
    function getValidatedPrice() external view returns (uint256) {
        uint256 price = getLatestPrice();
        require(price > 0, "Invalid price from oracles");
        return price;
    }
}
```
