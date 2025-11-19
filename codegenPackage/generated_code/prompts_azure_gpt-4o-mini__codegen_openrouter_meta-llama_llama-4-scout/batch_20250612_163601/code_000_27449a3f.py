"""
Generated Code Metadata:
========================
Original URL: https://uspepe-vip.pages.dev
Prompt: Generate a smart contract for a cryptocurrency token similar to USPEPE, including features like 0% taxes and liquidity pool burning.
Generated: DETERMINISTIC_27449a3f1101ad49
Batch ID: 20250612_163601
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

contract USPEPE is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Name and symbol of the token
    string private _name;
    string private _symbol;

    // Tax rate (0% in this case)
    uint256 private _taxRate;

    // Liquidity pool address
    address private _liquidityPool;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed sender, uint256 amount);

    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed sender, uint256 amount);

    /**
     * @dev Constructor function
     * @param name Name of the token
     * @param symbol Symbol of the token
     * @param totalSupply Total supply of the token
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _name = name;
        _symbol = symbol;
        _totalSupply = totalSupply;
        _taxRate = 0; // 0% tax rate
        _balances[msg.sender] = totalSupply; // Mint all tokens to the contract creator
    }

    /**
     * @dev Returns the name of the token
     * @return string Name of the token
     */
    function name() public view returns (string memory) {
        return _name;
    }

    /**
     * @dev Returns the symbol of the token
     * @return string Symbol of the token
     */
    function symbol() public view returns (string memory) {
        return _symbol;
    }

    /**
     * @dev Returns the total supply of the token
     * @return uint256 Total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of an address
     * @param account Address to query
     * @return uint256 Balance of the address
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from one address to another
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves an address to spend tokens on behalf of another address
     * @param spender Address to approve
     * @param amount Amount of tokens to approve
     * @return bool Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another on behalf of another address
     * @param sender Address to transfer tokens from
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool Whether the transfer was successful
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));
        return true;
    }

    /**
     * @dev Increases the allowance of an address to spend tokens on behalf of another address
     * @param spender Address to increase allowance for
     * @param addedValue Amount of tokens to add to allowance
     * @return bool Whether the increase was successful
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].add(addedValue));
        return true;
    }

    /**
     * @dev Decreases the allowance of an address to spend tokens on behalf of another address
     * @param spender Address to decrease allowance for
     * @param subtractedValue Amount of tokens to subtract from allowance
     * @return bool Whether the decrease was successful
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        _approve(
            msg.sender,
            spender,
            _allowances[msg.sender][spender].sub(subtractedValue, "ERC20: decreased allowance below zero")
        );
        return true;
    }

    /**
     * @dev Burns tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burns tokens on behalf of another address
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public override {
        _burnFrom(account, amount);
    }

    /**
     * @dev Adds liquidity to the liquidity pool
     * @param amount Amount of tokens to add to liquidity pool
     */
    function addLiquidity(uint256 amount) public {
        require(amount > 0, "USPEPE: amount must be greater than zero");
        _transfer(msg.sender, address(this), amount);
        emit LiquidityAdded(msg.sender, amount);
    }

    /**
     * @dev Removes liquidity from the liquidity pool
     * @param amount Amount of tokens to remove from liquidity pool
     */
    function removeLiquidity(uint256 amount) public {
        require(amount > 0, "USPEPE: amount must be greater than zero");
        require(_balances[address(this)] >= amount, "USPEPE: not enough liquidity");
        _transfer(address(this), msg.sender, amount);
        emit LiquidityRemoved(msg.sender, amount);
    }

    /**
     * @dev Internal function to transfer tokens
     * @param sender Address to transfer tokens from
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "USPEPE: sender must not be zero");
        require(recipient != address(0), "USPEPE: recipient must not be zero");

        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "USPEPE: not enough balance");

        _balances[sender] = senderBalance.sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to approve an address to spend tokens on behalf of another address
     * @param owner Address to approve
     * @param spender Address to spend tokens on behalf of
     * @param amount Amount of tokens to approve
     */
    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        require(owner != address(0), "USPEPE: owner must not be zero");
        require(spender != address(0), "USPEPE: spender must not be zero");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Internal function to burn tokens
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "USPEPE: account must not be zero");
        require(_balances[account] >= amount, "USPEPE: not enough balance");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(account, address(0), amount);
    }

    /**
     * @dev Internal function to burn tokens on behalf of another address
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function _burnFrom(address account, uint256 amount) internal {
        _burn(account, amount);
        _approve(
            account,
            msg.sender,
            _allowances[account][msg.sender].sub(amount, "USPEPE: burn amount exceeds allowance")
        );
    }
}
```
