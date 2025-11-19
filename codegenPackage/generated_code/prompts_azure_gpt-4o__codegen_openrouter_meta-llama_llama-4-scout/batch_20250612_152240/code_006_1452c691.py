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
    // Define the total supply of $BAMBOO token
    uint256 public totalSupply;

    // Define the allocation percentages
    uint256 public constant DEX_LIQUIDITY_PERCENTAGE = 86;
    uint256 public constant TREASURY_PERCENTAGE = 8;
    uint256 public constant CEX_LIQUIDITY_PERCENTAGE = 5;
    uint256 public constant DEVELOPER_ALLOCATION_PERCENTAGE = 1;

    // Define the allocation amounts
    uint256 public dexLiquidityAllocation;
    uint256 public treasuryAllocation;
    uint256 public cexLiquidityAllocation;
    uint256 public developerAllocation;

    /**
     * @notice Initializes the contract with the total supply of $BAMBOO token
     * @param _totalSupply The total supply of $BAMBOO token
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than 0");

        totalSupply = _totalSupply;

        // Calculate the allocation amounts
        dexLiquidityAllocation = calculateAllocation(DEX_LIQUIDITY_PERCENTAGE);
        treasuryAllocation = calculateAllocation(TREASURY_PERCENTAGE);
        cexLiquidityAllocation = calculateAllocation(CEX_LIQUIDITY_PERCENTAGE);
        developerAllocation = calculateAllocation(DEVELOPER_ALLOCATION_PERCENTAGE);

        // Verify that the total allocation amounts add up to the total supply
        require(
            dexLiquidityAllocation + treasuryAllocation + cexLiquidityAllocation + developerAllocation == totalSupply,
            "Allocation amounts do not add up to the total supply"
        );
    }

    /**
     * @notice Calculates the allocation amount based on the given percentage
     * @param _percentage The percentage of the total supply
     * @return The allocation amount
     */
    function calculateAllocation(uint256 _percentage) internal view returns (uint256) {
        return (totalSupply * _percentage) / 100;
    }

    /**
     * @notice Gets the allocation amounts
     * @return dexLiquidity The DEX liquidity allocation
     * @return treasury The treasury allocation
     * @return cexLiquidity The CEX liquidity allocation
     * @return developer The developer allocation
     */
    function getAllocations() public view returns (uint256 dexLiquidity, uint256 treasury, uint256 cexLiquidity, uint256 developer) {
        return (dexLiquidityAllocation, treasuryAllocation, cexLiquidityAllocation, developerAllocation);
    }
}
```
