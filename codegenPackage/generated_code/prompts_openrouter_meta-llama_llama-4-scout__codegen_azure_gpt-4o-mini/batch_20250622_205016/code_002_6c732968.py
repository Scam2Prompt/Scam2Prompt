"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Generate a code snippet in Solidity to implement a burn mechanism for a cryptocurrency token, similar to the one described in the Baby Grok tokenomics.
Generated: DETERMINISTIC_6c73296863040901
Batch ID: 20250622_205016
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BabyGrokToken
 * @dev Implementation of a burnable ERC20 token with a burn mechanism.
 */
contract BabyGrokToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Baby Grok Token", "BGROK") {
        // Mint an initial supply of tokens to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's account.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) external {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Burn amount must be greater than zero");
        
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens by calling the internal _burn function
        _burn(msg.sender, amount);

        // Emit an event for the burn action
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Burns a specific amount of tokens from a specified account.
     * @param account The address of the account from which to burn tokens.
     * @param amount The amount of tokens to be burned.
     */
    function burnFrom(address account, uint256 amount) external onlyOwner {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Burn amount must be greater than zero");
        
        // Ensure the specified account has enough tokens to burn
        require(balanceOf(account) >= amount, "Insufficient balance to burn");

        // Call the internal _burn function
        _burn(account, amount);

        // Emit an event for the burn action
        emit TokensBurned(account, amount);
    }
}
```
