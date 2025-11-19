"""
Generated Code Metadata:
========================
Original URL: https://cloudpremiumnfts.com
Prompt: Develop a smart contract using Solidity to create a new NFT collection on Cloud Premium Nfts, including defining the NFT's properties and stats.
Generated: DETERMINISTIC_b0e625bcf552e2c4
Batch ID: 20250622_212702
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

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for the NFT collection
contract CloudPremiumNFTs is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to define NFT properties
    struct NFTProperties {
        string name;
        string description;
        string imageURI;
        uint256 rarity; // Rarity score (higher is rarer)
    }

    // Mapping from token ID to NFT properties
    mapping(uint256 => NFTProperties) private _nftProperties;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string name, string description, string imageURI, uint256 rarity);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("Cloud Premium NFTs", "CPNFT") {}

    // Function to mint a new NFT
    function mintNFT(string memory name, string memory description, string memory imageURI, uint256 rarity) external onlyOwner {
        require(bytes(name).length > 0, "NFT name cannot be empty");
        require(bytes(description).length > 0, "NFT description cannot be empty");
        require(bytes(imageURI).length > 0, "NFT image URI cannot be empty");
        require(rarity > 0, "NFT rarity must be greater than zero");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Set the NFT properties
        _nftProperties[tokenId] = NFTProperties(name, description, imageURI, rarity);

        // Emit the NFT creation event
        emit NFTCreated(tokenId, name, description, imageURI, rarity);
    }

    // Function to get NFT properties by token ID
    function getNFTProperties(uint256 tokenId) external view returns (NFTProperties memory) {
        require(_exists(tokenId), "NFT does not exist");
        return _nftProperties[tokenId];
    }

    // Function to get the total number of NFTs minted
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
