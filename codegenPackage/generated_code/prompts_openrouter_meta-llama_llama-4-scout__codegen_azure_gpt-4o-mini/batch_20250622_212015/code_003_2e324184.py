"""
Generated Code Metadata:
========================
Original URL: https://raydium-ui-v3-inner-hcminfq31-raydium.vercel.app
Prompt: Design a function in Solidity to update the liquidity pool chart data for a DeFi platform, handling cases where no data is available for a specific time interval.
Generated: DETERMINISTIC_2e324184523cd85c
Batch ID: 20250622_212015
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

contract LiquidityPool {
    // Struct to hold liquidity pool data for a specific time interval
    struct PoolData {
        uint256 timestamp; // Time of the data entry
        uint256 liquidity;  // Amount of liquidity in the pool
    }

    // Mapping to store liquidity pool data by timestamp
    mapping(uint256 => PoolData) private poolData;
    // Array to keep track of all timestamps for iteration
    uint256[] private timestamps;

    // Event to emit when liquidity pool data is updated
    event PoolDataUpdated(uint256 timestamp, uint256 liquidity);

    // Function to update liquidity pool data
    function updateLiquidityPoolData(uint256 _timestamp, uint256 _liquidity) external {
        // Check if the timestamp is valid (not in the future)
        require(_timestamp <= block.timestamp, "Timestamp cannot be in the future");

        // Check if data already exists for the given timestamp
        if (poolData[_timestamp].timestamp == 0) {
            // If no data exists, create a new entry
            poolData[_timestamp] = PoolData(_timestamp, _liquidity);
            timestamps.push(_timestamp); // Add timestamp to the array
        } else {
            // If data exists, update the existing entry
            poolData[_timestamp].liquidity = _liquidity;
        }

        // Emit an event to notify that the pool data has been updated
        emit PoolDataUpdated(_timestamp, _liquidity);
    }

    // Function to retrieve liquidity data for a specific timestamp
    function getLiquidityData(uint256 _timestamp) external view returns (uint256 liquidity) {
        // Check if data exists for the given timestamp
        require(poolData[_timestamp].timestamp != 0, "No data available for this timestamp");
        return poolData[_timestamp].liquidity;
    }

    // Function to get all timestamps for iteration
    function getAllTimestamps() external view returns (uint256[] memory) {
        return timestamps;
    }
}
```
