"""
Generated Code Metadata:
========================
Original URL: https://artistichive.io
Prompt: Develop a smart contract using Solidity to facilitate the creation, sale, and ownership verification of NFTs on a platform like ArtisticHive.
Generated: DETERMINISTIC_8fc01b558277ff44
Batch ID: 20250622_212519
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title ArtisticHiveNFT
 * @dev This contract facilitates the creation, sale, and ownership verification of NFTs.
 */
contract ArtisticHiveNFT is ERC721, ERC721Burnable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to sale price
    mapping(uint256 => uint256) private _tokenPrices;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    /**
     * @dev Constructor to initialize the NFT contract with a name and symbol.
     */
    constructor() ERC721("ArtisticHiveNFT", "AHNFT") {}

    /**
     * @dev Creates a new NFT with a specified token URI and sale price.
     * @param tokenURI The URI pointing to the NFT's metadata.
     * @param price The sale price of the NFT.
     */
    function createNFT(string memory tokenURI, uint256 price) public onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _tokenPrices[tokenId] = price;

        emit NFTCreated(tokenId, tokenURI, price);
        _tokenIdCounter.increment();
    }

    /**
     * @dev Allows a user to purchase an NFT.
     * @param tokenId The ID of the NFT to purchase.
     */
    function buyNFT(uint256 tokenId) public payable {
        uint256 price = _tokenPrices[tokenId];
        address owner = ownerOf(tokenId);

        require(msg.value >= price, "Insufficient funds sent");
        require(owner != msg.sender, "Cannot buy your own NFT");
        require(price > 0, "NFT not for sale");

        // Transfer the NFT to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Transfer the sale price to the seller
        payable(owner).transfer(msg.value);

        // Reset the price of the NFT
        _tokenPrices[tokenId] = 0;

        emit NFTSold(tokenId, msg.sender, price);
    }

    /**
     * @dev Returns the sale price of a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return The sale price of the NFT.
     */
    function getNFTPrice(uint256 tokenId) public view returns (uint256) {
        return _tokenPrices[tokenId];
    }

    /**
     * @dev Allows the owner to set a new price for an NFT.
     * @param tokenId The ID of the NFT.
     * @param price The new sale price of the NFT.
     */
    function setNFTPrice(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can set the price");
        require(price > 0, "Price must be greater than zero");

        _tokenPrices[tokenId] = price;
    }

    /**
     * @dev Override the _burn function to clear the token price when an NFT is burned.
     * @param tokenId The ID of the NFT to burn.
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
        delete _tokenPrices[tokenId];
    }

    /**
     * @dev Returns the token URI for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return The token URI of the NFT.
     */
    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage) returns (string memory) {
        return super.tokenURI(tokenId);
    }
}
```
