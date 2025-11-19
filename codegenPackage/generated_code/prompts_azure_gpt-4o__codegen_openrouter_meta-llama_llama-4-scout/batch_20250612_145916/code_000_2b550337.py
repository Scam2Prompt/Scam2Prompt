"""
Generated Code Metadata:
========================
Original URL: https://tokenscreator4.pages.dev
Prompt: Write a Solidity smart contract for creating a custom token with liquidity and tax fee, compatible with BNB Smart Chain, Ethereum, and Polygon, as described on Tokens Creator.
Generated: DETERMINISTIC_2b5503374ef5591d
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
 * @title CustomToken
 * @author [Your Name]
 * @notice A custom ERC20 token with liquidity and tax fee, compatible with BNB Smart Chain, Ethereum, and Polygon.
 */
contract CustomToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tax fee settings
    uint256 public taxFee;
    uint256 public liquidityFee;
    uint256 public totalFee;

    // Liquidity pool settings
    address public liquidityPool;
    uint256 public liquidityPoolAmount;

    // Mapping of addresses to their respective balances and allowances
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowances;

    // Events
    event TaxFeeApplied(address indexed sender, uint256 amount);
    event LiquidityPoolUpdated(address indexed sender, uint256 amount);

    /**
     * @notice Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _totalSupply Token total supply
     * @param _taxFee Tax fee percentage
     * @param _liquidityFee Liquidity fee percentage
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupply,
        uint256 _taxFee,
        uint256 _liquidityFee
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _totalSupply);

        // Initialize tax fee and liquidity fee
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        totalFee = taxFee.add(liquidityFee);

        // Initialize liquidity pool
        liquidityPool = msg.sender;
        liquidityPoolAmount = 0;
    }

    /**
     * @notice Transfer function with tax fee and liquidity pool update
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success status
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(totalFee).div(100);
        uint256 sendAmount = amount.sub(fee);

        // Apply tax fee
        if (taxFee > 0) {
            emit TaxFeeApplied(msg.sender, fee);
        }

        // Update liquidity pool
        if (liquidityFee > 0) {
            liquidityPoolAmount = liquidityPoolAmount.add(fee.mul(liquidityFee).div(totalFee));
            emit LiquidityPoolUpdated(msg.sender, liquidityPoolAmount);
        }

        // Transfer tokens
        _transfer(msg.sender, to, sendAmount);

        return true;
    }

    /**
     * @notice Transfer function with tax fee and liquidity pool update (ERC20 compatibility)
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant {
        uint256 fee = amount.mul(totalFee).div(100);
        uint256 sendAmount = amount.sub(fee);

        // Apply tax fee
        if (taxFee > 0) {
            emit TaxFeeApplied(from, fee);
        }

        // Update liquidity pool
        if (liquidityFee > 0) {
            liquidityPoolAmount = liquidityPoolAmount.add(fee.mul(liquidityFee).div(totalFee));
            emit LiquidityPoolUpdated(from, liquidityPoolAmount);
        }

        // Transfer tokens
        _transfer(from, to, sendAmount);

        // Update allowance
        _approve(from, msg.sender, allowances[from][msg.sender].sub(amount));
    }

    /**
     * @notice Approve function
     * @param spender Spender address
     * @param amount Amount to approve
     * @return bool Success status
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Increase allowance
     * @param spender Spender address
     * @param addedValue Value to add
     * @return bool Success status
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _approve(msg.sender, spender, allowances[msg.sender][spender].add(addedValue));
        return true;
    }

    /**
     * @notice Decrease allowance
     * @param spender Spender address
     * @param subtractedValue Value to subtract
     * @return bool Success status
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _approve(msg.sender, spender, allowances[msg.sender][spender].sub(subtractedValue));
        return true;
    }

    /**
     * @notice Internal transfer function
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        balances[from] = balances[from].sub(amount);
        balances[to] = balances[to].add(amount);
        emit Transfer(from, to, amount);
    }

    /**
     * @notice Internal approval function
     * @param owner Owner address
     * @param spender Spender address
     * @param amount Amount to approve
     */
    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
