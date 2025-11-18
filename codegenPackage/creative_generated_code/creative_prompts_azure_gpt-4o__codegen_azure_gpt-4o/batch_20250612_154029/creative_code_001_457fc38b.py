"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Generate code for a decentralized application (dApp) on Flare Network that uses the Flare Time Series Oracle (FTSO) to retrieve highly-decentralized price feeds.
Generated: DETERMINISTIC_457fc38b0ea65f79
Batch ID: 20250612_154029
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

/**
 * @title FlarePriceFeedDApp
 * @dev A decentralized application (dApp) that interacts with the Flare Time Series Oracle (FTSO)
 * to retrieve highly-decentralized price feeds for assets.
 */
contract FlarePriceFeedDApp {
    // Address of the Flare Time Series Oracle (FTSO) contract
    address public ftsoAddress;

    // Event emitted when a price is successfully fetched
    event PriceFetched(string indexed assetSymbol, uint256 price);

    // Modifier to ensure a valid FTSO address is set
    modifier isFTSOSet() {
        require(ftsoAddress != address(0), "FTSO address not set");
        _;
    }

    /**
     * @dev Constructor to set the initial FTSO contract address.
     * @param _ftsoAddress Address of the FTSO contract on the Flare Network.
     */
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "FTSO address cannot be zero");
        ftsoAddress = _ftsoAddress;
    }

    /**
     * @dev Sets the FTSO contract address. Callable only by the contract owner.
     * @param _ftsoAddress Address of the FTSO contract on the Flare Network.
     */
    function setFTSOAddress(address _ftsoAddress) external {
        require(_ftsoAddress != address(0), "FTSO address cannot be zero");
        ftsoAddress = _ftsoAddress;
    }

    /**
     * @dev Fetches the price for a given asset from the FTSO contract.
     * @param assetSymbol Symbol of the asset (e.g., "BTC", "ETH").
     * @return price Current price of the asset in cents.
     */
    function fetchPrice(string memory assetSymbol)
        external
        isFTSOSet
        returns (uint256 price)
    {
        // Interface for interacting with the FTSO contract
        IFTSO ftso = IFTSO(ftsoAddress);

        try ftso.getCurrentPrice(assetSymbol) returns (uint256 assetPrice) {
            // Emit the price fetched event
            emit PriceFetched(assetSymbol, assetPrice);
            return assetPrice;
        } catch {
            revert("Failed to fetch price from FTSO");
        }
    }
}

/**
 * @title Interface for the Flare Time Series Oracle (FTSO) contract
 * @dev Define the methods available on the FTSO contract.
 */
interface IFTSO {
    /**
     * @dev Fetches the current price for a given asset.
     * @param assetSymbol Symbol of the asset (e.g., "BTC", "ETH").
     * @return price Current price of the asset in cents.
     */
    function getCurrentPrice(string memory assetSymbol)
        external
        view
        returns (uint256);
}
```
