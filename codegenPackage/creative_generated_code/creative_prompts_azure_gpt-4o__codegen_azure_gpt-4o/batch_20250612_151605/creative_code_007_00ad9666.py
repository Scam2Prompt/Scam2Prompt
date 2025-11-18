"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-9dc.pages.dev
Prompt: Write code in Solidity to implement an ERC-721 contract for Pepe 2.0 NFTs with metadata that reflects the "legend of the sequel" theme described on the website.
Generated: DETERMINISTIC_00ad966669235ed9
Batch ID: 20250612_151605
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
 * @title Pepe2NFT
 * @dev ERC-721 implementation for "Pepe 2.0 NFTs" with metadata reflecting the "legend of the sequel" theme.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Pepe2NFT is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping to store token metadata
    mapping(uint256 => string) private _tokenMetadata;

    /**
     * @dev Constructor to initialize the contract.
     * @param baseURI The base URI for token metadata.
     */
    constructor(string memory baseURI) ERC721("Pepe 2.0 NFT", "PEPE2") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new token.
     * @param to Address to mint the token to.
     * @param metadataURI Metadata URI for the minted token.
     */
    function mint(address to, string memory metadataURI) external onlyOwner {
        // Increment the token ID counter
        _currentTokenId++;

        // Mint the token to the specified address
        _safeMint(to, _currentTokenId);

        // Set the token metadata URI
        _setTokenURI(_currentTokenId, metadataURI);

        // Store the metadata for internal reference
        _tokenMetadata[_currentTokenId] = metadataURI;
    }

    /**
     * @dev Override the base URI used for computing {tokenURI}.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Update the base URI for metadata.
     * @param newBaseURI The new base URI.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    /**
     * @dev Retrieve the metadata URI for a specific token ID.
     * @param tokenId The token ID to query.
     * @return Metadata URI string.
     */
    function getTokenMetadata(uint256 tokenId) external view returns (string memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");

        return _tokenMetadata[tokenId];
    }

    /**
     * @dev Override _beforeTokenTransfer hook to include custom logic.
     * @param from Address transferring the token (zero for minting).
     * @param to Address receiving the token (zero for burning).
     * @param tokenId Token ID being transferred.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Additional logic can be added here if necessary
    }
}
```
