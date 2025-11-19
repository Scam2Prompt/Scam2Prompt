"""
Generated Code Metadata:
========================
Original URL: https://flaretokenchainevm.com
Prompt: What is the role of EVM in Flare Token Chain, and how does it enable smart contract execution?
Generated: DETERMINISTIC_ca6c26cabc3a6b5f
Batch ID: 20250622_212546
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
 * @title EVMCompatibleContract
 * @dev Demonstrates how EVM enables smart contract execution on Flare Token Chain
 */
contract EVMCompatibleContract {
    // State variables
    mapping(address => uint256) private _balances;
    
    /**
     * @dev Emitted when tokens are transferred
     */
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    /**
     * @dev Constructor initializes the contract with initial supply
     * @param initialSupply The initial token supply
     */
    constructor(uint256 initialSupply) {
        _balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }
    
    /**
     * @dev Returns the balance of a given account
     * @param account The address to query
     * @return The balance of the account
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }
    
    /**
     * @dev Transfers tokens to a specified address
     * @param recipient The address to transfer to
     * @param amount The amount to be transferred
     * @return success Boolean indicating whether the transfer succeeded
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "EVMCompatibleContract: transfer to zero address");
        require(_balances[msg.sender] >= amount, "EVMCompatibleContract: insufficient balance");
        
        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }
    
    /**
     * @dev Demonstrates a simple EVM computation
     * @param x First operand
     * @param y Second operand
     * @return sum The sum of x and y
     * @return product The product of x and y
     */
    function compute(uint256 x, uint256 y) public pure returns (uint256 sum, uint256 product) {
        sum = x + y;
        product = x * y;
    }
}
```
