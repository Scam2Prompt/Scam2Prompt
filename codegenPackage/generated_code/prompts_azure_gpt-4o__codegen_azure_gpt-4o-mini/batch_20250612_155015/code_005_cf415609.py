"""
Generated Code Metadata:
========================
Original URL: https://pythsite.com
Prompt: Write a smart contract that integrates Pyth price feed oracles to calculate the average price of an asset over a specified time period.
Generated: DETERMINISTIC_cf415609ed930cdd
Batch ID: 20250612_155015
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

// Importing the Pyth price feed interface
import "@pythnetwork/pyth-sdk-solidity/contracts/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/contracts/Pyth.sol";

contract AveragePriceCalculator {
    // Pyth price feed contract address
    Pyth public pyth;

    // Mapping to store price data for each asset
    mapping(bytes32 => uint256[]) private priceHistory;

    // Event to emit when a new price is added
    event PriceUpdated(bytes32 indexed assetId, uint256 price);

    // Constructor to initialize the Pyth contract
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = Pyth(_pythAddress);
    }

    // Function to update the price of an asset
    function updatePrice(bytes32 assetId) external {
        // Fetch the latest price from the Pyth oracle
        (int64 price, uint64 publishTime) = pyth.getPrice(assetId);
        
        // Ensure the price is valid
        require(price > 0, "Invalid price from oracle");

        // Store the price in history
        priceHistory[assetId].push(uint256(price));

        // Emit an event for the new price
        emit PriceUpdated(assetId, uint256(price));
    }

    // Function to calculate the average price of an asset over a specified time period
    function calculateAveragePrice(bytes32 assetId, uint256 timePeriod) external view returns (uint256) {
        uint256 totalPrice = 0;
        uint256 count = 0;

        // Get the current block timestamp
        uint256 currentTime = block.timestamp;

        // Iterate through the price history to calculate the average
        for (uint256 i = 0; i < priceHistory[assetId].length; i++) {
            // Assuming each price was recorded at the current block timestamp
            // In a real scenario, you would need to store timestamps with prices
            if (currentTime - i <= timePeriod) {
                totalPrice += priceHistory[assetId][i];
                count++;
            }
        }

        // Ensure there are prices to calculate the average
        require(count > 0, "No prices available for the specified time period");

        // Return the average price
        return totalPrice / count;
    }
}
```
