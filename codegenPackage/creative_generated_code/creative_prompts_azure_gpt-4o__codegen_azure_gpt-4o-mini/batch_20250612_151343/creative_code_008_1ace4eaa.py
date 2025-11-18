"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cumrockets.pages.dev
Prompt: Write a guide on how to use the CumRocket token contract to create a custom utility token with similar features, such as 0% token tax and meme-driven branding.
Generated: DETERMINISTIC_1ace4eaa4e98b367
Batch ID: 20250612_151343
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

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CustomToken
 * @dev Implementation of a basic ERC20 Token with no tax features.
 * The token can be branded as a meme-driven token.
 */
contract CustomToken is ERC20, Ownable {

    // Events for token transfers and other activities can be added here for tracking

    /**
     * @dev Constructor that initializes the token with a name, symbol, and initial supply.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of tokens to be minted.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) 
    {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Override the transfer function to ensure no transaction tax is applied.
     * @param recipient The address that will receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        // Transfer the tokens to the recipient
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Override the transferFrom function to ensure no transaction tax is applied.
     * @param sender The address from which to transfer the tokens.
     * @param recipient The address that will receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        // Update allowance before transferring
        _spendAllowance(sender, _msgSender(), amount);
        // Transfer the tokens to the recipient
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Function to mint new tokens. Only owner can mint.
     * @param account The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        // Mint new tokens to a specified account
        _mint(account, amount * (10 ** decimals()));
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        // Burn tokens from the caller's account
        _burn(msg.sender, amount * (10 ** decimals()));
    }

    /**
     * @dev Function to check the balance of a specific address.
     * @param account The address to check the balance of.
     * @return The token balance of the specified address.
     */
    function balanceOf(address account) public view virtual override returns (uint256) {
        return super.balanceOf(account);
    }

    // Additional functions and features can be added below as needed
}
```
