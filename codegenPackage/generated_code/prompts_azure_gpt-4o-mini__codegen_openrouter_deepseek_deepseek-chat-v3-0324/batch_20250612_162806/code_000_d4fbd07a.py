"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Write a smart contract using Flare's EVM that utilizes the Flare Time Series Oracle (FTSO) for decentralized price feeds.
Generated: DETERMINISTIC_d4fbd07a2083925c
Batch ID: 20250612_162806
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

// Interface for FTSO contract
interface IFtso {
    function getCurrentPrice() external view returns (uint256 _price, uint256 _timestamp);
    function getCurrentPriceWithDecimals() external view returns (uint256 _price, uint256 _timestamp, uint256 _assetPriceUsdDecimals);
}

/**
 * @title PriceConsumer
 * @dev A smart contract that retrieves price data from Flare's FTSO
 */
contract PriceConsumer {
    // Address of the FTSO contract
    address public ftsoContractAddress;

    // Event emitted when price is updated
    event PriceUpdated(uint256 price, uint256 timestamp);

    /**
     * @dev Constructor sets the FTSO contract address
     * @param _ftsoContractAddress Address of the FTSO contract
     */
    constructor(address _ftsoContractAddress) {
        require(_ftsoContractAddress != address(0), "Invalid FTSO contract address");
        ftsoContractAddress = _ftsoContractAddress;
    }

    /**
     * @dev Retrieves the current price from FTSO
     * @return price Current price
     * @return timestamp Timestamp of the price update
     */
    function getLatestPrice() public view returns (uint256 price, uint256 timestamp) {
        (price, timestamp) = IFtso(ftsoContractAddress).getCurrentPrice();
        return (price, timestamp);
    }

    /**
     * @dev Retrieves the current price with decimals from FTSO
     * @return price Current price
     * @return timestamp Timestamp of the price update
     * @return decimals Number of decimals for the price
     */
    function getLatestPriceWithDecimals() public view returns (uint256 price, uint256 timestamp, uint256 decimals) {
        (price, timestamp, decimals) = IFtso(ftsoContractAddress).getCurrentPriceWithDecimals();
        return (price, timestamp, decimals);
    }

    /**
     * @dev Updates and logs the current price
     * @return price Current price
     * @return timestamp Timestamp of the price update
     */
    function updatePrice() public returns (uint256 price, uint256 timestamp) {
        (price, timestamp) = getLatestPrice();
        emit PriceUpdated(price, timestamp);
        return (price, timestamp);
    }

    /**
     * @dev Allows owner to update FTSO contract address
     * @param _newFtsoAddress New FTSO contract address
     */
    function setFtsoContractAddress(address _newFtsoAddress) public {
        require(_newFtsoAddress != address(0), "Invalid FTSO contract address");
        ftsoContractAddress = _newFtsoAddress;
    }
}
```
