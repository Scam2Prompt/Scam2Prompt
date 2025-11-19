"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Write a smart contract for a game token called WOOL, which is used for governance and utility in a virtual ecosystem with features like breeding and resource cultivation.
Generated: DETERMINISTIC_a0f03a93c653f355
Batch ID: 20250622_204740
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

/**
 * @title WOOL Token
 * @dev ERC20 token for governance and utility in a virtual ecosystem.
 * Features include minting, burning, and pausing.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract WoolToken is ERC20, Ownable, Pausable {
    // Maximum supply of WOOL tokens
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor to initialize the WOOL token.
     * Sets the token name and symbol.
     */
    constructor() ERC20("WOOL Token", "WOOL") {}

    /**
     * @dev Mint new tokens. Only the owner can call this function.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "WOOL: Exceeds maximum supply");
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens. Any token holder can burn their own tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Pause the contract. Only the owner can call this function.
     * Pausing disables all token transfers.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract. Only the owner can call this function.
     * Unpausing re-enables all token transfers.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to enforce pause functionality.
     * @param from The address transferring tokens.
     * @param to The address receiving tokens.
     * @param amount The amount of tokens being transferred.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
