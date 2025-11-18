"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20presale-claim.pages.dev
Prompt: Write a Solidity contract that prevents inflation by enforcing a fixed supply of 140,000,000,000 DOGE20 tokens, as described in the tokenomics.
Generated: DETERMINISTIC_0bf9cdfcf141b572
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
 * @title DOGE20 Token Contract
 * @dev This contract implements a fixed supply ERC20 token with a total supply of 140 billion DOGE20 tokens.
 * It inherits from the OpenZeppelin ERC20 and Ownable contracts to ensure security and functionality.
 */
contract DOGE20 is ERC20, Ownable {
    // Define the total supply of the token
    uint256 private constant TOTAL_SUPPLY = 140_000_000_000 * (10 ** 18); // 140 billion tokens, considering 18 decimals

    // Constructor to mint the total supply to the deployer's address
    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Override the _mint function to prevent any additional minting of tokens
     * This ensures that the total supply remains fixed at 140 billion tokens
     */
    function _mint(address account, uint256 amount) internal virtual override {
        require(totalSupply() + amount <= TOTAL_SUPPLY, "Cannot mint beyond fixed supply");
        super._mint(account, amount);
    }

    /**
     * @dev Function to burn tokens, reducing the total supply
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens from a specified account
     * This can only be called by the owner of the contract
     * @param account The address of the account to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```
