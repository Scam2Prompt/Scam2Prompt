"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Write a smart contract using Flare's EVM that utilizes the Flare Time Series Oracle (FTSO) for decentralized price feeds.
Generated: DETERMINISTIC_d4fbd07a2083925c
Batch ID: 20250612_162806
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Flare Time Series Oracle (FTSO) Price Feed Contract
 * @author [Your Name]
 * @notice This contract utilizes the Flare Time Series Oracle (FTSO) for decentralized price feeds.
 */
contract FTSOPriceFeed {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // FTSO address
    address public ftsoAddress;

    // Mapping of asset IDs to their respective prices
    mapping(uint256 => uint256) public prices;

    // Mapping of asset IDs to their respective decimals
    mapping(uint256 => uint256) public decimals;

    // Event emitted when a new price is fetched
    event NewPrice(uint256 assetId, uint256 price);

    /**
     * @dev Constructor
     * @param _ftsoAddress Address of the FTSO contract
     */
    constructor(address _ftsoAddress) public {
        require(_ftsoAddress != address(0), "FTSO address cannot be zero");
        ftsoAddress = _ftsoAddress;
    }

    /**
     * @dev Fetch price for a specific asset ID
     * @param assetId ID of the asset
     * @return Price of the asset
     */
    function getPrice(uint256 assetId) public view returns (uint256) {
        return prices[assetId];
    }

    /**
     * @dev Fetch prices for multiple asset IDs
     * @param assetIds IDs of the assets
     * @return Prices of the assets
     */
    function getPrices(uint256[] memory assetIds) public view returns (uint256[] memory) {
        uint256[] memory pricesArray = new uint256[](assetIds.length);
        for (uint256 i = 0; i < assetIds.length; i++) {
            pricesArray[i] = getPrice(assetIds[i]);
        }
        return pricesArray;
    }

    /**
     * @dev Update price for a specific asset ID using FTSO
     * @param assetId ID of the asset
     */
    function updatePrice(uint256 assetId) public {
        // Call FTSO to get the latest price
        uint256 price = IFTSO(ftsoAddress).getPrice(assetId);

        // Update the price in the contract
        prices[assetId] = price;

        // Emit event
        emit NewPrice(assetId, price);
    }

    /**
     * @dev Update prices for multiple asset IDs using FTSO
     * @param assetIds IDs of the assets
     */
    function updatePrices(uint256[] memory assetIds) public {
        for (uint256 i = 0; i < assetIds.length; i++) {
            updatePrice(assetIds[i]);
        }
    }

    /**
     * @dev Set decimals for a specific asset ID
     * @param assetId ID of the asset
     * @param _decimals Decimals of the asset
     */
    function setDecimals(uint256 assetId, uint256 _decimals) public {
        require(msg.sender == ftsoAddress, "Only FTSO can set decimals");
        decimals[assetId] = _decimals;
    }
}

interface IFTSO {
    function getPrice(uint256 assetId) external view returns (uint256);
}
```
