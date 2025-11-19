"""
Generated Code Metadata:
========================
Original URL: https://oeth-route.pages.dev
Prompt: Provide an example of how to use Chainlink price oracles to calculate the value of collateral deposited into the Origin vault for minting OUSD.
Generated: DETERMINISTIC_620bd681ff67a14b
Batch ID: 20250612_150622
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

// Importing the Chainlink Aggregator interface
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// Interface for the Origin Vault
interface IOriginVault {
    function getCollateralValue(address user) external view returns (uint256);
}

// Main contract to interact with Chainlink price oracles and the Origin Vault
contract CollateralValueCalculator {
    // Address of the Chainlink price feed for the asset (e.g., ETH/USD)
    AggregatorV3Interface internal priceFeed;
    
    // Reference to the Origin Vault contract
    IOriginVault public originVault;

    // Event to log the calculated collateral value
    event CollateralValueCalculated(address indexed user, uint256 valueInUSD);

    // Constructor to initialize the price feed and origin vault
    constructor(address _priceFeed, address _originVault) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        originVault = IOriginVault(_originVault);
    }

    // Function to get the latest price from the Chainlink price feed
    function getLatestPrice() internal view returns (uint256) {
        (
            , 
            int price, 
            , 
            , 
        ) = priceFeed.latestRoundData();
        // Ensure the price is positive
        require(price > 0, "Invalid price from price feed");
        return uint256(price);
    }

    // Function to calculate the collateral value in USD
    function calculateCollateralValue(address user) external returns (uint256) {
        // Get the collateral value in the native asset (e.g., ETH)
        uint256 collateralValueInAsset = originVault.getCollateralValue(user);
        
        // Get the latest price of the asset in USD
        uint256 latestPrice = getLatestPrice();
        
        // Calculate the collateral value in USD
        uint256 collateralValueInUSD = (collateralValueInAsset * latestPrice) / 1e18; // Adjust for decimals
        
        // Emit the event with the calculated value
        emit CollateralValueCalculated(user, collateralValueInUSD);
        
        return collateralValueInUSD;
    }
}
```
