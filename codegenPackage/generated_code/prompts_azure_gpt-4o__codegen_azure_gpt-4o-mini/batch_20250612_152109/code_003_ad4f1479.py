"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Develop a DEX trading bot in Solidity that automatically burns 5% of BTCETF tokens from transactions when Bitcoin ETF milestones are reached, as per the roadmap.
Generated: DETERMINISTIC_ad4f147914063ab8
Batch ID: 20250612_152109
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the BTCETF token with automatic burning feature
contract BTCETF is IERC20, Ownable {
    string public name = "Bitcoin ETF Token";
    string public symbol = "BTCETF";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 private _totalSupply;
    
    // Mapping from address to balance
    mapping(address => uint256) private _balances;
    
    // Mapping from owner to spender allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Milestone tracking
    uint256 public milestone;
    uint256 public constant BURN_PERCENTAGE = 5;

    // Events for logging
    event MilestoneReached(uint256 milestone);
    
    // Constructor to initialize the total supply
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[msg.sender] = _totalSupply;
    }

    // Function to get the total supply of tokens
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Function to get the balance of a specific address
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Function to transfer tokens
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Function to approve a spender
    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    // Function to transfer tokens from one address to another
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    // Function to check the allowance of a spender
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Internal function to handle token transfers and burning
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        // Calculate burn amount
        uint256 burnAmount = (amount * BURN_PERCENTAGE) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        _balances[sender] -= amount;
        _balances[recipient] += transferAmount;
        _totalSupply -= burnAmount; // Burn the tokens

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, address(0), burnAmount); // Emit burn event

        // Check if a milestone is reached
        if (transferAmount >= milestone) {
            milestone += transferAmount; // Update milestone
            emit MilestoneReached(milestone);
        }
    }

    // Internal function to approve a spender
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
