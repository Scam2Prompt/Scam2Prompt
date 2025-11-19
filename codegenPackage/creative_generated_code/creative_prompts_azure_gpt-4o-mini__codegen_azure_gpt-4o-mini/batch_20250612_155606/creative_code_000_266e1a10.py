"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-rectify-presale-url.pages.dev
Prompt: Generate a smart contract in Solidity that implements a token similar to $EARNM, focusing on converting mobile activity into rewards.
Generated: DETERMINISTIC_266e1a10ee3755f6
Batch ID: 20250612_155606
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

// ERC20 Interface
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

// Context for managing the message sender
abstract contract Context {
    function _msgSender() internal view virtual returns (address) {
        return msg.sender;
    }

    function _msgData() internal view virtual returns (bytes calldata) {
        return msg.data;
    }
}

// Implementation of the ERC20 token with reward mechanics
contract EarnMobileToken is Context, IERC20 {
    string public constant name = "EarnMobileToken";
    string public constant symbol = "EARNM";
    uint8 public constant decimals = 18;
    uint256 private _totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize total supply
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero.");
        _totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[_msgSender()] = _totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), _msgSender(), _totalSupply);
    }

    // Total supply of tokens
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Balance of a specific account
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfer tokens from sender to recipient
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    // Allowance of tokens for a spender from an owner
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Approve a spender to spend a specific amount of tokens
    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(_msgSender(), spender, amount);
        return true;
    }

    // Transfer tokens from one account to another on behalf of the sender
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), _allowances[sender][_msgSender()] - amount);
        return true;
    }

    // Internal function to transfer tokens
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address is not allowed.");
        require(recipient != address(0), "Transfer to the zero address is not allowed.");
        require(_balances[sender] >= amount, "Insufficient balance for transfer.");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    // Internal function to approve a spender
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address is not allowed.");
        require(spender != address(0), "Approve to the zero address is not allowed.");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Function to claim rewards based on mobile activity
    // For demonstration purposes, we will use a simplified reward mechanism
    function claimRewards(uint256 rewardAmount) external {
        require(rewardAmount > 0, "Reward amount must be greater than zero.");
        require(_balances[address(this)] >= rewardAmount, "Not enough tokens in the contract for rewards.");

        _balances[address(this)] -= rewardAmount;
        _balances[_msgSender()] += rewardAmount;

        emit RewardsClaimed(_msgSender(), rewardAmount);
        emit Transfer(address(this), _msgSender(), rewardAmount);
    }

    // Function to deposit tokens into the contract for rewards
    function depositForRewards(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero.");
        _transfer(_msgSender(), address(this), amount);
    }
}
```
