"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reef-io.pages.dev
Prompt: Generate a smart contract for minting REEF-20 tokens on the Reef chain, including functionality for token transfers and approvals.
Generated: DETERMINISTIC_9dbfde5ee1228ce5
Batch ID: 20250612_145933
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

// Interface for ERC20 standard functions
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

// Implementation of the REEF-20 token standard
contract ReefToken is IERC20 {
    string public name; // Name of the token
    string public symbol; // Symbol of the token
    uint8 public decimals; // Number of decimals
    uint256 private _totalSupply; // Total supply of the token
    mapping(address => uint256) private _balances; // Mapping of balances
    mapping(address => mapping(address => uint256)) private _allowances; // Mapping of allowances

    // Constructor to initialize token details
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 initialSupply) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[msg.sender] = _totalSupply; // Assign initial supply to the contract creator
        emit Transfer(address(0), msg.sender, _totalSupply); // Emit transfer event
    }

    // Returns the total supply of tokens
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Returns the balance of a specific account
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfers tokens to a specified address
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance for transfer");

        _balances[msg.sender] -= amount; // Deduct amount from sender's balance
        _balances[recipient] += amount; // Add amount to recipient's balance
        emit Transfer(msg.sender, recipient, amount); // Emit transfer event
        return true;
    }

    // Returns the remaining number of tokens that spender can spend on behalf of owner
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Approves a spender to spend a specified amount of tokens on behalf of the owner
    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");
        
        _allowances[msg.sender][spender] = amount; // Set allowance
        emit Approval(msg.sender, spender, amount); // Emit approval event
        return true;
    }

    // Transfers tokens from a specified account to another account using allowance mechanism
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[sender] >= amount, "Insufficient balance for transfer");
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        _balances[sender] -= amount; // Deduct amount from sender's balance
        _balances[recipient] += amount; // Add amount to recipient's balance
        _allowances[sender][msg.sender] -= amount; // Deduct amount from allowance
        emit Transfer(sender, recipient, amount); // Emit transfer event
        return true;
    }
}
```
