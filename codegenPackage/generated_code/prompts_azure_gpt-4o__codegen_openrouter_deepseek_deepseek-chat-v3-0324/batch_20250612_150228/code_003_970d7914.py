"""
Generated Code Metadata:
========================
Original URL: https://bafybeielizhnh2kfpdv2iivhqh4ttf4kqfecv2qyislghqacr6n5gzcfzm.ipfs.dweb.link
Prompt: Create a smart contract for managing data ownership within the Vana decentralized AI ecosystem.
Generated: DETERMINISTIC_970d7914c4a00bdd
Batch ID: 20250612_150228
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

/**
 * @title VanaDataOwnership
 * @dev ERC721 token representing data ownership in the Vana ecosystem
 */
contract VanaDataOwnership is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to store data ownership information
    struct DataAsset {
        address owner;
        string uri;
        uint256 creationTimestamp;
        bool isActive;
    }

    // Mapping from token ID to DataAsset
    mapping(uint256 => DataAsset) private _dataAssets;

    // Events
    event DataAssetRegistered(
        uint256 indexed tokenId,
        address indexed owner,
        string uri,
        uint256 timestamp
    );
    event DataAssetTransferred(
        uint256 indexed tokenId,
        address indexed from,
        address indexed to
    );
    event DataAssetDeactivated(uint256 indexed tokenId);

    constructor() ERC721("VanaDataAsset", "VDA") {}

    /**
     * @dev Register a new data asset
     * @param uri Metadata URI for the data asset
     */
    function registerDataAsset(string memory uri) public {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, uri);

        _dataAssets[tokenId] = DataAsset({
            owner: msg.sender,
            uri: uri,
            creationTimestamp: block.timestamp,
            isActive: true
        });

        emit DataAssetRegistered(tokenId, msg.sender, uri, block.timestamp);
    }

    /**
     * @dev Transfer data asset ownership
     * @param from Current owner address
     * @param to New owner address
     * @param tokenId Token ID to transfer
     */
    function transferDataAsset(
        address from,
        address to,
        uint256 tokenId
    ) public {
        require(_exists(tokenId), "Token does not exist");
        require(_isApprovedOrOwner(msg.sender, tokenId), "Not approved");
        require(_dataAssets[tokenId].isActive, "Data asset is inactive");

        _transfer(from, to, tokenId);
        _dataAssets[tokenId].owner = to;

        emit DataAssetTransferred(tokenId, from, to);
    }

    /**
     * @dev Deactivate a data asset (soft delete)
     * @param tokenId Token ID to deactivate
     */
    function deactivateDataAsset(uint256 tokenId) public {
        require(_exists(tokenId), "Token does not exist");
        require(_isApprovedOrOwner(msg.sender, tokenId), "Not approved");
        require(_dataAssets[tokenId].isActive, "Already inactive");

        _dataAssets[tokenId].isActive = false;
        emit DataAssetDeactivated(tokenId);
    }

    /**
     * @dev Get data asset information
     * @param tokenId Token ID to query
     */
    function getDataAsset(uint256 tokenId)
        public
        view
        returns (
            address owner,
            string memory uri,
            uint256 creationTimestamp,
            bool isActive
        )
    {
        require(_exists(tokenId), "Token does not exist");
        DataAsset memory asset = _dataAssets[tokenId];
        return (asset.owner, asset.uri, asset.creationTimestamp, asset.isActive);
    }

    // Override functions
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
