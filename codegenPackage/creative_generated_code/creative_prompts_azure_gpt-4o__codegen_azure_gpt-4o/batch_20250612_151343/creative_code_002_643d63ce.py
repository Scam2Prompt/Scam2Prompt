"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimyourneiro.pages.dev
Prompt: Provide a Solidity smart contract example for managing the $NEIRO token on the Ethereum network, including details like the token name, symbol, and supply information outlined on the NEIRO site.
Generated: DETERMINISTIC_643d63ceb8c08ccb
Batch ID: 20250612_151343
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

// ERC-20 Token Standard Interface
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

// SafeMath Library for safer arithmetic operations
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        require(a + b >= a, "SafeMath: addition overflow");
        return a + b;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "SafeMath: subtraction overflow");
        return a - b;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        require(a == 0 || (a * b) / a == b, "SafeMath: multiplication overflow");
        return a * b;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "SafeMath: division by zero");
        return a / b;
    }
}

// NEIRO Token Contract
contract NEIROToken is IERC20 {
    using SafeMath for uint256;

    // Token Details
    string public name = "$NEIRO";
    string public symbol = "NEIRO";
    uint8 public decimals = 18;

    // Total Supply
    uint256 private _totalSupply = 1000000 * (10 ** uint256(decimals)); // 1 Million tokens

    // Internal Balances Mapping
    mapping(address => uint256) private _balances;

    // Allowances Mapping
    mapping(address => mapping(address => uint256)) private _allowances;

    // Owner of the contract
    address public owner;

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Assign ownership to the deployer
        _balances[owner] = _totalSupply; // Assign all tokens to the deployer
        emit Transfer(address(0), owner, _totalSupply); // Emit initial transfer event
    }

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Transfer ownership function
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // View total supply of tokens
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // View balance of a specific account
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfer tokens to a recipient
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Approve spender to spend tokens
    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    // Transfer tokens on behalf of sender
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));
        return true;
    }

    // View allowance of a spender
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Internal transfer function
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        emit Transfer(sender, recipient, amount);
    }

    // Internal approve function
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from zero address");
        require(spender != address(0), "Approve to zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
