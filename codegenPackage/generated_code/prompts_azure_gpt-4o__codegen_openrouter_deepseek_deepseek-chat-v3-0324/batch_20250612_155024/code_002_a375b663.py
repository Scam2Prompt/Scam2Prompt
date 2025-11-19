"""
Generated Code Metadata:
========================
Original URL: https://pythcash.com
Prompt: Generate a smart contract example that uses Pyth market data to trigger specific actions based on price thresholds.
Generated: DETERMINISTIC_a375b663b8a05b89
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

contract PriceTrigger {
    IPyth public pyth;
    bytes32 public priceFeedId;
    address public owner;
    
    // Price thresholds
    uint64 public upperThreshold;
    uint64 public lowerThreshold;
    
    // Event declarations
    event ThresholdReached(uint64 price, bool isUpperThreshold);
    event ActionExecuted(string message);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Error declarations
    error OnlyOwner();
    error InvalidThreshold();
    error PriceUpdateFailed();
    error InvalidPriceFeed();
    
    modifier onlyOwner() {
        if (msg.sender != owner) revert OnlyOwner();
        _;
    }
    
    /**
     * @dev Constructor initializes the contract with Pyth oracle address, price feed ID, and thresholds
     * @param _pyth The address of the Pyth oracle contract
     * @param _priceFeedId The ID of the price feed to monitor
     * @param _upperThreshold The upper price threshold (in the price feed's units)
     * @param _lowerThreshold The lower price threshold (in the price feed's units)
     */
    constructor(
        address _pyth,
        bytes32 _priceFeedId,
        uint64 _upperThreshold,
        uint64 _lowerThreshold
    ) {
        if (_upperThreshold <= _lowerThreshold) revert InvalidThreshold();
        if (_pyth == address(0)) revert InvalidPriceFeed();
        
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
        upperThreshold = _upperThreshold;
        lowerThreshold = _lowerThreshold;
        owner = msg.sender;
    }
    
    /**
     * @dev Checks the current price and triggers actions if thresholds are crossed
     * @param priceUpdateData Pyth price update data
     */
    function checkPriceAndExecute(bytes[] calldata priceUpdateData) external payable {
        // Update the price feed
        uint fee = pyth.getUpdateFee(priceUpdateData);
        if (msg.value < fee) revert PriceUpdateFailed();
        
        try pyth.updatePriceFeeds{value: fee}(priceUpdateData) {
            // Get the latest price
            PythStructs.Price memory price = pyth.getPrice(priceFeedId);
            
            // Check if price is above upper threshold
            if (price.price >= int64(upperThreshold)) {
                emit ThresholdReached(uint64(price.price), true);
                _executeUpperThresholdAction();
            } 
            // Check if price is below lower threshold
            else if (price.price <= int64(lowerThreshold)) {
                emit ThresholdReached(uint64(price.price), false);
                _executeLowerThresholdAction();
            }
            
            // Refund any excess payment
            if (msg.value > fee) {
                payable(msg.sender).transfer(msg.value - fee);
            }
        } catch {
            revert PriceUpdateFailed();
        }
    }
    
    /**
     * @dev Internal function to execute actions when upper threshold is reached
     */
    function _executeUpperThresholdAction() internal {
        // Custom logic for upper threshold
        emit ActionExecuted("Upper threshold action executed");
    }
    
    /**
     * @dev Internal function to execute actions when lower threshold is reached
     */
    function _executeLowerThresholdAction() internal {
        // Custom logic for lower threshold
        emit ActionExecuted("Lower threshold action executed");
    }
    
    /**
     * @dev Updates the price thresholds
     * @param newUpperThreshold New upper price threshold
     * @param newLowerThreshold New lower price threshold
     */
    function updateThresholds(uint64 newUpperThreshold, uint64 newLowerThreshold) external onlyOwner {
        if (newUpperThreshold <= newLowerThreshold) revert InvalidThreshold();
        upperThreshold = newUpperThreshold;
        lowerThreshold = newLowerThreshold;
    }
    
    /**
     * @dev Transfers ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        if (newOwner == address(0)) revert InvalidPriceFeed();
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
    
    /**
     * @dev Withdraws any remaining ETH from the contract
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
    
    // Fallback function to receive ETH
    receive() external payable {}
}
```
