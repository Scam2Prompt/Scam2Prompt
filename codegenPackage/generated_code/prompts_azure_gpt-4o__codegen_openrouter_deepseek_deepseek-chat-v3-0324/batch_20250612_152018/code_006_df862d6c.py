"""
Generated Code Metadata:
========================
Original URL: https://shardeumbeta.pages.dev
Prompt: Create a Solidity smart contract optimized for deployment on Shardeum Betanet, leveraging its linear scalability and low gas fees.
Generated: DETERMINISTIC_df862d6c35221d19
Batch ID: 20250612_152018
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
 * @title ShardeumOptimizedContract
 * @dev A smart contract optimized for Shardeum Betanet with linear scalability and low gas fees
 */
contract ShardeumOptimizedContract {
    // State variables
    address public owner;
    uint256 public totalSupply;
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the initial owner and total supply
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply;
        balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }

    /**
     * @dev Transfer tokens to a specified address
     * @param to The address to transfer to
     * @param value The amount to be transferred
     */
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= value, "Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approve the passed address to spend the specified amount of tokens
     * @param spender The address which will spend the funds
     * @param value The amount of tokens to be spent
     */
    function approve(address spender, uint256 value) external returns (bool) {
        allowances[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another
     * @param from The address to transfer from
     * @param to The address to transfer to
     * @param value The amount to be transferred
     */
    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(balances[from] >= value, "Insufficient balance");
        require(allowances[from][msg.sender] >= value, "Allowance exceeded");

        balances[from] -= value;
        balances[to] += value;
        allowances[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }

    /**
     * @dev Increase allowance for a spender
     * @param spender The address which will spend the funds
     * @param addedValue The additional amount of tokens to be spent
     */
    function increaseAllowance(address spender, uint256 addedValue) external returns (bool) {
        allowances[msg.sender][spender] += addedValue;
        emit Approval(msg.sender, spender, allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @dev Decrease allowance for a spender
     * @param spender The address which will spend the funds
     * @param subtractedValue The amount of tokens to decrease allowance by
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) external returns (bool) {
        uint256 currentAllowance = allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "Decreased allowance below zero");
        allowances[msg.sender][spender] = currentAllowance - subtractedValue;
        emit Approval(msg.sender, spender, allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @dev Transfer contract ownership to a new address
     * @param newOwner The address to transfer ownership to
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Mint new tokens (only owner)
     * @param amount The amount of tokens to mint
     */
    function mint(uint256 amount) external onlyOwner {
        totalSupply += amount;
        balances[owner] += amount;
        emit Transfer(address(0), owner, amount);
    }

    /**
     * @dev Burn tokens (only owner)
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external onlyOwner {
        require(balances[owner] >= amount, "Insufficient balance to burn");
        totalSupply -= amount;
        balances[owner] -= amount;
        emit Transfer(owner, address(0), amount);
    }
}
```
