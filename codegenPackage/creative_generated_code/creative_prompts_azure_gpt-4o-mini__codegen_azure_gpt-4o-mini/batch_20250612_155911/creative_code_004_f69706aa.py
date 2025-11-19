"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ether-creator-free.pages.dev
Prompt: What is the significance of 100% token ownership when creating a currency on the Ether Creator site, and how does it affect the smart contract?
Generated: DETERMINISTIC_f69706aa4e7a6899
Batch ID: 20250612_155911
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

/// @title ERC20 Token with 100% Ownership
/// @notice This contract implements a simple ERC20 token with the owner holding 100% of the initial supply.
/// @dev The token follows the ERC20 standard and includes basic functionality such as transfer and approval.

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OwnershipToken is ERC20, Ownable {
    // Event emitted when tokens are transferred
    event TokensTransferred(address indexed from, address indexed to, uint256 value);

    /// @notice Constructor to create the token with the specified name, symbol, and initial supply
    /// @param name The name of the token
    /// @param symbol The symbol of the token
    /// @param initialSupply The initial supply of tokens that will be minted to the owner's address
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) 
    {
        // Mint the entire initial supply to the owner
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    /// @notice Transfer tokens from the caller's account to a specified address
    /// @param to The address to which tokens are transferred
    /// @param amount The amount of tokens to transfer
    /// @return success A boolean indicating if the transfer was successful
    function transfer(address to, uint256 amount) public override returns (bool success) {
        // Call the parent transfer function
        success = super.transfer(to, amount);
        // Emit the transfer event
        if (success) {
            emit TokensTransferred(msg.sender, to, amount);
        }
    }

    /// @notice Transfer tokens on behalf of the caller to a specified address
    /// @param from The address to transfer tokens from
    /// @param to The address to which tokens are transferred
    /// @param amount The amount of tokens to transfer
    /// @return success A boolean indicating if the transfer was successful
    function transferFrom(address from, address to, uint256 amount) public override returns (bool success) {
        // Call the parent transferFrom function
        success = super.transferFrom(from, to, amount);
        // Emit the transfer event
        if (success) {
            emit TokensTransferred(from, to, amount);
        }
    }

    /// @notice Safely increase the allowance for a spender
    /// @param spender The address that will spend the tokens
    /// @param addedValue The additional amount to be added to the allowance
    /// @return success A boolean indicating if the operation was successful
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool success) {
        success = super.increaseAllowance(spender, addedValue);
    }

    /// @notice Safely decrease the allowance for a spender
    /// @param spender The address that will spend the tokens
    /// @param subtractedValue The amount to be subtracted from the allowance
    /// @return success A boolean indicating if the operation was successful
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool success) {
        success = super.decreaseAllowance(spender, subtractedValue);
    }
}
```
