"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Explain how to automate smart contracts using Chainlink's event-based triggers and provide a sample implementation.
Generated: DETERMINISTIC_3c9ea02918fb8dc1
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

// Import Chainlink contracts
import "@chainlink/contracts/src/v0.8/automation/AutomationCompatible.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title PriceFeedMonitor
 * @dev A contract that monitors price feeds and triggers actions when conditions are met
 */
contract PriceFeedMonitor is AutomationCompatibleInterface {
    // Price feed aggregator
    AggregatorV3Interface public priceFeed;
    
    // Target price threshold (in USD with 8 decimals)
    int256 public targetPrice;
    
    // Last price that was checked
    int256 public lastPrice;
    
    // Last time the price was checked
    uint256 public lastTimestamp;
    
    // Event emitted when price threshold is crossed
    event PriceThresholdCrossed(int256 currentPrice, uint256 timestamp);
    
    /**
     * @dev Constructor to initialize the price feed and target price
     * @param _priceFeedAddress Address of the Chainlink price feed
     * @param _targetPrice Target price threshold (in USD with 8 decimals)
     */
    constructor(address _priceFeedAddress, int256 _targetPrice) {
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        targetPrice = _targetPrice;
    }
    
    /**
     * @dev Checks if the price has crossed the threshold
     * @return upkeepNeeded Boolean indicating if upkeep is needed
     * @return performData Additional data (not used here)
     */
    function checkUpkeep(
        bytes calldata /* checkData */
    ) external view override returns (bool upkeepNeeded, bytes memory performData) {
        // Get latest price from Chainlink
        (, int256 currentPrice, , , ) = priceFeed.latestRoundData();
        
        // Check if price has crossed the threshold
        upkeepNeeded = (currentPrice >= targetPrice && lastPrice < targetPrice) || 
                      (currentPrice <= targetPrice && lastPrice > targetPrice);
        
        // performData is not used in this example
        performData = "";
    }
    
    /**
     * @dev Executes the upkeep when conditions are met
     * @param /* performData Additional data (not used here)
     */
    function performUpkeep(bytes calldata /* performData */) external override {
        // Revalidate the condition
        (bool upkeepNeeded, ) = this.checkUpkeep("");
        require(upkeepNeeded, "Price threshold not crossed");
        
        // Get latest price and timestamp
        (, int256 currentPrice, , uint256 timestamp, ) = priceFeed.latestRoundData();
        
        // Update state
        lastPrice = currentPrice;
        lastTimestamp = timestamp;
        
        // Emit event
        emit PriceThresholdCrossed(currentPrice, timestamp);
        
        // Here you would add your custom logic to execute when threshold is crossed
        // For example: trigger a trade, send a notification, etc.
    }
    
    /**
     * @dev Updates the target price threshold
     * @param _newTargetPrice New target price (in USD with 8 decimals)
     */
    function updateTargetPrice(int256 _newTargetPrice) external {
        targetPrice = _newTargetPrice;
    }
}
```
