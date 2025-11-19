"""
Generated Code Metadata:
========================
Original URL: https://spyro-vip.pages.dev
Prompt: Write a Solidity contract for an ERC-20 token with 0% taxes, similar to $SPYRO.
Generated: DETERMINISTIC_516d946c929c936e
Batch ID: 20250622_210008
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
 * @title SPYRO Token Contract
 * @author [Your Name]
 * @notice This contract implements an ERC-20 token with 0% taxes.
 */
contract SPYROToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token holder balances
    mapping(address => uint256) private _balances;

    // Mapping of token holder allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of tokens
    uint256 private _totalSupply;

    /**
     * @notice Constructor function to initialize the token contract.
     * @param initialSupply The initial supply of tokens.
     */
    constructor(uint256 initialSupply) ERC20("SPYRO", "SPYRO") {
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }

    /**
     * @notice Returns the total supply of tokens.
     * @return The total supply of tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of a token holder.
     * @param account The address of the token holder.
     * @return The balance of the token holder.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of the token holder.
     * @param sender The address of the token holder.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));
        return true;
    }

    /**
     * @notice Increases the allowance of a spender.
     * @param spender The address of the spender.
     * @param addedValue The amount to increase the allowance by.
     * @return A boolean indicating whether the allowance was successfully increased.
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].add(addedValue));
        return true;
    }

    /**
     * @notice Decreases the allowance of a spender.
     * @param spender The address of the spender.
     * @param subtractedValue The amount to decrease the allowance by.
     * @return A boolean indicating whether the allowance was successfully decreased.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].sub(subtractedValue));
        return true;
    }

    /**
     * @notice Approves a spender to spend a certain amount of tokens.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Burns tokens from the token holder.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burns tokens from a token holder on behalf of the token holder.
     * @param account The address of the token holder.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override {
        _burnFrom(account, amount);
    }

    /**
     * @dev Internal function to transfer tokens.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to approve a spender.
     * @param owner The address of the token holder.
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

    /**
     * @dev Internal function to burn tokens.
     * @param account The address of the token holder.
     * @param amount The amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(account, address(0), amount);
    }

    /**
     * @dev Internal function to burn tokens on behalf of a token holder.
     * @param account The address of the token holder.
     * @param amount The amount of tokens to burn.
     */
    function _burnFrom(address account, uint256 amount) internal {
        require(_allowances[account][msg.sender] >= amount, "ERC20: burn amount exceeds allowance");
        _allowances[account][msg.sender] = _allowances[account][msg.sender].sub(amount);
        _burn(account, amount);
    }
}
```
