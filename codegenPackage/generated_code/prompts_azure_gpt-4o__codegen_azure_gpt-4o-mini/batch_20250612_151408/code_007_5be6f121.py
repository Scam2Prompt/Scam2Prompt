"""
Generated Code Metadata:
========================
Original URL: https://snso.com.cn
Prompt: Write a Solidity smart contract that interacts with TPWallet to enhance security in multi-chain asset management.
Generated: DETERMINISTIC_5be6f121a959ca8a
Batch ID: 20250612_151408
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

// Importing the interface for TPWallet
interface ITPWallet {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function getBalance(address token) external view returns (uint256);
}

contract MultiChainAssetManager {
    // Address of the TPWallet contract
    ITPWallet public tpWallet;

    // Event emitted when assets are deposited
    event AssetsDeposited(address indexed token, uint256 amount);

    // Event emitted when assets are withdrawn
    event AssetsWithdrawn(address indexed token, uint256 amount);

    // Constructor to set the TPWallet address
    constructor(address _tpWallet) {
        require(_tpWallet != address(0), "Invalid TPWallet address");
        tpWallet = ITPWallet(_tpWallet);
    }

    // Function to deposit assets into TPWallet
    function depositAssets(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the tokens from the user to this contract
        // Assuming the token follows ERC20 standard
        bool success = IERC20(token).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Approve TPWallet to spend the tokens
        IERC20(token).approve(address(tpWallet), amount);

        // Deposit the tokens into TPWallet
        tpWallet.deposit(token, amount);

        emit AssetsDeposited(token, amount);
    }

    // Function to withdraw assets from TPWallet
    function withdrawAssets(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Withdraw the tokens from TPWallet
        tpWallet.withdraw(token, amount);

        // Transfer the tokens from this contract to the user
        bool success = IERC20(token).transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit AssetsWithdrawn(token, amount);
    }

    // Function to check the balance of a specific token in TPWallet
    function checkBalance(address token) external view returns (uint256) {
        return tpWallet.getBalance(token);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
