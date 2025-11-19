"""
Generated Code Metadata:
========================
Original URL: https://babywif-io.pages.dev
Prompt: Generate a smart contract in Solidity for the BEP20 token named "baby wif" with the token symbol "BIF" and a total supply of 420 trillion.
Generated: DETERMINISTIC_9b38aaf97d9a370a
Batch ID: 20250612_162325
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
 * @title BEP20 Token Implementation
 * @dev This is a BEP20-compliant token named "baby wif" with the symbol "BIF".
 *      The total supply is fixed at 420 trillion tokens.
 */
contract BabyWifToken {
    // Token metadata
    string public name = "baby wif";
    string public symbol = "BIF";
    uint8 public decimals = 18; // Standard BEP20 decimal places
    uint256 public totalSupply = 420_000_000_000_000 * (10 ** uint256(decimals)); // 420 trillion tokens

    // Mapping to store balances of each address
    mapping(address => uint256) private balances;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events as per BEP20 standard
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // The owner of the contract (deployer)
    address public owner;

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token and assign the total supply to the deployer.
     */
    constructor() {
        owner = msg.sender;
        balances[owner] = totalSupply; // Assign all tokens to the deployer
        emit Transfer(address(0), owner, totalSupply); // Emit transfer event from address(0) to owner
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer to.
     * @param amount The amount to be transferred.
     * @return True if the operation was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount of tokens to be spent.
     * @return True if the operation was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that `spender` is allowed to spend on behalf of `owner`.
     * @param owner The address which owns the tokens.
     * @param spender The address which will spend the tokens.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the operation was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```
