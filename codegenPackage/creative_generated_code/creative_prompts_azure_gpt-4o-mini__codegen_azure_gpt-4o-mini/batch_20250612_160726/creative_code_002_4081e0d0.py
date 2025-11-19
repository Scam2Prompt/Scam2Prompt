"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teddysbearprc20.com
Prompt: What are the tokenomics of Teddy Bear PRC20, and how do I implement a transaction that adheres to the 0% buy and sell tax policy?
Generated: DETERMINISTIC_4081e0d08d81390b
Batch ID: 20250612_160726
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

// Import the ERC20 interface and OpenZeppelin's SafeMath library
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Define the TeddyBearToken contract
contract TeddyBearToken is IERC20 {
    using SafeMath for uint256;

    // Token metadata
    string public constant name = "Teddy Bear";
    string public constant symbol = "TBR";
    uint8 public constant decimals = 18;

    // Total supply of the token
    uint256 private _totalSupply;

    // Mapping from addresses to their balances
    mapping(address => uint256) private _balances;

    // Mapping from addresses to their allowance
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events for transfer and approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply.mul(10 ** uint256(decimals)); // Adjust for decimals
        _balances[msg.sender] = _totalSupply; // Allocate the initial supply to the contract deployer
    }

    // Get the total supply of the token
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Get the balance of a specific address
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfer tokens from sender to recipient
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Allow spender to withdraw from sender's account
    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");
        
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Transfer from one address to another, respecting allowance
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);

        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Check the allowance of a spender on an owner's account
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
