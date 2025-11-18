"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave-v3.github.io
Prompt: Provide a Solidity example of how to implement credit delegation on Aave, where a user delegates their borrowing power to another address.
Generated: DETERMINISTIC_b925f4a72b930964
Batch ID: 20250612_154902
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
 * @title AaveCreditDelegation
 * @dev Example implementation of credit delegation on Aave
 * This contract allows a user to delegate their borrowing power to another address.
 * 
 * Requirements:
 * - Deploy on a network supported by Aave.
 * - Ensure the delegator has deposited collateral and has borrowing power available.
 */

interface ILendingPool {
    function approveDelegation(address delegatee, uint256 amount) external;
}

contract AaveCreditDelegation {
    // Address of Aave's Lending Pool contract (specific to the network in use)
    ILendingPool public immutable lendingPool;

    /**
     * @dev Constructor to initialize the Lending Pool address
     * @param _lendingPool Address of the Aave Lending Pool contract
     */
    constructor(address _lendingPool) {
        require(_lendingPool != address(0), "LendingPool address cannot be zero");
        lendingPool = ILendingPool(_lendingPool);
    }

    /**
     * @dev Delegate borrowing power to another address
     * @param delegatee Address receiving the delegated borrowing power
     * @param amount Amount of borrowing power to delegate (in Wei)
     */
    function delegateCredit(address delegatee, uint256 amount) external {
        require(delegatee != address(0), "Delegatee address cannot be zero");
        require(amount > 0, "Delegation amount must be greater than zero");

        // Delegate credit using Aave's approveDelegation function
        lendingPool.approveDelegation(delegatee, amount);
    }
}
```
