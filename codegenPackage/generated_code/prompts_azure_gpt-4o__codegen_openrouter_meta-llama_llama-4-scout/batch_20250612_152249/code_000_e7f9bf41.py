"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: Write a Solidity smart contract that is optimized for deployment on Linea's zkEVM ecosystem, ensuring compatibility with its EVM bytecode and leveraging low gas fees.
Generated: DETERMINISTIC_e7f9bf41837c9986
Batch ID: 20250612_152249
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/ERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/security/ReentrancyGuard.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/security/ReentrancyGuard.sol";

/**
 * @title LineaERC20Token
 * @author [Your Name]
 * @notice A basic ERC20 token contract optimized for deployment on Linea's zkEVM ecosystem.
 */
contract LineaERC20Token is ERC20, ReentrancyGuard {
    // Mapping of token allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Mapping of token balances
    mapping(address => uint256) private _balances;

    // Total supply of tokens
    uint256 private _totalSupply;

    /**
     * @notice Constructor for the LineaERC20Token contract.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param totalSupply_ The total supply of tokens.
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) ERC20(name_, symbol_) {
        _totalSupply = totalSupply_;
        _balances[msg.sender] = totalSupply_;
    }

    /**
     * @notice Returns the total supply of tokens.
     * @return The total supply of tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of a specific account.
     * @param account The address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one account to another.
     * @param from The address of the sender.
     * @param to The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(to != address(0), "ERC20: transfer to the zero address");

        uint256 fromBalance = _balances[msg.sender];
        require(fromBalance >= amount, "ERC20: transfer amount exceeds balance");

        _balances[msg.sender] = fromBalance - amount;
        _balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @notice Approves an address to spend a certain amount of tokens on behalf of another address.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Returns the allowance of a spender for a certain owner.
     * @param owner The address of the owner.
     * @param spender The address of the spender.
     * @return The allowance of the spender.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Transfers tokens from one account to another on behalf of the token owner.
     * @param from The address of the sender.
     * @param to The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        uint256 fromBalance = _balances[from];
        require(fromBalance >= amount, "ERC20: transfer amount exceeds balance");

        uint256 spenderAllowance = _allowances[from][msg.sender];
        require(spenderAllowance >= amount, "ERC20: transfer amount exceeds allowance");

        _balances[from] = fromBalance - amount;
        _balances[to] += amount;

        if (spenderAllowance != type(uint256).max) {
            _allowances[from][msg.sender] = spenderAllowance - amount;
        }

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @notice Increases the allowance of a spender for a certain owner.
     * @param spender The address of the spender.
     * @param addedValue The amount to add to the allowance.
     * @return A boolean indicating whether the increase was successful.
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        uint256 currentAllowance = allowance(msg.sender, spender);
        _approve(msg.sender, spender, currentAllowance + addedValue);
        return true;
    }

    /**
     * @notice Decreases the allowance of a spender for a certain owner.
     * @param spender The address of the spender.
     * @param subtractedValue The amount to subtract from the allowance.
     * @return A boolean indicating whether the decrease was successful.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = allowance(msg.sender, spender);
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        _approve(msg.sender, spender, currentAllowance - subtractedValue);
        return true;
    }

    /**
     * @notice Approves an address to spend a certain amount of tokens on behalf of another address.
     * @param owner The address of the owner.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
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
}
```
