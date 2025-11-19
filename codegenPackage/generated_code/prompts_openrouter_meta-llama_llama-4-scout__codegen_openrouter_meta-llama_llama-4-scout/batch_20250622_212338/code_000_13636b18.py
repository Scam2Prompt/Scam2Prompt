"""
Generated Code Metadata:
========================
Original URL: https://www.mellotoken.com
Prompt: Write a smart contract in Solidity for a redistributive cryptocurrency like Mello Token, which distributes 3% of each transaction to holders.
Generated: DETERMINISTIC_13636b180ebcd6f4
Batch ID: 20250622_212338
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

/**
 * @title MelloToken
 * @author [Your Name]
 * @notice A redistributive cryptocurrency that distributes 3% of each transaction to holders.
 */
contract MelloToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of user balances and transaction counts
    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _transactionCounts;

    // Constants
    uint256 private constant _redistributionPercentage = 300; // 3%
    uint256 private _totalSupply;
    address private _owner;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _owner = msg.sender;
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
    }

    /**
     * @notice Transfer tokens
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = _calculateFee(amount);
        uint256 netAmount = amount - fee;

        // Burn fee
        _burn(msg.sender, fee);

        // Distribute fee to holders
        _distributeFee(fee);

        // Transfer net amount
        _transfer(msg.sender, to, netAmount);

        return true;
    }

    /**
     * @notice Transfer tokens from one address to another
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = _calculateFee(amount);
        uint256 netAmount = amount - fee;

        // Burn fee
        _burn(from, fee);

        // Distribute fee to holders
        _distributeFee(fee);

        // Transfer net amount
        _transfer(from, to, netAmount);

        // Approve and transfer
        uint256 allowance = allowance(from, msg.sender);
        require(allowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(from, msg.sender, allowance - amount);

        return true;
    }

    /**
     * @notice Calculate redistribution fee
     * @param amount Amount to calculate fee for
     * @return uint256 Fee
     */
    function _calculateFee(uint256 amount) internal pure returns (uint256) {
        return (amount * _redistributionPercentage) / 10000;
    }

    /**
     * @notice Distribute fee to holders
     * @param fee Fee to distribute
     */
    function _distributeFee(uint256 fee) internal {
        for (address holder in _balances) {
            if (holder != address(this) && _balances[holder] > 0) {
                uint256 share = (fee * _balances[holder]) / _totalSupply;
                _transfer(address(this), holder, share);
            }
        }
    }

    /**
     * @notice Get balance of an address
     * @param owner Address to get balance for
     * @return uint256 Balance
     */
    function balanceOf(address owner) public view override returns (uint256) {
        return _balances[owner];
    }

    /**
     * @notice Get total supply
     * @return uint256 Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Handle ERC20 token burn
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Handle ERC20 token burn from an address
     * @param from Address to burn from
     * @param amount Amount to burn
     */
    function burnFrom(address from, uint256 amount) public override {
        uint256 allowance = allowance(from, msg.sender);
        require(allowance >= amount, "ERC20: burn amount exceeds allowance");
        _approve(from, msg.sender, allowance - amount);
        _burn(from, amount);
    }

    /**
     * @dev Internal function to handle token burn
     * @param account Account to burn from
     * @param amount Amount to burn
     */
    function _burn(address account, uint256 amount) internal override {
        require(account != address(0), "ERC20: burn from the zero address");

        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "ERC20: burn amount exceeds balance");

        unchecked {
            _balances[account] = accountBalance - amount;
        }
        _totalSupply -= amount;
        emit Transfer(account, address(0), amount);
    }

    /**
     * @dev Internal function to handle token transfer
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function _transfer(address from, address to, uint256 amount) internal override {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        uint256 fromBalance = _balances[from];
        require(fromBalance >= amount, "ERC20: transfer amount exceeds balance");

        unchecked {
            _balances[from] = fromBalance - amount;
            _balances[to] += amount;
        }

        emit Transfer(from, to, amount);
    }

    /**
     * @dev Internal function to handle token approval
     * @param owner Owner address
     * @param spender Spender address
     * @param amount Amount to approve
     */
    function _approve(address owner, address spender, uint256 amount) internal override {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
