"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Develop a basic example of how to use RedStone's oracle data feeds for lending markets, specifically for yield-bearing collateral, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_605c4f92829f70a0
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
import "@redstone-finance/evm-connector/contracts/data-services/LendingDataService.sol";

/**
 * @title YieldCollateralOracle
 * @dev A contract that uses RedStone's oracle data feeds for yield-bearing collateral in lending markets
 */
contract YieldCollateralOracle is Ownable {
    using LendingDataService for LendingDataService.LendingData;

    // Mapping to store collateral data (token address => LendingData)
    mapping(address => LendingDataService.LendingData) public collateralData;

    // Events
    event CollateralDataUpdated(address indexed token, uint256 apy, uint256 tvl);

    /**
     * @dev Updates collateral data for a specific token using RedStone oracle
     * @param token The address of the yield-bearing collateral token
     * @param redStonePayload The RedStone payload containing signed data
     */
    function updateCollateralData(
        address token,
        bytes calldata redStonePayload
    ) external onlyOwner {
        LendingDataService.LendingData memory data = LendingDataService
            .getLendingDataFromPayload(redStonePayload);

        require(data.isValid, "Invalid RedStone data");
        require(token != address(0), "Invalid token address");

        collateralData[token] = data;

        emit CollateralDataUpdated(token, data.apy, data.tvl);
    }

    /**
     * @dev Gets the current APY for a yield-bearing collateral token
     * @param token The address of the yield-bearing collateral token
     * @return The current APY (in basis points)
     */
    function getCurrentAPY(address token) external view returns (uint256) {
        require(token != address(0), "Invalid token address");
        LendingDataService.LendingData memory data = collateralData[token];
        require(data.isValid, "Data not available for token");
        return data.apy;
    }

    /**
     * @dev Gets the current TVL for a yield-bearing collateral token
     * @param token The address of the yield-bearing collateral token
     * @return The current TVL (in token's base units)
     */
    function getCurrentTVL(address token) external view returns (uint256) {
        require(token != address(0), "Invalid token address");
        LendingDataService.LendingData memory data = collateralData[token];
        require(data.isValid, "Data not available for token");
        return data.tvl;
    }

    /**
     * @dev Checks if data is available for a specific token
     * @param token The address of the yield-bearing collateral token
     * @return True if data is available, false otherwise
     */
    function isDataAvailable(address token) external view returns (bool) {
        require(token != address(0), "Invalid token address");
        return collateralData[token].isValid;
    }
}
```
