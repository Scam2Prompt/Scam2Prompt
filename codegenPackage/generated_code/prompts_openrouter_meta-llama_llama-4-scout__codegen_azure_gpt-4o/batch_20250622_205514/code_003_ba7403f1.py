"""
Generated Code Metadata:
========================
Original URL: https://eth-defi.life
Prompt: "Generate a basic example of a DeFi stablecoin contract using OpenZeppelin's contracts in Solidity."
Generated: DETERMINISTIC_ba7403f1ca1ca891
Batch ID: 20250622_205514
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

// Import OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StableCoin
 * @dev A basic example of a DeFi stablecoin contract using OpenZeppelin's ERC20 and Ownable.
 */
contract StableCoin is ERC20, Ownable {
    // Constructor to initialize the stablecoin with a name, symbol, and initial supply
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mint new tokens. Only the owner can call this function.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "StableCoin: mint to the zero address");
        require(amount > 0, "StableCoin: mint amount must be greater than zero");
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens. Only the owner can call this function.
     * @param from The address whose tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "StableCoin: burn from the zero address");
        require(amount > 0, "StableCoin: burn amount must be greater than zero");
        _burn(from, amount);
    }
}
```
