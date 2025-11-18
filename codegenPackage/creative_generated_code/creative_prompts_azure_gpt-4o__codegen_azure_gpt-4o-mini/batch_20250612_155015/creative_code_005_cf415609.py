"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythsite.com
Prompt: Write a smart contract that integrates Pyth price feed oracles to calculate the average price of an asset over a specified time period.
Generated: DETERMINISTIC_cf415609ed930cdd
Batch ID: 20250612_155015
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

// Importing necessary interfaces for interaction with the Pyth oracle
import "@pythnetwork/pyth-contracts/abi/PythInterface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AveragePriceCalculator
 * @dev A smart contract that integrates Pyth price feed oracles
 * to calculate the average price of an asset over a specified time period.
 */
contract AveragePriceCalculator is Ownable {
    // Define the Pyth interface
    PythInterface private pyth;

    // Mapping to store price history
    struct PriceRecord {
        uint256 price;
        uint256 timestamp;
    }

    // Array to hold price records
    PriceRecord[] private priceHistory;

    // Event emitted when a new price is recorded
    event PriceRecorded(uint256 price, uint256 timestamp);

    // Constructor to set the Pyth oracle address
    constructor(address _pythAddress) {
        pyth = PythInterface(_pythAddress);
    }

    /**
     * @dev Records the latest price from the Pyth oracle
     */
    function recordLatestPrice() external onlyOwner {
        // Fetch the latest price from Pyth
        (uint256 price, uint256 timestamp) = getLatestPrice();

        // Store the price and timestamp
        priceHistory.push(PriceRecord(price, timestamp));
        
        // Emit an event for the recorded price
        emit PriceRecorded(price, timestamp);
    }

    /**
     * @dev Fetches the latest price from the Pyth oracle.
     * @return price The latest price.
     * @return timestamp The timestamp when the price was fetched.
     */
    function getLatestPrice() internal view returns (uint256 price, uint256 timestamp) {
        // Get price data from Pyth
        (int64 pythPrice, uint64 pythTimestamp) = pyth.getPrice();
        
        require(pythTimestamp > 0, "Invalid timestamp from Pyth");
        
        // Convert the int64 price to uint256
        price = uint256(pythPrice);
        timestamp = uint256(pythTimestamp);
    }

    /**
     * @dev Calculates the average price over a specified time period.
     * @param _duration The duration in seconds to calculate the average price.
     * @return averagePrice The average price over the specified time period.
     */
    function calculateAveragePrice(uint256 _duration) external view returns (uint256 averagePrice) {
        uint256 totalPrice = 0;
        uint256 count = 0;

        // Iterate through the price history
        for (uint256 i = priceHistory.length; i > 0; i--) {
            // Check if the record is within the specified duration
            if (block.timestamp - priceHistory[i - 1].timestamp <= _duration) {
                totalPrice += priceHistory[i - 1].price;
                count++;
            }
        }

        // Calculate average price if we have at least one valid record
        require(count > 0, "No valid price records within the specified duration");
        
        averagePrice = totalPrice / count;
    }

    /**
     * @dev Gets the count of recorded price entries.
     * @return count The number of price records.
     */
    function getPriceRecordCount() external view returns (uint256 count) {
        return priceHistory.length;
    }
}
```
