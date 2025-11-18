"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quecko.com
Prompt: Write a smart contract for tokenization of Real World Assets (RWA) using Solidity, incorporating security best practices as described by Quecko's blockchain development services.
Generated: DETERMINISTIC_7f70a87be23ae5ae
Batch ID: 20250612_154029
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RealWorldAssetToken
 * @dev A smart contract for tokenizing real-world assets using ERC20 standard.
 * This contract allows for minting and transferring tokens that represent ownership of real-world assets.
 */
contract RealWorldAssetToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping from token ID to asset metadata
    mapping(uint256 => string) private _assetMetadata;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(uint256 indexed assetId, string metadata);

    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 indexed assetId, address indexed from, address indexed to, uint256 amount);

    // Counter for asset IDs
    uint256 private _assetCounter;

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Tokenizes a new real-world asset by minting new tokens.
     * @param assetId Unique identifier for the asset.
     * @param amount Number of tokens to mint representing the asset.
     * @param metadata Metadata associated with the asset.
     */
    function tokenizeAsset(uint256 assetId, uint256 amount, string memory metadata) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(metadata).length > 0, "Metadata cannot be empty");

        // Mint new tokens
        _mint(msg.sender, amount);
        
        // Store asset metadata
        _assetMetadata[assetId] = metadata;
        
        // Emit asset tokenized event
        emit AssetTokenized(assetId, metadata);
    }

    /**
     * @dev Transfers tokens representing an asset from one address to another.
     * @param to The address to transfer tokens to.
     * @param amount The number of tokens to transfer.
     * @param assetId Unique identifier for the asset being transferred.
     */
    function transferAsset(address to, uint256 amount, uint256 assetId) external {
        require(to != address(0), "Transfer to the zero address");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer tokens
        _transfer(msg.sender, to, amount);
        
        // Emit asset transferred event
        emit AssetTransferred(assetId, msg.sender, to, amount);
    }

    /**
     * @dev Returns the metadata associated with a specific asset ID.
     * @param assetId Unique identifier for the asset.
     * @return The metadata string associated with the asset.
     */
    function getAssetMetadata(uint256 assetId) external view returns (string memory) {
        return _assetMetadata[assetId];
    }

    /**
     * @dev Allows the owner to burn tokens representing an asset (e.g., when the asset is sold or removed).
     * @param amount The number of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    /**
     * @dev Prevents accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
