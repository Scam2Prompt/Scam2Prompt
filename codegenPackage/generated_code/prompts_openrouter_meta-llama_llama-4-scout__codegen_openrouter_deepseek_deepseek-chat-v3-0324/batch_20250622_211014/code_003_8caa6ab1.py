"""
Generated Code Metadata:
========================
Original URL: https://furies-mystery.pages.dev
Prompt: Develop a simple smart contract in Solidity to create a meme coin with similar characteristics to $MYSTERY, including a fixed supply and no taxes.
Generated: DETERMINISTIC_8caa6ab13e79e434
Batch ID: 20250622_211014
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
 * @title MysteryToken
 * @dev A simple ERC20 token with fixed supply and no taxes.
 */
contract MysteryToken {
    string public constant name = "Mystery";
    string public constant symbol = "MYSTERY";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 1_000_000_000 * 10**uint256(decimals); // 1 billion tokens

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor that mints the total supply to the deployer.
     */
    constructor() {
        _balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param account The address to query the balance of.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer to.
     * @param amount The amount to be transferred.
     * @return A boolean indicating if the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "MysteryToken: transfer to the zero address");
        require(_balances[msg.sender] >= amount, "MysteryToken: insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves the spender to spend a specified amount of tokens.
     * @param spender The address authorized to spend.
     * @param amount The amount authorized to spend.
     * @return A boolean indicating if the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "MysteryToken: approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that spender is allowed to spend.
     * @param owner The address owning the tokens.
     * @param spender The address authorized to spend.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender The address to transfer from.
     * @param recipient The address to transfer to.
     * @param amount The amount to be transferred.
     * @return A boolean indicating if the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "MysteryToken: transfer from the zero address");
        require(recipient != address(0), "MysteryToken: transfer to the zero address");
        require(_balances[sender] >= amount, "MysteryToken: insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "MysteryToken: insufficient allowance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```
