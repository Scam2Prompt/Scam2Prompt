"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Write a smart contract in Solidity for the $MASA token, ensuring compatibility with ERC-20 standards and incorporating token supply limits as described in Project DEKSA's whitepaper.
Generated: DETERMINISTIC_dbaa0f75d01c2b02
Batch ID: 20250612_145625
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MASAToken
 * @dev Implements an ERC20 token with a fixed supply
 */
contract MASAToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Maximum supply of tokens
    uint256 private constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all initial tokens.
     */
    constructor() ERC20("Masa Token", "$MASA") {
        _mint(msg.sender, MAX_SUPPLY); // Mint maximum supply to the deployer
    }

    /**
     * @dev Override the _mint function to prevent minting beyond MAX_SUPPLY
     * @param account The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal virtual override {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "MASA: Minting exceeds max supply");
        super._mint(account, amount);
    }

    /**
     * @dev Allows the owner to burn tokens from their account
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw any accidentally sent ERC20 tokens
     * @param tokenAddress The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "MASA: Cannot withdraw MASA tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
