"""
Generated Code Metadata:
========================
Original URL: https://normilio.pages.dev
Prompt: Write a Solidity smart contract for a community-driven cryptocurrency project on the Base blockchain, similar to Normilio.
Generated: DETERMINISTIC_1f09c498b093df88
Batch ID: 20250622_211131
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
 * @title CommunityToken
 * @dev A community-driven ERC20 token for the Base blockchain.
 *      This contract implements a basic ERC20 token with minting and governance features.
 */
contract CommunityToken {
    // Token details
    string public name = "CommunityToken";
    string public symbol = "CTKN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 value);

    // Governance variables
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract and set the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Transfer tokens from the caller to a recipient.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success True if the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool success) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the caller.
     * @param spender The address allowed to spend tokens.
     * @param amount The amount of tokens to approve.
     * @return success True if the approval was successful.
     */
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using an allowance.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success True if the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool success) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Mint new tokens to a specified address. Only the owner can call this function.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Mint to the zero address is not allowed");

        totalSupply += amount;
        balances[to] += amount;

        emit Mint(to, amount);
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account The address to query the balance of.
     * @return balance The balance of the specified address.
     */
    function balanceOf(address account) external view returns (uint256 balance) {
        return balances[account];
    }

    /**
     * @dev Get the remaining allowance for a spender on behalf of an owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return remaining The remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256 remaining) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfer ownership of the contract to a new address. Only the current owner can call this function.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
