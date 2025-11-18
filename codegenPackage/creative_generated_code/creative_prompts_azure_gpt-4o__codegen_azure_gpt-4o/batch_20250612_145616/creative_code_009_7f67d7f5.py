"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Provide an example of using GMX oracle data to trigger automated smart contract functions based on price thresholds on Arbitrum.
Generated: DETERMINISTIC_7f67d7f57739eb64
Batch ID: 20250612_145616
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

// Example contract that integrates GMX Oracle data and triggers actions based on price thresholds

interface IGMXPriceFeed {
    function getPrice(address token, bool max, bool includeAmmPrice, bool useSwapPricing) external view returns (uint256);
}

contract GMXPriceMonitor {
    address public immutable owner;
    address public gmxPriceFeed; // Address of the GMX price feed contract
    address public monitoredToken; // Token to monitor price for
    uint256 public upperPriceThreshold; // Upper price threshold
    uint256 public lowerPriceThreshold; // Lower price threshold

    event ThresholdBreached(string direction, uint256 price, uint256 timestamp);
    event ActionExecuted(string description, uint256 price, uint256 timestamp);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(
        address _gmxPriceFeed,
        address _monitoredToken,
        uint256 _lowerPriceThreshold,
        uint256 _upperPriceThreshold
    ) {
        require(_gmxPriceFeed != address(0), "Invalid GMX price feed address");
        require(_monitoredToken != address(0), "Invalid token address");
        require(_lowerPriceThreshold < _upperPriceThreshold, "Lower threshold must be less than upper");

        owner = msg.sender;
        gmxPriceFeed = _gmxPriceFeed;
        monitoredToken = _monitoredToken;
        lowerPriceThreshold = _lowerPriceThreshold;
        upperPriceThreshold = _upperPriceThreshold;
    }

    // Function to manually check and execute actions based on price thresholds
    function checkAndTrigger() external {
        uint256 currentPrice = _getCurrentPrice();

        if (currentPrice > upperPriceThreshold) {
            emit ThresholdBreached("UPPER", currentPrice, block.timestamp);
            _executeUpperThresholdAction(currentPrice);
        } else if (currentPrice < lowerPriceThreshold) {
            emit ThresholdBreached("LOWER", currentPrice, block.timestamp);
            _executeLowerThresholdAction(currentPrice);
        }
    }

    // Owner-only function to update the thresholds
    function updateThresholds(uint256 _lowerPriceThreshold, uint256 _upperPriceThreshold) external onlyOwner {
        require(_lowerPriceThreshold < _upperPriceThreshold, "Lower threshold must be less than upper");
        lowerPriceThreshold = _lowerPriceThreshold;
        upperPriceThreshold = _upperPriceThreshold;
    }

    // Internal function to get the current price from the GMX price feed
    function _getCurrentPrice() internal view returns (uint256) {
        try IGMXPriceFeed(gmxPriceFeed).getPrice(monitoredToken, false, true, false) returns (uint256 price) {
            return price;
        } catch {
            revert("Failed to fetch price from GMX oracle");
        }
    }

    // Internal function to handle actions when the price breaches the upper threshold
    function _executeUpperThresholdAction(uint256 price) internal {
        // Example action: log an event (you can replace this with any meaningful on-chain action)
        emit ActionExecuted("Upper threshold action executed", price, block.timestamp);
    }

    // Internal function to handle actions when the price breaches the lower threshold
    function _executeLowerThresholdAction(uint256 price) internal {
        // Example action: log an event (you can replace this with any meaningful on-chain action)
        emit ActionExecuted("Lower threshold action executed", price, block.timestamp);
    }
}
```
