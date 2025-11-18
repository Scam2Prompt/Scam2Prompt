"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Write a Solidity function to distribute protocol token incentives (e.g., CRV, CVX, COMP) earned by OUSD across its yield strategies.
Generated: DETERMINISTIC_0c6acd94929e8b14
Batch ID: 20250612_153526
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

// Import required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the yield strategy contract
interface IYieldStrategy {
    function distributeIncentives(address token, uint256 amount) external;
}

// Main contract for distributing token incentives
contract IncentiveDistributor is Ownable {
    // Mapping of strategy addresses to their respective incentive balances
    mapping(address => uint256) public strategyBalances;

    // Event emitted when incentives are distributed
    event IncentivesDistributed(address indexed token, address indexed strategy, uint256 amount);

    // Function to distribute protocol token incentives across yield strategies
    // @param token - Address of the incentive token (e.g., CRV, CVX, COMP)
    // @param strategies - Array of yield strategy contract addresses
    // @param amounts - Corresponding amounts of incentives to distribute
    function distributeIncentives(
        address token,
        address[] calldata strategies,
        uint256[] calldata amounts
    ) external onlyOwner {
        // Validate input lengths
        require(strategies.length == amounts.length, "Mismatched lengths");

        // Transfer incentive tokens from the distributor to this contract
        uint256 totalAmount = 0;
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }
        require(IERC20(token).transferFrom(msg.sender, address(this), totalAmount), "Transfer failed");

        // Distribute tokens to each strategy
        for (uint256 i = 0; i < strategies.length; i++) {
            uint256 amount = amounts[i];
            if (amount > 0) {
                // Update balance mapping
                strategyBalances[strategies[i]] += amount;

                // Call the strategy to distribute the incentive
                IYieldStrategy(strategies[i]).distributeIncentives(token, amount);

                // Emit event for tracking
                emit IncentivesDistributed(token, strategies[i], amount);
            }
        }
    }

    // Function to withdraw any tokens mistakenly sent to this contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
