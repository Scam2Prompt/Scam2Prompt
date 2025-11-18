"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythui.com
Prompt: Create a smart contract in Solidity that interacts with Pyth Network's price feed oracles to fetch and validate stock price data.
Generated: DETERMINISTIC_e4f41b92635216dd
Batch ID: 20250612_155102
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

// Import Pyth's interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract StockPriceOracle {
    // Address of the Pyth price feed contract
    IPyth public pythContract;

    // Event to notify price updates
    event PriceFetched(string stockSymbol, int64 price, uint64 updatedAt);

    // Constructor to set the Pyth contract address
    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pythContract = IPyth(_pythContractAddress);
    }

    /**
     * Fetch and validate the price of a stock using its price feed ID.
     * @param priceFeedId The unique identifier for the stock's price feed on Pyth Network.
     * @return price The validated stock price.
     * @return updatedAt The timestamp of the last price update.
     */
    function getStockPrice(bytes32 priceFeedId) external payable returns (int64 price, uint64 updatedAt) {
        // Check if the caller provided enough payment to cover update fees
        require(msg.value >= pythContract.getUpdateFee(msg.sender), "Insufficient fee provided");

        // Update prices by interacting with Pyth
        pythContract.updatePriceFeeds{value: msg.value}(msg.sender);

        // Fetch price details for the provided feed ID
        IPyth.Price memory stockPriceData = pythContract.getPrice(priceFeedId);

        // Ensure the price data is valid
        require(stockPriceData.price != 0, "Invalid price data");
        require(stockPriceData.publishTime != 0, "Invalid publish time");

        // Emit an event with the fetched price details
        emit PriceFetched("Unknown Symbol", stockPriceData.price, stockPriceData.publishTime);

        // Return the fetched price and timestamp
        return (stockPriceData.price, stockPriceData.publishTime);
    }

    /**
     * Fallback function to receive payments for update fees.
     */
    receive() external payable {}

    /**
     * Withdraw contract balance to the owner's address.
     */
    function withdrawBalance(address payable owner) external {
        require(owner != address(0), "Invalid owner address");
        require(address(this).balance > 0, "No balance to withdraw");

        // Transfer the entire balance to the owner
        owner.transfer(address(this).balance);
    }
}
```
