"""
Generated Code Metadata:
========================
Original URL: https://pythcloud.com
Prompt: Provide an example of using Pyth Network's price feed oracles to calculate asset volatility in a smart contract.
Generated: DETERMINISTIC_19c6b2a6537a8105
Batch ID: 20250612_155015
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract VolatilityCalculator {
    IPyth public pyth;
    bytes32 public priceFeedId;
    uint256 public observationPeriod;
    uint256 public observationFrequency;
    
    struct PriceObservation {
        uint64 timestamp;
        int64 price;
    }
    
    PriceObservation[] public observations;
    
    event VolatilityCalculated(uint256 volatility);
    event NewObservationAdded(uint64 timestamp, int64 price);
    
    constructor(
        address _pythContract,
        bytes32 _priceFeedId,
        uint256 _observationPeriod,
        uint256 _observationFrequency
    ) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        require(_observationPeriod > 0, "Observation period must be positive");
        require(_observationFrequency > 0, "Observation frequency must be positive");
        
        pyth = IPyth(_pythContract);
        priceFeedId = _priceFeedId;
        observationPeriod = _observationPeriod;
        observationFrequency = _observationFrequency;
    }
    
    function updatePrice() external payable {
        bytes[] memory priceUpdateData = new bytes[](1);
        priceUpdateData[0] = pyth.getPriceFeedUpdateData(priceFeedId);
        
        uint fee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");
        
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);
        
        PythStructs.Price memory currentPrice = pyth.getPrice(priceFeedId);
        
        // Only add observation if frequency has passed since last observation
        if (observations.length == 0 || 
            (block.timestamp - observations[observations.length - 1].timestamp) >= observationFrequency) {
            observations.push(PriceObservation(uint64(block.timestamp), currentPrice.price));
            emit NewObservationAdded(uint64(block.timestamp), currentPrice.price);
        }
        
        // Remove old observations outside the observation period
        while (observations.length > 0 && 
               (block.timestamp - observations[0].timestamp) > observationPeriod) {
            for (uint i = 0; i < observations.length - 1; i++) {
                observations[i] = observations[i + 1];
            }
            observations.pop();
        }
    }
    
    function calculateVolatility() external returns (uint256) {
        require(observations.length >= 2, "Insufficient data points");
        
        int256 sum = 0;
        int256 sumSquared = 0;
        uint256 count = observations.length;
        
        // Calculate mean
        for (uint i = 0; i < count; i++) {
            sum += observations[i].price;
        }
        int256 mean = sum / int256(count);
        
        // Calculate variance
        for (uint i = 0; i < count; i++) {
            int256 deviation = observations[i].price - mean;
            sumSquared += deviation * deviation;
        }
        uint256 variance = uint256(sumSquared) / count;
        
        // Volatility is the square root of variance
        uint256 volatility = sqrt(variance);
        
        emit VolatilityCalculated(volatility);
        return volatility;
    }
    
    // Babylonian method for square root
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
    }
    
    function getObservationCount() external view returns (uint256) {
        return observations.length;
    }
    
    function getLatestPrice() external view returns (int64) {
        require(observations.length > 0, "No observations available");
        return observations[observations.length - 1].price;
    }
    
    receive() external payable {}
}
```
