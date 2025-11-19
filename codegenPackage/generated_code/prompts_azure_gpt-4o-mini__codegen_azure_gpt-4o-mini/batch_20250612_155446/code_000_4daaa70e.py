"""
Generated Code Metadata:
========================
Original URL: https://panther-ai.pages.dev
Prompt: Generate a smart contract for the PantherAI token using BEP20 standards, ensuring it includes features for staking and liquidity management.
Generated: DETERMINISTIC_4daaa70eb87f350d
Batch ID: 20250612_155446
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

// Importing the BEP20 interface and SafeMath library
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PantherAI Token contract implementing BEP20 standards
contract PantherAIToken is IERC20, IERC20Metadata, Ownable {
    using SafeMath for uint256;

    // Token details
    string private _name = "PantherAI Token";
    string private _symbol = "PAI";
    uint8 private _decimals = 18;

    // Total supply and balances mapping
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Staking and liquidity management
    mapping(address => uint256) private _stakedBalances;
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the token supply
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * (10 ** uint256(_decimals));
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // BEP20 standard functions
    function name() external view override returns (string memory) {
        return _name;
    }

    function symbol() external view override returns (string memory) {
        return _symbol;
    }

    function decimals() external view override returns (uint8) {
        return _decimals;
    }

    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Staking function
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance to stake");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _stakedBalances[msg.sender] = _stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        emit Staked(msg.sender, amount);
    }

    // Unstaking function
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        _stakedBalances[msg.sender] = _stakedBalances[msg.sender].sub(amount);
        _balances[msg.sender] = _balances[msg.sender].add(amount);
        totalStaked = totalStaked.sub(amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to check staked balance
    function stakedBalanceOf(address account) external view returns (uint256) {
        return _stakedBalances[account];
    }
}
```
