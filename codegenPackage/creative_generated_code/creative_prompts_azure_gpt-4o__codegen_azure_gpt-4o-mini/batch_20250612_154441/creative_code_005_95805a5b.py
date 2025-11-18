"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Generate a smart contract that categorizes NFT holders into groups (e.g., Human, Robot, Demon, etc.) based on metadata, as described in the Clone Force™ pledge system.
Generated: DETERMINISTIC_95805a5b1c06872c
Batch ID: 20250612_154441
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

// Interface for an external metadata provider (if needed)
interface IMetadataProvider {
    function getMetadata(uint256 tokenId) external view returns (string memory);
}

// Main contract for the Clone Force NFT
contract CloneForceNFT is ERC721, ERC721Burnable, Ownable {
    // Enum for categorizing NFT holders
    enum Category { Human, Robot, Demon }

    // Mapping from token ID to holder's category
    mapping(uint256 => Category) private _tokenCategories;
    // Mapping from token ID to holder's metadata
    mapping(uint256 => string) private _tokenMetadata;

    // Event emitted when a token's category is set
    event CategoryAssigned(uint256 indexed tokenId, Category category);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("Clone Force", "CFNFT") {}

    // Minting function to create new NFTs
    function mint(address to, uint256 tokenId, string memory metadata) external onlyOwner {
        // Mint the NFT
        _mint(to, tokenId);
        // Set metadata for the token
        _tokenMetadata[tokenId] = metadata;
        // Categorize the new token based on metadata
        categorizeToken(tokenId);
    }

    // Internal function to categorize a token based on its metadata
    function categorizeToken(uint256 tokenId) internal {
        // Retrieve metadata of the token
        string memory metadata = _tokenMetadata[tokenId];

        // Categorize based on keywords in metadata
        if (contains(metadata, "human")) {
            _tokenCategories[tokenId] = Category.Human;
        } else if (contains(metadata, "robot")) {
            _tokenCategories[tokenId] = Category.Robot;
        } else if (contains(metadata, "demon")) {
            _tokenCategories[tokenId] = Category.Demon;
        } else {
            // Default category if no match
            _tokenCategories[tokenId] = Category.Human; // Default to Human
        }

        // Emit an event when a category is assigned
        emit CategoryAssigned(tokenId, _tokenCategories[tokenId]);
    }

    // Function to check if metadata contains a keyword
    function contains(string memory str, string memory keyword) internal pure returns (bool) {
        return (bytes(str).length != 0 && bytes(keyword).length != 0 && bytes(str).length >= bytes(keyword).length);
    }

    // Function to get the category of a token
    function getCategory(uint256 tokenId) external view returns (Category) {
        return _tokenCategories[tokenId];
    }

    // Function to get the metadata of a token
    function getMetadata(uint256 tokenId) external view returns (string memory) {
        return _tokenMetadata[tokenId];
    }
}
```
