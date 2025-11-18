"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Write a smart contract in Solidity that implements a meme-based cryptocurrency token similar to "Rich Pepe," incorporating features like 0% buy/sell tax, locked liquidity, and community-based ownership.
Generated: DETERMINISTIC_13c89cfd267863a3
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title RichPepeToken
 * @dev A meme-based cryptocurrency token with 0% buy/sell tax, locked liquidity, and community-based ownership.
 */
contract RichPepeToken {
    // Token details
    string public name = "Rich Pepe";
    string public symbol = "RPEPE";
    uint8 public decimals = 18;
    uint256 public totalSupply = 10_000_000 * (10 ** uint256(decimals)); // 10 million tokens

    // Mapping for balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Liquidity lock
    address public liquidityLocker;
    bool public isLiquidityLocked = false;

    // Ownership details
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event LiquidityLocked(address indexed locker);

    // Modifier for ownership checks
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the contract owner");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the owner to the deployer
        liquidityLocker = address(0); // No liquidity locker set initially
        _balances[owner] = totalSupply; // Assign all tokens to the owner

        emit Transfer(address(0), owner, totalSupply); // Emit transfer event for initial minting
    }

    // Transfer function
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    // Transfer tokens on behalf of another account
    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(_balances[from] >= amount, "Insufficient balance");
        require(_allowances[from][msg.sender] >= amount, "Allowance exceeded");

        _balances[from] -= amount;
        _balances[to] += amount;
        _allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    // Approve another account to spend tokens on behalf of the caller
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        _allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Check the balance of an account
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    // Check the allowance of a spender for a specific owner account
    function allowance(address owner_, address spender) external view returns (uint256) {
        return _allowances[owner_][spender];
    }

    // Transfer ownership to a new account
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Lock liquidity by assigning the liquidityLocker
    function lockLiquidity(address locker) external onlyOwner {
        require(!isLiquidityLocked, "Liquidity is already locked");
        require(locker != address(0), "Locker address cannot be the zero address");

        liquidityLocker = locker;
        isLiquidityLocked = true;

        emit LiquidityLocked(locker);
    }
}
```
