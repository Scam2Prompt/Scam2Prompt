"""
Generated Code Metadata:
========================
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Create a Solidity contract that uses Pyth Network's `getUpdateFee` function to calculate and pay the fee required for updating price feeds on-chain.
Generated: DETERMINISTIC_975d23191cace714
Batch ID: 20250612_153246
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

contract PythFeeCalculator {
    IPyth public pyth;

    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @notice Calculates the fee required to update the given price feed IDs
     * @param priceIds Array of price feed IDs to update
     * @return updateFee The fee required in wei
     */
    function calculateUpdateFee(bytes[] calldata priceIds) public view returns (uint256 updateFee) {
        require(priceIds.length > 0, "No price IDs provided");
        updateFee = pyth.getUpdateFee(priceIds);
        return updateFee;
    }

    /**
     * @notice Updates the price feeds by paying the required fee
     * @param priceIds Array of price feed IDs to update
     * @param updateData Array of update data for the price feeds
     * @return priceUpdateFee The actual fee paid in wei
     */
    function updatePriceFeeds(
        bytes[] calldata priceIds,
        bytes[] calldata updateData
    ) external payable returns (uint256 priceUpdateFee) {
        require(priceIds.length > 0, "No price IDs provided");
        require(priceIds.length == updateData.length, "Mismatched array lengths");

        uint256 requiredFee = pyth.getUpdateFee(priceIds);
        require(msg.value >= requiredFee, "Insufficient fee");

        priceUpdateFee = pyth.updatePriceFeeds{value: requiredFee}(updateData);

        // Refund any excess payment
        if (msg.value > requiredFee) {
            payable(msg.sender).transfer(msg.value - requiredFee);
        }

        return priceUpdateFee;
    }

    /**
     * @notice Withdraws any ETH accidentally sent to this contract
     * @param recipient Address to receive the ETH
     */
    function withdrawETH(address payable recipient) external {
        require(recipient != address(0), "Invalid recipient address");
        recipient.transfer(address(this).balance);
    }
}
```
