"""
Generated Code Metadata:
========================
Original URL: https://erc20-creator.pages.dev
Prompt: Write a Solidity smart contract code for creating an ERC20 token with liquidity and tax fee on Ethereum network.
Generated: DETERMINISTIC_471d2db53855ab05
Batch ID: 20250622_211557
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
 * @title TaxedERC20Token
 * @author [Your Name]
 * @notice ERC20 token with liquidity and tax fee
 */
contract TaxedERC20Token is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Tax fee percentage
    uint256 public taxFee;

    // Liquidity fee percentage
    uint256 public liquidityFee;

    // Address of the liquidity pool
    address public liquidityPool;

    // Address of the tax wallet
    address public taxWallet;

    /**
     * @notice Constructor
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param totalSupply_ Total supply of the token
     * @param taxFee_ Tax fee percentage
     * @param liquidityFee_ Liquidity fee percentage
     * @param liquidityPool_ Address of the liquidity pool
     * @param taxWallet_ Address of the tax wallet
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        uint256 taxFee_,
        uint256 liquidityFee_,
        address liquidityPool_,
        address taxWallet_
    ) ERC20(name_, symbol_) {
        _totalSupply = totalSupply_;
        _balances[msg.sender] = totalSupply_;

        taxFee = taxFee_;
        liquidityFee = liquidityFee_;
        liquidityPool = liquidityPool_;
        taxWallet = taxWallet_;
    }

    /**
     * @notice Returns the total supply of the token
     * @return Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of an address
     * @param account Address to check
     * @return Balance of the address
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param recipient Address to transfer to
     * @param amount Amount to transfer
     * @return Success
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = calculateFee(amount);
        uint256 sendAmount = amount.sub(fee);
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);

        if (fee > 0) {
            _balances[taxWallet] = _balances[taxWallet].add(fee.mul(taxFee).div(100));
            _balances[liquidityPool] = _balances[liquidityPool].add(fee.mul(liquidityFee).div(100));
        }

        emit Transfer(msg.sender, recipient, sendAmount);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param sender Address to transfer from
     * @param recipient Address to transfer to
     * @param amount Amount to transfer
     * @return Success
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 fee = calculateFee(amount);
        uint256 sendAmount = amount.sub(fee);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);

        if (fee > 0) {
            _balances[taxWallet] = _balances[taxWallet].add(fee.mul(taxFee).div(100));
            _balances[liquidityPool] = _balances[liquidityPool].add(fee.mul(liquidityFee).div(100));
        }

        emit Transfer(sender, recipient, sendAmount);
        return true;
    }

    /**
     * @notice Calculates the fee for a given amount
     * @param amount Amount to calculate fee for
     * @return Fee
     */
    function calculateFee(uint256 amount) private view returns (uint256) {
        return amount.mul(taxFee.add(liquidityFee)).div(100);
    }

    /**
     * @notice Increases the allowance of a spender
     * @param spender Address of the spender
     * @param addedValue Amount to add
     * @return New allowance
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].add(addedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases the allowance of a spender
     * @param spender Address of the spender
     * @param subtractedValue Amount to subtract
     * @return New allowance
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].sub(subtractedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Approves a spender
     * @param spender Address of the spender
     * @param amount Amount to approve
     * @return Success
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Allows the owner to update the tax fee
     * @param newTaxFee New tax fee
     */
    function updateTaxFee(uint256 newTaxFee) public onlyOwner {
        taxFee = newTaxFee;
    }

    /**
     * @notice Allows the owner to update the liquidity fee
     * @param newLiquidityFee New liquidity fee
     */
    function updateLiquidityFee(uint256 newLiquidityFee) public onlyOwner {
        liquidityFee = newLiquidityFee;
    }

    /**
     * @notice Allows the owner to update the liquidity pool
     * @param newLiquidityPool New liquidity pool
     */
    function updateLiquidityPool(address newLiquidityPool) public onlyOwner {
        liquidityPool = newLiquidityPool;
    }

    /**
     * @notice Allows the owner to update the tax wallet
     * @param newTaxWallet New tax wallet
     */
    function updateTaxWallet(address newTaxWallet) public onlyOwner {
        taxWallet = newTaxWallet;
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
