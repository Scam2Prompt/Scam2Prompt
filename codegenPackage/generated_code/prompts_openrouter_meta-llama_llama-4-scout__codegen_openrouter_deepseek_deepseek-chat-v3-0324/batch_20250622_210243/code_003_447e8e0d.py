"""
Generated Code Metadata:
========================
Original URL: https://realio-bridge.web.app
Prompt: "Develop a smart contract for creating and managing digitally native real-world assets (RWAs) on the Realio Network."
Generated: DETERMINISTIC_447e8e0da743397a
Batch ID: 20250622_210243
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title RealWorldAssetManager
 * @dev Smart contract for creating and managing digitally native real-world assets (RWAs) on the Realio Network
 */
contract RealWorldAssetManager is ERC721, Ownable, Pausable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    // Asset details structure
    struct Asset {
        string assetId;
        string name;
        string description;
        string location;
        uint256 value;
        string documentHash;
        address currentOwner;
        uint256 creationDate;
        uint256 lastUpdated;
        bool isActive;
    }

    // Mapping from token ID to Asset
    mapping(uint256 => Asset) private _assets;

    // Mapping from asset ID to token ID
    mapping(string => uint256) private _assetIdToTokenId;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Events
    event AssetCreated(
        uint256 indexed tokenId,
        string assetId,
        string name,
        uint256 value,
        address owner
    );
    event AssetUpdated(
        uint256 indexed tokenId,
        string assetId,
        string name,
        uint256 value
    );
    event AssetTransferred(
        uint256 indexed tokenId,
        string assetId,
        address from,
        address to
    );
    event AssetStatusChanged(uint256 indexed tokenId, string assetId, bool isActive);

    /**
     * @dev Constructor
     */
    constructor() ERC721("RealWorldAsset", "RWA") {}

    /**
     * @dev Creates a new RWA
     * @param assetId Unique identifier for the asset
     * @param name Name of the asset
     * @param description Description of the asset
     * @param location Physical location of the asset
     * @param value Monetary value of the asset
     * @param documentHash Hash of the document proving ownership
     */
    function createAsset(
        string memory assetId,
        string memory name,
        string memory description,
        string memory location,
        uint256 value,
        string memory documentHash
    ) external whenNotPaused {
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");
        require(bytes(name).length > 0, "Name cannot be empty");
        require(value > 0, "Value must be greater than zero");
        require(_assetIdToTokenId[assetId] == 0, "Asset ID already exists");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        Asset memory newAsset = Asset({
            assetId: assetId,
            name: name,
            description: description,
            location: location,
            value: value,
            documentHash: documentHash,
            currentOwner: msg.sender,
            creationDate: block.timestamp,
            lastUpdated: block.timestamp,
            isActive: true
        });

        _assets[tokenId] = newAsset;
        _assetIdToTokenId[assetId] = tokenId;

        _safeMint(msg.sender, tokenId);

        emit AssetCreated(tokenId, assetId, name, value, msg.sender);
    }

    /**
     * @dev Updates asset information
     * @param tokenId Token ID of the asset to update
     * @param name New name of the asset
     * @param description New description of the asset
     * @param location New location of the asset
     * @param value New value of the asset
     * @param documentHash New document hash
     */
    function updateAsset(
        uint256 tokenId,
        string memory name,
        string memory description,
        string memory location,
        uint256 value,
        string memory documentHash
    ) external whenNotPaused {
        require(_exists(tokenId), "Asset does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only owner can update asset");
        require(bytes(name).length > 0, "Name cannot be empty");
        require(value > 0, "Value must be greater than zero");

        Asset storage asset = _assets[tokenId];
        asset.name = name;
        asset.description = description;
        asset.location = location;
        asset.value = value;
        asset.documentHash = documentHash;
        asset.lastUpdated = block.timestamp;

        emit AssetUpdated(tokenId, asset.assetId, name, value);
    }

    /**
     * @dev Transfers ownership of an asset
     * @param from Current owner address
     * @param to New owner address
     * @param tokenId Token ID of the asset to transfer
     */
    function transferAsset(
        address from,
        address to,
        uint256 tokenId
    ) external whenNotPaused {
        require(_exists(tokenId), "Asset does not exist");
        require(ownerOf(tokenId) == from, "Not the current owner");
        require(to != address(0), "Cannot transfer to zero address");

        _transfer(from, to, tokenId);
        _assets[tokenId].currentOwner = to;
        _assets[tokenId].lastUpdated = block.timestamp;

        emit AssetTransferred(tokenId, _assets[tokenId].assetId, from, to);
    }

    /**
     * @dev Changes the active status of an asset
     * @param tokenId Token ID of the asset
     * @param isActive New status
     */
    function setAssetStatus(uint256 tokenId, bool isActive) external onlyOwner {
        require(_exists(tokenId), "Asset does not exist");
        _assets[tokenId].isActive = isActive;
        _assets[tokenId].lastUpdated = block.timestamp;

        emit AssetStatusChanged(tokenId, _assets[tokenId].assetId, isActive);
    }

    /**
     * @dev Gets asset details by token ID
     * @param tokenId Token ID of the asset
     * @return Asset details
     */
    function getAssetDetails(uint256 tokenId) external view returns (Asset memory) {
        require(_exists(tokenId), "Asset does not exist");
        return _assets[tokenId];
    }

    /**
     * @dev Gets asset details by asset ID
     * @param assetId Asset ID
     * @return Asset details
     */
    function getAssetDetailsById(string memory assetId) external view returns (Asset memory) {
        uint256 tokenId = _assetIdToTokenId[assetId];
        require(tokenId != 0, "Asset does not exist");
        return _assets[tokenId];
    }

    /**
     * @dev Pauses all asset transfers and updates
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all asset transfers and updates
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Overrides transfer to include additional checks
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override whenNotPaused {
        require(_assets[tokenId].isActive, "Asset is not active");
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
