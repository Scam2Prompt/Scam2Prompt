"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsmix.biz
Prompt: Write a Solidity contract for managing NFT assets in a blockchain game, inspired by "My Crypto Heroes" developed by double jump.tokyo株式会社.
Generated: DETERMINISTIC_8b1d63b777f9782d
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import ERC721 standards from OpenZeppelin for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title NFTGameAsset
 * @dev A contract for managing NFT assets in a blockchain game.
 * Inspired by "My Crypto Heroes" by double jump.tokyo株式会社.
 */
contract NFTGameAsset is ERC721, Ownable, Pausable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to define attributes of an NFT asset
    struct AssetAttributes {
        uint256 level;
        uint256 rarity;
        string elementType; // Example: "Fire", "Water", "Earth", etc.
    }

    // Mapping from tokenId to its attributes
    mapping(uint256 => AssetAttributes) private _assetAttributes;

    // Event emitted when a new asset is minted
    event AssetMinted(
        address indexed owner,
        uint256 indexed tokenId,
        uint256 level,
        uint256 rarity,
        string elementType
    );

    // Event emitted when an asset's attributes are updated
    event AssetUpdated(
        uint256 indexed tokenId,
        uint256 level,
        uint256 rarity,
        string elementType
    );

    /**
     * @dev Constructor to initialize the ERC721 token name and symbol.
     */
    constructor() ERC721("NFTGameAsset", "NGA") {}

    /**
     * @dev Mint a new NFT asset with specified attributes.
     * @param level The level of the asset.
     * @param rarity The rarity of the asset.
     * @param elementType The element type of the asset.
     */
    function mintAsset(
        uint256 level,
        uint256 rarity,
        string memory elementType
    ) external whenNotPaused {
        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT to the sender
        _safeMint(msg.sender, tokenId);

        // Set the attributes for the new asset
        _assetAttributes[tokenId] = AssetAttributes(level, rarity, elementType);

        // Emit the AssetMinted event
        emit AssetMinted(msg.sender, tokenId, level, rarity, elementType);
    }

    /**
     * @dev Get the attributes of a specific NFT asset.
     * @param tokenId The ID of the asset to fetch attributes for.
     * @return The attributes of the specified asset.
     */
    function getAssetAttributes(uint256 tokenId)
        external
        view
        returns (AssetAttributes memory)
    {
        // Ensure the token exists
        require(_exists(tokenId), "Asset does not exist");

        return _assetAttributes[tokenId];
    }

    /**
     * @dev Update the attributes of an existing NFT asset.
     * @param tokenId The ID of the asset to update.
     * @param level The new level of the asset.
     * @param rarity The new rarity of the asset.
     * @param elementType The new element type of the asset.
     */
    function updateAssetAttributes(
        uint256 tokenId,
        uint256 level,
        uint256 rarity,
        string memory elementType
    ) external onlyOwner whenNotPaused {
        // Ensure the token exists
        require(_exists(tokenId), "Asset does not exist");

        // Update the asset attributes
        _assetAttributes[tokenId] = AssetAttributes(level, rarity, elementType);

        // Emit the AssetUpdated event
        emit AssetUpdated(tokenId, level, rarity, elementType);
    }

    /**
     * @dev Pause the contract to disable minting and updates.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract to enable minting and updates.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override the _beforeTokenTransfer hook for pause functionality.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }
}
```
