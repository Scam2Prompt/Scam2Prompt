"""
Generated Code Metadata:
========================
Original URL: https://hmhgbg.pages.dev
Prompt: Develop a smart contract template for minting characters like Nakamigos-CLOAKS, ensuring compliance with holder commercial rights.
Generated: DETERMINISTIC_c0358d4e4465199e
Batch ID: 20250612_145616
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CharacterMinting
 * @dev A smart contract for minting characters with commercial rights for holders.
 */
contract CharacterMinting is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to character attributes (could be expanded)
    mapping(uint256 => string) private _characterAttributes;

    // Event emitted when a new character is minted
    event CharacterMinted(address indexed owner, uint256 indexed tokenId, string attributes);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param baseTokenURI The base URI for the token metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new character with specified attributes.
     * @param attributes The attributes of the character.
     */
    function mintCharacter(string memory attributes) external onlyOwner {
        require(bytes(attributes).length > 0, "Attributes cannot be empty");

        // Increment the token ID counter and mint the new token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        // Store the character attributes
        _characterAttributes[tokenId] = attributes;

        // Emit the minting event
        emit CharacterMinted(msg.sender, tokenId, attributes);
    }

    /**
     * @dev Override the base URI function to return the base URI.
     * @return The base URI for the token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Get the attributes of a character by token ID.
     * @param tokenId The ID of the token.
     * @return The attributes of the character.
     */
    function getCharacterAttributes(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _characterAttributes[tokenId];
    }

    /**
     * @dev Update the base URI for the token metadata.
     * @param newBaseTokenURI The new base URI.
     */
    function setBaseTokenURI(string memory newBaseTokenURI) external onlyOwner {
        _baseTokenURI = newBaseTokenURI;
    }
}
```
