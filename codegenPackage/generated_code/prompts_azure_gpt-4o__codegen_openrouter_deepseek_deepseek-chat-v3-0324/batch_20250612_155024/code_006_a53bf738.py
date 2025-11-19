"""
Generated Code Metadata:
========================
Original URL: https://pythpro.com
Prompt: How can I integrate Pyth price feed oracles into a DeFi application for real-time asset pricing?
Generated: DETERMINISTIC_a53bf738ca248e73
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

contract PythPriceFeed {
    IPyth public pyth;
    bytes32 public priceFeedId;
    
    event PriceUpdated(int64 price, uint64 conf, int32 expo, uint publishTime);
    
    /**
     * @dev Initialize the contract with Pyth oracle address and price feed ID
     * @param _pyth The address of the Pyth oracle contract
     * @param _priceFeedId The ID of the price feed to track
     */
    constructor(address _pyth, bytes32 _priceFeedId) {
        require(_pyth != address(0), "Invalid Pyth address");
        require(_priceFeedId != bytes32(0), "Invalid price feed ID");
        
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }
    
    /**
     * @dev Get the latest price from Pyth oracle
     * @return price The current price
     * @return conf The confidence interval
     * @return expo The exponent for the price
     * @return publishTime The timestamp when price was published
     */
    function getLatestPrice() public view returns (
        int64 price,
        uint64 conf,
        int32 expo,
        uint publishTime
    ) {
        PythStructs.Price memory currentPrice = pyth.getPrice(priceFeedId);
        return (
            currentPrice.price,
            currentPrice.conf,
            currentPrice.expo,
            currentPrice.publishTime
        );
    }
    
    /**
     * @dev Update the price by submitting the price update data from Pyth
     * @param updateData The price update data from Pyth
     */
    function updatePrice(bytes[] calldata updateData) external payable {
        // Pay the fee to update the price
        uint fee = pyth.getUpdateFee(updateData);
        require(msg.value >= fee, "Insufficient fee");
        
        // Submit the price update
        pyth.updatePriceFeeds{value: fee}(updateData);
        
        // Get the latest price after update
        (int64 price, uint64 conf, int32 expo, uint publishTime) = getLatestPrice();
        
        emit PriceUpdated(price, conf, expo, publishTime);
    }
    
    /**
     * @dev Withdraw any excess ETH sent to the contract
     */
    function withdrawExcessEth() external {
        uint balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(msg.sender).transfer(balance);
    }
    
    // Fallback function to receive ETH
    receive() external payable {}
}
```
