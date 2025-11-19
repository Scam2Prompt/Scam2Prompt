"""
Generated Code Metadata:
========================
Original URL: https://grokcoin.pages.dev
Prompt: Develop a smart contract in Solidity for managing GROK token transactions, including features for burning tokens and tracking total supply.
Generated: DETERMINISTIC_3c8e3b2c5f94b663
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GROKToken
 * @dev Implementation of the GROK token with burning functionality and total supply tracking.
 */
contract GROKToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply) ERC20("GROK Token", "GROK") {
        // Mint the initial supply of tokens to the contract deployer
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) external {
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn tokens");
        
        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
        
        // Emit the TokensBurned event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Function to get the total supply of tokens.
     * @return The total supply of the GROK token.
     */
    function totalSupply() public view override returns (uint256) {
        return super.totalSupply();
    }
}
```
