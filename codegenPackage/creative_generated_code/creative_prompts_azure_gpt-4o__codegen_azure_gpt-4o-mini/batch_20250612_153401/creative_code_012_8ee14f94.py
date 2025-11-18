"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shardeumorgio.pages.dev
Prompt: Develop a smart contract for a token on Shardeum's blockchain, adhering to its fixed supply tokenomics model.
Generated: DETERMINISTIC_8ee14f942ab9c7f2
Batch ID: 20250612_153401
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
 * @title MyToken
 * @dev This contract implements a fixed supply ERC20 token on the Shardeum blockchain.
 */
contract MyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     */
    constructor() ERC20("MyToken", "MTK") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens. Only the owner can call this function.
     * @param account The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     * Requirements:
     * - Cannot mint tokens as the supply is fixed.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= TOTAL_SUPPLY, "Minting exceeds total supply");
        _mint(account, amount);
    }

    /**
     * @dev Function to burn tokens. Only the owner can call this function.
     * @param amount The amount of tokens to burn.
     * Requirements:
     * - The sender must have enough tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        _burn(msg.sender, amount);
    }

    /**
     * @dev Override the _beforeTokenTransfer function to implement checks for fixed supply.
     * Prevents transferring tokens if it would exceed total supply.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Additional checks can be implemented here if needed
    }
}
```
