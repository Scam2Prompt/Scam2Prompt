"""
Generated Code Metadata:
========================
Original URL: https://presales-99bitcoin.pages.dev
Prompt: Create a BRC-20 token standard compatible smart contract for the 99Bitcoins token on the Bitcoin blockchain, enabling Learn-to-Earn functionality.
Generated: DETERMINISTIC_9dfa5a8b49f5dfd3
Batch ID: 20250622_210918
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

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BRC20Token contract implementing the Learn-to-Earn functionality
contract BRC20Token is IERC20, Ownable {
    // Token details
    string public constant name = "99Bitcoins Token";
    string public constant symbol = "99BTC";
    uint8 public constant decimals = 18;

    // Total supply of the token
    uint256 private _totalSupply;

    // Mapping from address to balance
    mapping(address => uint256) private _balances;

    // Mapping from owner to spender
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event declarations
    event LearnToEarn(address indexed learner, uint256 amount);

    // Constructor to initialize the total supply
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[msg.sender] = _totalSupply;
    }

    // Function to return the total supply of the token
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Function to return the balance of a specific address
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Function to transfer tokens from the sender to a recipient
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Function to approve a spender to spend tokens on behalf of the owner
    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Function to transfer tokens from one address to another on behalf of the owner
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

    // Function to return the allowance of a spender for a specific owner
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Learn-to-Earn function to reward learners with tokens
    function learnToEarn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[owner()] >= amount, "Insufficient tokens in contract");

        _balances[owner()] -= amount;
        _balances[msg.sender] += amount;

        emit LearnToEarn(msg.sender, amount);
        emit Transfer(owner(), msg.sender, amount);
    }
}
```
