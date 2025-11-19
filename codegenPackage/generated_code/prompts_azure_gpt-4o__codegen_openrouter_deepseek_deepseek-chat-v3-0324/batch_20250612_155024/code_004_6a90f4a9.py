"""
Generated Code Metadata:
========================
Original URL: https://pythshop.com
Prompt: Generate code for a smart contract that uses Pyth Network's price feed oracles to trigger actions based on specific market data thresholds.
Generated: DETERMINISTIC_6a90f4a9759754e4
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
    
    // Threshold values (scaled to 1e18)
    uint256 public upperThreshold;
    uint256 public lowerThreshold;
    
    // Last triggered price
    uint256 public lastTriggeredPrice;
    
    // Events
    event ThresholdReached(uint256 price, bool isUpperThreshold);
    event ThresholdsUpdated(uint256 newUpper, uint256 newLower);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Custom errors
    error Unauthorized();
    error InvalidThresholds();
    error PriceFeedNotAvailable();
    
    modifier onlyOwner() {
        if (msg.sender != owner) revert Unauthorized();
        _;
    }
    
    /**
     * @dev Constructor to initialize the contract
     * @param _pyth Pyth oracle contract address
     * @param _priceFeedId Pyth price feed ID for the asset
     * @param _upperThreshold Upper price threshold (scaled to 1e18)
     * @param _lowerThreshold Lower price threshold (scaled to 1e18)
     */
    constructor(
        address _pyth,
        bytes32 _priceFeedId,
        uint256 _upperThreshold,
        uint256 _lowerThreshold
    ) {
        if (_upperThreshold <= _lowerThreshold) revert InvalidThresholds();
        
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
        owner = msg.sender;
        upperThreshold = _upperThreshold;
        lowerThreshold = _lowerThreshold;
    }
    
    /**
     * @dev Check current price and trigger actions if thresholds are crossed
     * @param priceUpdateData Pyth price update data
     */
    function checkAndTrigger(bytes[] calldata priceUpdateData) external payable {
        // Update the price feed with the latest data
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);
        
        // Get the latest price
        PythStructs.Price memory priceData = pyth.getPrice(priceFeedId);
        
        // Check if price is available
        if (priceData.price <= 0) revert PriceFeedNotAvailable();
        
        // Convert price to 1e18 scale
        uint256 currentPrice = uint256(uint64(priceData.price)) * 
            10 ** (18 - uint256(uint32(-priceData.expo)));
        
        // Check thresholds
        if (currentPrice >= upperThreshold) {
            lastTriggeredPrice = currentPrice;
            emit ThresholdReached(currentPrice, true);
            // Add your custom logic for upper threshold here
        } else if (currentPrice <= lowerThreshold) {
            lastTriggeredPrice = currentPrice;
            emit ThresholdReached(currentPrice, false);
            // Add your custom logic for lower threshold here
        }
    }
    
    /**
     * @dev Update the price thresholds
     * @param newUpper New upper threshold (scaled to 1e18)
     * @param newLower New lower threshold (scaled to 1e18)
     */
    function updateThresholds(uint256 newUpper, uint256 newLower) external onlyOwner {
        if (newUpper <= newLower) revert InvalidThresholds();
        
        upperThreshold = newUpper;
        lowerThreshold = newLower;
        emit ThresholdsUpdated(newUpper, newLower);
    }
    
    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        if (newOwner == address(0)) revert Unauthorized();
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
    
    /**
     * @dev Withdraw any remaining ETH from the contract
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
    
    // Receive function to accept ETH for price updates
    receive() external payable {}
}
```
