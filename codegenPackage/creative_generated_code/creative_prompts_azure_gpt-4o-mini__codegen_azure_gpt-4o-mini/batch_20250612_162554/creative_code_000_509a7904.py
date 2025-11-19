"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythpm.com
Prompt: How can I implement price feed oracles in my smart contract using the data from pythpm.com?
Generated: DETERMINISTIC_509a79047a04610e
Batch ID: 20250612_162554
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

// Importing necessary interfaces from OpenZeppelin for safe math operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Pyth price feed
interface IPyth {
    function getPriceData(bytes32 _priceId) external view returns (int256 price, uint64 publisherTime);
}

contract PriceFeedOracle {
    using SafeMath for uint256;

    // Address of the Pyth contract
    address public pythAddress;

    // Mapping to store prices by asset ID
    mapping(bytes32 => int256) public prices;

    // Event to emit when price is updated
    event PriceUpdated(bytes32 indexed priceId, int256 price);

    // Constructor to set the Pyth contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pythAddress = _pythAddress;
    }

    // Function to fetch and update price from Pyth
    function updatePrice(bytes32 priceId) external {
        (int256 price, uint64 publisherTime) = IPyth(pythAddress).getPriceData(priceId);

        // Check if the price is valid
        require(price > 0, "Invalid price received");

        // Update the stored price
        prices[priceId] = price;

        // Emit an event for the updated price
        emit PriceUpdated(priceId, price);
    }

    // Function to retrieve the price for a specific price ID
    function getPrice(bytes32 priceId) external view returns (int256) {
        int256 price = prices[priceId];
        
        // Ensure price exists
        require(price != 0, "Price not set for this ID");

        return price;
    }
}
```
