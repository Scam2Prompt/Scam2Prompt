"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Develop a Solidity contract that implements the tokenomics for $BCB, including features for burning tokens and managing circulating supply.
Generated: DETERMINISTIC_4d8625d79442a01a
Batch ID: 20250612_163616
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
 * @title BCBToken
 * @dev Implementation of a token with burn functionality and circulating supply management.
 */
contract BCBToken {
    // Token details
    string public name = "$BCB Token";
    string public symbol = "BCB";
    uint8 public decimals = 18;

    // Total supply of tokens
    uint256 private _totalSupply;

    // Mapping to track balances of addresses
    mapping(address => uint256) private _balances;

    // Mapping to track allowances for token transfers
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when tokens are burned
    event Burn(address indexed burner, uint256 value);

    // Event emitted when an approval is made
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token with a total supply.
     * @param initialSupply The initial supply of tokens.
     */
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[msg.sender] = _totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    /**
     * @dev Returns the total supply of tokens.
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Burns a specified amount of tokens, reducing the total supply.
     * @param amount The amount of tokens to burn.
     * @return A boolean indicating success.
     */
    function burn(uint256 amount) public returns (bool) {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        emit Burn(msg.sender, amount);
        emit Transfer(msg.sender, address(0), amount);
        return true;
    }
}
```
