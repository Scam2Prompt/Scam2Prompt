"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Write a smart contract using Flare's EVM platform that integrates the Flare Time Series Oracle (FTSO) to fetch decentralized price data for a cryptocurrency trading application.
Generated: DETERMINISTIC_766f2c7a9c5b561b
Batch ID: 20250612_153848
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/flare-foundation/flare-smart-contracts/contracts/ftso/IFTSOManager.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/flare-foundation/flare-smart-contracts/contracts/ftso/IFTSO.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/flare-foundation/flare-smart-contracts/contracts/ftso/IFTSO.sol";
import "https://github.com/flare-foundation/flare-smart-contracts/contracts/ftso/IFTSOManager.sol";

/**
 * @title Flare Price Oracle Contract
 * @author [Your Name]
 * @notice This contract integrates the Flare Time Series Oracle (FTSO) to fetch decentralized price data.
 */
contract FlarePriceOracle {
    // Mapping of asset symbols to their respective FTSO contracts
    mapping(string => address) public assetToFtsos;

    // Mapping of asset symbols to their respective prices
    mapping(string => uint256) public assetPrices;

    // FTSO manager contract address
    address public ftsomanager;

    // Event emitted when a new price is fetched
    event NewPrice(string asset, uint256 price);

    /**
     * @dev Constructor
     * @param _ftsomanager FTSO manager contract address
     */
    constructor(address _ftsomanager) {
        require(_ftsomanager != address(0), "FTSO manager address cannot be zero");
        ftsomanager = _ftsomanager;
    }

    /**
     * @dev Add a new asset and its corresponding FTSO contract
     * @param _asset Asset symbol (e.g. "BTC")
     * @param _ftso FTSO contract address
     */
    function addAsset(string memory _asset, address _ftso) public {
        require(assetToFtsos[_asset] == address(0), "Asset already added");
        require(_ftso != address(0), "FTSO address cannot be zero");
        assetToFtsos[_asset] = _ftso;
    }

    /**
     * @dev Fetch the current price of an asset from the FTSO
     * @param _asset Asset symbol (e.g. "BTC")
     * @return The current price of the asset
     */
    function getPrice(string memory _asset) public view returns (uint256) {
        address ftsocontract = assetToFtsos[_asset];
        require(ftsocontract != address(0), "Asset not added");

        IFTSO ftsoconnect = IFTSO(ftsocontract);
        uint256 price = ftsoconnect.getLatestPrice();

        // Validate price
        require(price > 0, "Invalid price");

        return price;
    }

    /**
     * @dev Update the price of an asset
     * @param _asset Asset symbol (e.g. "BTC")
     */
    function updatePrice(string memory _asset) public {
        uint256 price = getPrice(_asset);
        assetPrices[_asset] = price;
        emit NewPrice(_asset, price);
    }

    /**
     * @dev Get the current price of an asset
     * @param _asset Asset symbol (e.g. "BTC")
     * @return The current price of the asset
     */
    function getAssetPrice(string memory _asset) public view returns (uint256) {
        return assetPrices[_asset];
    }
}
```
