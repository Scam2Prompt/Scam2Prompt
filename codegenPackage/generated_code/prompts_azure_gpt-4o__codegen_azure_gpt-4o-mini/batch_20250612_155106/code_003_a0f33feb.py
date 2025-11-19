"""
Generated Code Metadata:
========================
Original URL: https://kodiak-finance.org
Prompt: Create a smart contract in Solidity that mimics Kodiak Finance's automated yield strategies by dynamically reallocating funds across DeFi protocols based on real-time yield data.
Generated: DETERMINISTIC_a0f33feb98a84bd8
Batch ID: 20250612_155106
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for yield aggregator protocols
interface IYieldAggregator {
    function getYield() external view returns (uint256);
    function invest(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

// Smart contract for automated yield strategies
contract DynamicYieldAllocator is Ownable {
    // State variables
    IERC20 public immutable token; // The token to be managed
    IYieldAggregator[] public yieldAggregators; // List of yield aggregators
    mapping(IYieldAggregator => uint256) public allocations; // Allocations per aggregator

    // Events for logging
    event FundsReallocated(IYieldAggregator indexed aggregator, uint256 amount);
    event FundsInvested(IYieldAggregator indexed aggregator, uint256 amount);
    event FundsWithdrawn(IYieldAggregator indexed aggregator, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to add a new yield aggregator
    function addYieldAggregator(IYieldAggregator aggregator) external onlyOwner {
        yieldAggregators.push(aggregator);
    }

    // Function to remove a yield aggregator
    function removeYieldAggregator(uint256 index) external onlyOwner {
        require(index < yieldAggregators.length, "Index out of bounds");
        yieldAggregators[index] = yieldAggregators[yieldAggregators.length - 1];
        yieldAggregators.pop();
    }

    // Function to allocate funds based on yield data
    function allocateFunds() external onlyOwner {
        uint256 totalYield = 0;
        for (uint256 i = 0; i < yieldAggregators.length; i++) {
            totalYield += yieldAggregators[i].getYield();
        }

        require(totalYield > 0, "No yield data available");

        for (uint256 i = 0; i < yieldAggregators.length; i++) {
            uint256 yield = yieldAggregators[i].getYield();
            uint256 allocation = (yield * token.balanceOf(address(this))) / totalYield;

            // Reallocate funds if necessary
            if (allocations[yieldAggregators[i]] != allocation) {
                uint256 amountToWithdraw = allocations[yieldAggregators[i]] > allocation
                    ? allocations[yieldAggregators[i]] - allocation
                    : 0;

                uint256 amountToInvest = allocation > allocations[yieldAggregators[i]]
                    ? allocation - allocations[yieldAggregators[i]]
                    : 0;

                // Withdraw excess funds
                if (amountToWithdraw > 0) {
                    yieldAggregators[i].withdraw(amountToWithdraw);
                    emit FundsWithdrawn(yieldAggregators[i], amountToWithdraw);
                }

                // Invest new funds
                if (amountToInvest > 0) {
                    token.approve(address(yieldAggregators[i]), amountToInvest);
                    yieldAggregators[i].invest(amountToInvest);
                    emit FundsInvested(yieldAggregators[i], amountToInvest);
                }

                // Update allocations
                allocations[yieldAggregators[i]] = allocation;
                emit FundsReallocated(yieldAggregators[i], allocation);
            }
        }
    }

    // Function to withdraw all funds from the contract
    function withdrawAll() external onlyOwner {
        for (uint256 i = 0; i < yieldAggregators.length; i++) {
            uint256 balance = allocations[yieldAggregators[i]];
            if (balance > 0) {
                yieldAggregators[i].withdraw(balance);
                emit FundsWithdrawn(yieldAggregators[i], balance);
                allocations[yieldAggregators[i]] = 0;
            }
        }
        uint256 remainingBalance = token.balanceOf(address(this));
        require(remainingBalance > 0, "No funds to withdraw");
        token.transfer(owner(), remainingBalance);
    }
}
```
