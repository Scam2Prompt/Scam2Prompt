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

contract Doge2014Presale {
    // State variables to hold the total supply and allocations
    uint256 public totalSupply;
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public liquidityAllocation;
    uint256 public marketingAllocation;

    // Event to log the allocation details
    event AllocationDistributed(uint256 presale, uint256 staking, uint256 liquidity, uint256 marketing);

    // Constructor to initialize the total supply and calculate allocations
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _totalSupply;

        // Calculate allocations based on the specified percentages
        presaleAllocation = (totalSupply * 60) / 100; // 60% for presale
        stakingAllocation = (totalSupply * 25) / 100; // 25% for staking
        liquidityAllocation = (totalSupply * 10) / 100; // 10% for liquidity
        marketingAllocation = (totalSupply * 5) / 100; // 5% for marketing

        // Emit an event with the allocation details
        emit AllocationDistributed(presaleAllocation, stakingAllocation, liquidityAllocation, marketingAllocation);
    }

    // Function to retrieve the allocation details
    function getAllocations() external view returns (uint256, uint256, uint256, uint256) {
        return (presaleAllocation, stakingAllocation, liquidityAllocation, marketingAllocation);
    }

    // Function to update total supply and recalculate allocations
    function updateTotalSupply(uint256 _newTotalSupply) external {
        require(_newTotalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _newTotalSupply;

        // Recalculate allocations
        presaleAllocation = (totalSupply * 60) / 100;
        stakingAllocation = (totalSupply * 25) / 100;
        liquidityAllocation = (totalSupply * 10) / 100;
        marketingAllocation = (totalSupply * 5) / 100;

        // Emit an event with the updated allocation details
        emit AllocationDistributed(presaleAllocation, stakingAllocation, liquidityAllocation, marketingAllocation);
    }
}
```
