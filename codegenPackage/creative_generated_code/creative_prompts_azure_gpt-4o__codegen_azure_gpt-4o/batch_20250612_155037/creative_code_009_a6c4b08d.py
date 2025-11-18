"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trump47magameme.site
Prompt: Generate a Solidity code snippet for a token contract that includes metadata referencing "Make America Green Again" and Donald Trump.
Generated: DETERMINISTIC_a6c4b08db8c36e3a
Batch ID: 20250612_155037
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

/*
 * @title MAGA Token Contract
 * @dev ERC-20 Token with metadata referencing "Make America Green Again" and Donald Trump.
 * @author [Your Name]
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MAGAToken is ERC20, Ownable {
    // Metadata related to the token
    string public constant metadata = "Make America Green Again - Donald Trump";

    /*
     * @notice Constructor to initialize the MAGA token contract
     * @dev Sets the token name, symbol, and initial supply minted to the deployer address.
     * @param initialSupply The initial supply of tokens to mint, in smallest units (e.g., wei).
     */
    constructor(uint256 initialSupply) ERC20("MAGA Token", "MAGA") {
        _mint(msg.sender, initialSupply); // Mint the initial supply to the deployer (owner)
    }

    /*
     * @notice Function to mint new tokens (only callable by the contract owner)
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     * @dev Emits a Transfer event from the zero address upon successful minting.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /*
     * @notice Function to burn tokens (only callable by the contract owner)
     * @param from The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     * @dev Emits a Transfer event to the zero address upon successful burning.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
    }
}
```
