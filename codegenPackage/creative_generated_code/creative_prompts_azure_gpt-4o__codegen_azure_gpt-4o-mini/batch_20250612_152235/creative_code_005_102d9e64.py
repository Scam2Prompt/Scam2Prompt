"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintlama.pages.dev
Prompt: Create a Solidity-based smart contract for NFT trading that integrates with other platforms, as outlined in Phase 4 of the Cyber Lama project. Include features for enhanced exchange options.
Generated: DETERMINISTIC_102d9e64d39cef3d
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0; // Specify the Solidity version

import "@openzeppelin/contracts/token/ERC721/ERC721.sol"; // Import ERC721 for NFT functionality
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol"; // For enumerable NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol"; // For token URI management
import "@openzeppelin/contracts/access/Ownable.sol"; // For contract ownership functionalities
import "@openzeppelin/contracts/utils/Counters.sol"; // For counter utilities

/**
 * @title CyberLamaNFT
 * @dev A smart contract for trading NFTs with enhanced exchange options
 */
contract CyberLamaNFT is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Event to log NFT listing
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    // Event to log NFT sale
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    // Structure to store NFT listing details
    struct Listing {
        uint256 price;
        address seller;
    }

    // Mapping from token ID to listing details
    mapping(uint256 => Listing) private _listings;

    constructor() ERC721("CyberLamaNFT", "CLNFT") {}

    /**
     * @dev Creates a new NFT with a unique token URI
     * @param tokenURI The metadata URI associated with the NFT
     */
    function mintNFT(string memory tokenURI) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _tokenIdCounter.increment();
    }

    /**
     * @dev Lists an NFT for sale
     * @param tokenId The ID of the NFT to be listed
     * @param price The sale price of the NFT
     */
    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(price > 0, "Price must be greater than 0");
        
        _listings[tokenId] = Listing(price, msg.sender);
        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Purchase an NFT that is listed for sale
     * @param tokenId The ID of the NFT to be purchased
     */
    function buyNFT(uint256 tokenId) public payable {
        Listing memory listing = _listings[tokenId];
        require(listing.price > 0, "NFT is not for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");
        
        address seller = listing.seller;
        _transfer(seller, msg.sender, tokenId);
        delete _listings[tokenId]; // Remove the listing after purchase
        
        // Transfer funds to the seller
        payable(seller).transfer(msg.value); 

        emit NFTSold(tokenId, msg.sender, seller, listing.price);
    }

    /**
     * @dev Gets the listing details for a specific token ID
     * @param tokenId The ID of the NFT
     * @return price The price of the NFT
     * @return seller The seller of the NFT
     */
    function getListing(uint256 tokenId) public view returns (uint256 price, address seller) {
        Listing memory listing = _listings[tokenId];
        return (listing.price, listing.seller);
    }

    // Override required by Solidity to keep track of total supply for ERC721Enumerable
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // Override required by Solidity to ensure enumerability
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
