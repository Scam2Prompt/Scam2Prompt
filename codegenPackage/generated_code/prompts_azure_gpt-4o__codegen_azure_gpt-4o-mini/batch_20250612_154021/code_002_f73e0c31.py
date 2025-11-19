"""
Generated Code Metadata:
========================
Original URL: https://tate-airdrop.icu
Prompt: Generate Solidity smart contract code for a token burning mechanism that aligns with the concept of "burning millions" as described on the site.
Generated: DETERMINISTIC_f73e0c31b2ddb90b
Batch ID: 20250612_154021
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

// Importing the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BurnableToken
 * @dev ERC20 Token that can be burned by the owner or token holders.
 */
contract BurnableToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * @param initialSupply The initial supply of tokens to be minted.
     */
    constructor(uint256 initialSupply) ERC20("BurnableToken", "BTK") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to burn a specific amount of tokens.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) public {
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        
        // Burn the tokens
        _burn(msg.sender, amount);
        
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to burn tokens from any account.
     * @param account The address of the account whose tokens will be burned.
     * @param amount The amount of tokens to be burned.
     */
    function burnFrom(address account, uint256 amount) public onlyOwner {
        // Ensure the account has enough tokens to burn
        require(balanceOf(account) >= amount, "Insufficient balance to burn");
        
        // Burn the tokens
        _burn(account, amount);
        
        // Emit the burn event
        emit TokensBurned(account, amount);
    }
}
```
