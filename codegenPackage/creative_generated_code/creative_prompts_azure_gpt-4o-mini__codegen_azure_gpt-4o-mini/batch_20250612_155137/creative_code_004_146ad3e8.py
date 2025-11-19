"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://docs-beefmeme.pages.dev
Prompt: Create a Solidity contract that implements a token burning mechanism for BEEF Coin, similar to the deflationary model described on the website.
Generated: DETERMINISTIC_146ad3e8d740510d
Batch ID: 20250612_155137
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
 * @title BEEF Coin Token
 * @dev ERC20 Token with a burn mechanism for deflationary model
 */
contract BeefCoin is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Maximum supply of the token
    uint256 public immutable maxSupply;

    // Constructor to initialize the token with a name, symbol, and maximum supply
    constructor(uint256 _maxSupply) ERC20("BEEF Coin", "BEEF") {
        require(_maxSupply > 0, "Max supply should be greater than zero");
        maxSupply = _maxSupply;
        _mint(msg.sender, _maxSupply); // Mint entire supply to the owner
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);

        // Emit event for the burn action
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to enforce the maximum supply rules.
     * @param from The address tokens are being transferred from.
     * @param to The address tokens are being transferred to.
     * @param amount The amount of tokens being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);

        // Check if transfer exceeds total supply after burning
        require(totalSupply() + amount <= maxSupply, "Exceeds maximum supply after burn");
    }
}
```
