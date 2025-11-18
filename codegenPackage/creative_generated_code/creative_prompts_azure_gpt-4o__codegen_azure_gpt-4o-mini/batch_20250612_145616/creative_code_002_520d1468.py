"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Generate Solidity code to query GMX oracle data from a smart contract deployed on the Arbitrum network.
Generated: DETERMINISTIC_520d146825e96b48
Batch ID: 20250612_145616
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

// Importing necessary interfaces for interacting with GMX oracle
interface IOracle {
    function getPrice(address asset) external view returns (uint256);
}

contract GMXOracleConsumer {
    // Address of the GMX oracle deployed on the Arbitrum network
    IOracle public gmxOracle;

    // Event to emit when price is retrieved
    event PriceRetrieved(address indexed asset, uint256 price);

    // Constructor to set the GMX oracle address
    constructor(address _gmxOracle) {
        require(_gmxOracle != address(0), "Invalid oracle address");
        gmxOracle = IOracle(_gmxOracle);
    }

    /**
     * @dev Function to get the price of a specific asset from GMX oracle
     * @param asset The address of the asset to query
     * @return price The price of the asset in Wei
     */
    function getAssetPrice(address asset) external view returns (uint256 price) {
        require(asset != address(0), "Invalid asset address");
        
        try gmxOracle.getPrice(asset) returns (uint256 assetPrice) {
            emit PriceRetrieved(asset, assetPrice);
            return assetPrice;
        } catch {
            revert("Failed to retrieve price from GMX oracle");
        }
    }
}
```
