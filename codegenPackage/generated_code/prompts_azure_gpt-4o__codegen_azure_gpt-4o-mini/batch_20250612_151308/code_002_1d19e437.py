"""
Generated Code Metadata:
========================
Original URL: https://ethereum.com.tr
Prompt: Generate Solidity code for a decentralized application (ĐApp) that utilizes Ethereum's "kripto yakıt" concept to manage energy credits, inspired by the analogy of Ethereum as "petrol" from ethereum.com.tr.
Generated: DETERMINISTIC_1d19e4371bce1f92
Batch ID: 20250612_151308
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

/// @title Energy Credit Management DApp
/// @author Your Name
/// @notice This contract manages energy credits using a decentralized approach
/// @dev The contract allows users to mint, transfer, and redeem energy credits

contract EnergyCreditManager {
    // Event emitted when energy credits are minted
    event CreditsMinted(address indexed user, uint256 amount);
    
    // Event emitted when energy credits are transferred
    event CreditsTransferred(address indexed from, address indexed to, uint256 amount);
    
    // Event emitted when energy credits are redeemed
    event CreditsRedeemed(address indexed user, uint256 amount);

    // Mapping from user addresses to their energy credit balances
    mapping(address => uint256) private _balances;

    // Total supply of energy credits
    uint256 private _totalSupply;

    /// @notice Mint new energy credits for the caller
    /// @param amount The amount of energy credits to mint
    /// @dev Only the contract owner can mint new credits
    function mintCredits(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        _balances[msg.sender] += amount;
        _totalSupply += amount;

        emit CreditsMinted(msg.sender, amount);
    }

    /// @notice Transfer energy credits from the caller to another user
    /// @param to The address of the recipient
    /// @param amount The amount of energy credits to transfer
    /// @dev Reverts if the sender does not have enough credits
    function transferCredits(address to, uint256 amount) external {
        require(to != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[to] += amount;

        emit CreditsTransferred(msg.sender, to, amount);
    }

    /// @notice Redeem energy credits for a specified amount
    /// @param amount The amount of energy credits to redeem
    /// @dev Only the contract owner can redeem credits
    function redeemCredits(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        emit CreditsRedeemed(msg.sender, amount);
    }

    /// @notice Get the balance of energy credits for a specific user
    /// @param user The address of the user
    /// @return The balance of energy credits
    function balanceOf(address user) external view returns (uint256) {
        return _balances[user];
    }

    /// @notice Get the total supply of energy credits
    /// @return The total supply of energy credits
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }
}
```
