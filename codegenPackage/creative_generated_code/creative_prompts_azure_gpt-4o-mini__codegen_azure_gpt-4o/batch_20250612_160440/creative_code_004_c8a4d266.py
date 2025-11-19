"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaredrop.in
Prompt: Provide an example of how to optimize price feeds using Flare's decentralized services in a smart contract.
Generated: DETERMINISTIC_c8a4d2668c90a4bb
Batch ID: 20250612_160440
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
 * @title Flare Price Feed Optimizer
 * @dev This contract fetches and optimizes price feeds using Flare's decentralized services.
 */
interface IFlarePriceService {
    /**
     * @dev Interface to interact with Flare's price service.
     * @param asset The asset you want the price for (e.g., "BTC/USD").
     */
    function getPrice(string calldata asset) external view returns (uint256);
}

contract PriceFeedAggregator {
    // Address of the Flare price service contract
    address public flarePriceService;

    // Event emitted when a price is successfully fetched
    event PriceFetched(string asset, uint256 price);

    // Event emitted when the Flare price service address is updated
    event FlarePriceServiceUpdated(address indexed oldAddress, address indexed newAddress);
    
    // Modifier to ensure the Flare price service address is set
    modifier flareServiceAvailable() {
        require(flarePriceService != address(0), "Flare price service address is not set");
        _;
    }

    /**
     * @dev Constructor to set the initial Flare price service address.
     * @param _flarePriceService Address of the deployed Flare price service contract.
     */
    constructor(address _flarePriceService) {
        require(_flarePriceService != address(0), "Invalid Flare price service address");
        flarePriceService = _flarePriceService;
    }

    /**
     * @dev Fetches the price of the given asset using Flare's price service.
     * @param asset The asset symbol (e.g., "BTC/USD") to fetch the price of.
     * @return The price of the asset in wei.
     */
    function fetchPrice(string calldata asset) external flareServiceAvailable returns (uint256) {
        try IFlarePriceService(flarePriceService).getPrice(asset) returns (uint256 price) {
            emit PriceFetched(asset, price);
            return price; // Return the fetched price
        } catch {
            revert("Failed to fetch price from Flare price service");
        }
    }

    /**
     * @dev Updates the Flare price service contract address.
     * @param newFlarePriceService The new address of the Flare price service contract.
     */
    function updateFlarePriceService(address newFlarePriceService) external {
        require(newFlarePriceService != address(0), "Invalid Flare price service address");
        address oldAddress = flarePriceService;
        flarePriceService = newFlarePriceService;

        emit FlarePriceServiceUpdated(oldAddress, newFlarePriceService);
    }
}
```
