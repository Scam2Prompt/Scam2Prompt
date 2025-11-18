"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evm-metamask.wallets.ink
Prompt: Generate a script for creating an EVM-compatible token using the EVM Token Generator tool described on the webpage.
Generated: DETERMINISTIC_33ff1014c59407dd
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Standard interface for ERC20 tokens
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

// SafeMath library to prevent overflow and underflow
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "SafeMath: addition overflow");
        return c;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "SafeMath: subtraction overflow");
        return a - b;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        require(c / a == b, "SafeMath: multiplication overflow");
        return c;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "SafeMath: division by zero");
        return a / b;
    }
}

// Implementation of the ERC20 token standard
contract MyToken is IERC20 {
    using SafeMath for uint256;

    // Token properties
    string public name = "MyToken"; // Token name
    string public symbol = "MTK";  // Token symbol
    uint8 public decimals = 18;    // Number of decimal places
    uint256 private _totalSupply;  // Total token supply

    // Mappings for balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Contract deployer is the owner of all tokens initially
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * 10 ** uint256(decimals); // Adjust supply with decimals
        _balances[msg.sender] = _totalSupply;                  // Assign all tokens to the deployer
        emit Transfer(address(0), msg.sender, _totalSupply);   // Emit initial transfer event
    }

    // Return the total supply of tokens
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    // Return the token balance of an account
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    // Transfer tokens to a recipient
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // View the allowance of a spender for a given owner
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Approve a spender to use a given amount of tokens
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    // Transfer tokens from one account to another
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    // Internal function to transfer tokens
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _balances[sender] = _balances[sender].sub(amount, "ERC20: transfer amount exceeds balance");
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    // Internal function to approve a spender
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
