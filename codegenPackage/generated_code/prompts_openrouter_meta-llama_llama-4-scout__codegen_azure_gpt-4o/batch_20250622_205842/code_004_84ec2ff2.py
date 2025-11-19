"""
Generated Code Metadata:
========================
Original URL: https://doge2014sale.pages.dev
Prompt: Develop a function in Solidity to handle token allocation for the Doge2014 presale, considering the 60% presale allocation, 25% staking allocation, 10% liquidity allocation, and 5% marketing allocation.
Generated: DETERMINISTIC_84ec2ff2f985f8bc
Batch ID: 20250622_205842
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

/**
 * @title Doge2014TokenAllocation
 * @dev Handles token allocation for the Doge2014 presale and other purposes.
 */
contract Doge2014TokenAllocation {
    // Total supply of tokens
    uint256 public totalSupply;

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION_PERCENT = 60;
    uint256 public constant STAKING_ALLOCATION_PERCENT = 25;
    uint256 public constant LIQUIDITY_ALLOCATION_PERCENT = 10;
    uint256 public constant MARKETING_ALLOCATION_PERCENT = 5;

    // Allocated token amounts
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public liquidityAllocation;
    uint256 public marketingAllocation;

    // Event to log allocations
    event AllocationsSet(
        uint256 presaleAllocation,
        uint256 stakingAllocation,
        uint256 liquidityAllocation,
        uint256 marketingAllocation
    );

    /**
     * @dev Constructor to initialize the total supply and set allocations.
     * @param _totalSupply The total supply of tokens.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _totalSupply;

        // Calculate allocations based on percentages
        presaleAllocation = (totalSupply * PRESALE_ALLOCATION_PERCENT) / 100;
        stakingAllocation = (totalSupply * STAKING_ALLOCATION_PERCENT) / 100;
        liquidityAllocation = (totalSupply * LIQUIDITY_ALLOCATION_PERCENT) / 100;
        marketingAllocation = (totalSupply * MARKETING_ALLOCATION_PERCENT) / 100;

        // Emit event for transparency
        emit AllocationsSet(
            presaleAllocation,
            stakingAllocation,
            liquidityAllocation,
            marketingAllocation
        );
    }

    /**
     * @dev Function to retrieve allocation details.
     * @return Allocation details as a tuple.
     */
    function getAllocations()
        external
        view
        returns (
            uint256 presale,
            uint256 staking,
            uint256 liquidity,
            uint256 marketing
        )
    {
        return (
            presaleAllocation,
            stakingAllocation,
            liquidityAllocation,
            marketingAllocation
        );
    }
}
```
