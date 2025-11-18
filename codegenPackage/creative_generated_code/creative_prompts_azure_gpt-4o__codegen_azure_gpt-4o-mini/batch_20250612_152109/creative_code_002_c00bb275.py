"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beef-meme.pages.dev
Prompt: Provide a Solidity example for a smart contract that burns a percentage of BEEF tokens during every transaction to maintain deflationary tokenomics, similar to the model described on the BEEF Coin website.
Generated: DETERMINISTIC_c00bb27527d835a3
Batch ID: 20250612_152109
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BEEFToken is IERC20 {
    using SafeMath for uint256;

    string public constant name = "BEEF Token";
    string public constant symbol = "BEEF";
    uint8 public constant decimals = 18;

    // Mapping from user addresses to their balances
    mapping(address => uint256) private _balances;
    // Mapping from owner to spender allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    uint256 private _totalSupply;
    uint256 public burnPercentage = 2; // 2% burn on every transaction

    // Events for token transfers and approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * (10 ** uint256(decimals)); // Define total supply
        _balances[msg.sender] = _totalSupply; // Assign total supply to contract deployer
    }

    // Function to get the total token supply
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Function to get the balance of a specific address
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfer function with burn mechanism
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        uint256 burnAmount = amount.mul(burnPercentage).div(100); // Calculate burn amount
        uint256 transferAmount = amount.sub(burnAmount); // Calculate amount to transfer

        _balances[msg.sender] = _balances[msg.sender].sub(amount); // Deduct amount from sender
        _balances[recipient] = _balances[recipient].add(transferAmount); // Add transfer amount to recipient
        _totalSupply = _totalSupply.sub(burnAmount); // Burn the tokens

        emit Transfer(msg.sender, recipient, transferAmount);
        emit Transfer(msg.sender, address(0), burnAmount); // Emit burn event

        return true;
    }

    // Allowance function to check the remaining tokens that a spender is allowed to spend
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Approve the transfer of tokens by a spender
    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount; // Set allowance
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    // Transfer tokens from one address to another using the allowance mechanism
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        uint256 burnAmount = amount.mul(burnPercentage).div(100); // Calculate burn amount
        uint256 transferAmount = amount.sub(burnAmount); // Calculate amount to transfer

        _balances[sender] = _balances[sender].sub(amount); // Deduct amount from sender
        _balances[recipient] = _balances[recipient].add(transferAmount); // Add transfer amount to recipient
        _totalSupply = _totalSupply.sub(burnAmount); // Burn the tokens
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount); // Deduct from allowance
        
        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, address(0), burnAmount); // Emit burn event

        return true;
    }
}
```
