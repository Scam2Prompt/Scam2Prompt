"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-io-presalestokenclaim.pages.dev
Prompt: Implement a token burn mechanism in Solidity that reduces the circulating supply of tokens, inspired by Galaxy Fox's deflationary process.
Generated: DETERMINISTIC_d2c24a69d5601286
Batch ID: 20250612_152235
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

/**
 * @title GalaxyFoxToken
 * @dev Implementation of a deflationary ERC20 token with a burn mechanism.
 */
contract GalaxyFoxToken is ERC20, Ownable {
    // Event to log token burns
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("GalaxyFoxToken", "GFT") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        // Ensure the burn amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Burns a specific amount of tokens from a specified address.
     * @param account The address from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) external {
        // Ensure the burn amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        // Ensure the specified account has enough tokens to burn
        require(balanceOf(account) >= amount, "Insufficient balance to burn");

        // Allowance check
        uint256 currentAllowance = allowance(account, msg.sender);
        require(currentAllowance >= amount, "Burn amount exceeds allowance");

        // Burn the specified amount of tokens
        _burn(account, amount);
        // Update the allowance
        _approve(account, msg.sender, currentAllowance - amount);
        // Emit the burn event
        emit TokensBurned(account, amount);
    }
}
```
