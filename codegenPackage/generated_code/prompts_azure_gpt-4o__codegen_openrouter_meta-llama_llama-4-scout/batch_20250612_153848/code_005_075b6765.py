"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Create a decentralized application on Flare that leverages both the State Connector and FTSO protocols to provide real-time data feeds for DeFi applications.
Generated: DETERMINISTIC_075b676586c57f4d
Batch ID: 20250612_153848
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/flare-foundation/flare-smart-contracts/blob/main/contracts/FTSO.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://flare-rpc-url.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/flare-foundation/flare-smart-contracts/blob/main/contracts/StateConnector.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, as Flare is an EVM-compatible blockchain. Here's the code:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "https://github.com/flare-foundation/flare-smart-contracts/blob/main/contracts/StateConnector.sol";
import "https://github.com/flare-foundation/flare-smart-contracts/blob/main/contracts/FTSO.sol";

/**
 * @title Decentralized Application on Flare for Real-time Data Feeds
 * @author [Your Name]
 * @notice This contract provides real-time data feeds for DeFi applications
 *         leveraging the State Connector and FTSO protocols on Flare.
 */
contract RealTimeDataFeeds {
    using SafeMath for uint256;

    // State Connector instance
    StateConnector public stateConnector;

    // FTSO instance
    FTSO public ftso;

    // Mapping of asset symbols to their corresponding FTSO IDs
    mapping(string => bytes32) public assetToFtsoId;

    // Mapping of FTSO IDs to their corresponding asset symbols
    mapping(bytes32 => string) public ftsoIdToAsset;

    // Mapping of asset symbols to their current prices
    mapping(string => uint256) public assetPrices;

    /**
     * @dev Constructor
     * @param _stateConnector Address of the State Connector instance
     * @param _ftso Address of the FTSO instance
     */
    constructor(address _stateConnector, address _ftso) {
        stateConnector = StateConnector(_stateConnector);
        ftso = FTSO(_ftso);
    }

    /**
     * @dev Add an asset to the data feed
     * @param _asset Symbol of the asset to add (e.g. "BTC")
     * @param _ftsoId ID of the FTSO for the asset
     */
    function addAsset(string memory _asset, bytes32 _ftsoId) public {
        require(bytes(_asset).length > 0, "Asset symbol cannot be empty");
        require(_ftsoId != bytes32(0), "FTSO ID cannot be zero");

        assetToFtsoId[_asset] = _ftsoId;
        ftsoIdToAsset[_ftsoId] = _asset;
    }

    /**
     * @dev Update the price of an asset
     * @param _asset Symbol of the asset to update
     */
    function updatePrice(string memory _asset) public {
        bytes32 ftsoId = assetToFtsoId[_asset];
        require(ftsoId != bytes32(0), "Asset not found");

        // Get the current FTSO median price
        uint256 price = ftso.getMedian(ftsoId);

        // Validate the price using the State Connector
        stateConnector.validateData(ftsoId, price);

        assetPrices[_asset] = price;
    }

    /**
     * @dev Get the current price of an asset
     * @param _asset Symbol of the asset to retrieve
     * @return Current price of the asset
     */
    function getPrice(string memory _asset) public view returns (uint256) {
        return assetPrices[_asset];
    }

    /**
     * @dev Handle FTSO updates
     * @param _ftsoId ID of the FTSO that was updated
     * @param _newMedian New median price of the FTSO
     */
    function onFtsoUpdate(bytes32 _ftsoId, uint256 _newMedian) external {
        string memory asset = ftsoIdToAsset[_ftsoId];
        require(bytes(asset).length > 0, "Asset not found");

        assetPrices[asset] = _newMedian;
    }

    /**
     * @dev Handle State Connector validation results
     * @param _ftsoId ID of the FTSO that was validated
     * @param _isValid Whether the FTSO data is valid
     */
    function onStateConnectorValidation(bytes32 _ftsoId, bool _isValid) external {
        require(_isValid, "Invalid FTSO data");
    }
}
```

```javascript
// This is an example of how you might use the above contract with Web3.js and Ethers.js

const Web3 = require('web3');
const { ethers } = require('ethers');

// Assuming you have the contract ABI and address
const contractAbi = [...]; // RealTimeDataFeeds ABI
const contractAddress = '0x...'; // Deployed contract address

// Set up Web3 and Ethers.js providers
const web3 = new Web3(new Web3.providers.HttpProvider('https://flare-rpc-url.com'));
const provider = new ethers.providers.JsonRpcProvider('https://flare-rpc-url.com');
const signer = new ethers.Wallet('0x... private key ...', provider);

// Create a contract instance
const contract = new ethers.Contract(contractAddress, contractAbi, signer);

// Example usage:
async function main() {
    try {
        // Add an asset
        await contract.addAsset('BTC', '0x... FTSO ID ...');

        // Update the price of an asset
        await contract.updatePrice('BTC');

        // Get the current price of an asset
        const price = await contract.getPrice('BTC');
        console.log(`Current price of BTC: ${price}`);

    } catch (error) {
        console.error(error);
    }
}

main();
```
