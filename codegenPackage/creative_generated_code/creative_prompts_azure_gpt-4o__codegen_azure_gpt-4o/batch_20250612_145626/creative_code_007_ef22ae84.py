"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-network.xyz
Prompt: Recommend best practices for optimizing smart contract performance on the Linea Network.
Generated: DETERMINISTIC_ef22ae841222de32
Batch ID: 20250612_145626
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
 * @title OptimizedSmartContract
 * @dev Demonstrates best practices for optimizing smart contract performance on the Linea Network.
 */
contract OptimizedSmartContract {
    // State variables
    mapping(address => uint256) private balances; // Use mappings for efficient lookups
    uint256 private totalSupply; // Store total supply explicitly for gas efficiency

    /**
     * @dev Event to log token transfers, reduces need for fetching data via storage.
     */
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Constructor initializes the totalSupply and assigns to deployer.
     * Use immutable instead of storage where possible for gas optimization.
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;
    }

    /**
     * @dev Function to transfer tokens from one account to another.
     * @param _to The address of the recipient.
     * @param _amount The amount of tokens to send.
     */
    function transfer(address _to, uint256 _amount) external {
        // Check for valid input parameters
        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        // Emit the transfer event for logging
        emit Transfer(msg.sender, _to, _amount);
    }

    /**
     * @dev Function to get the balance of an address.
     * @param _account The address to query.
     * @return Balance of the queried address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Function to get the total supply of tokens.
     * @return Total supply of the token.
     */
    function getTotalSupply() external view returns (uint256) {
        return totalSupply;
    }

    /**
     * @dev Best Practices:
     * 1. Avoid costly operations like loops over the entire storage or array.
     * 2. Use mappings for efficient lookups.
     * 3. Minimize the use of storage writes (balance updates are optimized here).
     * 4. Avoid redundant state updates (no unnecessary writes to totalSupply).
     * 5. Utilize events to log data instead of relying on storage reads.
     * 6. Keep functions modular and avoid monolithic smart contract design.
     * 7. Use `require` for input validation to prevent invalid state changes.
     */
}
```
