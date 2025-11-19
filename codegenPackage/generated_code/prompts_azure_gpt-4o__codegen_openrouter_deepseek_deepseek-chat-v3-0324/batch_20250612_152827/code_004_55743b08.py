"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Develop a smart contract in Solidity that incorporates rarity traits for NFTs, similar to the KevinLand approach of generating NFTs from dozens of traits.
Generated: DETERMINISTIC_55743b0871d548d0
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract RarityNFT is ERC721, Ownable {
    using Strings for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Struct to define a trait
    struct Trait {
        string name;
        uint256 rarity; // Percentage (0-100)
    }

    // Mapping from trait category to array of traits
    mapping(string => Trait[]) private _traitCategories;

    // Mapping from token ID to its traits
    mapping(uint256 => mapping(string => string)) private _tokenTraits;

    // Events
    event TraitAdded(string category, string traitName, uint256 rarity);
    event NFTMinted(address indexed to, uint256 tokenId);

    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Add a new trait category with its traits
     * @param category The category name (e.g., "Background")
     * @param traitNames Array of trait names
     * @param rarities Array of corresponding rarities (0-100)
     */
    function addTraitCategory(
        string memory category,
        string[] memory traitNames,
        uint256[] memory rarities
    ) external onlyOwner {
        require(traitNames.length == rarities.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < traitNames.length; i++) {
            _traitCategories[category].push(Trait(traitNames[i], rarities[i]));
            emit TraitAdded(category, traitNames[i], rarities[i]);
        }
    }

    /**
     * @dev Mint a new NFT with randomly selected traits based on rarity
     */
    function mint(address to) external {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Assign random traits based on rarity
        _assignRandomTraits(tokenId);
        
        _safeMint(to, tokenId);
        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev Internal function to assign random traits to a token
     */
    function _assignRandomTraits(uint256 tokenId) private {
        // Get all trait categories
        string[] memory categories = _getTraitCategories();
        
        for (uint256 i = 0; i < categories.length; i++) {
            string memory category = categories[i];
            Trait[] storage traits = _traitCategories[category];
            
            if (traits.length > 0) {
                // Calculate total rarity weight
                uint256 totalRarity = 0;
                for (uint256 j = 0; j < traits.length; j++) {
                    totalRarity += traits[j].rarity;
                }
                
                // Generate random number within total rarity
                uint256 random = _random(totalRarity);
                uint256 cumulativeRarity = 0;
                
                // Select trait based on rarity
                for (uint256 j = 0; j < traits.length; j++) {
                    cumulativeRarity += traits[j].rarity;
                    if (random <= cumulativeRarity) {
                        _tokenTraits[tokenId][category] = traits[j].name;
                        break;
                    }
                }
            }
        }
    }

    /**
     * @dev Get all trait categories
     */
    function _getTraitCategories() private view returns (string[] memory) {
        // In production, you would store categories separately for efficiency
        // This is a simplified version
        string[] memory categories = new string[](3);
        categories[0] = "Background";
        categories[1] = "Body";
        categories[2] = "Accessory";
        return categories;
    }

    /**
     * @dev Generate a pseudo-random number
     */
    function _random(uint256 max) private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))) % max;
    }

    /**
     * @dev Get the traits for a specific token
     */
    function getTokenTraits(uint256 tokenId) external view returns (string[] memory, string[] memory) {
        require(_exists(tokenId), "Token does not exist");
        
        string[] memory categories = _getTraitCategories();
        string[] memory traits = new string[](categories.length);
        
        for (uint256 i = 0; i < categories.length; i++) {
            traits[i] = _tokenTraits[tokenId][categories[i]];
        }
        
        return (categories, traits);
    }

    /**
     * @dev Set base URI for metadata
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Get total supply
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
