"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lingoclaims.pages.dev
Prompt: Create a smart contract in Solidity that implements a utility token similar to Lingo, ensuring compliance with non-security token standards.
Generated: DETERMINISTIC_b70c44c84b0f7bfa
Batch ID: 20250612_151232
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

// Importing OpenZeppelin's ERC20 implementation for security and best practices
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title UtilityToken
 * @dev A simple ERC20-compliant utility token similar to Lingo.
 * The token is designed for utility purposes and not as a security.
 */
contract UtilityToken is ERC20, Ownable {

    // Define a maximum supply for the token
    uint256 private constant MAX_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimal places

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * Initializes the contract's name and symbol.
     */
    constructor() ERC20("UtilityToken", "UTK") {
        _mint(msg.sender, MAX_SUPPLY); // Mint the total supply to the contract owner
    }

    /**
     * @dev Function to burn tokens, reducing the total supply.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) external {
        // Require that the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance to burn");
        _burn(msg.sender, amount); // Call the internal burn function
    }

    /**
     * @dev Function to transfer tokens, ensuring compliance with ERC20 standards.
     * Overrides the transfer function to include custom logic, if needed in the future.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to be sent.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        // Call the inherited transfer function from ERC20
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to approve tokens for delegated transfer.
     * Overrides the approve function to include custom logic, if needed in the future.
     * @param spender The address to spend the tokens.
     * @param amount The amount of tokens to be approved.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        // Call the inherited approve function from ERC20
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to transfer tokens on behalf of another address.
     * Overrides the transferFrom function to include custom logic, if needed in the future.
     * @param sender The address from which tokens are being transferred.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to be transferred.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        // Call the inherited transferFrom function from ERC20
        return super.transferFrom(sender, recipient, amount);
    }
}
```
