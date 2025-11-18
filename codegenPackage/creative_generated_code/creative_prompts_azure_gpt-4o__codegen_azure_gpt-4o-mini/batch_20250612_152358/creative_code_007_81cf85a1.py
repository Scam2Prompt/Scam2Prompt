"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: Suggest best practices for creators using Truffle to manage their NFT collections efficiently.
Generated: DETERMINISTIC_81cf85a13ffdf152
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the ERC721 interface
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title: NFTCollectionManager
// @dev: Smart contract for managing NFT collections efficiently
contract NFTCollectionManager is ERC721Enumerable, Ownable {
    // Mapping from token ID to the token's metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Base URI for the metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI);

    // Constructor to set the NFT collection name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // @dev: Function to set the base URI for all NFTs
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // @dev: Function to mint a new NFT
    // @param to: The address that will receive the NFT
    // @param tokenId: The unique identifier for the NFT
    // @param tokenURI: The metadata URI for the NFT
    function mintNFT(address to, uint256 tokenId, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(!_exists(tokenId), "Token ID already exists");

        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit NFTCreated(tokenId, tokenURI);
    }

    // @dev: Function to set the URI for a specific token
    // @param tokenId: The unique identifier for the NFT
    // @param tokenURI: The metadata URI for the NFT
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token ID does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    // @dev: Override the base URI function to return the base URI with token ID
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // @dev: Function to retrieve the token URI for a specific token
    // @param tokenId: The unique identifier for the NFT
    // @return The metadata URI for the NFT
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token ID does not exist");
        return string(abi.encodePacked(_baseURI(), _tokenURIs[tokenId]));
    }

    // @dev: Function to burn an NFT
    // @param tokenId: The unique identifier for the NFT to burn
    function burnNFT(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _burn(tokenId);
        delete _tokenURIs[tokenId];
    }
}
```
