"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Write a Solidity smart contract that integrates the Pyth Network's price feed oracle to fetch the BTC/USD price using the `IPyth` interface and `getPrice` method.
Generated: DETERMINISTIC_4c5cc00f900d8200
Batch ID: 20250612_152000
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

contract PythBTCPriceFeed {
    IPyth public pyth;
    bytes32 public btcPriceId;

    event PriceUpdated(int64 price, uint64 confidence, uint64 publishTime);

    /**
     * @dev Initialize the contract with Pyth oracle address and BTC price feed ID
     * @param _pyth The address of the Pyth oracle contract
     * @param _btcPriceId The price feed ID for BTC/USD
     */
    constructor(address _pyth, bytes32 _btcPriceId) {
        require(_pyth != address(0), "Invalid Pyth address");
        require(_btcPriceId != bytes32(0), "Invalid price feed ID");
        
        pyth = IPyth(_pyth);
        btcPriceId = _btcPriceId;
    }

    /**
     * @dev Get the latest BTC/USD price from Pyth Network
     * @return price The current BTC price
     * @return confidence The confidence interval of the price
     * @return publishTime The timestamp when the price was published
     */
    function getLatestPrice() public view returns (int64, uint64, uint64) {
        PythStructs.Price memory priceData = pyth.getPrice(btcPriceId);
        return (priceData.price, priceData.confidence, priceData.publishTime);
    }

    /**
     * @dev Update the price by paying for the update fee
     * @param updateData The signed price update data from Pyth
     */
    function updatePrice(bytes[] calldata updateData) external payable {
        // Get the update fee required
        uint fee = pyth.getUpdateFee(updateData);
        require(msg.value >= fee, "Insufficient fee");

        // Update the price data
        pyth.updatePriceFeeds{value: fee}(updateData);

        // Refund any excess payment
        if (msg.value > fee) {
            payable(msg.sender).transfer(msg.value - fee);
        }

        // Get and emit the latest price
        (int64 price, uint64 confidence, uint64 publishTime) = getLatestPrice();
        emit PriceUpdated(price, confidence, publishTime);
    }

    /**
     * @dev Withdraw any remaining ETH from the contract
     * @param recipient The address to receive the ETH
     */
    function withdraw(address payable recipient) external {
        require(recipient != address(0), "Invalid recipient address");
        recipient.transfer(address(this).balance);
    }
}
```
