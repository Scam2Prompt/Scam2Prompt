"""
Generated Code Metadata:
========================
Original URL: https://tokenscreator.pages.dev
Prompt: Generate code to deploy a token on the BNB Smart Chain using a full audited smart contract, referencing the features provided by Tokens Creator.
Generated: DETERMINISTIC_b285aa19a1a809ff
Batch ID: 20250612_145916
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BEP20 Token with minting, burning, pausable, and ownership features
 * @dev Fully compliant with BEP20 standard
 */
contract BNBSmartChainToken is ERC20, ERC20Burnable, ERC20Pausable, Ownable, ReentrancyGuard {
    uint8 private immutable _decimals;
    uint256 private immutable _maxSupply;

    /**
     * @dev Constructor that initializes the token
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param decimals_ Token decimals
     * @param initialSupply_ Initial token supply
     * @param maxSupply_ Maximum token supply (0 for unlimited)
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint8 decimals_,
        uint256 initialSupply_,
        uint256 maxSupply_
    ) ERC20(name_, symbol_) {
        require(initialSupply_ > 0, "Initial supply must be greater than 0");
        if (maxSupply_ > 0) {
            require(initialSupply_ <= maxSupply_, "Initial supply exceeds max supply");
        }

        _decimals = decimals_;
        _maxSupply = maxSupply_;

        _mint(msg.sender, initialSupply_);
    }

    /**
     * @dev Returns the number of decimals used
     */
    function decimals() public view override returns (uint8) {
        return _decimals;
    }

    /**
     * @dev Returns the maximum token supply
     */
    function maxSupply() public view returns (uint256) {
        return _maxSupply;
    }

    /**
     * @dev Mints new tokens, can only be called by owner
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner nonReentrant {
        require(to != address(0), "Mint to zero address");
        require(amount > 0, "Amount must be greater than 0");

        if (_maxSupply > 0) {
            require(totalSupply() + amount <= _maxSupply, "Exceeds max supply");
        }

        _mint(to, amount);
    }

    /**
     * @dev Pauses all token transfers, can only be called by owner
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers, can only be called by owner
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override(ERC20, ERC20Pausable) {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Transfers ownership of the contract, can only be called by owner
     */
    function transferOwnership(address newOwner) public override onlyOwner {
        require(newOwner != address(0), "New owner is zero address");
        super.transferOwnership(newOwner);
    }
}
```
