"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Write a smart contract in Solidity for the $MASA token, ensuring compatibility with ERC-20 standards and incorporating token supply limits as described in Project DEKSA's whitepaper.
Generated: DETERMINISTIC_dbaa0f75d01c2b02
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Standard ERC-20 interface definition
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// The $MASA token contract implementing the ERC-20 standard
contract MASAToken is IERC20 {
    // Token details
    string public name = "$MASA Token";
    string public symbol = "MASA";
    uint8 public decimals = 18;

    // Maximum token supply
    uint256 private immutable _maxSupply;

    // Current total token supply
    uint256 private _totalSupply;

    // Balances for each account
    mapping(address => uint256) private _balances;

    // Allowances for spending
    mapping(address => mapping(address => uint256)) private _allowances;

    // Address of the contract owner
    address public owner;

    // Modifier to restrict certain functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "MASAToken: Caller is not the owner");
        _;
    }

    // Constructor sets the maximum supply and assigns all tokens to the deployer
    constructor(uint256 maxSupply) {
        require(maxSupply > 0, "MASAToken: Max supply must be greater than zero");
        _maxSupply = maxSupply;
        owner = msg.sender;

        // Mint the initial supply to the owner
        _mint(owner, maxSupply);
    }

    // Returns the maximum supply of tokens
    function maxSupply() external view returns (uint256) {
        return _maxSupply;
    }

    // Returns the total supply of tokens in circulation
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Returns the balance of a specific account
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfers tokens to a recipient
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Returns the remaining allowance of tokens for a spender
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Approves a spender to spend tokens on behalf of the caller
    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    // Transfers tokens from a sender to a recipient using the allowance mechanism
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "MASAToken: Transfer amount exceeds allowance");
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, currentAllowance - amount);
        return true;
    }

    // Internal function to transfer tokens
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "MASAToken: Transfer from the zero address");
        require(recipient != address(0), "MASAToken: Transfer to the zero address");
        require(amount > 0, "MASAToken: Transfer amount must be greater than zero");
        require(_balances[sender] >= amount, "MASAToken: Insufficient balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }

    // Internal function to mint tokens
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "MASAToken: Mint to the zero address");
        require(_totalSupply + amount <= _maxSupply, "MASAToken: Mint amount exceeds max supply");

        _totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    // Internal function to approve a spender
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "MASAToken: Approve from the zero address");
        require(spender != address(0), "MASAToken: Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
