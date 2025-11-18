"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hmhgbg.pages.dev
Prompt: Develop a smart contract template for minting characters like Nakamigos-CLOAKS, ensuring compliance with holder commercial rights.
Generated: DETERMINISTIC_c0358d4e4465199e
Batch ID: 20250612_145616
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

/**
 * @title NakamigosCloaksCharacterMinter
 * @dev A smart contract for minting character NFTs with holder commercial rights.
 *      This contract implements ERC-721 for NFTs and includes functions for minting,
 *      metadata management, and compliance with commercial rights.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NakamigosCloaksCharacterMinter is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Token ID tracker
    Counters.Counter private _tokenIdTracker;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new character is minted
    event CharacterMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Event emitted when the base URI is updated
    event BaseURIUpdated(string newBaseURI);

    /**
     * @dev Constructor to initialize the contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseTokenURI Initial base URI for metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to mint a new character NFT.
     * @param tokenURI URI for the metadata of the NFT.
     */
    function mintCharacter(string memory tokenURI) external {
        // Increment the token ID
        _tokenIdTracker.increment();
        uint256 newTokenId = _tokenIdTracker.current();

        // Mint the NFT to the caller
        _safeMint(msg.sender, newTokenId);

        // Set the metadata URI
        _setTokenURI(newTokenId, tokenURI);

        // Emit the minting event
        emit CharacterMinted(msg.sender, newTokenId, tokenURI);
    }

    /**
     * @dev Function to update the base URI for metadata.
     * @param baseTokenURI New base URI.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
        emit BaseURIUpdated(baseTokenURI);
    }

    /**
     * @dev Override of the _baseURI function from ERC721.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to verify holder commercial rights.
     *      Ensures NFT holders can use their NFTs for commercial purposes.
     * @param tokenId Token ID to check.
     * @return True if the caller owns the token or has been approved.
     */
    function verifyCommercialRights(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Query for non-existent token");
        return _isApprovedOrOwner(msg.sender, tokenId);
    }

    /**
     * @dev Internal override to add custom logic for token transfers if needed.
     * @param from Address transferring the token.
     * @param to Address receiving the token.
     * @param tokenId Token ID being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721) {
        super._beforeTokenTransfer(from, to, tokenId);
        // Additional checks or logic can be added here if needed in the future
    }
}
```
