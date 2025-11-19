"""
Generated Code Metadata:
========================
Original URL: https://shlbatoken.info
Prompt: Generate a smart contract for creating and managing a token like SHLBA Token.
Generated: DETERMINISTIC_46bdac18fb1d49a2
Batch ID: 20250622_205436
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SHLBAToken
 * @dev Implementation of the SHLBA Token with ERC20 standard, burnable, pausable,
 * and ownable features.
 */
contract SHLBAToken is ERC20, ERC20Burnable, ERC20Pausable, Ownable, ReentrancyGuard {
    uint256 private constant INITIAL_SUPPLY = 1000000000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Emitted when tokens are minted.
     */
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Emitted when tokens are burned.
     */
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token with initial supply.
     */
    constructor() ERC20("SHLBA Token", "SHLBA") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Mints new tokens to the specified address.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner nonReentrant {
        require(to != address(0), "SHLBA: mint to the zero address");
        require(amount > 0, "SHLBA: amount must be greater than zero");
        
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burns tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        require(amount > 0, "SHLBA: amount must be greater than zero");
        super.burn(amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Pauses all token transfers.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override(ERC20, ERC20Pausable) {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Transfers ownership of the contract to a new account.
     * @param newOwner The address to transfer ownership to.
     */
    function transferOwnership(address newOwner) public override onlyOwner {
        require(newOwner != address(0), "SHLBA: new owner is the zero address");
        super.transferOwnership(newOwner);
    }
}
```
