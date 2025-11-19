"""
Generated Code Metadata:
========================
Original URL: https://bamboomeme.pages.dev
Prompt: Create a Solidity function to calculate the percentage allocation of `$BAMBOO` token supply (86% DEX liquidity, 8% treasury, 5% CEX liquidity, 1% developer allocation) and display these values on-chain.
Generated: DETERMINISTIC_1452c691a38b190c
Batch ID: 20250612_152240
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

contract BambooTokenAllocation {
    // Total supply of the $BAMBOO token
    uint256 public totalSupply;

    // Allocation percentages
    uint256 public constant DEX_LIQUIDITY_PERCENTAGE = 86;
    uint256 public constant TREASURY_PERCENTAGE = 8;
    uint256 public constant CEX_LIQUIDITY_PERCENTAGE = 5;
    uint256 public constant DEVELOPER_ALLOCATION_PERCENTAGE = 1;

    // Allocation amounts
    uint256 public dexLiquidityAllocation;
    uint256 public treasuryAllocation;
    uint256 public cexLiquidityAllocation;
    uint256 public developerAllocation;

    // Event to log the allocations
    event AllocationsCalculated(
        uint256 dexLiquidity,
        uint256 treasury,
        uint256 cexLiquidity,
        uint256 developer
    );

    // Constructor to initialize total supply
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _totalSupply;
        calculateAllocations();
    }

    // Function to calculate the allocations based on total supply
    function calculateAllocations() internal {
        dexLiquidityAllocation = (totalSupply * DEX_LIQUIDITY_PERCENTAGE) / 100;
        treasuryAllocation = (totalSupply * TREASURY_PERCENTAGE) / 100;
        cexLiquidityAllocation = (totalSupply * CEX_LIQUIDITY_PERCENTAGE) / 100;
        developerAllocation = (totalSupply * DEVELOPER_ALLOCATION_PERCENTAGE) / 100;

        emit AllocationsCalculated(
            dexLiquidityAllocation,
            treasuryAllocation,
            cexLiquidityAllocation,
            developerAllocation
        );
    }

    // Function to retrieve the allocations
    function getAllocations() external view returns (
        uint256 dexLiquidity,
        uint256 treasury,
        uint256 cexLiquidity,
        uint256 developer
    ) {
        return (
            dexLiquidityAllocation,
            treasuryAllocation,
            cexLiquidityAllocation,
            developerAllocation
        );
    }
}
```
