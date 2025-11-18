"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepearab.pages.dev
Prompt: Write a Solidity smart contract to manage the supply of Arab NFTs (Legendary, Rare, Common) based on contribution thresholds and ensure no minting beyond the specified limits.
Generated: DETERMINISTIC_3913cb4b32787357
Batch ID: 20250612_145730
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

// Importing ERC721 interface from OpenZeppelin library
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to manage the supply of Arab NFTs
contract ArabNFT is ERC721Enumerable, Ownable {
    // Enum for NFT rarity levels
    enum Rarity { Legendary, Rare, Common }

    // Struct to define NFT properties
    struct NFT {
        Rarity rarity;
        uint256 tokenId;
    }

    // Mapping from tokenId to NFT
    mapping(uint256 => NFT) private nfts;

    // Maximum supply for each rarity level
    uint256 public constant MAX_LEGENDARY = 100;
    uint256 public constant MAX_RARE = 500;
    uint256 public constant MAX_COMMON = 1000;

    // Current supply for each rarity level
    uint256 public legendaryCount;
    uint256 public rareCount;
    uint256 public commonCount;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 tokenId, Rarity rarity);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("ArabNFT", "ANFT") {}

    // Function to mint a new NFT
    function mint(Rarity rarity) external onlyOwner {
        uint256 tokenId = totalSupply() + 1; // Unique tokenId based on total supply

        // Check for maximum supply limits based on rarity
        if (rarity == Rarity.Legendary) {
            require(legendaryCount < MAX_LEGENDARY, "Max legendary NFTs reached");
            legendaryCount++;
        } else if (rarity == Rarity.Rare) {
            require(rareCount < MAX_RARE, "Max rare NFTs reached");
            rareCount++;
        } else if (rarity == Rarity.Common) {
            require(commonCount < MAX_COMMON, "Max common NFTs reached");
            commonCount++;
        } else {
            revert("Invalid rarity level");
        }

        // Minting the NFT
        _mint(msg.sender, tokenId);
        nfts[tokenId] = NFT(rarity, tokenId);

        // Emit event for the minted NFT
        emit Minted(msg.sender, tokenId, rarity);
    }

    // Function to get NFT details by tokenId
    function getNFT(uint256 tokenId) external view returns (Rarity, uint256) {
        require(_exists(tokenId), "NFT does not exist");
        return (nfts[tokenId].rarity, nfts[tokenId].tokenId);
    }

    // Function to get the current supply for each rarity
    function getCurrentSupply() external view returns (uint256, uint256, uint256) {
        return (legendaryCount, rareCount, commonCount);
    }
}
```
