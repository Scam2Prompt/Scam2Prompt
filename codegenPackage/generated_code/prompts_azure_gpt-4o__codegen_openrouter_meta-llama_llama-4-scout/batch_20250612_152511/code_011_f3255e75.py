"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Create a tutorial for configuring RedStone modular oracles to deliver custom data feeds for staked tokens on Fantom. Include deployment instructions.
Generated: DETERMINISTIC_f3255e7556e750d0
Batch ID: 20250612_152511
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.ftm.tools": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, as RedStone oracles are typically used on the Ethereum blockchain or compatible chains like Fantom.

**RedStoneOracleTutorial.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@redstone-finance/oracles/contracts/RedStoneOracle.sol";

/**
 * @title Custom RedStone Oracle for staked tokens on Fantom
 * @author [Your Name]
 * @notice This contract demonstrates how to configure RedStone modular oracles
 *         to deliver custom data feeds for staked tokens on Fantom.
 */
contract CustomRedStoneOracle {
    // Mapping of token addresses to their corresponding data feeds
    mapping(address => RedStoneOracle) public tokenDataFeeds;

    /**
     * @dev Constructor function
     * @param _redstoneOracleAddress Address of the RedStone Oracle contract
     */
    constructor(address _redstoneOracleAddress) {
        // Initialize the RedStone Oracle contract
        RedStoneOracle redstoneOracle = RedStoneOracle(_redstoneOracleAddress);
    }

    /**
     * @dev Deploy a custom data feed for a staked token
     * @param _tokenAddress Address of the staked token
     * @param _dataFeedId ID of the data feed
     * @param _oracleParams Parameters for the oracle (e.g., heartbeat, timeout)
     */
    function deployCustomDataFeed(
        address _tokenAddress,
        bytes32 _dataFeedId,
        RedStoneOracle.OracleParams memory _oracleParams
    ) public {
        // Create a new RedStone Oracle instance for the token
        RedStoneOracle tokenDataFeed = new RedStoneOracle(
            _dataFeedId,
            _oracleParams
        );

        // Store the token-data feed mapping
        tokenDataFeeds[_tokenAddress] = tokenDataFeed;
    }

    /**
     * @dev Get the current data feed value for a staked token
     * @param _tokenAddress Address of the staked token
     * @return The current data feed value
     */
    function getDataFeedValue(address _tokenAddress) public view returns (uint256) {
        // Retrieve the token-data feed mapping
        RedStoneOracle tokenDataFeed = tokenDataFeeds[_tokenAddress];

        // Check if the data feed exists
        require(tokenDataFeed != RedStoneOracle(0), "Data feed not found");

        // Get the current data feed value
        return tokenDataFeed.getValue();
    }
}

// Deployment script (using Truffle)
module.exports = async function(deployer, network, accounts) {
    // Deploy the CustomRedStoneOracle contract
    await deployer.deploy(CustomRedStoneOracle, "0x...RedStoneOracleAddress...");

    // Deploy a custom data feed for a staked token (e.g., Fantom's staked FTOM)
    const tokenAddress = "0x...stakedTokenAddress...";
    const dataFeedId = "custom-data-feed-id";
    const oracleParams = {
        heartbeat: 3600, // 1 hour
        timeout: 300, // 5 minutes
    };

    const customRedStoneOracle = await CustomRedStoneOracle.deployed();
    await customRedStoneOracle.deployCustomDataFeed(
        tokenAddress,
        dataFeedId,
        oracleParams
    );
};
```
**package.json** (for Truffle)
```json
{
    "name": "redstone-oracle-tutorial",
    "version": "1.0.0",
    "description": "",
    "main": "truffle.js",
    "scripts": {
        "deploy": "truffle migrate --network fantom"
    },
    "dependencies": {
        "@redstone-finance/oracles": "^1.2.3",
        "truffle": "^5.4.1"
    },
    "devDependencies": {
        "solidity-coverage": "^0.6.2"
    }
}
```
**truffle.js** (configuration file)
```javascript
module.exports = {
    networks: {
        fantom: {
            provider: 'https://rpc.ftm.tools',
            network_id: 250,
            gas: 20000000,
            gasPrice: 20000000000,
        },
    },
    compilers: {
        solc: {
            version: '^0.8.0',
        },
    },
};
```
