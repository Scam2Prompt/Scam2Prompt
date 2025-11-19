"""
Generated Code Metadata:
========================
Original URL: https://genopets.eu
Prompt: Create a smart contract in Solidity for managing in-game assets and rewards in a blockchain-based game like Genopets.
Generated: DETERMINISTIC_7f7a39d15469140f
Batch ID: 20250612_151513
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title InGameAssetManager
// @dev A smart contract for managing in-game assets and rewards in a blockchain-based game.
contract InGameAssetManager is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an in-game asset
    struct Asset {
        uint256 id;
        string name;
        string assetType;
        uint256 value;
        bool isReward;
    }

    // Mapping from token ID to Asset
    mapping(uint256 => Asset) private _assets;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 indexed id, string name, string assetType, uint256 value, bool isReward);

    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 indexed id, address from, address to);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("InGameAsset", "IGA") {}

    // @dev Create a new in-game asset
    // @param name The name of the asset
    // @param assetType The type of the asset (e.g., "character", "item")
    // @param value The value of the asset
    // @param isReward Indicates if the asset is a reward
    function createAsset(string memory name, string memory assetType, uint256 value, bool isReward) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Create the asset and store it in the mapping
        _assets[tokenId] = Asset(tokenId, name, assetType, value, isReward);
        _mint(msg.sender, tokenId);

        emit AssetCreated(tokenId, name, assetType, value, isReward);
    }

    // @dev Transfer an asset to another address
    // @param to The address to transfer the asset to
    // @param tokenId The ID of the asset to transfer
    function transferAsset(address to, uint256 tokenId) external {
        require(_exists(tokenId), "Asset does not exist");
        require(ownerOf(tokenId) == msg.sender, "You do not own this asset");

        // Transfer the asset
        _transfer(msg.sender, to, tokenId);
        emit AssetTransferred(tokenId, msg.sender, to);
    }

    // @dev Retrieve asset details by token ID
    // @param tokenId The ID of the asset
    // @return The asset details
    function getAsset(uint256 tokenId) external view returns (Asset memory) {
        require(_exists(tokenId), "Asset does not exist");
        return _assets[tokenId];
    }

    // @dev Retrieve the total number of assets created
    // @return The total number of assets
    function totalAssets() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
