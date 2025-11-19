"""
Generated Code Metadata:
========================
Original URL: https://berryeth.vip
Prompt: Write a function in Solidity to create a smart contract for a new cryptocurrency token, inspired by the $BERRY token's features, such as 0% tax and 100% community-driven.
Generated: DETERMINISTIC_62342ae5e642abb5
Batch ID: 20250622_212712
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
 * @title BERRYToken
 * @author [Your Name]
 * @notice Inspired by $BERRY token, this contract creates a new cryptocurrency token with 0% tax and 100% community-driven.
 */
contract BERRYToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token holders to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of token allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of tokens
    uint256 private _totalSupply;

    // Token details
    string private _name;
    string private _symbol;
    uint8 private _decimals;

    /**
     * @notice Constructor for BERRYToken
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param totalSupply_ Total supply of tokens
     * @param decimals_ Token decimals
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_, uint8 decimals_) ERC20(name_, symbol_) {
        _name = name_;
        _symbol = symbol_;
        _decimals = decimals_;
        _totalSupply = totalSupply_;

        // Mint total supply to the contract creator
        _mint(msg.sender, totalSupply_);
    }

    /**
     * @notice Returns the name of the token
     * @return string Token name
     */
    function name() public view override returns (string memory) {
        return _name;
    }

    /**
     * @notice Returns the symbol of the token
     * @return string Token symbol
     */
    function symbol() public view override returns (string memory) {
        return _symbol;
    }

    /**
     * @notice Returns the decimals of the token
     * @return uint8 Token decimals
     */
    function decimals() public view override returns (uint8) {
        return _decimals;
    }

    /**
     * @notice Returns the total supply of tokens
     * @return uint256 Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Mints new tokens to the specified address
     * @param account Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address account, uint256 amount) public {
        require(msg.sender == owner(), "Only the owner can mint tokens");
        _mint(account, amount);
    }

    /**
     * @notice Burns tokens from the specified address
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool Success status
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 currentAllowance = _allowances[from][msg.sender];
        if (currentAllowance != 0) {
            _allowances[from][msg.sender] = currentAllowance.sub(amount);
        }

        return transferFrom(from, to, amount);
    }

    /**
     * @notice Approves an address to spend tokens on behalf of another address
     * @param spender Address to approve
     * @param amount Amount of tokens to approve
     * @return bool Success status
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Increases the allowance of an address to spend tokens on behalf of another address
     * @param spender Address to increase allowance for
     * @param addedValue Amount of tokens to add to allowance
     * @return bool Success status
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        _allowances[msg.sender][spender] = currentAllowance.add(addedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases the allowance of an address to spend tokens on behalf of another address
     * @param spender Address to decrease allowance for
     * @param subtractedValue Amount of tokens to subtract from allowance
     * @return bool Success status
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        _allowances[msg.sender][spender] = currentAllowance.sub(subtractedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Transfers tokens from the contract owner to another address
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function transfer(address to, uint256 amount) public override {
        require(msg.sender == owner(), "Only the owner can transfer tokens");
        _transfer(msg.sender, to, amount);
    }

    /**
     * @notice Internal function to handle token transfers
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        _balances[from] = _balances[from].sub(amount);
        _balances[to] = _balances[to].add(amount);

        emit Transfer(from, to, amount);
    }

    /**
     * @notice Internal function to handle token minting
     * @param account Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: mint to the zero address");

        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);

        emit Transfer(address(0), account, amount);
    }

    /**
     * @notice Internal function to handle token burning
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal override {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(account, address(0), amount);
    }
}
```
