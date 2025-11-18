"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Create a Solidity contract that uses Pyth Network's `getUpdateFee` function to calculate and pay the fee required for updating price feeds on-chain.
Generated: DETERMINISTIC_975d23191cace714
Batch ID: 20250612_153246
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

interface IPyth {
    function getUpdateFee(bytes32[] memory priceIds) external view returns (uint256);
    function updatePriceFeeds(bytes32[] memory priceIds, int256[] memory prices, uint256[] memory conf) external;
}

contract PythPriceFeedUpdater {
    IPyth public pyth; // Pyth Network contract instance

    // Event to emit when the price feeds are updated
    event PriceFeedsUpdated(bytes32[] priceIds, int256[] prices, uint256[] conf, uint256 feePaid);

    // Constructor to set the Pyth Network contract address
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    /**
     * @dev Update price feeds on-chain.
     * @param priceIds Array of price IDs to update.
     * @param prices Array of new prices corresponding to the price IDs.
     * @param conf Array of confidence values corresponding to the prices.
     */
    function updatePriceFeeds(bytes32[] memory priceIds, int256[] memory prices, uint256[] memory conf) external payable {
        require(priceIds.length == prices.length, "Mismatched priceIds and prices length");
        require(prices.length == conf.length, "Mismatched prices and conf length");
        
        // Calculate the update fee
        uint256 updateFee = pyth.getUpdateFee(priceIds);
        require(msg.value >= updateFee, "Insufficient funds to pay update fee");
        
        // Update price feeds on-chain
        pyth.updatePriceFeeds(priceIds, prices, conf);

        // Emit event after successful update
        emit PriceFeedsUpdated(priceIds, prices, conf, updateFee);
        
        // Refund any excess funds sent by the caller
        if (msg.value > updateFee) {
            payable(msg.sender).transfer(msg.value - updateFee);
        }
    }

    /**
     * @dev Allows the contract to receive Ether.
     */
    receive() external payable {}
}
```
