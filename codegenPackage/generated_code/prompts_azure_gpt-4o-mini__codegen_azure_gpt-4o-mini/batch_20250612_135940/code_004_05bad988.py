"""
Generated Code Metadata:
========================
Original URL: https://defiwalletswap.com
Prompt: Provide an example of how to set up anti-whale trading fee logic in a smart contract for a DeFi wallet.
Generated: DETERMINISTIC_05bad9883888825a
Batch ID: 20250612_135940
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
 * @title AntiWhaleToken
 * @dev A simple ERC20 token with anti-whale trading fee logic.
 */
contract AntiWhaleToken is IERC20, Ownable {
    string public name = "AntiWhaleToken";
    string public symbol = "AWT";
    uint8 public decimals = 18;
    uint256 private _totalSupply;
    
    // Mapping from address to balance
    mapping(address => uint256) private _balances;
    // Mapping from address to allowance
    mapping(address => mapping(address => uint256)) private _allowances;

    // Trading fee percentage (in basis points, e.g., 100 = 1%)
    uint256 public tradingFeePercentage = 100; // 1%
    // Maximum transaction amount (in tokens)
    uint256 public maxTransactionAmount;

    event TradingFeeUpdated(uint256 newFee);
    event MaxTransactionAmountUpdated(uint256 newMaxAmount);

    constructor(uint256 initialSupply, uint256 _maxTransactionAmount) {
        _totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[msg.sender] = _totalSupply;
        maxTransactionAmount = _maxTransactionAmount * 10 ** uint256(decimals);
    }

    // ERC20 functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    // Internal transfer function with anti-whale logic
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(amount <= maxTransactionAmount, "Transfer amount exceeds the max transaction limit");

        uint256 fee = (amount * tradingFeePercentage) / 10000; // Calculate fee
        uint256 amountAfterFee = amount - fee; // Amount after fee deduction

        // Update balances
        _balances[sender] -= amount;
        _balances[recipient] += amountAfterFee;
        _balances[owner()] += fee; // Transfer fee to the contract owner

        emit Transfer(sender, recipient, amountAfterFee);
        emit Transfer(sender, owner(), fee); // Emit fee transfer
    }

    // Internal approve function
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Owner functions to update trading fee and max transaction amount
    function updateTradingFee(uint256 newFee) external onlyOwner {
        require(newFee <= 1000, "Fee cannot exceed 10%");
        tradingFeePercentage = newFee;
        emit TradingFeeUpdated(newFee);
    }

    function updateMaxTransactionAmount(uint256 newMaxAmount) external onlyOwner {
        maxTransactionAmount = newMaxAmount * 10 ** uint256(decimals);
        emit MaxTransactionAmountUpdated(maxTransactionAmount);
    }
}
```
