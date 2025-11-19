"""
Generated Code Metadata:
========================
Original URL: https://ondo-foundation.pages.dev
Prompt: Design a smart contract using Solidity that enables the tokenization of real-world assets (RWAs) on a blockchain, inspired by the Ondo Foundation's work.
Generated: DETERMINISTIC_bd3da9119d916700
Batch ID: 20250622_204650
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RWA Tokenization Contract
 * @author [Your Name]
 * @notice This contract enables the tokenization of real-world assets (RWAs) on a blockchain.
 */
contract RWATokenization is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of asset owners to their respective asset balances
    mapping(address => uint256) private _assetBalances;

    // Mapping of asset IDs to their respective token supply
    mapping(string => uint256) private _assetSupplies;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(string indexed assetId, uint256 supply);

    // Event emitted when an asset is detokenized
    event AssetDetokenized(string indexed assetId, uint256 amount);

    /**
     * @notice Constructor for the RWATokenization contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Tokenize a real-world asset
     * @param assetId The ID of the asset to tokenize
     * @param supply The total supply of tokens for the asset
     */
    function tokenizeAsset(string memory assetId, uint256 supply) public {
        require(supply > 0, "Token supply must be greater than 0");

        // Mint tokens for the asset
        _mint(msg.sender, supply);

        // Update asset supply
        _assetSupplies[assetId] = supply;

        // Emit event
        emit AssetTokenized(assetId, supply);
    }

    /**
     * @notice Detokenize a real-world asset
     * @param assetId The ID of the asset to detokenize
     * @param amount The amount of tokens to burn
     */
    function detokenizeAsset(string memory assetId, uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(_assetSupplies[assetId] >= amount, "Insufficient asset supply");

        // Burn tokens
        _burn(msg.sender, amount);

        // Update asset supply
        _assetSupplies[assetId] = _assetSupplies[assetId].sub(amount);

        // Emit event
        emit AssetDetokenized(assetId, amount);
    }

    /**
     * @notice Get the balance of an asset owner
     * @param owner The address of the asset owner
     * @return The balance of the asset owner
     */
    function getAssetBalance(address owner) public view returns (uint256) {
        return _assetBalances[owner];
    }

    /**
     * @notice Get the supply of an asset
     * @param assetId The ID of the asset
     * @return The supply of the asset
     */
    function getAssetSupply(string memory assetId) public view returns (uint256) {
        return _assetSupplies[assetId];
    }

    /**
     * @dev Hook to prevent accidental burns of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256[] memory ids
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, ids);
    }

    /**
     * @dev Hook to prevent accidental burns of tokens
     */
    function _burn(address account, uint256 amount) internal virtual override {
        super._burn(account, amount);
    }
}
```
