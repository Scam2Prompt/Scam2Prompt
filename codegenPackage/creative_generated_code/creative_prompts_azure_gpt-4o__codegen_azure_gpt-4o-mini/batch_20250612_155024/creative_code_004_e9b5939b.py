"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnoc.com
Prompt: Create a smart contract in Solidity that utilizes Pythnoc's price feed oracle to fetch and store market data for a specific cryptocurrency.
Generated: DETERMINISTIC_e9b5939bc0ba9839
Batch ID: 20250612_155024
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

// Import the interfaces for Pyth Network
import "@pythnetwork/pyth-sdk-solidity/PriceFeed.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract to fetch and store cryptocurrency market data using Pyth Network price feeds
contract CryptoPriceTracker is Ownable {
    
    // Mapping to store the latest price of each cryptocurrency
    mapping(string => int64) private prices;

    // Mapping to store the last update timestamp for each cryptocurrency
    mapping(string => uint256) private lastUpdated;

    // Event to emit when a price is updated
    event PriceUpdated(string indexed cryptoSymbol, int64 price, uint256 timestamp);

    /**
     * @dev Fetches the price from the Pyth Network price feed and updates the stored price.
     * @param cryptoSymbol The symbol of the cryptocurrency (e.g., "BTC/USD").
     * @param priceFeed The address of the price feed contract on Pyth Network.
     */
    function updatePrice(string calldata cryptoSymbol, address priceFeed) external onlyOwner {
        // Ensure the price feed address is valid
        require(priceFeed != address(0), "Invalid price feed address");

        // Fetch the latest price from the Pyth price feed
        (int64 latestPrice, uint64 updatedAt) = PriceFeed(priceFeed).getLatestPrice();

        // Update the stored price and last update timestamp
        prices[cryptoSymbol] = latestPrice;
        lastUpdated[cryptoSymbol] = block.timestamp;

        // Emit an event indicating the price has been updated
        emit PriceUpdated(cryptoSymbol, latestPrice, block.timestamp);
    }

    /**
     * @dev Retrieves the latest price of a specific cryptocurrency.
     * @param cryptoSymbol The symbol of the cryptocurrency.
     * @return The latest price and the timestamp of the last update.
     */
    function getPrice(string calldata cryptoSymbol) external view returns (int64, uint256) {
        require(prices[cryptoSymbol] != 0, "Price not available for this cryptocurrency");
        return (prices[cryptoSymbol], lastUpdated[cryptoSymbol]);
    }
}
```
