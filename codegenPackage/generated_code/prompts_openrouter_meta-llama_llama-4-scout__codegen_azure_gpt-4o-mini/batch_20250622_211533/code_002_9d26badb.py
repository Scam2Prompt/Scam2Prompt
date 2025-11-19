"""
Generated Code Metadata:
========================
Original URL: https://bulldogito.pages.dev
Prompt: Generate a smart contract in Solidity that implements a token buyback and burn mechanism for a cryptocurrency like Bulldogito Coin.
Generated: DETERMINISTIC_9d26badb71f884c6
Batch ID: 20250622_211533
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BulldogitoCoin
 * @dev Implementation of a token with buyback and burn mechanism
 */
contract BulldogitoCoin is IERC20, Ownable {
    string public name = "Bulldogito Coin";
    string public symbol = "BULL";
    uint8 public decimals = 18;
    uint256 private _totalSupply;
    
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    event Buyback(uint256 amount);
    event TokensBurned(uint256 amount);

    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[msg.sender] = _totalSupply;
    }

    // ERC20 standard functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

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

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Buyback and burn tokens from the contract's balance
     * @param amount The amount of tokens to buy back and burn
     */
    function buybackAndBurn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[address(this)] >= amount, "Insufficient contract balance");

        // Burn the tokens
        _balances[address(this)] -= amount;
        _totalSupply -= amount;

        emit TokensBurned(amount);
        emit Buyback(amount);
    }

    /**
     * @dev Function to receive Ether. msg.value will be the amount of Ether sent.
     */
    receive() external payable {
        // Accept Ether for buyback purposes
    }

    /**
     * @dev Withdraw Ether from the contract
     * @param to The address to send Ether to
     * @param amount The amount of Ether to withdraw
     */
    function withdrawEther(address payable to, uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");
        to.transfer(amount);
    }
}
```
