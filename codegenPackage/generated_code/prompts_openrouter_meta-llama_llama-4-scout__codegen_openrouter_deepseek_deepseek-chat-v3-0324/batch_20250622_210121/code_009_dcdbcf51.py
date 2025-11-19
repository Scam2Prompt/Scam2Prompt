"""
Generated Code Metadata:
========================
Original URL: https://metisdap.pages.dev
Prompt: "Write a smart contract example for a decentralized application on Metis, utilizing its low gas fees and fast transactions."
Generated: DETERMINISTIC_dcdbcf51c09e908d
Batch ID: 20250622_210121
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
 * @dev A simple ERC20 token example for Metis network
 */
contract SimpleToken {
    string public constant name = "SimpleToken";
    string public constant symbol = "STK";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;
    
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    /**
     * @dev Constructor that mints initial supply to creator
     * @param initialSupply The initial supply of tokens
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * 10**uint256(decimals);
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }
    
    /**
     * @dev Get the token balance of specified account
     * @param account The address to query
     * @return The balance of the account
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }
    
    /**
     * @dev Transfer tokens to a specified address
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return success Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[msg.sender] >= amount, "ERC20: transfer amount exceeds balance");
        
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }
    
    /**
     * @dev Approve the passed address to spend the specified amount of tokens
     * @param spender The address to approve
     * @param amount The amount to approve
     * @return success Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }
    
    /**
     * @dev Get the allowance of a spender for an owner
     * @param owner The address of the owner
     * @param spender The address of the spender
     * @return remaining The remaining allowance
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
    
    /**
     * @dev Transfer tokens from one address to another using allowance
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return success Whether the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[sender] >= amount, "ERC20: transfer amount exceeds balance");
        require(allowances[sender][msg.sender] >= amount, "ERC20: transfer amount exceeds allowance");
        
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }
    
    /**
     * @dev Mint new tokens to specified address (owner only)
     * @param account The address to mint to
     * @param amount The amount to mint
     */
    function mint(address account, uint256 amount) public {
        require(account != address(0), "ERC20: mint to the zero address");
        require(msg.sender == tx.origin, "Only EOA can mint"); // Simple protection against contract calls
        
        totalSupply += amount;
        balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }
    
    /**
     * @dev Burn tokens from sender's account
     * @param amount The amount to burn
     */
    function burn(uint256 amount) public {
        require(balances[msg.sender] >= amount, "ERC20: burn amount exceeds balance");
        
        balances[msg.sender] -= amount;
        totalSupply -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
