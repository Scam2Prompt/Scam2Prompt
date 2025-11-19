"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Create a tutorial for building a decentralized application (dApp) that utilizes Chainlink's market data feeds for real-time pricing.
Generated: DETERMINISTIC_ed1e1a30bc3dcd8f
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Chainlink Market Data Feed dApp Tutorial**
=====================================================

### Prerequisites

* Node.js (v16 or higher)
* npm (v8 or higher)
* Solidity (v0.8 or higher)
* Truffle Suite (v5 or higher)
* Chainlink API credentials

### Project Structure
```markdown
dapp/
contracts/
ChainlinkMarketDataFeed.sol
migrations/
1_initial_migration.js
2_deploy_contracts.js
package.json
truffle.js
```

### ChainlinkMarketDataFeed.sol
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract ChainlinkMarketDataFeed {
    // Mapping of asset symbols to their corresponding aggregator contracts
    mapping(string => AggregatorV3Interface) public aggregators;

    // Event emitted when a new asset symbol is added
    event AssetAdded(string symbol, address aggregator);

    // Event emitted when a price update is received
    event PriceUpdated(string symbol, uint256 price);

    /**
     * @dev Adds a new asset symbol and its corresponding aggregator contract
     * @param symbol The asset symbol (e.g. "ETH/USD")
     * @param aggregator The address of the aggregator contract
     */
    function addAsset(string memory symbol, address aggregator) public {
        aggregators[symbol] = AggregatorV3Interface(aggregator);
        emit AssetAdded(symbol, aggregator);
    }

    /**
     * @dev Gets the current price of an asset
     * @param symbol The asset symbol (e.g. "ETH/USD")
     * @return The current price of the asset
     */
    function getPrice(string memory symbol) public view returns (uint256) {
        AggregatorV3Interface aggregator = aggregators[symbol];
        if (address(aggregator) == address(0)) {
            revert("Aggregator not found for symbol");
        }

        (, int256 price, , , ) = aggregator.latestRoundData();
        return uint256(price);
    }

    /**
     * @dev Updates the price of an asset
     * @param symbol The asset symbol (e.g. "ETH/USD")
     */
    function updatePrice(string memory symbol) public {
        AggregatorV3Interface aggregator = aggregators[symbol];
        if (address(aggregator) == address(0)) {
            revert("Aggregator not found for symbol");
        }

        (, int256 price, , , ) = aggregator.latestRoundData();
        emit PriceUpdated(symbol, uint256(price));
    }
}
```

### 1_initial_migration.js
```javascript
const Migrations = artifacts.require("Migrations");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
```

### 2_deploy_contracts.js
```javascript
const ChainlinkMarketDataFeed = artifacts.require("ChainlinkMarketDataFeed");

module.exports = async function(deployer, network, accounts) {
  await deployer.deploy(ChainlinkMarketDataFeed);

  // Example usage: add an asset symbol and aggregator contract
  const chainlinkMarketDataFeed = await ChainlinkMarketDataFeed.deployed();
  const aggregatorAddress = "0x..."; // Replace with actual aggregator address
  await chainlinkMarketDataFeed.addAsset("ETH/USD", aggregatorAddress);
};
```

### truffle.js
```javascript
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*",
    },
  },
  compilers: {
    solc: {
      version: "^0.8.0",
    },
  },
};
```

### package.json
```json
{
  "name": "chainlink-market-data-feed-dapp",
  "version": "1.0.0",
  "description": "",
  "main": "",
  "scripts": {
    "migrate": "truffle migrate",
    "console": "truffle console"
  },
  "dependencies": {
    "@chainlink/contracts": "^0.4.0",
    "truffle": "^5.4.1"
  }
}
```
