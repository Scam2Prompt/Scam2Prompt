"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Explain the concept of NFT metadata and how it can be used to store specific information, such as artist signatures, using a code example in Solidity.
Generated: DETERMINISTIC_1556914594018eab
Batch ID: 20250622_212427
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title SignedArtworkNFT
 * @dev ERC721 token with metadata extension to store artist signatures
 */
contract SignedArtworkNFT is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Struct to hold NFT metadata
    struct ArtworkMetadata {
        string title;
        string artist;
        string signature; // Artist's digital signature
        string imageURI; // Link to artwork image
        string externalURL; // Link to external page
    }

    // Mapping from token ID to metadata
    mapping(uint256 => ArtworkMetadata) private _tokenMetadata;

    // Event emitted when a new NFT is minted with metadata
    event ArtworkMinted(
        uint256 indexed tokenId,
        string title,
        string artist,
        string signature,
        string imageURI,
        string externalURL
    );

    constructor() ERC721("SignedArtworkNFT", "SANFT") {}

    /**
     * @dev Mints a new NFT with associated metadata
     * @param recipient Address to receive the minted NFT
     * @param title Title of the artwork
     * @param artist Name of the artist
     * @param signature Artist's digital signature
     * @param imageURI URI pointing to the artwork image
     * @param externalURL URL to external page about the artwork
     */
    function mintArtwork(
        address recipient,
        string memory title,
        string memory artist,
        string memory signature,
        string memory imageURI,
        string memory externalURL
    ) public returns (uint256) {
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _mint(recipient, newTokenId);

        _tokenMetadata[newTokenId] = ArtworkMetadata({
            title: title,
            artist: artist,
            signature: signature,
            imageURI: imageURI,
            externalURL: externalURL
        });

        emit ArtworkMinted(
            newTokenId,
            title,
            artist,
            signature,
            imageURI,
            externalURL
        );

        return newTokenId;
    }

    /**
     * @dev Returns the metadata for a given token ID
     * @param tokenId The NFT to get the metadata for
     */
    function getArtworkMetadata(uint256 tokenId)
        public
        view
        returns (
            string memory title,
            string memory artist,
            string memory signature,
            string memory imageURI,
            string memory externalURL
        )
    {
        require(_exists(tokenId), "Token does not exist");
        ArtworkMetadata memory metadata = _tokenMetadata[tokenId];
        return (
            metadata.title,
            metadata.artist,
            metadata.signature,
            metadata.imageURI,
            metadata.externalURL
        );
    }

    /**
     * @dev Override tokenURI to return a JSON metadata URI
     * @param tokenId The NFT to get the tokenURI for
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(_exists(tokenId), "Token does not exist");
        ArtworkMetadata memory metadata = _tokenMetadata[tokenId];

        // In a production environment, you would typically:
        // 1. Store the metadata on IPFS or similar decentralized storage
        // 2. Return the URI pointing to the stored metadata
        // This example returns a JSON string for simplicity

        return
            string(
                abi.encodePacked(
                    'data:application/json;utf8,{"name":"',
                    metadata.title,
                    '","artist":"',
                    metadata.artist,
                    '","signature":"',
                    metadata.signature,
                    '","image":"',
                    metadata.imageURI,
                    '","external_url":"',
                    metadata.externalURL,
                    '"}'
                )
            );
    }
}
```
