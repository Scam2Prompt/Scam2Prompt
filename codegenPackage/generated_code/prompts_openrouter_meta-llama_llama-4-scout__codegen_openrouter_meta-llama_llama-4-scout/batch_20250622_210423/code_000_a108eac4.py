"""
Generated Code Metadata:
========================
Original URL: https://voters4pepe.pages.dev
Prompt: Write a Solidity smart contract for a token named President Pepe, similar to meme coins, with a supply mechanism.
Generated: DETERMINISTIC_a108eac46df11331
Batch ID: 20250622_210423
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title President Pepe Token
 * @author [Your Name]
 * @notice A meme token with a supply mechanism.
 */
contract PresidentPepeToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their minting limits
    mapping(address => uint256) public mintLimits;

    // Mapping of addresses to their minted amounts
    mapping(address => uint256) public mintedAmounts;

    // Maximum supply of the token
    uint256 public maxSupply;

    // Minting limit per address
    uint256 public defaultMintLimit;

    /**
     * @notice Constructor for the President Pepe Token contract.
     * @param maxSupply_ The maximum supply of the token.
     * @param defaultMintLimit_ The default minting limit per address.
     */
    constructor(uint256 maxSupply_, uint256 defaultMintLimit_) ERC20("President Pepe", "PRPE") {
        maxSupply = maxSupply_;
        defaultMintLimit = defaultMintLimit_;
    }

    /**
     * @notice Sets the minting limit for an address.
     * @param account The address to set the limit for.
     * @param limit The new minting limit.
     */
    function setMintLimit(address account, uint256 limit) public onlyOwner {
        mintLimits[account] = limit;
    }

    /**
     * @notice Mints tokens to an address.
     * @param account The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) public onlyOwner nonReentrant {
        // Check if the total supply exceeds the maximum supply
        require(totalSupply() + amount <= maxSupply, "Total supply exceeds maximum supply");

        // Get the minting limit for the owner
        uint256 ownerMintLimit = mintLimits[msg.sender];
        // If no limit is set, use the default limit
        if (ownerMintLimit == 0) {
            ownerMintLimit = defaultMintLimit;
        }

        // Check if the owner has exceeded their minting limit
        require(mintedAmounts[msg.sender] + amount <= ownerMintLimit, "Owner has exceeded minting limit");

        // Update the minted amount for the owner
        mintedAmounts[msg.sender] += amount;

        // Mint the tokens
        _mint(account, amount);
    }

    /**
     * @notice Burns tokens from an address.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        // Check if the account has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn the tokens
        _burn(msg.sender, amount);
    }
}
```
