"""
Generated Code Metadata:
========================
Original URL: https://safemoonx.xyz
Prompt: Create a smart contract in Solidity that mimics the tokenomics of SafeMoonX, including features like 5% redistribution and 5% liquidity pool acquisition.
Generated: DETERMINISTIC_9d96af8eb8c54d4a
Batch ID: 20250612_162554
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SafeMoonX is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _reflectionBalances;
    uint256 private _totalSupply;
    uint256 private _totalReflections;
    uint256 private constant _initialSupply = 1000000 * 10**18; // 1,000,000 tokens with 18 decimals

    uint256 private constant _redistributionFee = 5;
    uint256 private constant _liquidityFee = 5;
    uint256 private constant _totalFee = _redistributionFee.add(_liquidityFee);

    address private _owner;
    address private _liquidityPool;

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event LiquidityPoolUpdated(address indexed previousLiquidityPool, address indexed newLiquidityPool);

    constructor() ERC20("SafeMoonX", "SMX") {
        _owner = msg.sender;
        _totalSupply = _initialSupply;
        _balances[msg.sender] = _initialSupply;
        _reflectionBalances[msg.sender] = _initialSupply;
        _totalReflections = 0;

        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    // Functions
    function transferOwnership(address newOwner) public {
        require(msg.sender == _owner, "Caller is not the owner");
        require(newOwner != address(0), "New owner is the zero address");

        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }

    function setLiquidityPool(address newLiquidityPool) public {
        require(msg.sender == _owner, "Caller is not the owner");
        require(newLiquidityPool != address(0), "New liquidity pool is the zero address");

        emit LiquidityPoolUpdated(_liquidityPool, newLiquidityPool);
        _liquidityPool = newLiquidityPool;
    }

    // Token functions
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].add(addedValue));
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].sub(subtractedValue, "ERC20: decreased allowance below zero"));
        return true;
    }

    function burn(uint256 amount) public override nonReentrant {
        _burn(msg.sender, amount);
    }

    function burnFrom(address account, uint256 amount) public override nonReentrant {
        _burnFrom(account, amount);
    }

    // Internal functions
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");

        uint256 fee = amount.mul(_totalFee).div(100);
        uint256 redistribution = fee.mul(_redistributionFee).div(_totalFee);
        uint256 liquidity = fee.mul(_liquidityFee).div(_totalFee);

        _balances[sender] = senderBalance.sub(amount);
        _balances[recipient] = _balances[recipient].add(amount.sub(fee));
        _balances[_owner] = _balances[_owner].add(redistribution);
        _balances[_liquidityPool] = _balances[_liquidityPool].add(liquidity);

        emit Transfer(sender, recipient, amount.sub(fee));
        emit Transfer(sender, _owner, redistribution);
        emit Transfer(sender, _liquidityPool, liquidity);
    }

    function _burn(address account, uint256 amount) internal override {
        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "ERC20: burn amount exceeds balance");

        _balances[account] = accountBalance.sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(account, address(0), amount);
    }

    function _burnFrom(address account, uint256 amount) internal override {
        uint256 accountBalance = _allowances[account][msg.sender];
        require(accountBalance >= amount, "ERC20: burn amount exceeds allowance");

        _allowances[account][msg.sender] = accountBalance.sub(amount);
        _burn(account, amount);
    }

    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
