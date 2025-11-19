"""
Generated Code Metadata:
========================
Original URL: https://bitconnect666.vercel.app
Prompt: Create a simple smart contract for a cryptocurrency like $BITCONNECT using Solidity.
Generated: DETERMINISTIC_57f636af3a3d54bc
Batch ID: 20250622_211350
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
 * @title BitConnectToken
 * @dev A simple ERC20-compliant token contract mimicking a cryptocurrency like BITCONNECT.
 * Implements basic functionality including transfers, approvals, and balance tracking.
 */
contract BitConnectToken {
    string public constant name = "BitConnect";
    string public constant symbol = "BITCONNECT";
    uint8 public constant decimals = 18;

    uint256 private _totalSupply;
    address private _owner;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Constructor that initializes the contract with initial supply.
     * @param initialSupply The initial supply of tokens (in smallest denomination).
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _owner = msg.sender;
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[_owner] = _totalSupply;
        emit Transfer(address(0), _owner, _totalSupply);
    }

    /**
     * @dev Returns the total token supply.
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the token balance of a given account.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer to.
     * @param amount The amount to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the owner.
     * @param spender The address authorized to spend.
     * @param amount The max amount they can spend.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the allowance for a spender.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one address to another using allowance.
     * @param sender The address to transfer from.
     * @param recipient The address to transfer to.
     * @param amount The amount to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the address of the current owner.
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) public {
        require(msg.sender == _owner, "Only owner can transfer ownership");
        require(newOwner != address(0), "New owner cannot be the zero address");

        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }

    /**
     * @dev Mints new tokens and assigns them to an account.
     * @param account The account to receive the tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) public {
        require(msg.sender == _owner, "Only owner can mint tokens");
        require(account != address(0), "Mint to the zero address");

        _totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Burns tokens from an account.
     * @param account The account to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) public {
        require(msg.sender == _owner, "Only owner can burn tokens");
        require(account != address(0), "Burn from the zero address");
        require(_balances[account] >= amount, "Burn amount exceeds balance");

        _balances[account] -= amount;
        _totalSupply -= amount;
        emit Transfer(account, address(0), amount);
    }
}
```
