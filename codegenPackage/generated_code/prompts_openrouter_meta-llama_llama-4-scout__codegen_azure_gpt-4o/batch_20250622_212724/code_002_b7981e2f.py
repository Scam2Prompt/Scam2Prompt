"""
Generated Code Metadata:
========================
Original URL: https://peppermeme.org
Prompt: Generate a smart contract code snippet in Solidity for a token with a total supply of 1 billion, similar to the $PEPPER token economics described on the webpage.
Generated: DETERMINISTIC_b7981e2fffc35370
Batch ID: 20250622_212724
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
 * @title PEPPER Token
 * @dev ERC20 Token implementation with a fixed total supply of 1 billion tokens.
 */
contract PepperToken {
    // Token details
    string public name = "PepperToken";
    string public symbol = "PEPPER";
    uint8 public decimals = 18;

    // Total supply of the token (1 billion tokens with 18 decimals)
    uint256 public totalSupply = 1_000_000_000 * (10 ** uint256(decimals));

    // Mapping to store balances of each address
    mapping(address => uint256) private balances;

    // Mapping to store allowances for token transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Address of the contract owner
    address public owner;

    // Events for logging token transfers and approvals
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the contract and mint the total supply to the owner.
     */
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
        balances[owner] = totalSupply; // Mint all tokens to the owner
        emit Transfer(address(0), owner, totalSupply); // Emit transfer event for minting
    }

    /**
     * @dev Function to check the balance of a given address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to transfer tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount; // Deduct from sender's balance
        balances[recipient] += amount; // Add to recipient's balance

        emit Transfer(msg.sender, recipient, amount); // Emit transfer event
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller.
     * @param spender The address authorized to spend the tokens.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        allowances[msg.sender][spender] = amount; // Set the allowance
        emit Approval(msg.sender, spender, amount); // Emit approval event
        return true;
    }

    /**
     * @dev Function to transfer tokens on behalf of another address.
     * @param sender The address from which tokens will be transferred.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[sender] -= amount; // Deduct from sender's balance
        balances[recipient] += amount; // Add to recipient's balance
        allowances[sender][msg.sender] -= amount; // Deduct from allowance

        emit Transfer(sender, recipient, amount); // Emit transfer event
        return true;
    }

    /**
     * @dev Function to check the remaining allowance for a spender.
     * @param owner The address of the token owner.
     * @param spender The address authorized to spend the tokens.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
