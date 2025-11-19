"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: What are the advantages of using RedStone's modular oracles for LSTs and LRTs compared to traditional oracle solutions, and how can RedStone's solution benefit DeFi applications on multiple EVM and non-EVM ecosystems?
Generated: DETERMINISTIC_b06f965654af34d5
Batch ID: 20250622_210053
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@redstone-finance/evm-connector/contracts/data-services/LSTPriceFeed.sol";
import "@redstone-finance/evm-connector/contracts/data-services/LRTPriceFeed.sol";

/**
 * @title DeFiOracleIntegration
 * @dev Demonstrates integration with RedStone's modular oracles for LSTs and LRTs
 */
contract DeFiOracleIntegration is Ownable {
    using LSTPriceFeed for bytes32;
    using LRTPriceFeed for bytes32;

    // Mapping of supported LST tokens
    mapping(bytes32 => bool) public supportedLSTs;
    
    // Mapping of supported LRT tokens
    mapping(bytes32 => bool) public supportedLRTs;

    event LSTAdded(bytes32 tokenSymbol);
    event LRTAdded(bytes32 tokenSymbol);
    event PriceUpdated(bytes32 tokenSymbol, uint256 price);

    /**
     * @dev Add supported LST token
     * @param tokenSymbol Symbol of the LST token (e.g., "stETH")
     */
    function addSupportedLST(bytes32 tokenSymbol) external onlyOwner {
        require(!supportedLSTs[tokenSymbol], "Token already supported");
        supportedLSTs[tokenSymbol] = true;
        emit LSTAdded(tokenSymbol);
    }

    /**
     * @dev Add supported LRT token
     * @param tokenSymbol Symbol of the LRT token (e.g., "eETH")
     */
    function addSupportedLRT(bytes32 tokenSymbol) external onlyOwner {
        require(!supportedLRTs[tokenSymbol], "Token already supported");
        supportedLRTs[tokenSymbol] = true;
        emit LRTAdded(tokenSymbol);
    }

    /**
     * @dev Get LST price from RedStone oracle
     * @param tokenSymbol Symbol of the LST token
     * @return price The current price of the LST token
     */
    function getLSTPrice(bytes32 tokenSymbol) public view returns (uint256) {
        require(supportedLSTs[tokenSymbol], "Unsupported LST token");
        uint256 price = tokenSymbol.getLSTPrice();
        require(price > 0, "Invalid price");
        return price;
    }

    /**
     * @dev Get LRT price from RedStone oracle
     * @param tokenSymbol Symbol of the LRT token
     * @return price The current price of the LRT token
     */
    function getLRTPrice(bytes32 tokenSymbol) public view returns (uint256) {
        require(supportedLRTs[tokenSymbol], "Unsupported LRT token");
        uint256 price = tokenSymbol.getLRTPrice();
        require(price > 0, "Invalid price");
        return price;
    }

    /**
     * @dev Example function demonstrating usage in a DeFi application
     * @param tokenSymbol Symbol of the token (LST or LRT)
     * @param amount Amount to calculate value for
     * @return value The calculated value in USD
     */
    function calculateTokenValue(bytes32 tokenSymbol, uint256 amount) external returns (uint256) {
        uint256 price;
        
        if (supportedLSTs[tokenSymbol]) {
            price = getLSTPrice(tokenSymbol);
        } else if (supportedLRTs[tokenSymbol]) {
            price = getLRTPrice(tokenSymbol);
        } else {
            revert("Unsupported token");
        }

        uint256 value = price * amount / (10 ** 18); // Assuming 18 decimals
        emit PriceUpdated(tokenSymbol, price);
        return value;
    }
}
```
