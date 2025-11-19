"""
Generated Code Metadata:
========================
Original URL: https://1inch-docs.vercel.app
Prompt: Provide an example of using the 1inch Spot Price Aggregator smart contract to extract the current price of USDT from decentralized exchanges (DEXes).
Generated: DETERMINISTIC_2278784aa455945f
Batch ID: 20250612_155028
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

// Importing the interface for the 1inch Spot Price Aggregator
import "@1inch/spot-price-contracts/contracts/interfaces/IPriceOracle.sol";

contract PriceFetcher {
    // Address of the 1inch Spot Price Aggregator contract
    IPriceOracle public priceOracle;

    // Event to emit when the price is fetched
    event PriceFetched(uint256 price);

    // Constructor to set the price oracle address
    constructor(address _priceOracle) {
        require(_priceOracle != address(0), "Invalid price oracle address");
        priceOracle = IPriceOracle(_priceOracle);
    }

    // Function to fetch the current price of USDT in terms of ETH
    function getUSDTPrice() external returns (uint256) {
        // Fetching the price from the 1inch Spot Price Aggregator
        uint256 price;
        try priceOracle.getSpotPrice("USDT", "ETH") returns (uint256 fetchedPrice) {
            price = fetchedPrice;
        } catch {
            revert("Failed to fetch price from the price oracle");
        }

        // Emitting the fetched price
        emit PriceFetched(price);
        return price;
    }
}
```

Make sure to replace the `@1inch/spot-price-contracts/contracts/interfaces/IPriceOracle.sol` import path with the correct path based on your project structure and the version of the 1inch contracts you are using.
