"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: What are the steps to build a stablecoin on the Ethereum network that maintains a stable value?
Generated: DETERMINISTIC_d35ad3eb3b6eeced
Batch ID: 20250612_155301
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
 * @title StableCoin
 * @dev A simple implementation of a stablecoin on the Ethereum network.
 *      This contract uses a centralized approach where an admin can mint and burn tokens
 *      to maintain the stable value of the coin.
 */
contract StableCoin {
    // Token metadata
    string public name = "StableCoin";
    string public symbol = "STC";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances of users
    mapping(address => uint256) private balances;

    // Mapping to track allowances for token transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Address of the admin (central authority)
    address public admin;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "StableCoin: Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract and set the admin.
     */
    constructor() {
        admin = msg.sender;
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
     * @param to The address to transfer tokens to.
     * @param value The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 value) public returns (bool) {
        require(to != address(0), "StableCoin: Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= value, "StableCoin: Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller.
     * @param spender The address to approve.
     * @param value The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 value) public returns (bool) {
        require(spender != address(0), "StableCoin: Approve to the zero address is not allowed");

        allowances[msg.sender][spender] = value;

        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Function to transfer tokens on behalf of another address.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param value The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address from, address to, uint256 value) public returns (bool) {
        require(to != address(0), "StableCoin: Transfer to the zero address is not allowed");
        require(balances[from] >= value, "StableCoin: Insufficient balance");
        require(allowances[from][msg.sender] >= value, "StableCoin: Transfer amount exceeds allowance");

        balances[from] -= value;
        balances[to] += value;
        allowances[from][msg.sender] -= value;

        emit Transfer(from, to, value);
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
     * @dev Admin-only function to mint new tokens.
     * @param to The address to mint tokens to.
     * @param value The amount of tokens to mint.
     */
    function mint(address to, uint256 value) public onlyAdmin {
        require(to != address(0), "StableCoin: Mint to the zero address is not allowed");

        totalSupply += value;
        balances[to] += value;

        emit Mint(to, value);
        emit Transfer(address(0), to, value);
    }

    /**
     * @dev Admin-only function to burn tokens from a specified address.
     * @param from The address to burn tokens from.
     * @param value The amount of tokens to burn.
     */
    function burn(address from, uint256 value) public onlyAdmin {
        require(from != address(0), "StableCoin: Burn from the zero address is not allowed");
        require(balances[from] >= value, "StableCoin: Insufficient balance to burn");

        totalSupply -= value;
        balances[from] -= value;

        emit Burn(from, value);
        emit Transfer(from, address(0), value);
    }
}
```
