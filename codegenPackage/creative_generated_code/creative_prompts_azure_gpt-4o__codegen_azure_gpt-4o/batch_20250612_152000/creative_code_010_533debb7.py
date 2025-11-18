"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45y54.pages.dev
Prompt: Provide a Solidity example for implementing Pyth's pull-based oracle mechanism to fetch price updates only when triggered by a smart contract.
Generated: DETERMINISTIC_533debb7dd572f3b
Batch ID: 20250612_152000
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

// Import Pyth's interface for interacting with their oracle.
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PythPriceFetcher {
    // Address of the deployed Pyth contract on the target network.
    IPyth public pythContract;

    // Event to log fetched price updates.
    event PriceUpdated(bytes32 priceFeedId, int64 price, uint64 publishTime);

    // Mapping to store latest fetched prices for specific feeds.
    mapping(bytes32 => int64) public latestPrices;

    // Constructor to initialize the Pyth contract address.
    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pythContract = IPyth(_pythContractAddress);
    }

    /**
     * @notice Fetch the latest price for a specific price feed from the Pyth oracle.
     * @param priceFeedId The unique identifier of the price feed.
     * @param updateData Encoded update data provided by Pyth.
     */
    function fetchPrice(bytes32 priceFeedId, bytes calldata updateData) external payable {
        // Update prices by calling the Pyth contract's updatePriceFeeds method.
        // The caller must provide sufficient funds to cover the update fee.
        uint fee = pythContract.getUpdateFee(updateData);
        require(msg.value >= fee, "Insufficient fee");

        pythContract.updatePriceFeeds{value: fee}(updateData);

        // Get the price information for the requested price feed.
        IPyth.Price memory price = pythContract.getPrice(priceFeedId);

        // Store the latest price in the mapping.
        latestPrices[priceFeedId] = price.price;

        // Emit an event with the updated price details.
        emit PriceUpdated(priceFeedId, price.price, price.publishTime);
    }

    /**
     * @notice Get the latest price stored for a specific price feed.
     * @param priceFeedId The unique identifier of the price feed.
     * @return price The latest price fetched and stored in the contract.
     */
    function getLatestPrice(bytes32 priceFeedId) external view returns (int64) {
        require(latestPrices[priceFeedId] != 0, "Price not available");
        return latestPrices[priceFeedId];
    }

    /**
     * @notice Fallback function to handle accidental Ether transfers.
     */
    receive() external payable {
        revert("Do not send Ether directly");
    }

    /**
     * @notice Withdraw any remaining Ether balance from the contract.
     * @param recipient The address to send the Ether to.
     */
    function withdrawEther(address payable recipient) external {
        require(recipient != address(0), "Invalid recipient address");
        recipient.transfer(address(this).balance);
    }
}
```
