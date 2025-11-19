"""
Generated Code Metadata:
========================
Original URL: https://zootopia.finance
Prompt: Generate a smart contract code for a DeFi application similar to Zootopia Finance.
Generated: DETERMINISTIC_54d11c2307d0ec17
Batch ID: 20250622_212813
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

/**
 * @title Zootopia Finance Token Contract
 * @author [Your Name]
 * @notice This contract represents the Zootopia Finance token, 
 *         a DeFi application token for lending and borrowing.
 */
contract ZootopiaFinanceToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Token information
    string private _name;
    string private _symbol;
    uint256 private _totalSupply;

    // Lending and borrowing configuration
    uint256 public lendingRate;
    uint256 public borrowingRate;
    address public lendingPool;

    /**
     * @notice Constructor for the Zootopia Finance token contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param totalSupply The total supply of the token
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _name = name;
        _symbol = symbol;
        _totalSupply = totalSupply;
        _balances[msg.sender] = totalSupply;

        // Initialize lending and borrowing rates
        lendingRate = 5; // 5%
        borrowingRate = 10; // 10%
        lendingPool = msg.sender;
    }

    /**
     * @notice Lend tokens to the lending pool
     * @param amount The amount of tokens to lend
     */
    function lend(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid amount");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[lendingPool] = _balances[lendingPool].add(amount);

        emit Transfer(msg.sender, lendingPool, amount);
    }

    /**
     * @notice Borrow tokens from the lending pool
     * @param amount The amount of tokens to borrow
     */
    function borrow(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid amount");
        require(_balances[lendingPool] >= amount, "Insufficient liquidity");

        _balances[msg.sender] = _balances[msg.sender].add(amount);
        _balances[lendingPool] = _balances[lendingPool].sub(amount);

        emit Transfer(lendingPool, msg.sender, amount);

        // Calculate interest
        uint256 interest = amount.mul(borrowingRate).div(100);
        _balances[msg.sender] = _balances[msg.sender].sub(interest);
        _balances[lendingPool] = _balances[lendingPool].add(interest);

        emit Transfer(msg.sender, lendingPool, interest);
    }

    /**
     * @notice Repay borrowed tokens to the lending pool
     * @param amount The amount of tokens to repay
     */
    function repay(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid amount");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[lendingPool] = _balances[lendingPool].add(amount);

        emit Transfer(msg.sender, lendingPool, amount);
    }

    /**
     * @notice Get the balance of a user
     * @param user The address of the user
     * @return The balance of the user
     */
    function balanceOf(address user) public view override returns (uint256) {
        return _balances[user];
    }

    /**
     * @notice Get the allowance of a user
     * @param owner The address of the owner
     * @param spender The address of the spender
     * @return The allowance of the user
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Approve a spender to spend tokens on behalf of the owner
     * @param spender The address of the spender
     * @param amount The amount of tokens to approve
     * @return A boolean indicating whether the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfer tokens from the owner to the recipient
     * @param from The address of the owner
     * @param to The address of the recipient
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        require(_allowances[from][msg.sender] >= amount, "Insufficient allowance");
        _allowances[from][msg.sender] = _allowances[from][msg.sender].sub(amount);
        _balances[from] = _balances[from].sub(amount);
        _balances[to] = _balances[to].add(amount);

        emit Transfer(from, to, amount);
        return true;
    }
}
```
