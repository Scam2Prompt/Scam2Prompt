"""
Generated Code Metadata:
========================
Original URL: https://bonkai-buy.pages.dev
Prompt: Develop a Solidity smart contract for the BONKAI token ($BONKAI) on the Solana blockchain, ensuring compliance with the distribution model outlined in the tokenomics section.
Generated: DETERMINISTIC_77768a06c1388bf1
Batch ID: 20250612_150601
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/AccessControl.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/AccessControl.sol";

contract BonkaiToken {
    // Mapping of token distribution
    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;

    // Token information
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Distribution model
    address public teamWallet;
    address public advisorsWallet;
    address public communityWallet;
    address public liquidityWallet;

    // Percentages for distribution
    uint256 public teamPercentage;
    uint256 public advisorsPercentage;
    uint256 public communityPercentage;
    uint256 public liquidityPercentage;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Access control
    mapping (address => bool) public isExcluded;

    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _totalSupply,
        address _teamWallet,
        address _advisorsWallet,
        address _communityWallet,
        address _liquidityWallet,
        uint256 _teamPercentage,
        uint256 _advisorsPercentage,
        uint256 _communityPercentage,
        uint256 _liquidityPercentage
    ) public {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;

        teamWallet = _teamWallet;
        advisorsWallet = _advisorsWallet;
        communityWallet = _communityWallet;
        liquidityWallet = _liquidityWallet;

        teamPercentage = _teamPercentage;
        advisorsPercentage = _advisorsPercentage;
        communityPercentage = _communityPercentage;
        liquidityPercentage = _liquidityPercentage;

        // Mint initial tokens
        _balances[teamWallet] = totalSupply * teamPercentage / 100;
        _balances[advisorsWallet] = totalSupply * advisorsPercentage / 100;
        _balances[communityWallet] = totalSupply * communityPercentage / 100;
        _balances[liquidityWallet] = totalSupply * liquidityPercentage / 100;

        emit Transfer(address(0), teamWallet, _balances[teamWallet]);
        emit Transfer(address(0), advisorsWallet, _balances[advisorsWallet]);
        emit Transfer(address(0), communityWallet, _balances[communityWallet]);
        emit Transfer(address(0), liquidityWallet, _balances[liquidityWallet]);
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] - subtractedValue);
        return true;
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }
}
```
