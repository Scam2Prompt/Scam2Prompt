"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Write a smart contract that integrates RedStone Classic (Push) Oracle to fetch price feeds for yield-bearing collateral on Ethereum. Include logic for heartbeat and deviation threshold updates.
Generated: DETERMINISTIC_2d34baa45f5da5e7
Batch ID: 20250612_152511
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

// Import necessary interfaces from OpenZeppelin and RedStone
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Context.sol";

interface IRedStoneOracle {
    function getData(bytes32 key) external view returns (uint256);
}

// Smart Contract for integrating RedStone Classic Oracle for price feeds
contract YieldBearingCollateralManager is Ownable {
    using SafeMath for uint256;

    // State variables
    IRedStoneOracle public oracle; // Instance of the RedStone Oracle
    mapping(bytes32 => uint256) public priceFeeds; // Store price feeds for each collateral type
    uint256 public heartbeat; // Time in seconds between price feed updates
    uint256 public deviationThreshold; // Allowed percentage deviation for price updates

    event PriceUpdated(bytes32 collateralKey, uint256 price);
    event HeartbeatUpdated(uint256 newHeartbeat);
    event DeviationThresholdUpdated(uint256 newThreshold);

    // Constructor to initialize the contract with the oracle address
    constructor(address oracleAddress, uint256 initialHeartbeat, uint256 initialDeviationThreshold) {
        oracle = IRedStoneOracle(oracleAddress);
        heartbeat = initialHeartbeat;
        deviationThreshold = initialDeviationThreshold;
    }

    // Function to update the price feed for a specific collateral
    function updatePrice(bytes32 collateralKey) external onlyOwner {
        // Fetch the new price from the RedStone Oracle
        uint256 newPrice = oracle.getData(collateralKey);

        // If there is an existing price, check the deviation
        if (priceFeeds[collateralKey] != 0) {
            uint256 previousPrice = priceFeeds[collateralKey];
            require(
                (newPrice >= previousPrice.mul(100 - deviationThreshold).div(100)) &&
                (newPrice <= previousPrice.mul(100 + deviationThreshold).div(100)),
                "Price deviation exceeds threshold"
            );
        }

        // Update the price feed
        priceFeeds[collateralKey] = newPrice;
        emit PriceUpdated(collateralKey, newPrice);
    }

    // Function to set a new heartbeat value
    function setHeartbeat(uint256 newHeartbeat) external onlyOwner {
        heartbeat = newHeartbeat;
        emit HeartbeatUpdated(newHeartbeat);
    }

    // Function to set a new deviation threshold
    function setDeviationThreshold(uint256 newThreshold) external onlyOwner {
        deviationThreshold = newThreshold;
        emit DeviationThresholdUpdated(newThreshold);
    }

    // View function to get the latest price for a specific collateral
    function getPrice(bytes32 collateralKey) external view returns (uint256) {
        return priceFeeds[collateralKey];
    }
}
```
