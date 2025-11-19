"""
Generated Code Metadata:
========================
Original URL: https://ethereum.fit
Prompt: Design a library for creating custom fantasy instruments of technology on Ethereum FIT.
Generated: DETERMINISTIC_478bb80f9d42f4c6
Batch ID: 20250622_205436
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title FantasyInstrumentTechnology (FIT)
 * @dev A contract for creating custom fantasy instruments of technology as NFTs
 */
contract FantasyInstrumentTechnology is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Mapping from token ID to instrument attributes
    mapping(uint256 => InstrumentAttributes) private _instrumentAttributes;

    // Struct to store instrument attributes
    struct InstrumentAttributes {
        string name;
        string description;
        string powerType;
        uint256 powerLevel;
        string rarity;
    }

    // Events
    event InstrumentCreated(
        uint256 indexed tokenId,
        string name,
        string description,
        string powerType,
        uint256 powerLevel,
        string rarity
    );

    /**
     * @dev Constructor
     * @param baseTokenURI Base URI for token metadata
     */
    constructor(string memory baseTokenURI) ERC721("FantasyInstrumentTechnology", "FIT") {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Creates a new fantasy instrument
     * @param name Name of the instrument
     * @param description Description of the instrument
     * @param powerType Type of power the instrument has
     * @param powerLevel Power level of the instrument (1-100)
     * @param rarity Rarity of the instrument
     * @return The new token ID
     */
    function createInstrument(
        string memory name,
        string memory description,
        string memory powerType,
        uint256 powerLevel,
        string memory rarity
    ) public onlyOwner returns (uint256) {
        require(powerLevel > 0 && powerLevel <= 100, "FIT: Invalid power level");
        require(bytes(name).length > 0, "FIT: Name cannot be empty");
        require(bytes(description).length > 0, "FIT: Description cannot be empty");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _instrumentAttributes[tokenId] = InstrumentAttributes(
            name,
            description,
            powerType,
            powerLevel,
            rarity
        );

        _safeMint(msg.sender, tokenId);

        emit InstrumentCreated(
            tokenId,
            name,
            description,
            powerType,
            powerLevel,
            rarity
        );

        return tokenId;
    }

    /**
     * @dev Returns the attributes of a specific instrument
     * @param tokenId The token ID to query
     * @return InstrumentAttributes The attributes of the instrument
     */
    function getInstrumentAttributes(uint256 tokenId) public view returns (InstrumentAttributes memory) {
        require(_exists(tokenId), "FIT: Nonexistent token");
        return _instrumentAttributes[tokenId];
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseTokenURI The new base URI
     */
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     * @return The base URI string
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The token ID to query
     * @return The token URI string
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "FIT: Nonexistent token");
        return string(abi.encodePacked(_baseURI(), tokenId.toString()));
    }
}
```
