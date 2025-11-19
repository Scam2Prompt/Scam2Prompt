"""
Generated Code Metadata:
========================
Original URL: https://pepe20-vip.web.app
Prompt: Write a Solidity smart contract for a token named PEPE 2.0 with a fixed supply of 469,000,000,000,000 tokens.
Generated: DETERMINISTIC_bfc2c012d4e9ce16
Batch ID: 20250622_210027
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
 * @title PEPE 2.0 Token Contract
 * @dev ERC20-compliant token with a fixed supply
 */
contract PEPE20Token {
    // Token details
    string public constant name = "PEPE 2.0";
    string public constant symbol = "PEPE2";
    uint8 public constant decimals = 18;

    // Total supply of tokens (fixed)
    uint256 public constant totalSupply = 469_000_000_000_000 * (10 ** uint256(decimals));

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Address of the contract owner
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the contract and mint the total supply to the owner
     */
    constructor() {
        owner = msg.sender;
        balances[owner] = totalSupply; // Mint all tokens to the owner
        emit Transfer(address(0), owner, totalSupply); // Emit transfer event for minting
    }

    /**
     * @dev Returns the balance of a given address
     * @param account The address to query the balance of
     * @return The balance of the given address
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return True if the transfer is successful
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller
     * @param spender The address authorized to spend
     * @param amount The amount of tokens to approve
     * @return True if the approval is successful
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return True if the transfer is successful
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(from != address(0), "Transfer from the zero address is not allowed");
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        // Perform the transfer
        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender is allowed to spend
     * @param owner The address of the token owner
     * @param spender The address of the spender
     * @return The remaining allowance
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
