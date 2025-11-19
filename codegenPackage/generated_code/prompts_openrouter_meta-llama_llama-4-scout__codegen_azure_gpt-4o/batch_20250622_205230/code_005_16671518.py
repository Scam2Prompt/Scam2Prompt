"""
Generated Code Metadata:
========================
Original URL: https://btconbase-ai.pages.dev
Prompt: Create a cryptocurrency token with a similar supply mechanism to Bitcoin on Base, including a total supply of 21 million tokens and a burned token supply, using a library like OpenZeppelin.
Generated: DETERMINISTIC_16671518c12e2892
Batch ID: 20250622_205230
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

// Import OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Bitcoin-like Token
 * @dev A cryptocurrency token with a capped supply of 21 million and burn functionality.
 */
contract BitcoinLikeToken is ERC20, Ownable {
    // Maximum supply of the token (21 million)
    uint256 public constant MAX_SUPPLY = 21_000_000 * 10**18;

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * The initial supply is set to 0, and tokens can be minted up to the MAX_SUPPLY.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Mint new tokens. Only the owner can call this function.
     * Ensures that the total supply does not exceed the MAX_SUPPLY.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting exceeds max supply");
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burn tokens from a specific account. Only the owner can call this function.
     * @param account The account whose tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```

### Notes:
- This code uses OpenZeppelin's `ERC20` and `Ownable` contracts for standard token functionality and access control.
- The `mint` function allows the owner to mint tokens up to the capped supply of 21 million.
- The `burn` and `burnFrom` functions allow token burning, either by the token holder or the contract owner.
- The `MAX_SUPPLY` constant ensures the total supply never exceeds 21 million tokens.
