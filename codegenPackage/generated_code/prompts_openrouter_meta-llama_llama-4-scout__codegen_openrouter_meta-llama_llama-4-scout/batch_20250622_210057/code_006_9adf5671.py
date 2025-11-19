"""
Generated Code Metadata:
========================
Original URL: https://journey-cyberkong.pages.dev
Prompt: Write a Solidity function to implement the $BANANA token, a key component of the CyberKongz ecosystem, and describe its potential use cases.
Generated: DETERMINISTIC_9adf56712cc9feea
Batch ID: 20250622_210057
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
 * @title $BANANA Token Contract
 * @author [Your Name]
 * @notice Implementation of the $BANANA token for the CyberKongz ecosystem.
 */
contract BananaToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of $BANANA tokens
    uint256 private _totalSupply;

    // Event emitted when tokens are minted
    event Mint(address indexed to, uint256 amount);

    // Event emitted when tokens are burned
    event Burn(address indexed from, uint256 amount);

    /**
     * @dev Initializes the $BANANA token contract.
     * @param initialSupply The initial supply of $BANANA tokens.
     */
    constructor(uint256 initialSupply) ERC20("BananaToken", "BANANA") {
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
        emit Mint(msg.sender, initialSupply);
    }

    /**
     * @dev Returns the total supply of $BANANA tokens.
     * @return The total supply of $BANANA tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param account The address to query.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from the caller's address to the specified address.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address from, address to, uint256 amount) internal {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        uint256 fromBalance = _balances[from];
        require(fromBalance >= amount, "ERC20: transfer amount exceeds balance");

        unchecked {
            _balances[from] = fromBalance - amount;
        }

        _balances[to] += amount;

        emit Transfer(from, to, amount);
    }

    /**
     * @dev Increases the allowance of the specified spender.
     * @param spender The address to increase the allowance for.
     * @param addedValue The amount to increase the allowance by.
     * @return A boolean indicating whether the allowance was successfully increased.
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
        return true;
    }

    /**
     * @dev Decreases the allowance of the specified spender.
     * @param spender The address to decrease the allowance for.
     * @param subtractedValue The amount to decrease the allowance by.
     * @return A boolean indicating whether the allowance was successfully decreased.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        unchecked {
            _approve(msg.sender, spender, currentAllowance - subtractedValue);
        }
        return true;
    }

    /**
     * @dev Approves the specified spender to spend the specified amount of tokens.
     * @param owner The address to approve the spender for.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Mints additional $BANANA tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(uint256 amount) external {
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        emit Mint(msg.sender, amount);
    }

    /**
     * @dev Burns $BANANA tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        uint256 accountBalance = _balances[msg.sender];
        require(accountBalance >= amount, "ERC20: burn amount exceeds balance");
        unchecked {
            _balances[msg.sender] = accountBalance - amount;
        }
        _totalSupply -= amount;
        emit Burn(msg.sender, amount);
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
