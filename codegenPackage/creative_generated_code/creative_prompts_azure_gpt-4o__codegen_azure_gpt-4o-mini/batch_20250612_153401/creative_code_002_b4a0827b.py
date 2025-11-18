"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Create a function in Solidity to enforce a maximum total supply of 100,000,000 "DRE" tokens and prevent minting beyond this limit.
Generated: DETERMINISTIC_b4a0827bc6898277
Batch ID: 20250612_153401
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

// Interface for ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// DRE Token Contract
contract DREToken is IERC20 {
    string public constant name = "DRE Token";
    string public constant symbol = "DRE";
    uint8 public constant decimals = 18;
    
    // Maximum supply constant
    uint256 public constant MAX_SUPPLY = 100000000 * (10 ** uint256(decimals));
    
    // State variables
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events
    event Mint(address indexed to, uint256 amount);

    // Modifier to check for maximum supply
    modifier onlyMintable(uint256 amount) {
        require(_totalSupply + amount <= MAX_SUPPLY, "Minting exceeds maximum supply");
        _;
    }

    // Constructor
    constructor() {
        // Initial supply can be set here if needed, currently set to 0
        _totalSupply = 0;
    }

    // Returns the total supply of the token
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Returns the balance of a specific account
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfers tokens to a recipient
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Allows a spender to spend a specific amount of tokens
    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Transfers tokens from one address to another using allowance
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
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

    // Returns the allowance of a spender for a specific owner
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Function to mint new tokens, can only mint up to the maximum supply
    function mint(address to, uint256 amount) external onlyMintable(amount) {
        require(to != address(0), "Mint to the zero address");

        _totalSupply += amount;
        _balances[to] += amount;

        emit Transfer(address(0), to, amount);
        emit Mint(to, amount);
    }
}
```
