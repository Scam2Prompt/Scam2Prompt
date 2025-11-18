"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-ae.web.app
Prompt: Write a smart contract in Solidity that enables tokenization of real-world assets like real estate or art, similar to the functionality described in the Rexas Finance ecosystem.
Generated: DETERMINISTIC_72d4a609ec3b533d
Batch ID: 20250612_145242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title AssetTokenization
 * @dev A smart contract to tokenize real-world assets like real estate or art. 
 * Inspired by Rexas Finance ecosystem. This contract follows ERC721 standard for 
 * non-fungible tokens (NFTs) to represent unique assets.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract AssetTokenization is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an asset
    struct Asset {
        string name;        // Name of the asset (e.g., "Beachfront Property")
        string metadataURI; // IPFS/other URI pointing to asset metadata
        address owner;      // Address of the asset's owner
        uint256 value;      // Appraised value of the asset in wei
    }

    // Mapping from tokenId to Asset
    mapping(uint256 => Asset) private _assets;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(
        uint256 indexed tokenId,
        string name,
        string metadataURI,
        address indexed owner,
        uint256 value
    );

    // Constructor to initialize the ERC721 token
    constructor() ERC721("AssetToken", "AT") {}

    /**
     * @dev Tokenize a new asset.
     * @param name The name of the asset.
     * @param metadataURI The metadata URI for the asset (e.g., IPFS link).
     * @param owner The address of the initial owner of the asset.
     * @param value The value of the asset in wei.
     */
    function tokenizeAsset(
        string memory name,
        string memory metadataURI,
        address owner,
        uint256 value
    ) public onlyOwner {
        require(bytes(name).length > 0, "Asset name cannot be empty");
        require(bytes(metadataURI).length > 0, "Metadata URI is required");
        require(owner != address(0), "Owner address cannot be zero");
        require(value > 0, "Asset value must be greater than zero");

        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the new NFT
        _safeMint(owner, newTokenId);

        // Save the asset details
        _assets[newTokenId] = Asset(name, metadataURI, owner, value);

        // Emit event
        emit AssetTokenized(newTokenId, name, metadataURI, owner, value);
    }

    /**
     * @dev Get details of a tokenized asset.
     * @param tokenId The ID of the tokenized asset.
     * @return name The name of the asset.
     * @return metadataURI The metadata URI of the asset.
     * @return owner The owner of the asset.
     * @return value The appraised value of the asset in wei.
     */
    function getAssetDetails(uint256 tokenId)
        public
        view
        returns (
            string memory name,
            string memory metadataURI,
            address owner,
            uint256 value
        )
    {
        require(_exists(tokenId), "Asset does not exist");

        Asset memory asset = _assets[tokenId];
        return (asset.name, asset.metadataURI, asset.owner, asset.value);
    }

    /**
     * @dev Override the ERC721 _transfer function to ensure the asset owner is updated.
     * @param from The address of the current owner.
     * @param to The address of the new owner.
     * @param tokenId The ID of the token being transferred.
     */
    function _transfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._transfer(from, to, tokenId);
        _assets[tokenId].owner = to;
    }
}
```
