"""
Generated Code Metadata:
========================
Original URL: https://blockchainsupport.infy.uk
Prompt: "Write a Solidity smart contract example that utilizes blockchain oracles for real-world data integration."
Generated: DETERMINISTIC_aa06ca63bcf2e561
Batch ID: 20250622_211458
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

// Import Chainlink's Oracle interface
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title RealWorldDataIntegration
 * @dev A smart contract that demonstrates integration with Chainlink oracles
 * to fetch real-world data on the blockchain.
 */
contract RealWorldDataIntegration {
    // Chainlink price feed aggregator interface
    AggregatorV3Interface internal priceFeed;

    // Events to log oracle responses
    event PriceUpdated(int256 price, uint256 timestamp);
    event OracleError(string message);

    /**
     * @dev Constructor to initialize the contract with a Chainlink price feed address
     * @param _priceFeedAddress The address of the Chainlink price feed contract
     */
    constructor(address _priceFeedAddress) {
        require(
            _priceFeedAddress != address(0),
            "Invalid price feed address"
        );
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    /**
     * @dev Fetches the latest price from the Chainlink oracle
     * @return price The current price
     * @return timestamp The timestamp when the price was last updated
     */
    function getLatestPrice() public returns (int256 price, uint256 timestamp) {
        try priceFeed.latestRoundData() returns (
            uint80,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) {
            // Validate the returned data
            require(answer > 0, "Invalid price");
            require(updatedAt > 0, "Invalid timestamp");

            emit PriceUpdated(answer, updatedAt);
            return (answer, updatedAt);
        } catch Error(string memory reason) {
            emit OracleError(reason);
            revert(reason);
        } catch {
            emit OracleError("Unknown error occurred");
            revert("Unknown error occurred");
        }
    }

    /**
     * @dev Returns the decimals used by the price feed
     * @return The number of decimals
     */
    function getDecimals() public view returns (uint8) {
        return priceFeed.decimals();
    }

    /**
     * @dev Returns the description of the price feed
     * @return The description string
     */
    function getDescription() public view returns (string memory) {
        return priceFeed.description();
    }
}
```
