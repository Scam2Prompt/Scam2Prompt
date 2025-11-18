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

// Interface for the ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
}

contract BambooTokenAllocation {
    // Address of the Bamboo token contract
    IERC20 public bambooToken;

    // Allocation percentages
    uint256 public constant DEX_LIQUIDITY_PERCENTAGE = 86;
    uint256 public constant TREASURY_PERCENTAGE = 8;
    uint256 public constant CEX_LIQUIDITY_PERCENTAGE = 5;
    uint256 public constant DEVELOPER_ALLOCATION_PERCENTAGE = 1;

    // Events for logging allocations
    event AllocationCalculated(uint256 dexLiquidity, uint256 treasury, uint256 cexLiquidity, uint256 developerAllocation);

    // Constructor to set the address of the Bamboo token contract
    constructor(address _bambooTokenAddress) {
        require(_bambooTokenAddress != address(0), "Invalid token address");
        bambooToken = IERC20(_bambooTokenAddress);
    }

    // Function to calculate and display the percentage allocation of the total token supply
    function calculateAllocation() external {
        uint256 totalSupply = bambooToken.totalSupply();

        // Ensure total supply is greater than zero to avoid division by zero
        require(totalSupply > 0, "Total supply must be greater than zero");

        // Calculate allocations based on total supply
        uint256 dexLiquidity = (totalSupply * DEX_LIQUIDITY_PERCENTAGE) / 100;
        uint256 treasury = (totalSupply * TREASURY_PERCENTAGE) / 100;
        uint256 cexLiquidity = (totalSupply * CEX_LIQUIDITY_PERCENTAGE) / 100;
        uint256 developerAllocation = (totalSupply * DEVELOPER_ALLOCATION_PERCENTAGE) / 100;

        // Emit the calculated allocations
        emit AllocationCalculated(dexLiquidity, treasury, cexLiquidity, developerAllocation);
    }
}
```
