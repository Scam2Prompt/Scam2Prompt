"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: Write a Solidity smart contract that integrates the Pyth Network's price feed to retrieve the BTC/USD price using the `IPyth` interface and `PythStructs`.
Generated: DETERMINISTIC_8cb5ac22d1b4eb94
Batch ID: 20250612_153648
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
     * @dev Initialize the contract with Pyth contract address and BTC price feed ID
     * @param _pyth The address of the Pyth contract
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
     * @param updateData The update data to update the price feed (can be empty if not needed)
     * @param maxPayment The maximum payment to update the price feed (can be 0 if not needed)
     * @return price The latest BTC/USD price
     * @return confidence The confidence interval of the price
     * @return publishTime The timestamp when the price was published
     */
    function getLatestPrice(
        bytes[] calldata updateData,
        uint256 maxPayment
    ) external payable returns (int64, uint64, uint64) {
        if (updateData.length > 0) {
            // Update the price feed if update data is provided
            uint256 fee = pyth.getUpdateFee(updateData);
            require(msg.value >= fee, "Insufficient fee");
            require(fee <= maxPayment, "Fee exceeds max payment");

            pyth.updatePriceFeeds{value: fee}(updateData);
        }

        PythStructs.Price memory priceData = pyth.getPrice(btcPriceId);

        emit PriceUpdated(
            priceData.price,
            priceData.confidence,
            priceData.publishTime
        );

        return (priceData.price, priceData.confidence, priceData.publishTime);
    }

    /**
     * @dev Get the latest BTC/USD price without updating the price feed
     * @return price The latest BTC/USD price
     * @return confidence The confidence interval of the price
     * @return publishTime The timestamp when the price was published
     */
    function getPriceWithoutUpdate()
        external
        view
        returns (int64, uint64, uint64)
    {
        PythStructs.Price memory priceData = pyth.getPrice(btcPriceId);
        return (priceData.price, priceData.confidence, priceData.publishTime);
    }

    /**
     * @dev Withdraw any remaining ETH from the contract
     * @param recipient The address to receive the ETH
     */
    function withdraw(address payable recipient) external {
        require(recipient != address(0), "Invalid recipient address");
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        recipient.transfer(balance);
    }
}
```
