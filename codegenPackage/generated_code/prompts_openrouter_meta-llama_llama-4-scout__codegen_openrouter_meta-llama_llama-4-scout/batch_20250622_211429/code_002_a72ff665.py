"""
Generated Code Metadata:
========================
Original URL: https://drop-catcoincom.pages.dev
Prompt: Generate a simple smart contract in Solidity for a token with zero taxes and locked liquidity, similar to $CAT.
Generated: DETERMINISTIC_a72ff665e6b0a08c
Batch ID: 20250622_211429
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
 * @title CatToken
 * @author [Your Name]
 * @notice A simple ERC20 token with zero taxes and locked liquidity.
 */
contract CatToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Liquidity lock status
    bool private _liquidityLocked;

    // Tax rate (set to 0 for zero taxes)
    uint256 private _taxRate;

    // Address of the liquidity pool
    address private _liquidityPool;

    /**
     * @notice Constructor for the CatToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param totalSupply The total supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _totalSupply = totalSupply;
        _balances[msg.sender] = totalSupply;

        // Initialize tax rate to 0
        _taxRate = 0;

        // Initialize liquidity lock status to true
        _liquidityLocked = true;

        // Emit event for initial supply
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @notice Returns the total supply of the token.
     * @return The total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of the specified address.
     * @param account The address to query.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from the sender's account to the recipient's account.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        // Check if liquidity is locked
        require(!_liquidityLocked || msg.sender == _liquidityPool, "Liquidity is locked");

        // Perform transfer
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        // Emit event for transfer
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @notice Transfers tokens from the sender's account to the recipient's account on behalf of the sender.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        // Check if liquidity is locked
        require(!_liquidityLocked || msg.sender == _liquidityPool, "Liquidity is locked");

        // Check allowance
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Perform transfer
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);

        // Emit event for transfer
        emit Transfer(sender, recipient, amount);

        return true;
    }

    /**
     * @notice Approves the specified address to transfer tokens on behalf of the sender.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;

        // Emit event for approval
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @notice Increases the allowance of the specified spender.
     * @param spender The address of the spender.
     * @param addedValue The amount to add to the allowance.
     * @return A boolean indicating whether the increase was successful.
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        _allowances[msg.sender][spender] = currentAllowance.add(addedValue);

        // Emit event for approval
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);

        return true;
    }

    /**
     * @notice Decreases the allowance of the specified spender.
     * @param spender The address of the spender.
     * @param subtractedValue The amount to subtract from the allowance.
     * @return A boolean indicating whether the decrease was successful.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "Allowance cannot be decreased below zero");
        _allowances[msg.sender][spender] = currentAllowance.sub(subtractedValue);

        // Emit event for approval
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);

        return true;
    }

    /**
     * @notice Burns tokens from the sender's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        // Perform burn
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        // Emit event for burn
        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @notice Locks the liquidity pool.
     */
    function lockLiquidity() public {
        require(msg.sender == _liquidityPool, "Only liquidity pool can lock liquidity");
        _liquidityLocked = true;
    }

    /**
     * @notice Unlocks the liquidity pool.
     */
    function unlockLiquidity() public {
        require(msg.sender == _liquidityPool, "Only liquidity pool can unlock liquidity");
        _liquidityLocked = false;
    }
}
```
