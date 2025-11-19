"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowonbasenets.pages.dev
Prompt: How can I implement a liquidity burn feature in a smart contract for a cryptocurrency like $COW?
Generated: DETERMINISTIC_cbea65f6172d3b50
Batch ID: 20250612_163840
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title A simple ERC20 token with a liquidity burn feature
/// @notice This contract allows the token owner to burn a specified amount of tokens to decrease the total supply
contract CowToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("COW Token", "COW") {
        // Mint an initial supply of tokens to the owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1,000,000 tokens
    }

    /// @notice Burn a specified amount of tokens from the caller's balance
    /// @param amount The number of tokens to burn
    /// @dev Only the owner of the contract can invoke this function
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        
        emit TokensBurned(msg.sender, amount);
    }

    /// @notice Allow the owner to burn tokens from a specified address
    /// @param account The address from which to burn tokens
    /// @param amount The number of tokens to burn
    /// @dev Only the owner can call this function
    function burnFrom(address account, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(account) >= amount, "Insufficient balance in account");
        
        // Call the internal burn function
        _burn(account, amount);
        
        emit TokensBurned(account, amount);
    }
}
```
