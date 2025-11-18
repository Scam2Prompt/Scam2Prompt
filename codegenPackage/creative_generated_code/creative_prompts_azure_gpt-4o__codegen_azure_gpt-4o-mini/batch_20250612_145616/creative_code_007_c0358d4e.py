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
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CharacterMinting
 * @dev A smart contract for minting unique characters with holder commercial rights.
 */
contract CharacterMinting is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new character is minted
    event CharacterMinted(address indexed owner, uint256 indexed tokenId);

    // Counter for tracking the token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to character metadata
    mapping(uint256 => string) private _characterMetadata;

    // Constructor to set the name and symbol of the token
    constructor(string memory name_, string memory symbol_) ERC721(name_, symbol_) {}

    /**
     * @dev Function to mint a new character.
     * @param metadata The metadata associated with the character.
     * Requirements:
     * - `metadata` should not be an empty string.
     */
    function mintCharacter(string memory metadata) external onlyOwner {
        require(bytes(metadata).length > 0, "CharacterMinting: Metadata cannot be empty");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);

        _characterMetadata[tokenId] = metadata; // Store character metadata
        _tokenIdCounter.increment();

        emit CharacterMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function to retrieve character metadata.
     * @param tokenId The ID of the token.
     * @return The metadata associated with the character.
     * Requirements:
     * - `tokenId` must exist.
     */
    function getCharacterMetadata(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "CharacterMinting: Token ID does not exist");
        return _characterMetadata[tokenId];
    }

    /**
     * @dev Function to set the base URI for metadata.
     * @param baseURI The base URI to be set.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to override the baseURI for metadata.
     * @return The base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
