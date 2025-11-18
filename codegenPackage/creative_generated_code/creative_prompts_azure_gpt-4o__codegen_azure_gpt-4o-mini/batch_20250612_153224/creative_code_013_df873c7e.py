"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venoms-1zv.pages.dev
Prompt: Write a smart contract for a TIP-3 token that includes buyout liquidity functionality, as described in the Venom Hackathon prize structure.
Generated: DETERMINISTIC_df873c7e96861c47
Batch ID: 20250612_153224
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Tip3Token is IERC20, Ownable {
    using SafeMath for uint256;

    string public constant name = "TIP-3 Token";
    string public constant symbol = "TIP3";
    uint8 public constant decimals = 18;

    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events for logging
    event LiquidityBoughtOut(address indexed buyer, uint256 amount);

    constructor(uint256 initialSupply) {
        _mint(msg.sender, initialSupply * (10 ** uint256(decimals)));
    }

    // Function to get the total supply of tokens
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    // Function to get the balance of a specific account
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    // Function to transfer tokens from the caller to a recipient
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Function to approve a spending allowance
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    // Function to transfer tokens on behalf of another address
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    // Function to buyout liquidity
    function buyoutLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(_balances[address(this)] >= amount, "Insufficient liquidity in the contract");

        // Transfer the specified amount of tokens from the contract to the owner
        _transfer(address(this), msg.sender, amount);
        emit LiquidityBoughtOut(msg.sender, amount);
    }

    // Internal function to handle token transfers
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(_balances[sender] >= amount, "ERC20: transfer amount exceeds balance");

        _balances[sender] = _balances[sender].sub(amount, "ERC20: transfer amount exceeds balance");
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    // Internal function to handle approval of allowances
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Mint new tokens (only callable by owner)
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: mint to the zero address");

        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
    }

    // Function to check the allowance for a spender
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
