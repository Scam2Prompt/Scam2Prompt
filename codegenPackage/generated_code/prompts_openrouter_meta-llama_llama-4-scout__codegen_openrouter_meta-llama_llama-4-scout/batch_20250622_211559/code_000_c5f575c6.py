"""
Generated Code Metadata:
========================
Original URL: https://ethereum-creator.pages.dev
Prompt: Write a Solidity smart contract code for creating a token with liquidity and tax fee on Ethereum network.
Generated: DETERMINISTIC_c5f575c638fececa
Batch ID: 20250622_211559
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
 * @title TokenWithLiquidityAndTaxFee
 * @author [Your Name]
 * @notice A token with liquidity and tax fee on Ethereum network
 */
contract TokenWithLiquidityAndTaxFee is ERC20, ERC20Burnable, ReentrancyGuard {
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
        _balances[msg.sender] = _totalSupply;

        taxFee = taxFee_;
        liquidityFee = liquidityFee_;
        liquidityPool = liquidityPool_;
        taxWallet = taxWallet_;
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
     * @param account Address to check balance
     * @return uint256 Balance
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param recipient Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = calculateFee(amount);
        uint256 sendAmount = amount.sub(fee);
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);
        if (fee > 0) {
            _balances[taxWallet] = _balances[taxWallet].add(fee);
        }
        emit Transfer(msg.sender, recipient, sendAmount);
        if (fee > 0) {
            emit Transfer(msg.sender, taxWallet, fee);
        }
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param sender Address to transfer from
     * @param recipient Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 fee = calculateFee(amount);
        uint256 sendAmount = amount.sub(fee);
        _balances[sender] = _balances[sender].sub(amount);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);
        if (fee > 0) {
            _balances[taxWallet] = _balances[taxWallet].add(fee);
        }
        emit Transfer(sender, recipient, sendAmount);
        if (fee > 0) {
            emit Transfer(sender, taxWallet, fee);
        }
        return true;
    }

    /**
     * @notice Calculates the fee for a given amount
     * @param amount Amount to calculate fee for
     * @return uint256 Fee
     */
    function calculateFee(uint256 amount) private view returns (uint256) {
        uint256 tax = amount.mul(taxFee).div(100);
        uint256 liquidity = amount.mul(liquidityFee).div(100);
        return tax.add(liquidity);
    }

    /**
     * @notice Adds liquidity to the pool
     * @param amount Amount to add
     */
    function addLiquidity(uint256 amount) public nonReentrant {
        require(msg.sender == liquidityPool, "Only liquidity pool can add liquidity");
        _balances[liquidityPool] = _balances[liquidityPool].add(amount);
        emit Transfer(msg.sender, liquidityPool, amount);
    }

    /**
     * @notice Removes liquidity from the pool
     * @param amount Amount to remove
     */
    function removeLiquidity(uint256 amount) public nonReentrant {
        require(msg.sender == liquidityPool, "Only liquidity pool can remove liquidity");
        _balances[liquidityPool] = _balances[liquidityPool].sub(amount);
        emit Transfer(liquidityPool, msg.sender, amount);
    }

    /**
     * @notice Increases the allowance of an address
     * @param spender Address to increase allowance for
     * @param addedValue Amount to increase allowance by
     * @return bool Success
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].add(addedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases the allowance of an address
     * @param spender Address to decrease allowance for
     * @param subtractedValue Amount to decrease allowance by
     * @return bool Success
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].sub(subtractedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Approves an address to spend tokens on behalf of the owner
     * @param spender Address to approve
     * @param amount Amount to approve
     * @return bool Success
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Allows an address to spend tokens on behalf of another address
     * @param owner Address of the token owner
     * @param spender Address to spend tokens
     * @return uint256 Allowance
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
