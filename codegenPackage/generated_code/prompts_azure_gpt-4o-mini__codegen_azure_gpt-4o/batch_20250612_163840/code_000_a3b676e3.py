"""
Generated Code Metadata:
========================
Original URL: https://cowonbasenets.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a total supply of 1 billion, similar to the $COW token on Cow On Base.
Generated: DETERMINISTIC_a3b676e3bf9ce10d
Batch ID: 20250612_163840
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
 * @title COWToken
 * @dev Implementation of a basic ERC20 token with a fixed total supply of 1 billion tokens.
 */
contract COWToken {
    // Token details
    string public name = "COW Token";
    string public symbol = "COW";
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
     * @dev Constructor that initializes the token and assigns the total supply to the contract owner.
     */
    constructor() {
        owner = msg.sender;
        balances[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply); // Emit transfer event for minting
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address authorized to spend the tokens.
     * @param amount The amount of tokens to approve.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender is allowed to transfer on behalf of the owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
