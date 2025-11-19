"""
Generated Code Metadata:
========================
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: "Develop an oracle that utilizes EigenLayer's restaked ETH to provide a trustworthy price feed on Ethereum."
Generated: DETERMINISTIC_6b320b8730d999dc
Batch ID: 20250622_205836
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

/**
 * @title PriceOracle
 * @dev A decentralized oracle that utilizes EigenLayer's restaked ETH to provide a trustworthy price feed on Ethereum.
 */
contract PriceOracle {
    // Event emitted when a new price is submitted
    event PriceSubmitted(address indexed submitter, uint256 price, uint256 timestamp);

    // Struct to store price data
    struct PriceData {
        uint256 price; // Price value
        uint256 timestamp; // Timestamp of the price submission
    }

    // Mapping to store submitted prices by address
    mapping(address => PriceData) public submittedPrices;

    // Aggregated price data
    uint256 public aggregatedPrice;
    uint256 public lastUpdated;

    // Minimum number of submissions required for aggregation
    uint256 public constant MIN_SUBMISSIONS = 3;

    // Array to store addresses of trusted submitters (EigenLayer restakers)
    address[] public trustedSubmitters;

    // Modifier to restrict access to trusted submitters
    modifier onlyTrustedSubmitter() {
        require(isTrustedSubmitter(msg.sender), "Not a trusted submitter");
        _;
    }

    /**
     * @dev Constructor to initialize the trusted submitters.
     * @param _trustedSubmitters Array of addresses of trusted submitters.
     */
    constructor(address[] memory _trustedSubmitters) {
        require(_trustedSubmitters.length > 0, "Trusted submitters required");
        trustedSubmitters = _trustedSubmitters;
    }

    /**
     * @dev Function to check if an address is a trusted submitter.
     * @param submitter Address to check.
     * @return bool True if the address is a trusted submitter, false otherwise.
     */
    function isTrustedSubmitter(address submitter) public view returns (bool) {
        for (uint256 i = 0; i < trustedSubmitters.length; i++) {
            if (trustedSubmitters[i] == submitter) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Function for trusted submitters to submit a price.
     * @param price The price value to submit.
     */
    function submitPrice(uint256 price) external onlyTrustedSubmitter {
        require(price > 0, "Price must be greater than zero");

        // Store the submitted price
        submittedPrices[msg.sender] = PriceData(price, block.timestamp);

        emit PriceSubmitted(msg.sender, price, block.timestamp);

        // Attempt to aggregate prices if enough submissions are available
        aggregatePrices();
    }

    /**
     * @dev Internal function to aggregate prices from trusted submitters.
     */
    function aggregatePrices() internal {
        uint256 totalPrice = 0;
        uint256 validSubmissions = 0;

        for (uint256 i = 0; i < trustedSubmitters.length; i++) {
            address submitter = trustedSubmitters[i];
            PriceData memory data = submittedPrices[submitter];

            // Ensure the price is recent (within the last hour)
            if (data.timestamp > block.timestamp - 1 hours) {
                totalPrice += data.price;
                validSubmissions++;
            }
        }

        // Update the aggregated price if enough valid submissions are available
        if (validSubmissions >= MIN_SUBMISSIONS) {
            aggregatedPrice = totalPrice / validSubmissions;
            lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev Function to get the current aggregated price.
     * @return uint256 The aggregated price.
     */
    function getAggregatedPrice() external view returns (uint256) {
        require(aggregatedPrice > 0, "No valid aggregated price available");
        return aggregatedPrice;
    }

    /**
     * @dev Function to get the last updated timestamp of the aggregated price.
     * @return uint256 The timestamp of the last update.
     */
    function getLastUpdated() external view returns (uint256) {
        return lastUpdated;
    }
}
```
