"""
Generated Code Metadata:
========================
Original URL: https://pythsite.com
Prompt: Write a smart contract that integrates Pyth price feed oracles to calculate the average price of an asset over a specified time period.
Generated: DETERMINISTIC_cf415609ed930cdd
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

contract PythPriceAverager {
    IPyth public pyth;
    bytes32 public priceFeedId;
    
    struct PriceSnapshot {
        uint64 timestamp;
        int64 price;
        uint64 conf;
    }
    
    PriceSnapshot[] public priceSnapshots;
    uint256 public snapshotInterval;
    uint256 public lastSnapshotTimestamp;
    
    event PriceSnapshotAdded(uint64 timestamp, int64 price, uint64 conf);
    event AveragePriceCalculated(int64 averagePrice, uint64 averageConf);
    
    constructor(
        address _pythAddress,
        bytes32 _priceFeedId,
        uint256 _snapshotInterval
    ) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        require(_priceFeedId != bytes32(0), "Invalid price feed ID");
        require(_snapshotInterval > 0, "Snapshot interval must be positive");
        
        pyth = IPyth(_pythAddress);
        priceFeedId = _priceFeedId;
        snapshotInterval = _snapshotInterval;
    }
    
    function updatePrice(bytes[] calldata priceUpdateData) external payable {
        require(priceUpdateData.length > 0, "No price update data provided");
        
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");
        
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);
        
        if (block.timestamp >= lastSnapshotTimestamp + snapshotInterval) {
            _takeSnapshot();
        }
    }
    
    function _takeSnapshot() private {
        try pyth.getPrice(priceFeedId) returns (PythStructs.Price memory price) {
            priceSnapshots.push(PriceSnapshot({
                timestamp: uint64(block.timestamp),
                price: price.price,
                conf: price.conf
            }));
            
            lastSnapshotTimestamp = block.timestamp;
            emit PriceSnapshotAdded(uint64(block.timestamp), price.price, price.conf);
        } catch Error(string memory reason) {
            revert(string(abi.encodePacked("Failed to get price: ", reason)));
        } catch {
            revert("Failed to get price: Unknown error");
        }
    }
    
    function calculateAveragePrice(uint256 period) external view returns (int64, uint64) {
        require(period > 0, "Period must be positive");
        require(priceSnapshots.length > 0, "No snapshots available");
        
        uint256 cutoff = block.timestamp - period;
        uint256 count = 0;
        int256 sumPrice = 0;
        uint256 sumConf = 0;
        
        for (uint256 i = priceSnapshots.length; i > 0; i--) {
            PriceSnapshot memory snapshot = priceSnapshots[i - 1];
            if (snapshot.timestamp < cutoff) {
                break;
            }
            
            sumPrice += snapshot.price;
            sumConf += snapshot.conf;
            count++;
        }
        
        require(count > 0, "No snapshots in the specified period");
        
        int64 averagePrice = int64(sumPrice / int256(count));
        uint64 averageConf = uint64(sumConf / count);
        
        return (averagePrice, averageConf);
    }
    
    function withdrawFees() external {
        payable(msg.sender).transfer(address(this).balance);
    }
    
    function getSnapshotCount() external view returns (uint256) {
        return priceSnapshots.length;
    }
    
    receive() external payable {}
}
```
