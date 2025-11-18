"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Write a Solidity contract to tokenize freelancers' work as NFTs, including functionality for royalties and ownership verification, as described in DeeLance's NFT marketplace.
Generated: DETERMINISTIC_46cf523f97b43d69
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FreelanceWorkNFT
 * @dev A contract for tokenizing freelancers' work as NFTs, with royalty functionality and ownership verification.
 */
contract FreelanceWorkNFT is ERC721URIStorage, ERC721Royalty, Ownable {
    uint256 private _tokenIdCounter;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 tokenId, address owner, string metadataURI, uint96 royaltyPercentage);

    // Event emitted when royalties are updated
    event RoyaltiesUpdated(uint256 tokenId, address receiver, uint96 royaltyPercentage);

    constructor() ERC721("FreelanceWorkNFT", "FWNFT") {}

    /**
     * @notice Mints a new NFT representing freelance work.
     * @param to Address of the recipient.
     * @param metadataURI Metadata URI pointing to the details of the work.
     * @param royaltyReceiver Address to receive royalty payments.
     * @param royaltyPercentage Percentage of royalties (in basis points, e.g., 500 = 5%).
     */
    function mintNFT(
        address to,
        string memory metadataURI,
        address royaltyReceiver,
        uint96 royaltyPercentage
    ) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;

        // Mint the NFT
        _safeMint(to, newTokenId);

        // Set the metadata URI
        _setTokenURI(newTokenId, metadataURI);

        // Set the royalty information
        _setTokenRoyalty(newTokenId, royaltyReceiver, royaltyPercentage);

        // Emit an event for the new NFT creation
        emit NFTCreated(newTokenId, to, metadataURI, royaltyPercentage);
    }

    /**
     * @notice Updates the royalty details for a specific NFT.
     * @param tokenId Token ID of the NFT.
     * @param royaltyReceiver Address to receive royalty payments.
     * @param royaltyPercentage Percentage of royalties (in basis points, e.g., 500 = 5%).
     */
    function updateRoyalty(
        uint256 tokenId,
        address royaltyReceiver,
        uint96 royaltyPercentage
    ) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");

        // Update royalty information
        _setTokenRoyalty(tokenId, royaltyReceiver, royaltyPercentage);

        // Emit an event for royalty update
        emit RoyaltiesUpdated(tokenId, royaltyReceiver, royaltyPercentage);
    }

    /**
     * @notice Verifies ownership of a given NFT.
     * @param tokenId Token ID of the NFT.
     * @return The address of the owner of the token.
     */
    function verifyOwnership(uint256 tokenId) external view returns (address) {
        require(_exists(tokenId), "Token does not exist");
        return ownerOf(tokenId);
    }

    // Override required by Solidity due to inheritance
    function supportsInterface(bytes4 interfaceId)
        public
        view
        virtual
        override(ERC721, ERC721Royalty)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
