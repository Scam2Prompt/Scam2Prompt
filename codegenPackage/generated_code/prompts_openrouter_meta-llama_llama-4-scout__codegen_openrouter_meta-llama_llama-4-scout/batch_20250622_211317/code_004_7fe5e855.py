"""
Generated Code Metadata:
========================
Original URL: https://dcqef.com
Prompt: "Create a basic Ethereum smart contract using Solidity for a DeFi application, inspired by dcqef.com's functionalities."
Generated: DETERMINISTIC_7fe5e85533c5a3aa
Batch ID: 20250622_211317
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
 * @title Basic DeFi Smart Contract
 * @author [Your Name]
 * @notice Inspired by dcqef.com's functionalities
 */
contract BasicDeFiContract is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of user balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Contract settings
    uint256 public _totalSupply;
    uint256 public _feeRate;

    /**
     * @notice Constructor function
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param totalSupply_ Total supply of the token
     * @param feeRate_ Fee rate for transactions
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_, uint256 feeRate_) ERC20(name_, symbol_) {
        _totalSupply = totalSupply_;
        _feeRate = feeRate_;
        _balances[msg.sender] = totalSupply_;
        emit Transfer(address(0), msg.sender, totalSupply_);
    }

    /**
     * @notice Returns the total supply of the token
     * @return uint256 Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of an account
     * @param account Address of the account
     * @return uint256 Balance of the account
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one account to another
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success status
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = (amount * _feeRate) / 10000;
        uint256 netAmount = amount - fee;

        _balances[msg.sender] -= amount;
        _balances[to] += netAmount;

        emit Transfer(msg.sender, to, netAmount);
        emit Transfer(msg.sender, address(this), fee);

        return true;
    }

    /**
     * @notice Approves an account to spend tokens on behalf of another account
     * @param spender Address to approve
     * @param amount Amount to approve
     * @return bool Success status
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers tokens from one account to another, allowed by a third account
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success status
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = (amount * _feeRate) / 10000;
        uint256 netAmount = amount - fee;

        _balances[from] -= amount;
        _balances[to] += netAmount;
        _allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, netAmount);
        emit Transfer(from, address(this), fee);

        return true;
    }

    /**
     * @notice Increases the allowance of a spender
     * @param spender Address of the spender
     * @param addedValue Amount to add
     * @return bool Success status
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        _allowances[msg.sender][spender] = currentAllowance + addedValue;
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases the allowance of a spender
     * @param spender Address of the spender
     * @param subtractedValue Amount to subtract
     * @return bool Success status
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        _allowances[msg.sender][spender] = currentAllowance - subtractedValue;
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Burns tokens from an account
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        _balances[msg.sender] -= amount;
        _totalSupply -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @notice Mints new tokens
     * @param to Address to mint to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) public {
        require(msg.sender == owner(), "Only the owner can mint");
        _balances[to] += amount;
        _totalSupply += amount;
        emit Transfer(address(0), to, amount);
    }

    /**
     * @notice Sets the fee rate
     * @param feeRate_ New fee rate
     */
    function setFeeRate(uint256 feeRate_) public {
        require(msg.sender == owner(), "Only the owner can set the fee rate");
        _feeRate = feeRate_;
    }

    /**
     * @notice Returns the owner of the contract
     * @return address Owner address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
