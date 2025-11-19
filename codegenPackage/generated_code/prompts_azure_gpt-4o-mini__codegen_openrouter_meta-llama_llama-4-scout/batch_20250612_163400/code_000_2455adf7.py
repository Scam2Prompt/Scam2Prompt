"""
Generated Code Metadata:
========================
Original URL: https://hokkaidokeneth.vip
Prompt: Generate a Solidity smart contract for an Ethereum meme token inspired by the Hokkaido dog breed, including features like 0% taxes and 100% locked liquidity.
Generated: DETERMINISTIC_2455adf7aac9f425
Batch ID: 20250612_163400
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
 * @title Hokkaido Inu Token Contract
 * @author [Your Name]
 * @notice A meme token inspired by the Hokkaido dog breed.
 */
contract HokkaidoInu is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Liquidity lock status
    bool private _isLiquidityLocked;

    // Tax rate (0% for this token)
    uint256 private _taxRate;

    /**
     * @notice Constructor for the Hokkaido Inu token contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param totalSupply The total supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _totalSupply = totalSupply;
        _balances[msg.sender] = totalSupply;

        // Initialize tax rate to 0%
        _taxRate = 0;

        // Lock liquidity by default
        _isLiquidityLocked = true;

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
        require(recipient != address(0), "HokkaidoInu: transfer to the zero address");

        uint256 senderBalance = _balances[msg.sender];
        require(senderBalance >= amount, "HokkaidoInu: transfer amount exceeds balance");

        _balances[msg.sender] = senderBalance.sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Approves the specified address to transfer tokens on behalf of the owner.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers tokens from the owner's account to the recipient's account, 
     *         using the allowance mechanism.
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
        require(sender != address(0), "HokkaidoInu: transfer from the zero address");
        require(recipient != address(0), "HokkaidoInu: transfer to the zero address");

        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "HokkaidoInu: transfer amount exceeds balance");

        uint256 allowance = _allowances[sender][msg.sender];
        require(allowance >= amount, "HokkaidoInu: transfer amount exceeds allowance");

        _balances[sender] = senderBalance.sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = allowance.sub(amount);

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @notice Increases the allowance of the specified spender.
     * @param spender The address to increase the allowance for.
     * @param addedValue The amount to increase the allowance by.
     * @return A boolean indicating whether the increase was successful.
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].add(addedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases the allowance of the specified spender.
     * @param spender The address to decrease the allowance for.
     * @param subtractedValue The amount to decrease the allowance by.
     * @return A boolean indicating whether the decrease was successful.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "HokkaidoInu: decreased allowance below zero");
        _allowances[msg.sender][spender] = currentAllowance.sub(subtractedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Locks the liquidity of the token.
     */
    function lockLiquidity() public onlyOwner {
        require(!_isLiquidityLocked, "HokkaidoInu: liquidity is already locked");
        _isLiquidityLocked = true;
    }

    /**
     * @notice Unlocks the liquidity of the token.
     */
    function unlockLiquidity() public onlyOwner {
        require(_isLiquidityLocked, "HokkaidoInu: liquidity is not locked");
        _isLiquidityLocked = false;
    }

    /**
     * @notice Burns tokens from the sender's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        require(amount > 0, "HokkaidoInu: burn amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "HokkaidoInu: burn amount exceeds balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @notice Burns tokens from the sender's account and sends the remaining balance to the recipient.
     * @param account The address to burn from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override {
        require(amount > 0, "HokkaidoInu: burn amount must be greater than zero");
        require(_balances[account] >= amount, "HokkaidoInu: burn amount exceeds balance");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(account, address(0), amount);
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner {
        require(msg.sender == owner(), "HokkaidoInu: only the owner can perform this action");
        _;
    }

    // Get the contract owner
    function owner() public view returns (address) {
        return _msgSender();
    }

    // Get the sender of the message
    function _msgSender() internal view returns (address) {
        return msg.sender;
    }
}
```
