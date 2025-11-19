"""
Generated Code Metadata:
========================
Original URL: https://meties.pages.dev
Prompt: Generate a sample smart contract that utilizes the low gas fees and fast transactions features of the Metis Layer 2 network.
Generated: DETERMINISTIC_9fcfdf4ae1b66da2
Batch ID: 20250612_155159
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
 * @title SimpleToken
 * @dev A simple ERC20 token implementation optimized for Metis Layer 2
 */
contract SimpleToken {
    string public constant name = "MetisToken";
    string public constant symbol = "MTK";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;
    
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    /**
     * @dev Constructor that mints initial supply to creator
     * @param initialSupply The initial token supply
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }
    
    /**
     * @dev Returns the balance of an account
     * @param account The address to query
     * @return The balance of the account
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }
    
    /**
     * @dev Transfers tokens to a specified address
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return success Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        
        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }
    
    /**
     * @dev Approves a spender to spend tokens on behalf of the owner
     * @param spender The address allowed to spend
     * @param amount The amount allowed to spend
     * @return success Whether the approval was successful
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to zero address");
        
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }
    
    /**
     * @dev Returns the allowance of a spender for an owner
     * @param owner The address of the owner
     * @param spender The address of the spender
     * @return The remaining allowance
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return _allowances[owner][spender];
    }
    
    /**
     * @dev Transfers tokens from one address to another using allowance
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return success Whether the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        
        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        
        emit Transfer(sender, recipient, amount);
        return true;
    }
    
    /**
     * @dev Burns tokens from the caller's account
     * @param amount The amount to burn
     */
    function burn(uint256 amount) external {
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        
        _balances[msg.sender] -= amount;
        totalSupply -= amount;
        
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
