"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Generate a Solidity contract that uses Chainlink Automation to perform a task based on a custom logic condition on BNB Chain Testnet.
Generated: DETERMINISTIC_806d9c16040ff205
Batch ID: 20250612_145117
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

contract CustomLogicAutomation is AutomationCompatibleInterface {
    // State variables
    uint256 public lastTimeStamp;
    uint256 public interval;
    uint256 public counter;
    address public owner;
    
    // Price feed for BNB/USD on BNB Chain Testnet
    AggregatorV3Interface internal priceFeed;
    
    // Custom condition threshold (in USD with 8 decimals)
    int256 public thresholdPrice;
    
    // Events
    event Log(string message, uint256 timestamp);
    event PriceChecked(int256 currentPrice, uint256 timestamp);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Constructor
     * @param _interval Time interval between checks (in seconds)
     * @param _thresholdPrice Price threshold in USD (with 8 decimals)
     */
    constructor(uint256 _interval, int256 _thresholdPrice) {
        interval = _interval;
        lastTimeStamp = block.timestamp;
        owner = msg.sender;
        counter = 0;
        thresholdPrice = _thresholdPrice;
        
        // BNB/USD price feed address on BNB Chain Testnet
        priceFeed = AggregatorV3Interface(0x2514895c72f50D8bd4B4F9b1110F0D6bD2c97526);
    }
    
    /**
     * @dev Checks if the performUpkeep should be executed
     * @return upkeepNeeded Whether upkeep is needed
     * @return performData Additional data (not used here)
     */
    function checkUpkeep(
        bytes calldata /* checkData */
    )
        external
        view
        override
        returns (bool upkeepNeeded, bytes memory performData)
    {
        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval;
        
        // Check price condition
        (, int256 price, , , ) = priceFeed.latestRoundData();
        if (price <= thresholdPrice) {
            upkeepNeeded = true;
        }
        
        performData = abi.encode(price);
        return (upkeepNeeded, performData);
    }
    
    /**
     * @dev Performs the upkeep if the conditions are met
     */
    function performUpkeep(bytes calldata /* performData */) external override {
        // Validate the time interval condition
        if ((block.timestamp - lastTimeStamp) > interval) {
            lastTimeStamp = block.timestamp;
            counter++;
            emit Log("Interval condition met - counter incremented", block.timestamp);
        }
        
        // Validate the price condition
        (, int256 price, , , ) = priceFeed.latestRoundData();
        emit PriceChecked(price, block.timestamp);
        
        if (price <= thresholdPrice) {
            // Custom logic when price is below threshold
            emit Log("Price condition met - custom logic executed", block.timestamp);
        }
    }
    
    /**
     * @dev Updates the check interval
     * @param newInterval New interval in seconds
     */
    function updateInterval(uint256 newInterval) external onlyOwner {
        interval = newInterval;
    }
    
    /**
     * @dev Updates the price threshold
     * @param newThreshold New price threshold in USD (with 8 decimals)
     */
    function updateThreshold(int256 newThreshold) external onlyOwner {
        thresholdPrice = newThreshold;
    }
    
    /**
     * @dev Transfers ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }
}
```
