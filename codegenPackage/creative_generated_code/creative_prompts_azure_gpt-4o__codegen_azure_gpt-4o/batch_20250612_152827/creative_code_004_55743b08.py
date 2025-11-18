"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Develop a smart contract in Solidity that incorporates rarity traits for NFTs, similar to the KevinLand approach of generating NFTs from dozens of traits.
Generated: DETERMINISTIC_55743b0871d548d0
Batch ID: 20250612_152827
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
 * @title NFTWithRarity
 * @dev A smart contract for generating NFTs with rarity traits
 */
contract NFTWithRarity {
    // State variables
    uint256 public totalNFTs; // Total NFTs minted
    address public owner; // Contract owner

    // Struct to represent an NFT trait
    struct Trait {
        string name; // Trait name
        uint256 rarity; // Rarity value (e.g., 1 to 100)
    }

    // Mapping from trait category to available traits
    mapping(string => Trait[]) public traitsByCategory;

    // Struct to represent an NFT
    struct NFT {
        uint256 id; // NFT ID
        mapping(string => Trait) selectedTraits; // Selected traits for this NFT
    }

    // Mapping from NFT ID to NFT metadata
    mapping(uint256 => NFT) public nftData;

    // Events
    event NFTMinted(uint256 indexed id, address indexed minter, string[] categories, string[] selectedTraitNames);

    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new trait to a specific category
     * @param category The trait category (e.g., "Background", "Hat")
     * @param name The name of the trait (e.g., "Blue Sky", "Cowboy Hat")
     * @param rarity The rarity value of the trait (e.g., 50 means 50% chance)
     */
    function addTrait(string memory category, string memory name, uint256 rarity) external onlyOwner {
        require(rarity > 0 && rarity <= 100, "Rarity must be between 1 and 100");
        traitsByCategory[category].push(Trait(name, rarity));
    }

    /**
     * @dev Mint a new NFT with randomized traits based on rarity
     * @return nftId The ID of the newly minted NFT
     */
    function mintNFT() external returns (uint256 nftId) {
        nftId = ++totalNFTs; // Increment the total NFT count
        NFT storage newNFT = nftData[nftId];
        newNFT.id = nftId;

        string[] memory categories = _getTraitCategories();
        string[] memory selectedTraitNames = new string[](categories.length);

        for (uint256 i = 0; i < categories.length; i++) {
            string memory category = categories[i];
            Trait memory selectedTrait = _selectTraitByRarity(category);
            newNFT.selectedTraits[category] = selectedTrait;
            selectedTraitNames[i] = selectedTrait.name;
        }

        emit NFTMinted(nftId, msg.sender, categories, selectedTraitNames);
    }

    /**
     * @dev Internal function to retrieve all trait categories
     * @return categories An array of trait category names
     */
    function _getTraitCategories() internal view returns (string[] memory categories) {
        uint256 count = 0;
        for (string storage category in traitsByCategory) {
            count++;
        }

        categories = new string[](count);
        uint256 index = 0;
        for (string storage category in traitsByCategory) {
            categories[index++] = category;
        }
    }

    /**
     * @dev Internal function to select a trait from a category based on rarity
     * @param category The category to select from
     * @return selectedTrait The selected trait
     */
    function _selectTraitByRarity(string memory category) internal view returns (Trait memory selectedTrait) {
        require(traitsByCategory[category].length > 0, "No traits available in this category");

        uint256 randomValue = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))) % 100;
        Trait[] memory availableTraits = traitsByCategory[category];

        for (uint256 i = 0; i < availableTraits.length; i++) {
            if (randomValue < availableTraits[i].rarity) {
                return availableTraits[i];
            }
        }

        // Default to the last trait if none matched
        return availableTraits[availableTraits.length - 1];
    }
}
```
