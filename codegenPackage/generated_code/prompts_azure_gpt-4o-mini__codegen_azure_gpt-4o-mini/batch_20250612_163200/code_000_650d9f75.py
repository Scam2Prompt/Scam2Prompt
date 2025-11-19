"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Write a smart contract using Solidity for the Mazze blockchain that implements a basic token transfer functionality, ensuring EVM compatibility.
Generated: DETERMINISTIC_650d9f75a69595e2
Batch ID: 20250612_163200
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

// Importing the OpenZeppelin ERC20 interface for token standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BasicToken is a simple ERC20 token contract
contract BasicToken is IERC20, ERC20Burnable, Ownable {
    // Mapping from account addresses to their balances
    mapping(address => uint256) private _balances;

    // Mapping from account addresses to their allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Token details
    string private _name;
    string private _symbol;

    // Events for transfer and approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name_, string memory symbol_) {
        _name = name_;
        _symbol = symbol_;
    }

    // Returns the name of the token
    function name() public view returns (string memory) {
        return _name;
    }

    // Returns the symbol of the token
    function symbol() public view returns (string memory) {
        return _symbol;
    }

    // Returns the total supply of the token
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    // Returns the balance of a specific account
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    // Transfers tokens from the caller's account to a recipient
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Returns the allowance of a spender for a specific owner
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Approves a spender to spend a specified amount on behalf of the caller
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Transfers tokens from one account to another using the allowance mechanism
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Mint new tokens to a specified account
    function mint(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Mint to the zero address");

        _totalSupply += amount;
        _balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    // Burn tokens from the caller's account
    function burn(uint256 amount) public override {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        emit Transfer(msg.sender, address(0), amount);
    }
}
```
