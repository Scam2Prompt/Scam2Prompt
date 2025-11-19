"""
Generated Code Metadata:
========================
Original URL: https://pythnew.com
Prompt: Provide a step-by-step guide to integrating Pyth Network's price feed oracles into a DeFi protocol for accurate market data.
Generated: DETERMINISTIC_ead953a96d29aea0
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

contract PythOracleIntegration {
    IPyth public pyth;
    bytes32 public priceFeedId;
    
    // Events
    event PriceUpdated(int64 price, uint64 publishTime);
    event PriceFeedIdSet(bytes32 priceFeedId);
    
    /**
     * @dev Initialize the contract with Pyth contract address
     * @param _pyth The address of the Pyth contract
     */
    constructor(address _pyth) {
        require(_pyth != address(0), "Invalid Pyth address");
        pyth = IPyth(_pyth);
    }
    
    /**
     * @dev Set the price feed ID for the asset
     * @param _priceFeedId The Pyth price feed ID for the asset
     */
    function setPriceFeedId(bytes32 _priceFeedId) external {
        require(_priceFeedId != bytes32(0), "Invalid price feed ID");
        priceFeedId = _priceFeedId;
        emit PriceFeedIdSet(_priceFeedId);
    }
    
    /**
     * @dev Get the latest price from Pyth oracle
     * @return price The current price
     * @return publishTime The timestamp when the price was published
     */
    function getLatestPrice() public view returns (int64 price, uint64 publishTime) {
        require(priceFeedId != bytes32(0), "Price feed ID not set");
        
        PythStructs.Price memory pythPrice = pyth.getPrice(priceFeedId);
        return (pythPrice.price, pythPrice.publishTime);
    }
    
    /**
     * @dev Update the price by submitting the price update data from Pyth
     * @param updateData The Pyth price update data
     */
    function updatePrice(bytes[] calldata updateData) external payable {
        require(updateData.length > 0, "No update data provided");
        
        // Pay the fee to update the price
        uint fee = pyth.getUpdateFee(updateData);
        require(msg.value >= fee, "Insufficient fee");
        
        // Submit the price update
        pyth.updatePriceFeeds{value: fee}(updateData);
        
        // Get the latest price after update
        (int64 price, uint64 publishTime) = getLatestPrice();
        emit PriceUpdated(price, publishTime);
    }
    
    /**
     * @dev Withdraw any excess ETH sent to the contract
     */
    function withdrawExcessEth() external {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(msg.sender).transfer(balance);
    }
    
    // Receive function to accept ETH
    receive() external payable {}
}
```
