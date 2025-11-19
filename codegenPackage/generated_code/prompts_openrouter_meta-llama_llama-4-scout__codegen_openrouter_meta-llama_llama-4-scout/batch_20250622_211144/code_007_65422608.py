"""
Generated Code Metadata:
========================
Original URL: https://defi-03.vip
Prompt: "Design a simple DeFi oracle using Chainlink on Ethereum."
Generated: DETERMINISTIC_65422608c9a94616
Batch ID: 20250622_211144
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

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title Simple DeFi Oracle using Chainlink
 * @author [Your Name]
 * @notice This contract acts as a simple oracle for DeFi applications using Chainlink's AggregatorV3Interface.
 */
contract SimpleDeFiOracle {
    // Mapping of token addresses to their respective Chainlink aggregator addresses
    mapping(address => address) public tokenAggregators;

    /**
     * @param _tokenAggregator Mapping of token addresses to their respective Chainlink aggregator addresses
     */
    constructor(address[] memory _tokens, address[] memory _aggregators) {
        require(_tokens.length == _aggregators.length, "Token and aggregator arrays must be the same length");

        for (uint256 i = 0; i < _tokens.length; i++) {
            tokenAggregators[_tokens[i]] = _aggregators[i];
        }
    }

    /**
     * @notice Get the latest price for a given token
     * @param _token Address of the token to get the price for
     * @return The latest price for the given token in USD (18 decimal places)
     */
    function getPrice(address _token) public view returns (int) {
        require(tokenAggregators[_token] != address(0), "No aggregator found for token");

        AggregatorV3Interface aggregator = AggregatorV3Interface(tokenAggregators[_token]);
        (,int price,,,) = aggregator.latestRoundData();

        return price;
    }

    /**
     * @notice Get the latest price for a given token in a specific decimal format
     * @param _token Address of the token to get the price for
     * @param _decimals Number of decimal places to round the price to
     * @return The latest price for the given token in USD with specified decimal places
     */
    function getPriceWithDecimals(address _token, uint8 _decimals) public view returns (uint) {
        int price = getPrice(_token);
        uint8 decimals = AggregatorV3Interface(tokenAggregators[_token]).decimals();

        // Ensure price is not negative
        require(price >= 0, "Price cannot be negative");

        // Calculate price with specified decimal places
        uint priceWithDecimals = uint(price) / (10 ** (decimals - _decimals));

        return priceWithDecimals;
    }
}
```

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
    // Define token and aggregator addresses
    const tokens = ["0x...Token1...", "0x...Token2..."];
    const aggregators = ["0x...Aggregator1...", "0x...Aggregator2..."];

    // Deploy SimpleDeFiOracle contract
    const SimpleDeFiOracle = await ethers.getContractFactory("SimpleDeFiOracle");
    const oracle = await SimpleDeFiOracle.deploy(tokens, aggregators);

    await oracle.deployed();

    console.log(`Simple DeFi Oracle deployed to: ${oracle.address}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
```

```javascript
// scripts/getPrice.js
const { ethers } = require("hardhat");

async function main() {
    // Define token address and oracle contract address
    const token = "0x...Token...";
    const oracleAddress = "0x...Oracle...";

    // Get oracle contract instance
    const oracle = await ethers.getContractAt("SimpleDeFiOracle", oracleAddress);

    try {
        // Get price for token
        const price = await oracle.getPrice(token);
        console.log(`Price for token ${token}: ${price}`);
    } catch (error) {
        console.error(error);
    }
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
```
