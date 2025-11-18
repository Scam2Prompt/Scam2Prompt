"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Write a smart contract to deploy a memecoin on Linea, ensuring compatibility with its zkEVM and leveraging its low gas fees.
Generated: DETERMINISTIC_10e70546dbeba456
Batch ID: 20250612_152240
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Memecoin
 * @dev A simple ERC20 token implementation for a memecoin on Linea
 */
contract Memecoin is ERC20, Ownable {
    
    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Memecoin", "MEME") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    /**
     * @dev Allows the owner to mint new tokens.
     * @param to The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        
        _mint(to, amount);
    }

    /**
     * @dev Allows the owner to burn tokens from a specified address.
     * @param from The address from which tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Amount must be greater than zero");
        
        _burn(from, amount);
    }
}
```
