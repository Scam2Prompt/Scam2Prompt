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

// Import Chainlink's interfaces for interacting with oracles
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract OracleIntegration {
    // State variable to store the address of the Chainlink price feed
    AggregatorV3Interface internal priceFeed;

    // Event to emit the latest price fetched from the oracle
    event LatestPriceFetched(int256 price);

    /**
     * @dev Constructor to initialize the contract with the Chainlink price feed address.
     * @param _priceFeedAddress The address of the Chainlink price feed contract.
     */
    constructor(address _priceFeedAddress) {
        require(_priceFeedAddress != address(0), "Invalid price feed address");
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    /**
     * @dev Fetches the latest price from the Chainlink oracle.
     * @return The latest price as an integer.
     */
    function getLatestPrice() public returns (int256) {
        // Fetch the latest round data from the price feed
        (
            uint80 roundID,
            int256 price,
            uint256 startedAt,
            uint256 timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();

        // Ensure the price data is valid
        require(price > 0, "Invalid price data");
        require(answeredInRound >= roundID, "Stale price data");

        // Emit the fetched price
        emit LatestPriceFetched(price);

        return price;
    }

    /**
     * @dev Returns the decimals used by the price feed.
     * @return The number of decimals.
     */
    function getDecimals() public view returns (uint8) {
        return priceFeed.decimals();
    }

    /**
     * @dev Returns the description of the price feed.
     * @return The description string.
     */
    function getDescription() public view returns (string memory) {
        return priceFeed.description();
    }

    /**
     * @dev Returns the version of the price feed contract.
     * @return The version number.
     */
    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }
}
```

### Notes:
- This contract uses Chainlink's `AggregatorV3Interface` to interact with a price feed oracle.
- Replace `_priceFeedAddress` in the constructor with the address of the desired Chainlink price feed (e.g., ETH/USD price feed on your target network).
- Ensure the Chainlink contracts are properly installed in your project (`npm install @chainlink/contracts`).
- Deploy the contract on a network supported by Chainlink oracles.
