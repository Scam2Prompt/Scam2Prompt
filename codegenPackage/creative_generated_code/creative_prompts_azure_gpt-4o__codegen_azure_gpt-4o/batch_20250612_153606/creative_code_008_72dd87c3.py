"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a Solidity contract that generates NFTs with 170+ traits and varying rarity, similar to the algorithmic generation process described for Robotos on the Robots NFT Minting website.
Generated: DETERMINISTIC_72dd87c33d4fe582
Batch ID: 20250612_153606
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
 * @title NFTGenerator
 * @dev A contract to generate NFTs with 170+ traits and varying rarity.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTGenerator is ERC721Enumerable, Ownable {
    // Struct to hold trait information
    struct Trait {
        string name; // Name of the trait
        uint256 rarity; // Rarity value (1 to 100)
    }

    // Mapping for trait categories and their traits
    mapping(string => Trait[]) public traitCategories;

    // Token ID to traits mapping
    mapping(uint256 => string[]) public tokenTraits;

    // Base URI for metadata
    string private _baseTokenURI;

    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Add a new trait category with traits.
     * @param category The category name (e.g., "Head", "Body").
     * @param traits The array of trait names.
     * @param rarities The corresponding array of rarity values for each trait.
     */
    function addTraitCategory(string memory category, string[] memory traits, uint256[] memory rarities) external onlyOwner {
        require(traits.length == rarities.length, "Traits and rarities length mismatch");
        for (uint256 i = 0; i < traits.length; i++) {
            traitCategories[category].push(Trait(traits[i], rarities[i]));
        }
    }

    /**
     * @dev Mint a new NFT with randomly generated traits.
     * @param to The address to mint the NFT to.
     */
    function mintNFT(address to) external onlyOwner {
        uint256 tokenId = totalSupply() + 1;

        // Generate traits for the NFT
        string[] memory generatedTraits = new string[](170); // Assuming 170 traits
        uint256 index = 0;

        for (uint256 i = 0; i < 170; i++) {
            string memory category = getRandomCategory();
            Trait memory trait = getRandomTrait(category);
            generatedTraits[index] = trait.name;
            index++;
        }

        // Store the traits for the token ID
        tokenTraits[tokenId] = generatedTraits;

        // Mint the NFT
        _safeMint(to, tokenId);
    }

    /**
     * @dev Get random category based on available categories.
     */
    function getRandomCategory() private view returns (string memory) {
        uint256 categoriesCount = getTraitCategoriesCount();
        uint256 randomIndex = random(categoriesCount);
        // Assume traitCategories keys are enumerable
        string[] memory keys = getTraitCategoryNames();
        return keys[randomIndex];
    }

    /**
     * @dev Generate Randomly trait n stepsx
