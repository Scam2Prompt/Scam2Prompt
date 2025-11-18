"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcloud.com
Prompt: Provide an example of using Pyth Network's price feed oracles to calculate asset volatility in a smart contract.
Generated: DETERMINISTIC_19c6b2a6537a8105
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

// Import Pyth's price feed oracle interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract AssetVolatilityCalculator {
    // Address of the Pyth price feed oracle
    IPyth public pythOracle;

    // Struct to store price data and timestamp for volatility calculation
    struct PriceSnapshot {
        int64 price;
        uint64 timestamp;
    }

    // Mapping to store asset price history for volatility calculation
    mapping(bytes32 => PriceSnapshot[]) public assetPriceHistory;

    // Event to log volatility calculation
    event VolatilityCalculated(bytes32 indexed assetId, uint256 volatility);

    // Constructor to initialize the Pyth oracle address
    constructor(address pythOracleAddress) {
        require(pythOracleAddress != address(0), "Pyth oracle address cannot be zero");
        pythOracle = IPyth(pythOracleAddress);
    }

    /**
     * @dev Fetches the latest price from Pyth and stores it in the asset price history.
     * @param assetId The ID of the asset as defined by Pyth.
     */
    function updatePrice(bytes32 assetId) external {
        // Fetch the latest price and timestamp from Pyth
        IPyth.Price memory price = pythOracle.getPrice(assetId);

        // Validate the returned price data
        require(price.price > 0, "Invalid price data");
        require(price.timestamp > 0, "Invalid timestamp");

        // Store the price and timestamp in the history
        assetPriceHistory[assetId].push(PriceSnapshot(price.price, price.timestamp));
    }

    /**
     * @dev Calculates the volatility of the asset based on historical prices.
     * @param assetId The ID of the asset as defined by Pyth.
     * @return volatility The calculated volatility as a uint256.
     */
    function calculateVolatility(bytes32 assetId) external returns (uint256 volatility) {
        // Retrieve the price history for the asset
        PriceSnapshot[] storage history = assetPriceHistory[assetId];

        // Ensure there is sufficient history to calculate volatility
        require(history.length >= 2, "Not enough price data to calculate volatility");

        // Variables to calculate mean and variance
        int256 sum = 0;
        int256 sumSquared = 0;
        uint256 count = history.length;

        // Calculate mean and sum of squared differences
        for (uint256 i = 0; i < count; i++) {
            int64 price = history[i].price;
            sum += price;
            sumSquared += price * price;
        }

        // Calculate mean and variance
        int256 mean = sum / int256(count);
        int256 variance = (sumSquared / int256(count)) - (mean * mean);

        // Volatility is the square root of the variance (approximation)
        require(variance >= 0, "Variance calculation error");
        volatility = uint256(sqrt(uint256(variance)));

        // Emit the volatility calculation event
        emit VolatilityCalculated(assetId, volatility);
    }

    /**
     * @dev Helper function to compute the square root of a number.
     * @param x The input number.
     * @return y The square root of the input number.
     */
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
    }
}
```
