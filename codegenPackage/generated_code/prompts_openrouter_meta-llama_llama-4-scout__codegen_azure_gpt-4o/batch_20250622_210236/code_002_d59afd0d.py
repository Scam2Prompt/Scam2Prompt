"""
Generated Code Metadata:
========================
Original URL: https://thoreumdashboard.com
Prompt: Generate a smart contract code snippet in Solidity for a token with a 1% transaction burn mechanism, similar to Thoreum's burn protocol.
Generated: DETERMINISTIC_d59afd0d9e4795f1
Batch ID: 20250622_210236
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
 * @title BurnableToken
 * @dev ERC20 Token with a 1% transaction burn mechanism.
 */
contract BurnableToken {
    // Token details
    string public name = "BurnableToken";
    string public symbol = "BURN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private balances;
    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the token supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address with a 1% burn mechanism.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * 1) / 100; // Calculate 1% burn
        uint256 transferAmount = amount - burnAmount; // Calculate the amount to transfer

        balances[msg.sender] -= amount; // Deduct full amount from sender
        balances[recipient] += transferAmount; // Add transfer amount to recipient
        totalSupply -= burnAmount; // Reduce total supply by burn amount

        emit Transfer(msg.sender, recipient, transferAmount);
        emit Transfer(msg.sender, address(0), burnAmount); // Emit burn event

        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        uint256 burnAmount = (amount * 1) / 100; // Calculate 1% burn
        uint256 transferAmount = amount - burnAmount; // Calculate the amount to transfer

        balances[sender] -= amount; // Deduct full amount from sender
        balances[recipient] += transferAmount; // Add transfer amount to recipient
        totalSupply -= burnAmount; // Reduce total supply by burn amount
        allowances[sender][msg.sender] -= amount; // Deduct allowance

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, address(0), burnAmount); // Emit burn event

        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender is allowed to spend on behalf of the owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
