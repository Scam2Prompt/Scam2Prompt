"""
Generated Code Metadata:
========================
Original URL: https://bnbfour-meme.pages.dev
Prompt: Write a Solidity smart contract for a cryptocurrency token with a fixed supply of 4 billion tokens, 0% buy/sell tax, and a roadmap similar to the $FOUR token described on the webpage.
Generated: DETERMINISTIC_44becfe209db3079
Batch ID: 20250612_151207
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
 * @title FourToken
 * @author [Your Name]
 * @notice A cryptocurrency token with a fixed supply of 4 billion tokens and 0% buy/sell tax.
 */
contract FourToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Fixed supply of 4 billion tokens
    uint256 private constant _totalSupply = 4_000_000_000 * 10**18;

    // No buy/sell tax
    uint256 private constant _taxRate = 0;

    // Mapping of token holders to their balances
    mapping(address => uint256) private _balances;

    // Mapping of allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    /**
     * @notice Constructor
     */
    constructor() ERC20("Four Token", "FOUR") {
        // Mint the total supply to the contract creator
        _mint(msg.sender, _totalSupply);
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
     * @notice Transfers tokens from the sender to a recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        // Check if the sender has sufficient balance
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Transfer tokens
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        // Emit a transfer event
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @notice Approves a spender to spend a certain amount of tokens on behalf of the owner.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        // Approve the spender
        _allowances[msg.sender][spender] = amount;

        // Emit an approval event
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @notice Returns the allowance of a spender for a certain owner.
     * @param owner The address of the owner.
     * @param spender The address of the spender.
     * @return The allowance of the spender for the owner.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Transfers tokens from an owner to a recipient, allowed by a spender.
     * @param sender The address of the owner.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        // Check if the spender has sufficient allowance
        require(_allowances[sender][msg.sender] >= amount, "Insufficient allowance");

        // Transfer tokens
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        // Decrease the allowance
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);

        // Emit a transfer event
        emit Transfer(sender, recipient, amount);

        return true;
    }

    /**
     * @notice Burns tokens from the sender.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        // Check if the sender has sufficient balance
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Burn tokens
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        // Emit a transfer event
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
