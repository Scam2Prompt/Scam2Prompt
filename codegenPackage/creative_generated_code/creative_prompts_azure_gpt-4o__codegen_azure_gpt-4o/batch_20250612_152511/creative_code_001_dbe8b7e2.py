"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Generate code to connect RedStone Core (Pull) Oracle to a DeFi dApp on Polygon, ensuring low gas costs and on-demand signed data package delivery.
Generated: DETERMINISTIC_dbe8b7e2e53afb9a
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import the RedStone Core library
import "@redstone-finance/evm-connector/contracts/core/RedstoneConsumer.sol";

// Interface for interacting with the DeFi dApp
interface IDeFiApp {
    function executeAction(uint256 priceData) external;
}

// Contract to integrate RedStone Oracle with a DeFi dApp on Polygon
contract RedStoneOracleConnector is RedstoneConsumer {
    // Address of the DeFi dApp contract
    address public defiAppAddress;

    // Event for logging data retrieval and usage
    event PriceDataRetrieved(uint256 timestamp, uint256 priceData);

    // Constructor accepting the DeFi dApp address
    constructor(address _defiAppAddress) {
        require(_defiAppAddress != address(0), "Invalid DeFi dApp address");
        defiAppAddress = _defiAppAddress;
    }

    /**
     * @dev Fetch signed price data from RedStone Oracle
     * @param dataFeedId - The ID of the data feed to use (e.g., "BTC", "ETH", etc.)
     */
    function fetchAndUsePriceData(bytes32 dataFeedId) external {
        // Fetch the signed data package from RedStone
        uint256 priceData = getPriceFromMsg(dataFeedId);

        // Ensure the fetched price data is valid
        require(priceData > 0, "Invalid price data");

        // Call the specified DeFi dApp action with the price data
        IDeFiApp(defiAppAddress).executeAction(priceData);

        // Emit an event for logging purposes
        emit PriceDataRetrieved(block.timestamp, priceData);
    }

    /**
     * @dev Function to update the DeFi dApp address if needed
     * @param _newDefiAppAddress - The new address of the DeFi dApp contract
     */
    function updateDefiAppAddress(address _newDefiAppAddress) external {
        require(_newDefiAppAddress != address(0), "Invalid new DeFi dApp address");
        defiAppAddress = _newDefiAppAddress;
    }

    /**
     * @dev Internal function to fetch price from the RedStone data package
     * @param dataFeedId - The ID of the data feed
     * @return price - The extracted price data
     */
    function getPriceFromMsg(bytes32 dataFeedId) internal view returns (uint256 price) {
        // Use RedStone EVM Connector to extract price
        return RedstoneConsumer._extractDataFromMsg(dataFeedId);
    }
}
```
