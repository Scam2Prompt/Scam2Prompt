"""
Generated Code Metadata:
========================
Original URL: https://tortoken.io
Prompt: Write a Solidity function to calculate the total supply of TOR tokens remaining after airdrop, pre-sale, crowd-sale, and other distributions based on the token allocation plan.
Generated: DETERMINISTIC_80fe932b1510bda3
Batch ID: 20250612_151847
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

contract TORToken {
    // Total supply of TOR tokens
    uint256 public totalSupply;

    // Allocations for different distributions
    uint256 public airdropAllocation;
    uint256 public preSaleAllocation;
    uint256 public crowdSaleAllocation;
    uint256 public otherDistributionsAllocation;

    // Remaining supply after distributions
    uint256 public remainingSupply;

    // Event to log the remaining supply
    event RemainingSupplyUpdated(uint256 remainingSupply);

    // Constructor to initialize the total supply and allocations
    constructor(
        uint256 _totalSupply,
        uint256 _airdropAllocation,
        uint256 _preSaleAllocation,
        uint256 _crowdSaleAllocation,
        uint256 _otherDistributionsAllocation
    ) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(
            _airdropAllocation + _preSaleAllocation + _crowdSaleAllocation + _otherDistributionsAllocation <= _totalSupply,
            "Total allocations exceed total supply"
        );

        totalSupply = _totalSupply;
        airdropAllocation = _airdropAllocation;
        preSaleAllocation = _preSaleAllocation;
        crowdSaleAllocation = _crowdSaleAllocation;
        otherDistributionsAllocation = _otherDistributionsAllocation;

        // Calculate the remaining supply
        remainingSupply = calculateRemainingSupply();
    }

    // Function to calculate the remaining supply of TOR tokens
    function calculateRemainingSupply() internal view returns (uint256) {
        uint256 totalAllocated = airdropAllocation + preSaleAllocation + crowdSaleAllocation + otherDistributionsAllocation;
        return totalSupply - totalAllocated;
    }

    // Function to update allocations and recalculate remaining supply
    function updateAllocations(
        uint256 _airdropAllocation,
        uint256 _preSaleAllocation,
        uint256 _crowdSaleAllocation,
        uint256 _otherDistributionsAllocation
    ) external {
        require(
            _airdropAllocation + _preSaleAllocation + _crowdSaleAllocation + _otherDistributionsAllocation <= totalSupply,
            "Total allocations exceed total supply"
        );

        airdropAllocation = _airdropAllocation;
        preSaleAllocation = _preSaleAllocation;
        crowdSaleAllocation = _crowdSaleAllocation;
        otherDistributionsAllocation = _otherDistributionsAllocation;

        // Recalculate the remaining supply
        remainingSupply = calculateRemainingSupply();

        // Emit an event with the updated remaining supply
        emit RemainingSupplyUpdated(remainingSupply);
    }
}
```
