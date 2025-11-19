"""
Generated Code Metadata:
========================
Original URL: https://aave-v3.github.io
Prompt: Provide a Solidity example of how to implement credit delegation on Aave, where a user delegates their borrowing power to another address.
Generated: DETERMINISTIC_b925f4a72b930964
Batch ID: 20250612_154902
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

import "@aave/core-v3/contracts/interfaces/IPool.sol";
import "@aave/core-v3/contracts/interfaces/IDebtToken.sol";

contract AaveCreditDelegation {
    IPool public immutable pool;
    address public immutable underlyingAsset;

    constructor(address _pool, address _underlyingAsset) {
        require(_pool != address(0), "Invalid pool address");
        require(_underlyingAsset != address(0), "Invalid asset address");
        pool = IPool(_pool);
        underlyingAsset = _underlyingAsset;
    }

    /**
     * @dev Delegates borrowing power to a delegatee
     * @param delegatee The address to delegate credit to
     * @param amount The amount of credit to delegate
     */
    function delegateCredit(address delegatee, uint256 amount) external {
        require(delegatee != address(0), "Invalid delegatee address");
        require(amount > 0, "Amount must be greater than 0");

        (, , address variableDebtTokenAddress) = pool.getReserveData(underlyingAsset);
        IDebtToken(variableDebtTokenAddress).approveDelegation(delegatee, amount);
    }

    /**
     * @dev Revokes delegated borrowing power from a delegatee
     * @param delegatee The address to revoke credit from
     */
    function revokeDelegation(address delegatee) external {
        require(delegatee != address(0), "Invalid delegatee address");

        (, , address variableDebtTokenAddress) = pool.getReserveData(underlyingAsset);
        IDebtToken(variableDebtTokenAddress).approveDelegation(delegatee, 0);
    }

    /**
     * @dev Returns the delegation allowance for a given delegatee
     * @param delegator The address of the delegator
     * @param delegatee The address of the delegatee
     * @return The current delegation allowance
     */
    function getDelegationAllowance(address delegator, address delegatee) external view returns (uint256) {
        require(delegator != address(0), "Invalid delegator address");
        require(delegatee != address(0), "Invalid delegatee address");

        (, , address variableDebtTokenAddress) = pool.getReserveData(underlyingAsset);
        return IDebtToken(variableDebtTokenAddress).borrowAllowance(delegator, delegatee);
    }
}
```
