"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: Write a Solidity smart contract that interacts with TPWallet to enhance security in multi-chain asset management.
Generated: DETERMINISTIC_5be6f121a959ca8a
Batch ID: 20250612_151408
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

// Interface for interacting with the TPWallet
interface ITPWallet {
    function deposit(address token, uint256 amount) external;
    function withdraw(address token, uint256 amount) external;
    function getBalance(address token) external view returns (uint256);
}

contract MultiChainAssetManager {
    // State variable to store the address of the TPWallet
    ITPWallet public tpWallet;

    // Event to emit when funds are deposited
    event Deposited(address indexed token, uint256 amount);

    // Event to emit when funds are withdrawn
    event Withdrawn(address indexed token, uint256 amount);

    // Constructor to set the TPWallet address
    constructor(address _tpWallet) {
        require(_tpWallet != address(0), "TPWallet address cannot be zero");
        tpWallet = ITPWallet(_tpWallet);
    }

    // Function to deposit tokens into the TPWallet
    function depositTokens(address token, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the sender to this contract
        (bool success, ) = token.call(abi.encodeWithSignature("transferFrom(address,address,uint256)", msg.sender, address(this), amount));
        require(success, "Token transfer failed");

        // Approve TPWallet to spend the tokens
        (success, ) = token.call(abi.encodeWithSignature("approve(address,uint256)", address(tpWallet), amount));
        require(success, "Token approval failed");

        // Deposit tokens into TPWallet
        tpWallet.deposit(token, amount);

        emit Deposited(token, amount);
    }

    // Function to withdraw tokens from the TPWallet
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(tpWallet.getBalance(token) >= amount, "Insufficient balance in TPWallet");

        // Withdraw tokens from TPWallet
        tpWallet.withdraw(token, amount);

        // Transfer tokens from this contract back to the sender
        (bool success, ) = token.call(abi.encodeWithSignature("transfer(address,uint256)", msg.sender, amount));
        require(success, "Token transfer failed");

        emit Withdrawn(token, amount);
    }

    // Function to check the balance of a specific token in the TPWallet
    function getWalletBalance(address token) external view returns (uint256) {
        return tpWallet.getBalance(token);
    }
}
```
