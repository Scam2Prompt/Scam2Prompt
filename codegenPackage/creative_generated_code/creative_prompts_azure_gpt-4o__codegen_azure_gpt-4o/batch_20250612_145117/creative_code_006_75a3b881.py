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

// Importing Chainlink Automation interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
// Importing Chainlink Aggregator interface for external API data fetching
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract OptimismChainlinkAutomation is AutomationCompatibleInterface {
    // Address of Chainlink price feed
    AggregatorV3Interface public priceFeed;

    // State variable to store the last executed value
    int256 public lastCheckedPrice;

    // Threshold value for triggering the automated function
    int256 public priceThreshold;

    // Event to emit when the automated function is executed
    event FunctionExecuted(int256 price, uint256 timestamp);

    /**
     * @notice Constructor to initialize the price feed and the threshold
     * @param _priceFeed Address of the Chainlink Price Feed
     * @param _priceThreshold Threshold for triggering the function
     */
    constructor(address _priceFeed, int256 _priceThreshold) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        priceThreshold = _priceThreshold;
        lastCheckedPrice = 0;
    }

    /**
     * @notice Fetch the latest price from Chainlink Price Feed
     * @return The latest price
     */
    function getLatestPrice() public view returns (int256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return price;
    }

    /**
     * @notice Check if the automated function should be executed
     * @dev Chainlink Automation will call this function to determine if upkeep is needed
     * @return upkeepNeeded Boolean indicating whether upkeep is required
     * @return performData Data to pass to `performUpkeep`
     */
    function checkUpkeep(bytes calldata /* checkData */)
        external
        view
        override
        returns (bool upkeepNeeded, bytes memory performData)
    {
        int256 currentPrice = getLatestPrice();
        upkeepNeeded = currentPrice >= priceThreshold && currentPrice != lastCheckedPrice;
        performData = abi.encode(currentPrice);
    }

    /**
     * @notice Execute the automated function when upkeep is needed
     * @dev Chainlink Automation will call this function to execute the function
     * @param performData Data passed from `checkUpkeep`
     */
    function performUpkeep(bytes calldata performData) external override {
        int256 currentPrice = abi.decode(performData, (int256));

        // Ensure the function is executed only when needed
        if (currentPrice >= priceThreshold && currentPrice != lastCheckedPrice) {
            lastCheckedPrice = currentPrice;

            // Emit an event to signify the execution
            emit FunctionExecuted(currentPrice, block.timestamp);
        } else {
            revert("Upkeep not needed");
        }
    }

    /**
     * @notice Update the price threshold for triggering upkeep
     * @param _priceThreshold New price threshold
     */
    function updatePriceThreshold(int256 _priceThreshold) external {
        priceThreshold = _priceThreshold;
    }
}
```

### Notes:
- This code uses Chainlink Automation and Chainlink Price Feeds to trigger a function based on an external data source.
- Make sure to replace `address _priceFeed` in the constructor with the appropriate Chainlink Price Feed address for Optimism Mainnet.
- Deploy this contract on Optimism Mainnet and configure Chainlink Automation for upkeep registration.
