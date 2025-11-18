"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepseachain.online
Prompt: Create a function in Solidity to track ownership and display rights of NFTs purchased on the DeepSea marketplace.
Generated: DETERMINISTIC_911a5de4276acfb0
Batch ID: 20250612_153925
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title DeepSeaNFT
// @dev This contract manages the ownership and rights of NFTs on the DeepSea marketplace.
contract DeepSeaNFT is ERC721, Ownable {
    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed owner, string metadataURI);

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // @dev Constructor to initialize the ERC721 token with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _tokenIdCounter = 1; // Start token IDs at 1
    }

    // @dev Function to mint a new NFT
    // @param to The address of the NFT owner
    // @param metadataURI The URI linking to the NFT's metadata
    function mintNFT(address to, string memory metadataURI) external onlyOwner {
        require(to != address(0), "Invalid address: zero address");
        require(bytes(metadataURI).length > 0, "Invalid URI: must not be empty");

        uint256 tokenId = _tokenIdCounter; // Store current token ID
        _tokenIdCounter++; // Increment counter for next mint

        // Mint the NFT and assign ownership
        _mint(to, tokenId);
        _setTokenURI(tokenId, metadataURI); // Set the metadata URI

        emit NFTMinted(tokenId, to, metadataURI); // Emit mint event
    }

    // @dev Function to set the token URI for a specific token ID
    // @param tokenId The ID of the token to update
    // @param metadataURI The URI to set for the token
    function _setTokenURI(uint256 tokenId, string memory metadataURI) internal {
        require(_exists(tokenId), "Token does not exist"); // Check if token exists
        _tokenURIs[tokenId] = metadataURI; // Set the token URI
    }

    // @dev Function to retrieve the token URI for a given token ID
    // @param tokenId The ID of the token to query
    // @return The metadata URI of the token
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist"); // Check if token exists
        return _tokenURIs[tokenId]; // Return the token URI
    }

    // @dev Function to get the total number of minted tokens
    // @return The total token count
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter - 1; // Return total minted NFTs
    }

    // @dev Function to check if an address owns a specific token
    // @param owner The address to check for ownership
    // @param tokenId The ID of the token to check
    // @return True if the address owns the token, false otherwise
    function isOwner(address owner, uint256 tokenId) external view returns (bool) {
        return ownerOf(tokenId) == owner; // Return ownership status
    }
}
```
