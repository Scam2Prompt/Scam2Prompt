"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bamboomeme.pages.dev
Prompt: Create a Solidity function to calculate the percentage allocation of `$BAMBOO` token supply (86% DEX liquidity, 8% treasury, 5% CEX liquidity, 1% developer allocation) and display these values on-chain.
Generated: DETERMINISTIC_1452c691a38b190c
Batch ID: 20250612_152240
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
 * @title BambooTokenAllocation
 * @dev A contract to calculate and display percentage allocation of $BAMBOO token supply.
 */
contract BambooTokenAllocation {
    // State variable for total token supply
    uint256 public totalSupply;

    // Event to emit allocation details
    event AllocationDetails(
        uint256 dexLiquidity,
        uint256 treasury,
        uint256 cexLiquidity,
        uint256 developerAllocation
    );

    /**
     * @dev Constructor to set the total token supply.
     * @param _totalSupply The total supply of $BAMBOO tokens.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than 0");
        totalSupply = _totalSupply;
    }

    /**
     * @dev Function to calculate percentage allocations and display on-chain.
     * @return dexLiquidity The allocation for DEX liquidity (86%).
     * @return treasury The allocation for treasury (8%).
     * @return cexLiquidity The allocation for CEX liquidity (5%).
     * @return developerAllocation The allocation for developer (1%).
     */
    function calculateAllocations()
        external
        returns (
            uint256 dexLiquidity,
            uint256 treasury,
            uint256 cexLiquidity,
            uint256 developerAllocation
        )
    {
        // Calculate allocations based on percentage
        dexLiquidity = (totalSupply * 86) / 100; // 86% for DEX liquidity
        treasury = (totalSupply * 8) / 100;     // 8% for treasury
        cexLiquidity = (totalSupply * 5) / 100; // 5% for CEX liquidity
        developerAllocation = (totalSupply * 1) / 100; // 1% for developer

        // Emit the allocation details
        emit AllocationDetails(dexLiquidity, treasury, cexLiquidity, developerAllocation);

        return (dexLiquidity, treasury, cexLiquidity, developerAllocation);
    }
}
```
