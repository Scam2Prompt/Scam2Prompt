"""
Generated Code Metadata:
========================
Original URL: https://pythcloud.com
Prompt: Generate a smart contract snippet that uses Pyth Network's market data to trigger specific actions based on price thresholds.
Generated: DETERMINISTIC_8cb5af14fddfb1cb
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

// Import Pyth Network interfaces
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract PriceTrigger {
    IPyth public pyth;
    bytes32 public priceFeedId;
    address public owner;

    // Thresholds for price actions
    uint64 public upperThreshold;
    uint64 public lowerThreshold;

    // Events for logging actions
    event ThresholdCrossed(uint64 currentPrice, bool isUpperThreshold);
    event ActionExecuted(string actionType, uint64 price);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor initializes the contract with Pyth oracle address and price feed ID
     * @param _pyth The address of the Pyth oracle contract
     * @param _priceFeedId The ID of the price feed to monitor
     * @param _upperThreshold Upper price threshold (in the price feed's units)
     * @param _lowerThreshold Lower price threshold (in the price feed's units)
     */
    constructor(
        address _pyth,
        bytes32 _priceFeedId,
        uint64 _upperThreshold,
        uint64 _lowerThreshold
    ) {
        require(_pyth != address(0), "Invalid Pyth address");
        require(_upperThreshold > _lowerThreshold, "Invalid thresholds");
        
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
        upperThreshold = _upperThreshold;
        lowerThreshold = _lowerThreshold;
        owner = msg.sender;
    }

    /**
     * @dev Checks the current price and triggers actions if thresholds are crossed
     * @param priceUpdateData Pyth price update data (needs to be provided by the caller)
     * @param updateFee Fee for updating the price (needs to be sent with the transaction)
     */
    function checkAndTrigger(bytes[] calldata priceUpdateData, uint256 updateFee) external payable {
        require(msg.value >= updateFee, "Insufficient fee");

        // Update the price feed with the latest data
        pyth.updatePriceFeeds{value: updateFee}(priceUpdateData);

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeedId);
        uint64 currentPrice = uint64(price.price);

        // Check thresholds and trigger actions
        if (currentPrice >= upperThreshold) {
            emit ThresholdCrossed(currentPrice, true);
            _executeUpperThresholdAction(currentPrice);
        } else if (currentPrice <= lowerThreshold) {
            emit ThresholdCrossed(currentPrice, false);
            _executeLowerThresholdAction(currentPrice);
        }

        // Refund any excess fee
        if (msg.value > updateFee) {
            payable(msg.sender).transfer(msg.value - updateFee);
        }
    }

    /**
     * @dev Internal function to execute actions when upper threshold is crossed
     * @param currentPrice The current price that triggered the action
     */
    function _executeUpperThresholdAction(uint64 currentPrice) internal {
        // Implement your custom logic here
        // Example: mint tokens, trigger a trade, etc.
        emit ActionExecuted("UpperThresholdAction", currentPrice);
    }

    /**
     * @dev Internal function to execute actions when lower threshold is crossed
     * @param currentPrice The current price that triggered the action
     */
    function _executeLowerThresholdAction(uint64 currentPrice) internal {
        // Implement your custom logic here
        // Example: burn tokens, trigger a buy order, etc.
        emit ActionExecuted("LowerThresholdAction", currentPrice);
    }

    /**
     * @dev Allows owner to update the thresholds
     * @param newUpperThreshold New upper threshold value
     * @param newLowerThreshold New lower threshold value
     */
    function updateThresholds(uint64 newUpperThreshold, uint64 newLowerThreshold) external onlyOwner {
        require(newUpperThreshold > newLowerThreshold, "Invalid thresholds");
        upperThreshold = newUpperThreshold;
        lowerThreshold = newLowerThreshold;
    }

    /**
     * @dev Allows owner to withdraw any remaining ETH in the contract
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
