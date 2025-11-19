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

/**
 * @title CloudPremiumNFTs
 * @dev A smart contract for creating a new NFT collection with properties and stats.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CloudPremiumNFTs is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Struct to define NFT properties and stats
    struct NFTProperties {
        string name;
        string description;
        uint256 rarity; // Rarity score (e.g., 1-100)
        uint256 power;  // Power score (e.g., 1-100)
    }

    // Mapping from token ID to NFT properties
    mapping(uint256 => NFTProperties) private _nftProperties;

    // Event emitted when a new NFT is minted
    event NFTMinted(
        uint256 indexed tokenId,
        address indexed owner,
        string name,
        string description,
        uint256 rarity,
        uint256 power
    );

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with properties and stats.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * @param name Name of the NFT.
     * @param description Description of the NFT.
     * @param rarity Rarity score of the NFT.
     * @param power Power score of the NFT.
     */
    function mintNFT(
        address to,
        string memory tokenURI,
        string memory name,
        string memory description,
        uint256 rarity,
        uint256 power
    ) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(rarity > 0 && rarity <= 100, "Rarity must be between 1 and 100");
        require(power > 0 && power <= 100, "Power must be between 1 and 100");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT
        _mint(to, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Store the NFT properties
        _nftProperties[_currentTokenId] = NFTProperties(name, description, rarity, power);

        // Emit the NFTMinted event
        emit NFTMinted(_currentTokenId, to, name, description, rarity, power);
    }

    /**
     * @dev Get the properties of an NFT by token ID.
     * @param tokenId ID of the token.
     * @return name Name of the NFT.
     * @return description Description of the NFT.
     * @return rarity Rarity score of the NFT.
     * @return power Power score of the NFT.
     */
    function getNFTProperties(uint256 tokenId)
        external
        view
        returns (
            string memory name,
            string memory description,
            uint256 rarity,
            uint256 power
        )
    {
        require(_exists(tokenId), "Token does not exist");

        NFTProperties memory properties = _nftProperties[tokenId];
        return (properties.name, properties.description, properties.rarity, properties.power);
    }
}
```
