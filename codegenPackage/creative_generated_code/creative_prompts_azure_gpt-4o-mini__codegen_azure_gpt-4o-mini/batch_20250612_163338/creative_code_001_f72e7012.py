"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cosmostrader.pages.dev
Prompt: Write a code snippet that demonstrates how to use smart contracts for NFT transactions on the Ethereum blockchain as described on the Cosmos Home site.
Generated: DETERMINISTIC_f72e70125a6c4a74
Batch ID: 20250612_163338
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

// Importing OpenZeppelin's ERC721 for NFT functionality
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for creating and managing NFTs
contract MyNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private _baseTokenURI;
    
    // Mapping from token ID to token price
    mapping(uint256 => uint256) private _tokenPrices;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner, uint256 price);
    
    // Event emitted when an NFT is bought
    event Bought(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Function to set the base URI for the metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to get the base URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(uint256 tokenId, uint256 price) external onlyOwner {
        require(!_exists(tokenId), "Token ID already exists");
        _mint(msg.sender, tokenId);
        _tokenPrices[tokenId] = price;
        
        emit Minted(tokenId, msg.sender, price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        require(_exists(tokenId), "Token does not exist");
        require(msg.value >= _tokenPrices[tokenId], "Insufficient funds");

        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "Cannot buy your own NFT");

        // Transfer NFT to buyer
        _transfer(owner, msg.sender, tokenId);
        
        // Transfer Ether to the seller
        payable(owner).transfer(msg.value);
        
        emit Bought(tokenId, msg.sender, msg.value);
    }

    // Function to get the price of an NFT
    function getTokenPrice(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenPrices[tokenId];
    }
}
```
