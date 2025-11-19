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

// Importing Chainlink and DIA interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DIA oracle
interface IDIAOracle {
    function getPrice(string calldata asset) external view returns (uint256);
}

// Main contract for zkFinance lending application
contract zkFinanceLending is Ownable {
    // State variables for oracles
    AggregatorV3Interface internal chainlinkOracle;
    IDIAOracle internal diaOracle;

    // Fallback price variable
    uint256 public fallbackPrice;

    // Event for price updates
    event PriceUpdated(uint256 price);

    // Constructor to initialize oracles
    constructor(address _chainlinkOracle, address _diaOracle) {
        chainlinkOracle = AggregatorV3Interface(_chainlinkOracle);
        diaOracle = IDIAOracle(_diaOracle);
    }

    // Function to get the latest price from Chainlink
    function getChainlinkPrice() internal view returns (uint256) {
        (
            /* uint80 roundID */,
            int256 price,
            /* uint256 startedAt */,
            /* uint256 timeStamp */,
            /* uint80 answeredInRound */
        ) = chainlinkOracle.latestRoundData();
        
        require(price > 0, "Invalid Chainlink price");
        return uint256(price);
    }

    // Function to get the latest price from DIA
    function getDIAPrice(string calldata asset) internal view returns (uint256) {
        uint256 price = diaOracle.getPrice(asset);
        require(price > 0, "Invalid DIA price");
        return price;
    }

    // Function to get the accurate price using both oracles with fallback
    function getAccuratePrice(string calldata asset) external returns (uint256) {
        uint256 price;
        try this.getChainlinkPrice() returns (uint256 chainlinkPrice) {
            price = chainlinkPrice;
        } catch {
            // Fallback to DIA if Chainlink fails
            price = getDIAPrice(asset);
        }

        // Update fallback price
        fallbackPrice = price;
        emit PriceUpdated(price);
        return price;
    }

    // Function to set a new DIA oracle address (only owner)
    function setDIAOracle(address _diaOracle) external onlyOwner {
        diaOracle = IDIAOracle(_diaOracle);
    }

    // Function to set a new Chainlink oracle address (only owner)
    function setChainlinkOracle(address _chainlinkOracle) external onlyOwner {
        chainlinkOracle = AggregatorV3Interface(_chainlinkOracle);
    }
}
```
