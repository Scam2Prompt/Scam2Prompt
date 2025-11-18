"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythim.com
Prompt: Write a Solidity smart contract that incorporates Pythim's price feed oracles to calculate the value of a portfolio in real-time.
Generated: DETERMINISTIC_e109e08e456ec348
Batch ID: 20250612_155048
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

// Import the interface for Pyth's price feed
import "@pythnetwork/pyth-sdk-solidity/contracts/PythStructs.sol";
import "@pythnetwork/pyth-sdk-solidity/contracts/Pyth.sol";

// Define the PortfolioValueCalculator contract
contract PortfolioValueCalculator {
    // State variables
    Pyth public pyth; // Instance of the Pyth price feed oracle
    address public owner; // Owner of the contract

    // Event for logging the portfolio value
    event PortfolioValueUpdated(uint256 value);

    // Mapping to store token addresses and their corresponding Pyth price feed IDs
    mapping(address => bytes32) public priceFeeds;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with Pyth oracle and set the owner
    constructor(address _pythAddress) {
        pyth = Pyth(_pythAddress);
        owner = msg.sender;
    }

    // Function to set the price feed for a specific token
    function setPriceFeed(address token, bytes32 priceFeedId) external onlyOwner {
        priceFeeds[token] = priceFeedId;
    }

    // Function to get the current price of a token using Pyth's price feed
    function getCurrentPrice(address token) public view returns (uint256) {
        // Retrieve the price from Pyth
        // The price returned is scaled by 10^8 as per Pyth's protocol
        (int64 price, uint64 publishTime) = pyth.getPrice(priceFeeds[token]);
        
        // Check for outdated price
        require(publishTime > block.timestamp - 30 minutes, "Price data is outdated");

        // Ensure price is non-negative
        require(price >= 0, "Price cannot be negative");

        // Return the price as a uint256
        return uint256(price);
    }

    // Function to calculate the total value of a portfolio in terms of a specific token
    function calculatePortfolioValue(address[] calldata tokens, uint256[] calldata amounts) external view returns (uint256 totalValue) {
        require(tokens.length == amounts.length, "Tokens and amounts length mismatch");

        for (uint256 i = 0; i < tokens.length; i++) {
            uint256 currentPrice = getCurrentPrice(tokens[i]);
            totalValue += currentPrice * amounts[i];
        }

        emit PortfolioValueUpdated(totalValue);
    }
}
```
