"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-free-ethereum.pages.dev
Prompt: Create a Solidity contract template for generating tokens with customizable parameters like liquidity and tax fee, referencing the features mentioned on the "Token-Free Ethereum" webpage.
Generated: DETERMINISTIC_d1aaf7a3ac0e91ee
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
 * @title CustomToken
 * @dev ERC20 Token implementation with customizable liquidity fee and tax fee.
 */
contract CustomToken {
    // State variables
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Fees and liquidity settings
    uint256 public taxFee; // Fee percentage for tax (e.g., 2%)
    uint256 public liquidityFee; // Fee percentage for liquidity (e.g., 3%)
    address public liquidityWallet; // Address for receiving liquidity fees
    address public taxWallet; // Address for receiving tax fees

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _totalSupply,
        uint256 _taxFee,
        uint256 _liquidityFee,
        address _liquidityWallet,
        address _taxWallet
    ) {
        require(_taxFee + _liquidityFee <= 100, "Invalid fee percentages");

        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        liquidityWallet = _liquidityWallet;
        taxWallet = _taxWallet;

        // Mint the entire supply to the deployer
        balances[msg.sender] = totalSupply;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Public functions
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    // Internal functions
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");

        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 liquidityAmount = (amount * liquidityFee) / 100;
        uint256 transferAmount = amount - taxAmount - liquidityAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[taxWallet] += taxAmount;
        balances[liquidityWallet] += liquidityAmount;

        emit Transfer(sender, recipient, transferAmount);
        if (taxAmount > 0) {
            emit Transfer(sender, taxWallet, taxAmount);
        }
        if (liquidityAmount > 0) {
            emit Transfer(sender, liquidityWallet, liquidityAmount);
        }
    }
}
```
