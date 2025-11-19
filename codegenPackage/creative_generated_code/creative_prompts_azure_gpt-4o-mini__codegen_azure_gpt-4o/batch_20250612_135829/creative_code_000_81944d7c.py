"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Generate a smart contract for minting NFTs on the Ethereum blockchain for the Clash of DragonZ project, including unique traits for each dragon.
Generated: DETERMINISTIC_81944d7c65bb5e5d
Batch ID: 20250612_135829
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
 * @title ClashOfDragonZ NFT Contract
 * @dev Smart contract for minting unique NFTs with traits for Clash of DragonZ project
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ClashOfDragonZ is ERC721Enumerable, Ownable {
    // Base URI for metadata storage
    string private baseURI;

    // Counter for token IDs
    uint256 private tokenCounter;

    // Structure for dragon traits
    struct DragonTraits {
        string name;
        string color;
        string element;
        uint256 powerLevel;
    }

    // Mapping from token ID to dragon traits
    mapping(uint256 => DragonTraits) private dragonTraits;

    // Event emitted when a new dragon is minted
    event DragonMinted(uint256 indexed tokenId, DragonTraits traits);

    /**
     * @dev Constructor to initialize contract with name and symbol
     * @param _name Name of the NFT collection
     * @param _symbol Symbol of the NFT collection
     */
    constructor(string memory _name, string memory _symbol) ERC721(_name, _symbol) {
        tokenCounter = 0;
    }

    /**
     * @dev Function to mint a new dragon NFT
     * @param _name Name of the dragon
     * @param _color Color of the dragon
     * @param _element Element of the dragon (e.g., Fire, Water, Earth)
     * @param _powerLevel Power level of the dragon
     */
    function mintDragon(
        string memory _name,
        string memory _color,
        string memory _element,
        uint256 _powerLevel
    ) external onlyOwner {
        // Increment token counter
        tokenCounter++;

        // Set dragon traits
        DragonTraits memory newTraits = DragonTraits({
            name: _name,
            color: _color,
            element: _element,
            powerLevel: _powerLevel
        });

        // Map traits to the new token ID
        dragonTraits[tokenCounter] = newTraits;

        // Mint the NFT
        _safeMint(msg.sender, tokenCounter);

        // Emit event
        emit DragonMinted(tokenCounter, newTraits);
    }

    /**
     * @dev Function to get traits of a specific dragon
     * @param _tokenId Token ID of the dragon NFT
     * @return DragonTraits structure containing traits
     */
    function getDragonTraits(uint256 _tokenId)
        external
        view
        returns (DragonTraits memory)
    {
        require(_exists(_tokenId), "Token does not exist");
        return dragonTraits[_tokenId];
    }

    /**
     * @dev Function to set base URI for metadata
     * @param _baseURI Base URI string
     */
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    /**
     * @dev Function to override the base URI
     * @return string Base URI for metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Function to get the current token counter
     * @return uint256 Current token counter value
     */
    function getTokenCounter() external view returns (uint256) {
        return tokenCounter;
    }
}
```
