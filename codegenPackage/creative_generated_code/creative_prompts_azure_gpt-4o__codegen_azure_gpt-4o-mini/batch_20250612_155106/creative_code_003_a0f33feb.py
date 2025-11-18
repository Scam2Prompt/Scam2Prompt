"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kodiak-finance.org
Prompt: Create a smart contract in Solidity that mimics Kodiak Finance's automated yield strategies by dynamically reallocating funds across DeFi protocols based on real-time yield data.
Generated: DETERMINISTIC_a0f33feb98a84bd8
Batch ID: 20250612_155106
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for a DeFi protocol to get yield information
interface IYieldStrategy {
    function getYield() external view returns (uint256);
    function invest(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

// Main contract
contract DynamicYieldAllocator is Ownable {
    // State variables
    IERC20 public immutable stablecoin; // The stablecoin used for investment
    IYieldStrategy[] public yieldStrategies; // Array of yield strategies
    mapping(address => uint256) public investedAmounts; // Tracking invested amounts per strategy

    // Events for logging
    event Allocated(address indexed strategy, uint256 amount);
    event Withdrawn(address indexed strategy, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stablecoin) {
        stablecoin = _stablecoin;
    }

    // Function to add a new yield strategy
    function addYieldStrategy(IYieldStrategy strategy) external onlyOwner {
        yieldStrategies.push(strategy);
    }

    // Function to dynamically allocate funds based on yield
    function allocateFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(stablecoin.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Withdraw funds from previous strategies
        for (uint256 i = 0; i < yieldStrategies.length; i++) {
            IYieldStrategy strategy = yieldStrategies[i];
            uint256 investedAmount = investedAmounts[address(strategy)];

            if (investedAmount > 0) {
                strategy.withdraw(investedAmount);
                investedAmounts[address(strategy)] = 0; // Reset invested amount
                emit Withdrawn(address(strategy), investedAmount);
            }
        }

        // Allocate funds based on current yields
        uint256 totalYield = 0;
        for (uint256 i = 0; i < yieldStrategies.length; i++) {
            totalYield += yieldStrategies[i].getYield();
        }

        // Invest in strategies proportional to their yield
        for (uint256 i = 0; i < yieldStrategies.length; i++) {
            IYieldStrategy strategy = yieldStrategies[i];
            uint256 strategyYield = strategy.getYield();

            if (totalYield > 0 && strategyYield > 0) {
                uint256 allocation = (amount * strategyYield) / totalYield;
                strategy.invest(allocation);
                investedAmounts[address(strategy)] += allocation; // Update invested amount
                emit Allocated(address(strategy), allocation);
            }
        }
    }

    // Function to withdraw all funds from a specific strategy
    function withdrawFromStrategy(IYieldStrategy strategy) external onlyOwner {
        uint256 investedAmount = investedAmounts[address(strategy)];
        require(investedAmount > 0, "No funds invested in this strategy");

        strategy.withdraw(investedAmount);
        investedAmounts[address(strategy)] = 0; // Reset invested amount
        emit Withdrawn(address(strategy), investedAmount);
    }

    // Function to withdraw all funds to the owner's address
    function withdrawAll() external onlyOwner {
        for (uint256 i = 0; i < yieldStrategies.length; i++) {
            IYieldStrategy strategy = yieldStrategies[i];
            uint256 investedAmount = investedAmounts[address(strategy)];

            if (investedAmount > 0) {
                strategy.withdraw(investedAmount);
                investedAmounts[address(strategy)] = 0; // Reset invested amount
                emit Withdrawn(address(strategy), investedAmount);
            }
        }

        uint256 balance = stablecoin.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        stablecoin.transfer(owner(), balance);
    }
}
```
