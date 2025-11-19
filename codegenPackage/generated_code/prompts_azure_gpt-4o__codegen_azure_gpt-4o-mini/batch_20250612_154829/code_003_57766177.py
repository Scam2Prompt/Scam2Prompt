"""
Generated Code Metadata:
========================
Original URL: https://predelin.ru
Prompt: Write a Solidity smart contract to interact with Beethoven X's liquidity pools, enabling users to deposit and withdraw assets securely.
Generated: DETERMINISTIC_577661778558df45
Batch ID: 20250612_154829
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Beethoven X liquidity pool
interface IBeethovenXPool {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for interacting with Beethoven X liquidity pools
contract BeethovenXLiquidityManager is Ownable {
    // State variables
    IBeethovenXPool public pool; // Instance of the Beethoven X liquidity pool
    IERC20 public asset; // ERC20 token used for deposits and withdrawals

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the pool and asset
    constructor(IBeethovenXPool _pool, IERC20 _asset) {
        pool = _pool;
        asset = _asset;
    }

    // Function to deposit assets into the liquidity pool
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer the specified amount of tokens from the user to this contract
        require(asset.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the pool to spend the tokens
        require(asset.approve(address(pool), amount), "Approval failed");

        // Deposit the tokens into the liquidity pool
        pool.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw assets from the liquidity pool
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        
        // Check the user's balance in the pool
        uint256 poolBalance = pool.balanceOf(address(this));
        require(poolBalance >= amount, "Insufficient pool balance");

        // Withdraw the specified amount from the liquidity pool
        pool.withdraw(amount);

        // Transfer the withdrawn tokens back to the user
        require(asset.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to set a new liquidity pool (only owner)
    function setPool(IBeethovenXPool _pool) external onlyOwner {
        pool = _pool;
    }

    // Function to set a new asset (only owner)
    function setAsset(IERC20 _asset) external onlyOwner {
        asset = _asset;
    }
}
```
