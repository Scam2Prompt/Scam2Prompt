"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-io.web.app
Prompt: Write a smart contract in Solidity for an Ethereum-based token named "$RBLZ" with 18 decimals, a total supply of 250,000,000, and no buy or sell tax. Ensure the contract includes basic ERC-20 functionality and is audit-ready.
Generated: DETERMINISTIC_66c64815914bd28e
Batch ID: 20250612_152620
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

// Importing the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RBLZToken
 * @dev Implementation of the ERC20 Token standard with 18 decimals and a total supply of 250 million.
 */
contract RBLZToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 250_000_000 * 10 ** 18; // 250 million tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("$RBLZ", "$RBLZ") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Allows the owner to mint new tokens.
     * @param account The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        // Ensure the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        // Mint the tokens to the specified account
        _mint(account, amount);
    }

    /**
     * @dev Allows the owner to burn tokens from a specific account.
     * @param account The address from which tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        // Ensure the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        // Burn the tokens from the specified account
        _burn(account, amount);
    }
}
```
