"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuki-nft.pages.dev
Prompt: Create a Solidity smart contract snippet for handling NFT purchases, specifically tailored for Azuki Elementals.
Generated: DETERMINISTIC_dec8e9117c6a46aa
Batch ID: 20250612_150552
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AzukiElementalsNFT is ERC721, ERC721Enumerable, Ownable {
    // Mapping from token ID to purchase price
    mapping(uint256 => uint256) private _tokenPrices;
    
    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Base URI for the metadata of the NFTs
    string private _baseTokenURI;

    // Counter for the total supply of NFTs
    uint256 private _tokenIdCounter;

    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
        _tokenIdCounter = 0; // Start token IDs from 0
    }

    // Function to mint a new NFT
    function mintNFT(uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        
        uint256 tokenId = _tokenIdCounter;
        _mint(msg.sender, tokenId); // Mint NFT to the owner's address
        _tokenPrices[tokenId] = price; // Set the purchase price for the NFT
        _tokenIdCounter++; // Increment the token ID counter
        
        emit NFTPurchased(tokenId, msg.sender, price); // Emit purchase event
    }

    // Function to purchase an NFT
    function purchaseNFT(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist"); // Check if token exists
        require(msg.value >= _tokenPrices[tokenId], "Insufficient funds sent"); // Validate purchase price
        
        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "Cannot purchase your own NFT"); // Prevent self-purchase

        // Transfer the NFT to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Transfer funds to the seller (previous owner)
        payable(owner).transfer(msg.value);

        emit NFTPurchased(tokenId, msg.sender, msg.value); // Emit purchase event
    }

    // Function to get the price of a specific NFT
    function getNFTPrice(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "NFT does not exist");
        return _tokenPrices[tokenId];
    }

    // Override required functions from ERC721 and ERC721Enumerable
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    function supportsInterface(bytes4 interfaceId) 
        public view virtual override(ERC721, ERC721Enumerable) returns (bool) 
    {
        return super.supportsInterface(interfaceId);
    }
}
```
