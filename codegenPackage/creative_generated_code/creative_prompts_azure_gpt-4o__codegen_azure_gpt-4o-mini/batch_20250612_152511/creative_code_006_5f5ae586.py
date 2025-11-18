"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Write a Solidity function to fetch and verify price data from RedStone modular oracles for non-EVM chains like Starknet. Ensure compatibility with decentralized juries for dispute resolution.
Generated: DETERMINISTIC_5f5ae5869a1e32fa
Batch ID: 20250612_152511
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

// Importing required interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

// Interface for the RedStone oracle
interface IRedStoneOracle {
    function getPrice(string calldata asset) external view returns (uint256 price);
}

contract PriceVerifier is Ownable {
    // Oracle contract address
    IRedStoneOracle public oracle;

    // Event emitted when a price is fetched
    event PriceFetched(string asset, uint256 price);
    
    // Event emitted when a dispute is created
    event DisputeCreated(string asset, uint256 claimedPrice, uint256 actualPrice);
    
    // Mapping to keep track of fetched prices
    mapping(string => uint256) public fetchedPrices;

    // Constructor to initialize the oracle address
    constructor(address _oracleAddress) {
        require(_oracleAddress != address(0), "Invalid oracle address");
        oracle = IRedStoneOracle(_oracleAddress);
    }

    // Function to fetch price data from the RedStone oracle
    function fetchPrice(string calldata asset) external onlyOwner returns (uint256 price) {
        // Fetching price from the oracle
        price = oracle.getPrice(asset);
        
        // Check for a valid price
        require(price > 0, "Invalid price fetched");

        // Storing the fetched price
        fetchedPrices[asset] = price;

        // Emitting the price fetched event
        emit PriceFetched(asset, price);
    }

    // Function to verify fetched price against a claimed price
    function verifyPrice(string calldata asset, uint256 claimedPrice) external {
        // Fetching the actual price from the oracle
        uint256 actualPrice = fetchedPrices[asset];

        // Validate if the price has been previously fetched
        require(actualPrice > 0, "Price not fetched");

        // Check if there is a dispute
        if (claimedPrice != actualPrice) {
            // Emit dispute event
            emit DisputeCreated(asset, claimedPrice, actualPrice);
        }
    }
}
```
