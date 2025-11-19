"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gen-da6.pages.dev
Prompt: How can I implement a smart contract for the $ENTS token on Ethereum?
Generated: DETERMINISTIC_292b2da976136ffe
Batch ID: 20250612_163400
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

/**
 * @title ENTS Token Smart Contract
 * @dev Implements a standard ERC20 token for the $ENTS cryptocurrency.
 */
 
// Import OpenZeppelin's ERC20 implementation for safer token development.
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ENTS is ERC20, Ownable {
    // Define the initial supply of tokens (e.g., 1 million tokens)
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * (10 ** 18); // Adjust decimals as per requirements
    
    /**
     * @dev Constructor that initializes the token with the given name and symbol.
     * It also mints the initial supply to the contract's owner.
     */
    constructor() ERC20("ENTS Token", "$ENTS") {
        // Mint initial supply to the contract's owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Mint new tokens. Restricted to the contract owner.
     * @param to Address to receive the minted tokens.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens from the sender's account.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burn tokens from a specified account. Restricted to the contract owner.
     * @param account Address of the account to burn tokens from.
     * @param amount Amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```

### Notes:
- This implementation uses OpenZeppelin's libraries (`ERC20` and `Ownable`) for best practices.
- The `mint` and `burnFrom` functions are restricted to the contract owner for better control.
- Make sure to install OpenZeppelin contracts in your project via npm (`npm install @openzeppelin/contracts`).
