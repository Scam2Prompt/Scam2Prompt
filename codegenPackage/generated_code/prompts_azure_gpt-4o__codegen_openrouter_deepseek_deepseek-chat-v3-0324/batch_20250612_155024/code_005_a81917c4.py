"""
Generated Code Metadata:
========================
Original URL: https://pythcall.com
Prompt: Write a Solidity smart contract that integrates Pyth Network's price feed oracles to trigger specific actions based on market data thresholds.
Generated: DETERMINISTIC_a81917c43c1dbb92
Batch ID: 20250612_155024
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

contract PythPriceTrigger {
    IPyth public pyth;
    bytes32 public priceFeedId;
    address public owner;

    // Threshold values for price actions
    uint64 public upperThreshold;
    uint64 public lowerThreshold;

    // Event declarations
    event ThresholdReached(uint64 price, string direction);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event ThresholdsUpdated(uint64 upper, uint64 lower);

    // Custom errors
    error Unauthorized();
    error InvalidThreshold();
    error PriceUpdateFailed();

    modifier onlyOwner() {
        if (msg.sender != owner) revert Unauthorized();
        _;
    }

    constructor(
        address _pythAddress,
        bytes32 _priceFeedId,
        uint64 _upperThreshold,
        uint64 _lowerThreshold
    ) {
        pyth = IPyth(_pythAddress);
        priceFeedId = _priceFeedId;
        owner = msg.sender;
        
        if (_upperThreshold <= _lowerThreshold) revert InvalidThreshold();
        upperThreshold = _upperThreshold;
        lowerThreshold = _lowerThreshold;
    }

    function updatePriceAndCheckThresholds(bytes[] calldata priceUpdateData) external payable {
        // Update the price feed
        uint fee = pyth.getUpdateFee(priceUpdateData);
        try pyth.updatePriceFeeds{value: fee}(priceUpdateData) {
            // Price update succeeded, now check thresholds
            PythStructs.Price memory currentPrice = pyth.getPrice(priceFeedId);
            uint64 price = uint64(currentPrice.price);

            if (price >= upperThreshold) {
                emit ThresholdReached(price, "above");
                _executeUpperThresholdAction();
            } else if (price <= lowerThreshold) {
                emit ThresholdReached(price, "below");
                _executeLowerThresholdAction();
            }
        } catch {
            revert PriceUpdateFailed();
        }

        // Refund any remaining ETH sent for the update
        if (address(this).balance > 0) {
            payable(msg.sender).transfer(address(this).balance);
        }
    }

    function setThresholds(uint64 _upperThreshold, uint64 _lowerThreshold) external onlyOwner {
        if (_upperThreshold <= _lowerThreshold) revert InvalidThreshold();
        upperThreshold = _upperThreshold;
        lowerThreshold = _lowerThreshold;
        emit ThresholdsUpdated(_upperThreshold, _lowerThreshold);
    }

    function transferOwnership(address newOwner) external onlyOwner {
        if (newOwner == address(0)) revert Unauthorized();
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Internal functions to be overridden for custom actions
    function _executeUpperThresholdAction() internal virtual {
        // Default implementation does nothing
    }

    function _executeLowerThresholdAction() internal virtual {
        // Default implementation does nothing
    }

    // Allow contract to receive ETH for price updates
    receive() external payable {}
}
```
