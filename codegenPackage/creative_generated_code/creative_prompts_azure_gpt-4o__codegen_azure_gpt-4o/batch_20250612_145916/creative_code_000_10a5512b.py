"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-screator-ethereum-free.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee, referencing the process described on the "Tokens Creator" webpage. Ensure the contract supports Ethereum network integration and wallet connection.
Generated: DETERMINISTIC_10a5512b6fc9b05f
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title LiquidityToken
 * @dev A smart contract for creating a token with liquidity and tax fee support.
 * This contract implements ERC20 standards and includes specific functionalities.
 */
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract LiquidityToken is IERC20 {
    string public name = "LiquidityToken";
    string public symbol = "LQT";
    uint256 public decimals = 18;
    uint256 public override totalSupply;

    address public owner;
    uint256 public taxFee; // Tax fee percentage.
    uint256 public liquidityFee; // Liquidity fee percentage.

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor(uint256 _initialSupply, uint256 _taxFee, uint256 _liquidityFee) {
        require(_taxFee <= 100, "Tax fee cannot exceed 100%");
        require(_liquidityFee <= 100, "Liquidity fee cannot exceed 100%");

        owner = msg.sender;
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        totalSupply = _initialSupply * (10 ** decimals);
        _balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 liquidityAmount = (amount * liquidityFee) / 100;
        uint256 transferAmount = amount - taxAmount - liquidityAmount;

        _balances[msg.sender] -= amount;
        _balances[recipient] += transferAmount;
        _balances[owner] += taxAmount + liquidityAmount; // Tax and liquidity fees go to the owner.

        emit Transfer(msg.sender, recipient, transferAmount);
        if (taxAmount > 0) {
            emit Transfer(msg.sender, owner, taxAmount);
        }
        if (liquidityAmount > 0) {
            emit Transfer(msg.sender, owner, liquidityAmount);
        }

        return true;
    }

    function allowance(address account, address spender) public view override returns (uint256) {
        return _allowances[account][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 liquidityAmount = (amount * liquidityFee) / 100;
        uint256 transferAmount = amount - taxAmount - liquidityAmount;

        _balances[sender] -= amount;
        _balances[recipient] += transferAmount;
        _balances[owner] += taxAmount + liquidityAmount; // Tax and liquidity fees go to the owner.

        _allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, transferAmount);
        if (taxAmount > 0) {
            emit Transfer(sender, owner, taxAmount);
        }
        if (liquidityAmount > 0) {
            emit Transfer(sender, owner, liquidityAmount);
        }

        return true;
    }

    function setTaxFee(uint256 _taxFee) public onlyOwner {
        require(_taxFee <= 100, "Tax fee cannot exceed 100%");
        taxFee = _taxFee;
    }

    function setLiquidityFee(uint256 _liquidityFee) public onlyOwner {
        require(_liquidityFee <= 100, "Liquidity fee cannot exceed 100%");
        liquidityFee = _liquidityFee;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
