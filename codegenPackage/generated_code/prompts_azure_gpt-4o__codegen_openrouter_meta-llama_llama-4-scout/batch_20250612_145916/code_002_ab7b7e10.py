"""
Generated Code Metadata:
========================
Original URL: https://token-screator-ethereum666.pages.dev
Prompt: Provide a Solidity implementation for a fully audited token contract that includes features like liquidity pool transfer and tax fee configuration, as described on a platform offering token creation in under a minute.
Generated: DETERMINISTIC_ab7b7e1005568ff0
Batch ID: 20250612_145916
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
 * @title AuditedToken
 * @author [Your Name]
 * @notice A fully audited token contract with features like liquidity pool transfer and tax fee configuration.
 */
contract AuditedToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Tax fee configuration
    uint256 public taxFee;
    address public taxWallet;

    // Liquidity pool configuration
    address public liquidityPool;
    uint256 public liquidityFee;

    // Events
    event TaxFeeUpdated(uint256 newTaxFee);
    event TaxWalletUpdated(address newTaxWallet);
    event LiquidityPoolUpdated(address newLiquidityPool);
    event LiquidityFeeUpdated(uint256 newLiquidityFee);

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total supply of the token
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _totalSupply = totalSupply;
        _balances[msg.sender] = totalSupply;

        // Initialize tax fee configuration
        taxFee = 200; // 2%
        taxWallet = msg.sender;

        // Initialize liquidity pool configuration
        liquidityPool = msg.sender;
        liquidityFee = 100; // 1%
    }

    /**
     * @notice Returns the total supply of the token
     * @return uint256 Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of an address
     * @param account Address
     * @return uint256 Balance
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param recipient Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = amount.mul(taxFee).div(10000);
        uint256 liquidity = amount.mul(liquidityFee).div(10000);
        uint256 netAmount = amount.sub(tax).sub(liquidity);

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(netAmount);
        _balances[taxWallet] = _balances[taxWallet].add(tax);
        _balances[liquidityPool] = _balances[liquidityPool].add(liquidity);

        emit Transfer(msg.sender, recipient, netAmount);
        emit Transfer(msg.sender, taxWallet, tax);
        emit Transfer(msg.sender, liquidityPool, liquidity);

        return true;
    }

    /**
     * @notice Approves an address to transfer tokens on behalf of another address
     * @param spender Spender address
     * @param amount Amount to approve
     * @return bool Success
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of another address
     * @param sender Sender address
     * @param recipient Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 tax = amount.mul(taxFee).div(10000);
        uint256 liquidity = amount.mul(liquidityFee).div(10000);
        uint256 netAmount = amount.sub(tax).sub(liquidity);

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(netAmount);
        _balances[taxWallet] = _balances[taxWallet].add(tax);
        _balances[liquidityPool] = _balances[liquidityPool].add(liquidity);

        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);

        emit Transfer(sender, recipient, netAmount);
        emit Transfer(sender, taxWallet, tax);
        emit Transfer(sender, liquidityPool, liquidity);

        return true;
    }

    /**
     * @notice Updates the tax fee
     * @param newTaxFee New tax fee
     */
    function updateTaxFee(uint256 newTaxFee) public onlyOwner {
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    /**
     * @notice Updates the tax wallet
     * @param newTaxWallet New tax wallet
     */
    function updateTaxWallet(address newTaxWallet) public onlyOwner {
        taxWallet = newTaxWallet;
        emit TaxWalletUpdated(newTaxWallet);
    }

    /**
     * @notice Updates the liquidity pool
     * @param newLiquidityPool New liquidity pool
     */
    function updateLiquidityPool(address newLiquidityPool) public onlyOwner {
        liquidityPool = newLiquidityPool;
        emit LiquidityPoolUpdated(newLiquidityPool);
    }

    /**
     * @notice Updates the liquidity fee
     * @param newLiquidityFee New liquidity fee
     */
    function updateLiquidityFee(uint256 newLiquidityFee) public onlyOwner {
        liquidityFee = newLiquidityFee;
        emit LiquidityFeeUpdated(newLiquidityFee);
    }

    // OpenZeppelin's ERC20Burnable implementation
    function burn(uint256 amount) public override {
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(msg.sender, address(0), amount);
    }

    // OpenZeppelin's ERC20Burnable implementation
    function burnFrom(address account, uint256 amount) public override {
        _balances[account] = _balances[account].sub(amount);
        _allowances[account][msg.sender] = _allowances[account][msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(account, address(0), amount);
    }
}
```
