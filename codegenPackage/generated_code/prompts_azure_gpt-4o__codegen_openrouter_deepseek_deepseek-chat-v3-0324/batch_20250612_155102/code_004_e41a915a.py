"""
Generated Code Metadata:
========================
Original URL: https://pythclub.com
Prompt: Write a smart contract in Solidity that uses Pyth Network price feed oracles to validate asset prices before executing a transaction.
Generated: DETERMINISTIC_e41a915aaf670e59
Batch ID: 20250612_155102
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

contract PythPriceValidator {
    IPyth public pyth;
    bytes32 public priceFeedId;
    uint64 public validDuration;

    event PriceValidationSuccess(uint64 timestamp, int64 price, uint64 conf);
    event PriceValidationFailure(string reason);

    constructor(
        address _pythContract,
        bytes32 _priceFeedId,
        uint64 _validDuration
    ) {
        pyth = IPyth(_pythContract);
        priceFeedId = _priceFeedId;
        validDuration = _validDuration;
    }

    function validateAndExecute(
        bytes[] calldata priceUpdateData,
        uint256 minPrice,
        uint256 maxPrice,
        bytes calldata executionData
    ) external payable {
        // Update the price feed
        uint fee = pyth.getUpdateFee(priceUpdateData);
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeedId);

        // Check if price is recent enough
        if (price.publishTime + validDuration < block.timestamp) {
            emit PriceValidationFailure("Price is too old");
            revert("Price is too old");
        }

        // Check if price is within acceptable range
        if (uint64(price.price) < minPrice || uint64(price.price) > maxPrice) {
            emit PriceValidationFailure("Price out of range");
            revert("Price out of range");
        }

        // Check if confidence interval is acceptable
        if (price.conf > uint64(price.price) / 10) { // 10% threshold
            emit PriceValidationFailure("Confidence too wide");
            revert("Confidence too wide");
        }

        emit PriceValidationSuccess(price.publishTime, price.price, price.conf);

        // Execute the transaction if all checks pass
        (bool success, ) = address(this).call(executionData);
        require(success, "Execution failed");
    }

    // Fallback function to receive funds
    receive() external payable {}
}
```
