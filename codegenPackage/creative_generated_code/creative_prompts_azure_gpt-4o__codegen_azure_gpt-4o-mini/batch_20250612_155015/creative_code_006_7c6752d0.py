"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnet.com
Prompt: Write a smart contract function in Solidity that uses PythNet's market data to trigger an event when an asset price crosses a specific threshold.
Generated: DETERMINISTIC_7c6752d053b29458
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

// Interface for interacting with PythNet's price feed
interface IPyth {
    function getPriceData(bytes32 id) external view returns (uint256 price, uint256 timestamp);
}

// Event to be emitted when asset price crosses the threshold
event PriceCrossedThreshold(bytes32 indexed assetId, uint256 price, uint256 threshold, bool aboveThreshold);

contract PriceThresholdWatcher {
    // State variable to store the Pyth price feed contract address
    IPyth public pyth;

    // Mapping to store thresholds for each asset
    mapping(bytes32 => uint256) public thresholds;

    // Constructor to initialize the Pyth price feed address
    constructor(address _pythAddress) {
        pyth = IPyth(_pythAddress);
    }

    // Function to set the price threshold for a specific asset
    function setThreshold(bytes32 assetId, uint256 threshold) external {
        thresholds[assetId] = threshold;
    }

    // Function to check the asset price and emit an event if it crosses the threshold
    function checkPriceAndEmitEvent(bytes32 assetId) external {
        // Retrieve the current price and timestamp from PythNet
        (uint256 currentPrice, uint256 timestamp) = pyth.getPriceData(assetId);
        
        // Ensure the price data is recent
        require(timestamp > 0, "Invalid price data");

        uint256 threshold = thresholds[assetId];
        
        // Check if the current price crosses the threshold
        if (currentPrice > threshold) {
            emit PriceCrossedThreshold(assetId, currentPrice, threshold, true);
        } else if (currentPrice < threshold) {
            emit PriceCrossedThreshold(assetId, currentPrice, threshold, false);
        }
    }
}
```
