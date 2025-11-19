"""
Generated Code Metadata:
========================
Original URL: https://pepecoin.blog
Prompt: Write a smart contract (if applicable) or a simple program to demonstrate Pepecoin's "no pre-mining or pre-sale" feature, ensuring equal access to mining and purchasing.
Generated: DETERMINISTIC_ce8024173a1b7ec8
Batch ID: 20250622_211652
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
 * @title Pepecoin
 * @dev A simple ERC20 token contract demonstrating no pre-mining or pre-sale.
 * Ensures equal access to mining and purchasing by:
 * 1. No initial token allocation
 * 2. Public minting function available to all
 * 3. No privileged addresses
 */
contract Pepecoin {
    string public constant name = "Pepecoin";
    string public constant symbol = "PEPE";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;
    
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed minter, uint256 amount);

    /**
     * @dev Public minting function available to anyone
     * @param amount The amount of Pepecoin to mint
     */
    function mint(uint256 amount) public {
        require(amount > 0, "Pepecoin: Amount must be greater than 0");
        
        balanceOf[msg.sender] += amount;
        totalSupply += amount;
        
        emit Transfer(address(0), msg.sender, amount);
        emit Mint(msg.sender, amount);
    }

    /**
     * @dev Transfer tokens to a specified address
     * @param to The address to transfer to
     * @param value The amount to be transferred
     */
    function transfer(address to, uint256 value) public returns (bool) {
        require(to != address(0), "Pepecoin: Transfer to zero address");
        require(balanceOf[msg.sender] >= value, "Pepecoin: Insufficient balance");

        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        
        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approve the passed address to spend the specified amount of tokens
     * @param spender The address which will spend the funds
     * @param value The amount of tokens to be spent
     */
    function approve(address spender, uint256 value) public returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another
     * @param from The address to transfer from
     * @param to The address to transfer to
     * @param value The amount to be transferred
     */
    function transferFrom(address from, address to, uint256 value) public returns (bool) {
        require(to != address(0), "Pepecoin: Transfer to zero address");
        require(balanceOf[from] >= value, "Pepecoin: Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Pepecoin: Insufficient allowance");

        balanceOf[from] -= value;
        balanceOf[to] += value;
        allowance[from][msg.sender] -= value;
        
        emit Transfer(from, to, value);
        return true;
    }
}
```
