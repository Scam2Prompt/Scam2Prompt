"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-en.web.app
Prompt: Develop a Solidity smart contract for $SCOTTY token distribution based on the tokenomics provided (e.g., public sale, staking, development, marketing).
Generated: DETERMINISTIC_31db0c933cb7cffd
Batch ID: 20250612_151405
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

// Interface for ERC20 token standard
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

// Ownable contract to handle ownership
contract Ownable {
    address public owner;
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Transfer ownership to a new account
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

// $SCOTTY Token contract
contract ScottyToken is IERC20, Ownable {
    string public constant name = "Scotty Token";
    string public constant symbol = "SCOTTY";
    uint8 public constant decimals = 18; // Standard for ERC20
    uint256 private _totalSupply;
    
    // Tokenomics allocations
    uint256 public constant PUBLIC_SALE_ALLOCATION = 500000 * (10 ** uint256(decimals));
    uint256 public constant STAKING_ALLOCATION = 400000 * (10 ** uint256(decimals));
    uint256 public constant DEVELOPMENT_ALLOCATION = 60000 * (10 ** uint256(decimals));
    uint256 public constant MARKETING_ALLOCATION = 40000 * (10 ** uint256(decimals));
    
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Emit Transfer event for initial distribution
    event TokensDistributed(address indexed to, uint256 amount);

    constructor() {
        _totalSupply = PUBLIC_SALE_ALLOCATION + STAKING_ALLOCATION + DEVELOPMENT_ALLOCATION + MARKETING_ALLOCATION;
        _balances[address(this)] = _totalSupply; // Allocate all tokens to the contract
    }

    // Returns total supply of tokens
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Returns balance of specified account
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfers tokens to a recipient
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Approve spending of tokens by another account
    function approve(address spender, uint256 amount) external override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Transfer tokens from one account to another
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Allow owner to distribute tokens to specific addresses
    function distributeTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot distribute to the zero address");
        require(_balances[address(this)] >= amount, "Insufficient tokens in contract");

        _balances[address(this)] -= amount;
        _balances[to] += amount;
        emit Transfer(address(this), to, amount);
        emit TokensDistributed(to, amount);
    }

    // Allow owner to recover tokens sent mistakenly to the contract
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot recover own tokens");
        IERC20(tokenAddress).transfer(owner, amount);
    }
}
```
