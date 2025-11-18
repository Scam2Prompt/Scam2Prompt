"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Provide code to implement Pyth Network's on-demand price feed updates in a smart contract deployed on Optimism.
Generated: DETERMINISTIC_0306cd3c23f492d8
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready code for implementing Pyth Network's on-demand price feed updates in a smart contract deployed on Optimism. This example assumes Solidity as the programming language and the use of the Pyth price feed.

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import Pyth interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract PythPriceFeed {
    // Address of the Pyth contract on Optimism (replace with the correct address for the network)
    address public immutable pythContract;

    // A mapping to store the latest price information by feed ID
    mapping(bytes32 => int64) public latestPrices;

    // A mapping to store the latest price confidence intervals by feed ID
    mapping(bytes32 => uint64) public latestConfidenceIntervals;

    // Event to notify when price is updated
    event PriceUpdated(bytes32 indexed priceFeedId, int64 price, uint64 confidenceInterval);

    /**
     * @dev Constructor to initialize the Pyth contract address.
     * @param _pythContract Address of the deployed Pyth contract on Optimism.
     */
    constructor(address _pythContract) {
        require(_pythContract != address(0), "Invalid Pyth contract address");
        pythContract = _pythContract;
    }

    /**
     * @dev Function to update the price for a given feed ID using Pyth.
     * @param priceFeedId The ID of the price feed to update.
     * @param updateData The update data obtained off-chain from Pyth's API.
     */
    function updatePrice(bytes32 priceFeedId, bytes[] calldata updateData) external payable {
        // Retrieve Pyth instance
        IPyth pyth = IPyth(pythContract);

        // Update price feeds using the off-chain data provided
        pyth.updatePriceFeeds{value: msg.value}(updateData);

        // Fetch the updated price information from Pyth
        (int64 price, uint64 confidenceInterval) = pyth.getPrice(priceFeedId);

        // Store the latest price and confidence interval
        latestPrices[priceFeedId] = price;
        latestConfidenceIntervals[priceFeedId] = confidenceInterval;

        // Emit event to notify about the price update
        emit PriceUpdated(priceFeedId, price, confidenceInterval);
    }

    /**
     * @dev Fallback function to refund any excess Ether sent to the contract.
     */
    receive() external payable {
        // Refund any Ether sent to the contract by mistake
        if (msg.value > 0) {
            payable(msg.sender).transfer(msg.value);
        }
    }

    /**
     * @dev Getter function to fetch the latest price of a feed ID.
     * @param priceFeedId The ID of the price feed.
     * @return price The latest price.
     */
    function getLatestPrice(bytes32 priceFeedId) external view returns (int64 price) {
        return latestPrices[priceFeedId];
    }

    /**
     * @dev Getter function to fetch the latest confidence interval of a feed ID.
     * @param priceFeedId The ID of the price feed.
     * @return confidenceInterval The latest confidence interval.
     */
    function getLatestConfidenceInterval(bytes32 priceFeedId) external view returns (uint64 confidenceInterval) {
        return latestConfidenceIntervals[priceFeedId];
    }
}
