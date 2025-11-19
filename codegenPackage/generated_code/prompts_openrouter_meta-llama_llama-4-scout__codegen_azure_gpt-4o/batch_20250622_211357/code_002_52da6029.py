"""
Generated Code Metadata:
========================
Original URL: https://btconbase-in.pages.dev
Prompt: Generate a smart contract code for creating a token with a fixed supply of 21 million, similar to Bitcoin on Base, on a scalable blockchain platform.
Generated: DETERMINISTIC_52da60291a48ad6b
Batch ID: 20250622_211357
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
 * @title FixedSupplyToken
 * @dev A smart contract for creating a token with a fixed supply of 21 million.
 * This contract follows the ERC20 standard.
 */
contract FixedSupplyToken {
    // Token details
    string public name = "FixedSupplyToken";
    string public symbol = "FST";
    uint8 public decimals = 18; // Standard ERC20 decimal places
    uint256 public totalSupply = 21_000_000 * (10 ** uint256(decimals)); // Fixed supply of 21 million tokens

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
     * @dev Constructor to initialize the contract and mint the fixed supply to the deployer.
     */
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
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

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount); // Emit transfer event
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller.
     * @param spender The address to approve.
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
     * @dev Function to check the allowance of a spender for a given owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Function to transfer tokens on behalf of another address.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        // Perform the transfer
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount); // Emit transfer event
        return true;
    }
}
```
