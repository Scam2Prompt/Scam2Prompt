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

/**
 * @title NFTMetadata
 * @dev A simple example of an ERC721 contract with metadata storage for NFTs.
 * Metadata includes artist signature and other details.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMetadata is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _currentTokenId;

    // Mapping to store artist signatures for each token ID
    mapping(uint256 => string) private _artistSignatures;

    /**
     * @dev Constructor to initialize the NFT contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with metadata and artist signature.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata (e.g., JSON file on IPFS).
     * @param artistSignature Signature of the artist associated with the NFT.
     */
    function mintNFT(
        address to,
        string memory tokenURI,
        string memory artistSignature
    ) external onlyOwner {
        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT to the specified address
        _mint(to, _currentTokenId);

        // Set the token URI for metadata
        _setTokenURI(_currentTokenId, tokenURI);

        // Store the artist signature
        _artistSignatures[_currentTokenId] = artistSignature;
    }

    /**
     * @dev Retrieve the artist signature for a given token ID.
     * @param tokenId ID of the token.
     * @return The artist signature associated with the token.
     */
    function getArtistSignature(uint256 tokenId) external view returns (string memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");

        // Return the artist signature
        return _artistSignatures[tokenId];
    }

    /**
     * @dev Override the _burn function to clean up metadata and artist signature.
     * @param tokenId ID of the token to burn.
     */
    function _burn(uint256 tokenId) internal override {
        super._burn(tokenId);

        // Delete the artist signature for the burned token
        delete _artistSignatures[tokenId];
    }
}
```
