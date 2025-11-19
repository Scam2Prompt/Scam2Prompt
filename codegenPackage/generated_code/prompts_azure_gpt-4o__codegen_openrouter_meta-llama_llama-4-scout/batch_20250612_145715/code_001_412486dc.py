"""
Generated Code Metadata:
========================
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Using the Deadpool Inu tokenomics (0% tax for buy and sell), write a smart contract in Solidity that facilitates trading of $DPOOL tokens while ensuring no transaction fees are applied.
Generated: DETERMINISTIC_412486dce3d04112
Batch ID: 20250612_145715
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
 * @title Deadpool Inu Token Contract
 * @author [Your Name]
 * @notice This contract facilitates trading of $DPOOL tokens with 0% tax for buy and sell transactions.
 */
contract DeadpoolInuToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping to store token balances
    mapping(address => uint256) private _balances;

    // Mapping to store token allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of $DPOOL tokens
    uint256 private _totalSupply;

    /**
     * @notice Constructor to initialize the contract
     * @param initialSupply Initial supply of $DPOOL tokens
     */
    constructor(uint256 initialSupply) ERC20("Deadpool Inu", "DPOOL") {
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }

    /**
     * @notice Returns the total supply of $DPOOL tokens
     * @return uint256 Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of $DPOOL tokens for a given address
     * @param account Address to check balance for
     * @return uint256 Balance of $DPOOL tokens
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers $DPOOL tokens from one address to another
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool Success status
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Transfers $DPOOL tokens from one address to another with allowance
     * @param sender Address to transfer tokens from
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool Success status
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    /**
     * @notice Approves an address to spend a certain amount of $DPOOL tokens on behalf of the owner
     * @param spender Address to approve
     * @param amount Amount of tokens to approve
     * @return bool Success status
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Increases the allowance of an address to spend more $DPOOL tokens
     * @param spender Address to increase allowance for
     * @param addedValue Amount to add to allowance
     * @return bool Success status
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
        return true;
    }

    /**
     * @notice Decreases the allowance of an address to spend fewer $DPOOL tokens
     * @param spender Address to decrease allowance for
     * @param subtractedValue Amount to subtract from allowance
     * @return bool Success status
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] - subtractedValue);
        return true;
    }

    /**
     * @notice Burns $DPOOL tokens from an address
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burns $DPOOL tokens from an address on behalf of the owner
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public override {
        _burn(account, amount);
    }

    /**
     * @dev Internal function to transfer $DPOOL tokens
     * @param sender Address to transfer tokens from
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to approve an address to spend $DPOOL tokens
     * @param owner Address to approve from
     * @param spender Address to approve
     * @param amount Amount of tokens to approve
     */
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

    /**
     * @dev Internal function to burn $DPOOL tokens
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] -= amount;
        _totalSupply -= amount;

        emit Transfer(account, address(0), amount);
    }
}
```
