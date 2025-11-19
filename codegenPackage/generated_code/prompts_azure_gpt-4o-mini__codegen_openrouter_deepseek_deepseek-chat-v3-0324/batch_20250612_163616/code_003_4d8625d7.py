"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Develop a Solidity contract that implements the tokenomics for $BCB, including features for burning tokens and managing circulating supply.
Generated: DETERMINISTIC_4d8625d79442a01a
Batch ID: 20250612_163616
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

/**
 * @title BCB Token Contract
 * @dev Implements tokenomics for $BCB including burning and supply management
 */
contract BCBToken is ERC20, Ownable {
    uint256 private _totalBurned;
    uint256 private _maxSupply;

    /**
     * @dev Emitted when tokens are burned
     */
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor that initializes the token
     * @param initialSupply Initial token supply
     * @param maxSupply Maximum token supply (can be 0 for unlimited)
     */
    constructor(uint256 initialSupply, uint256 maxSupply) ERC20("BCB Token", "BCB") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        if (maxSupply > 0) {
            require(initialSupply <= maxSupply, "Initial supply exceeds max supply");
        }

        _maxSupply = maxSupply;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Returns the maximum token supply
     */
    function maxSupply() public view returns (uint256) {
        return _maxSupply;
    }

    /**
     * @dev Returns the total burned tokens
     */
    function totalBurned() public view returns (uint256) {
        return _totalBurned;
    }

    /**
     * @dev Returns the circulating supply (total supply - burned)
     */
    function circulatingSupply() public view returns (uint256) {
        return totalSupply() - _totalBurned;
    }

    /**
     * @dev Burns tokens from caller's balance
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
        _totalBurned += amount;
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Mints new tokens (owner only)
     * @param to Address to receive the tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        if (_maxSupply > 0) {
            require(totalSupply() + amount <= _maxSupply, "Minting would exceed max supply");
        }
        _mint(to, amount);
    }

    /**
     * @dev Overrides the transfer function to include additional checks
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        require(to != address(0) || from == address(0), "Transfers to zero address not allowed except for minting");
    }
}
```
