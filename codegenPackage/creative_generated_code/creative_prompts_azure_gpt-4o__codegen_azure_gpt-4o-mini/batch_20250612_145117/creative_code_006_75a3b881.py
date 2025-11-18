"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Write a smart contract that integrates Chainlink Automation to execute a function on Optimism Mainnet based on external API data.
Generated: DETERMINISTIC_75a3b881b3f7360f
Batch ID: 20250612_145117
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

// Import OpenZeppelin's Ownable to manage contract ownership
import "@openzeppelin/contracts/access/Ownable.sol";

// Import Chainlink's Automation interface
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";

// Import Chainlink's Aggregator interface for price feeds
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract SmartContractWithChainlinkAutomation is Ownable, AutomationCompatibleInterface {
    // State variables
    uint256 public threshold; // The threshold value for triggering the function
    uint256 public data;      // The latest data fetched from the external API
    uint256 public lastTimeStamp; // Timestamp of the last execution

    // Address of the Chainlink price feed
    AggregatorV3Interface internal priceFeed;

    // Event emitted when the function is executed
    event Executed(uint256 newData);

    // Constructor to initialize the contract
    constructor(address _priceFeed, uint256 _threshold) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        threshold = _threshold;
        lastTimeStamp = block.timestamp;
    }

    // Function to fetch the latest price data from Chainlink or an external API
    function fetchData() external {
        // Check if the price feed is available
        (
            /* uint80 roundID */,
            int256 price,
            /* uint256 startedAt */,
            /* uint256 timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();

        // Ensure price is positive
        require(price > 0, "Invalid price data");
        
        // Update the latest data based on the fetched price
        data = uint256(price);
    }

    // Function to execute when conditions are met
    function execute() internal {
        // Only execute if data meets the threshold
        require(data > threshold, "Data does not meet the threshold");

        // Emit the event indicating execution
        emit Executed(data);
        
        // Reset last timestamp
        lastTimeStamp = block.timestamp;
    }

    // Chainlink Automation checkUpkeep function
    function checkUpkeep(bytes calldata) external view override returns (bool upkeepNeeded, bytes memory) {
        upkeepNeeded = (data > threshold && lastTimeStamp + 1 minutes < block.timestamp);
    }

    // Chainlink Automation performUpkeep function
    function performUpkeep(bytes calldata) external override {
        (bool upkeepNeeded, ) = checkUpkeep("");
        require(upkeepNeeded, "No upkeep needed");

        // Execute the function
        execute();
    }

    // Owner function to update the threshold value
    function updateThreshold(uint256 _newThreshold) external onlyOwner {
        threshold = _newThreshold;
    }
}
```
