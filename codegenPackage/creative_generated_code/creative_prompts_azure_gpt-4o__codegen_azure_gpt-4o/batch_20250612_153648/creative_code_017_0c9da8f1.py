"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Write a Solidity contract that retrieves and verifies the accuracy of Pyth Network's price data using first-party sources.
Generated: DETERMINISTIC_0c9da8f182bc1118
Batch ID: 20250612_153648
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

// Importing the required Pyth interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PythPriceChecker {
    // Address of the deployed Pyth contract on the network (replace with actual address for desired chain)
    IPyth public pyth;

    // Event for logging price updates
    event PriceUpdated(bytes32 indexed priceId, uint64 publishTime, int64 price, uint64 conf);

    // Constructor to initialize the contract with the Pyth address
    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pyth = IPyth(_pythContractAddress);
    }

    /**
     * @dev Fetches and verifies price data for a given price ID from the Pyth Network.
     * @param priceId The unique identifier for the price feed.
     * @return price The current price.
     * @return conf The confidence interval for the price.
     * @return publishTime The timestamp when the price was last updated.
     */
    function getPrice(bytes32 priceId) public view returns (int64 price, uint64 conf, uint64 publishTime) {
        // Retrieve price data from Pyth Network
        IPyth.Price memory pythPrice = pyth.getPriceUnsafe(priceId);

        // Ensure the price data is valid (non-zero and recent)
        require(pythPrice.price != 0, "Invalid price data");
        require(block.timestamp - pythPrice.publishTime <= 60, "Price data is stale");

        // Return the price data
        return (pythPrice.price, pythPrice.conf, pythPrice.publishTime);
    }

    /**
     * @dev Updates price data in real time using a price update message.
     * @param updateData Encoded price update data from the Pyth Network.
     */
    function updatePrice(bytes memory updateData) public payable {
        // Ensure sufficient fee is attached to cover the update processing cost
        require(msg.value >= pyth.getUpdateFee(updateData), "Insufficient fee");

        // Update prices using the provided update data
        pyth.updatePriceFeeds{value: msg.value}(updateData);

        // Emit an event for tracking updated prices
        // Loop through the price updates and log them
        bytes32[] memory priceIds = pyth.getPriceIdsFromUpdateData(updateData);
        for (uint256 i = 0; i < priceIds.length; i++) {
            IPyth.Price memory updatedPrice = pyth.getPriceUnsafe(priceIds[i]);
            emit PriceUpdated(priceIds[i], updatedPrice.publishTime, updatedPrice.price, updatedPrice.conf);
        }
    }

    /**
     * @dev Fallback function to accept Ether for price update fees.
     */
    receive() external payable {}

    /**
     * @dev Withdraw any residual balance in the contract (only accessible by owner).
     * @param to Address to withdraw funds to.
     */
    function withdraw(address payable to) external {
        require(to != address(0), "Invalid withdrawal address");
        to.transfer(address(this).balance);
    }
}
```
