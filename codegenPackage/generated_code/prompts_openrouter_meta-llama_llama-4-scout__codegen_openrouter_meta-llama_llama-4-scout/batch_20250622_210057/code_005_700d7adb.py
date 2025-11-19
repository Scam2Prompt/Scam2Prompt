"""
Generated Code Metadata:
========================
Original URL: https://redstone-fi.pages.dev
Prompt: Create a simple smart contract on Solidity that utilizes RedStone's oracle services to fetch price feeds for a specific asset, and explain the benefits of using RedStone.
Generated: DETERMINISTIC_700d7adbfeb3beab
Batch ID: 20250622_210057
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

import "@redstone-finance/oracle-contracts/contracts/interfaces/IDataSource.sol";
import "@redstone-finance/oracle-contracts/contracts/Oracle.sol";

/**
 * @title SimplePriceFeedContract
 * @author [Your Name]
 * @notice A simple smart contract that utilizes RedStone's oracle services to fetch price feeds for a specific asset.
 */
contract SimplePriceFeedContract {
    // Mapping of asset symbols to their corresponding data sources
    mapping(string => IDataSource) public assetDataSources;

    // Mapping of asset symbols to their current prices
    mapping(string => uint256) public assetPrices;

    // Event emitted when a new price is fetched for an asset
    event NewPriceFetched(string assetSymbol, uint256 price);

    /**
     * @notice Constructor function to initialize the contract with RedStone oracle
     * @param _redstoneOracleAddress Address of the RedStone oracle contract
     */
    constructor(address _redstoneOracleAddress) {
        // Initialize the RedStone oracle contract
        Oracle(_redstoneOracleAddress).initialize();
    }

    /**
     * @notice Function to set the data source for a specific asset
     * @param _assetSymbol Symbol of the asset (e.g. "ETH")
     * @param _dataSourceAddress Address of the data source contract
     */
    function setDataSource(string memory _assetSymbol, address _dataSourceAddress) public {
        // Validate the input parameters
        require(bytes(_assetSymbol).length > 0, "Asset symbol cannot be empty");
        require(_dataSourceAddress != address(0), "Data source address cannot be zero");

        // Set the data source for the asset
        IDataSource dataSource = IDataSource(_dataSourceAddress);
        assetDataSources[_assetSymbol] = dataSource;
    }

    /**
     * @notice Function to fetch the current price for a specific asset
     * @param _assetSymbol Symbol of the asset (e.g. "ETH")
     */
    function fetchPrice(string memory _assetSymbol) public {
        // Get the data source for the asset
        IDataSource dataSource = assetDataSources[_assetSymbol];
        require(address(dataSource) != address(0), "Data source not set for asset");

        // Fetch the current price from the data source
        uint256 price = dataSource.getValue();

        // Update the current price for the asset
        assetPrices[_assetSymbol] = price;

        // Emit an event to notify that a new price has been fetched
        emit NewPriceFetched(_assetSymbol, price);
    }

    /**
     * @notice Function to get the current price for a specific asset
     * @param _assetSymbol Symbol of the asset (e.g. "ETH")
     * @return The current price of the asset
     */
    function getPrice(string memory _assetSymbol) public view returns (uint256) {
        return assetPrices[_assetSymbol];
    }
}
```
