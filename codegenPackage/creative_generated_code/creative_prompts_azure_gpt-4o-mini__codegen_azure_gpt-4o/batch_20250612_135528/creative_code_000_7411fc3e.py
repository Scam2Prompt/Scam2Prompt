"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: How can I create a dynamic NFT that evolves based on user decisions, similar to the HV-MTL collection?
Generated: DETERMINISTIC_7411fc3e7a7c3776
Batch ID: 20250612_135528
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

/**
 * @title DynamicNFT
 * @dev A contract for creating dynamic NFTs that evolve based on user decisions.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DynamicNFT is ERC721, Ownable {
    // Struct to hold NFT attributes
    struct NFTAttributes {
        uint256 level; // Represents the evolution stage
        string metadataURI; // URI of the metadata or image
    }

    // Mapping from tokenId to NFT attributes
    mapping(uint256 => NFTAttributes) private _nftAttributes;

    // Event when an NFT evolves
    event NFTUpdated(uint256 tokenId, uint256 newLevel, string newMetadataURI);

    uint256 private _nextTokenId = 1;

    // Constructor to initialize the NFT collection
    constructor() ERC721("Dynamic NFT", "DNFT") {}

    /**
     * @dev Mint a new NFT.
     * @param metadataURI The initial metadata URI for the NFT.
     */
    function mintNFT(string memory metadataURI) external {
        uint256 tokenId = _nextTokenId;

        // Mint the NFT to the caller
        _safeMint(msg.sender, tokenId);

        // Initialize attributes for the new NFT
        _nftAttributes[tokenId] = NFTAttributes({level: 1, metadataURI: metadataURI});

        // Increment the tokenId counter for the next mint
        _nextTokenId++;
    }

    /**
     * @dev Get the attributes of a specific NFT.
     * @param tokenId The tokenId of the NFT to query.
     * @return The level and metadata URI of the NFT.
     */
    function getNFTAttributes(uint256 tokenId)
        external
        view
        returns (uint256 level, string memory metadataURI)
    {
        require(_exists(tokenId), "Query for nonexistent token");
        NFTAttributes memory attributes = _nftAttributes[tokenId];
        return (attributes.level, attributes.metadataURI);
    }

    /**
     * @dev Update the NFT's attributes based on user interaction.
     * @param tokenId The tokenId of the NFT to update.
     * @param newLevel The new level of the NFT.
     * @param newMetadataURI The new metadata URI representing the evolved state.
     */
    function updateNFT(uint256 tokenId, uint256 newLevel, string memory newMetadataURI) external {
        require(_exists(tokenId), "Update for nonexistent token");
        require(ownerOf(tokenId) == msg.sender, "Only the owner can update this NFT");

        // Update the attributes of the NFT
        NFTAttributes storage attributes = _nftAttributes[tokenId];
        attributes.level = newLevel;
        attributes.metadataURI = newMetadataURI;

        // Emit an event to signal the update
        emit NFTUpdated(tokenId, newLevel, newMetadataURI);
    }

    /**
     * @dev Override the tokenURI function to dynamically return the metadata URI.
     * @param tokenId The tokenId of the NFT.
     * @return The metadata URI of the NFT.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _nftAttributes[tokenId].metadataURI;
    }
}
```
