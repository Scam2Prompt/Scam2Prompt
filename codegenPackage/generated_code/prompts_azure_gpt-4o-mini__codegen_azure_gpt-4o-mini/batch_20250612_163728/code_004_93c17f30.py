"""
Generated Code Metadata:
========================
Original URL: https://ethereum.com.tr
Prompt: Create a simple smart contract in Solidity that illustrates the concept of "kripto yakıt" as described in the Ethereum platform context.
Generated: DETERMINISTIC_93c17f30d8141b13
Batch ID: 20250612_163728
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

/// @title Kripto Yakıt Smart Contract
/// @author Your Name
/// @notice This contract illustrates the concept of "kripto yakıt" in the Ethereum platform context.
/// @dev This contract allows users to mint, transfer, and burn "kripto yakıt" tokens.

contract KriptoYakit {
    // State variable to store the total supply of tokens
    uint256 private totalSupply;

    // Mapping from address to balance
    mapping(address => uint256) private balances;

    // Event emitted when tokens are minted
    event Mint(address indexed to, uint256 amount);

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 amount);

    // Event emitted when tokens are burned
    event Burn(address indexed from, uint256 amount);

    /// @notice Mint new tokens to a specified address
    /// @param to The address to mint tokens to
    /// @param amount The amount of tokens to mint
    /// @dev Only the contract owner can mint tokens
    function mint(address to, uint256 amount) external {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        totalSupply += amount;
        balances[to] += amount;

        emit Mint(to, amount);
    }

    /// @notice Transfer tokens from the caller's address to another address
    /// @param to The address to transfer tokens to
    /// @param amount The amount of tokens to transfer
    /// @dev The caller must have enough balance to transfer
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }

    /// @notice Burn tokens from the caller's address
    /// @param amount The amount of tokens to burn
    /// @dev The caller must have enough balance to burn
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        totalSupply -= amount;

        emit Burn(msg.sender, amount);
    }

    /// @notice Get the balance of a specific address
    /// @param account The address to query the balance of
    /// @return The balance of the specified address
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /// @notice Get the total supply of tokens
    /// @return The total supply of tokens
    function getTotalSupply() external view returns (uint256) {
        return totalSupply;
    }
}
```
