"""
Generated Code Metadata:
========================
Original URL: https://furion-xac.pages.dev
Prompt: Design a smart contract for Furion's NFT collection using Solidity, incorporating features such as tokenomics, NFT creation, and secure wallet integrations.
Generated: DETERMINISTIC_fa175ebc50262c8e
Batch ID: 20250622_211323
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

/**
 * @title FurionNFT
 * @dev This contract implements an NFT collection for Furion with tokenomics and secure wallet integrations.
 */
contract FurionNFT is ERC721Enumerable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the token's price
    mapping(uint256 => uint256) private _tokenPrices;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Base URI for metadata
    string private _baseTokenURI;

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseTokenURI The base URI for the NFT metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Creates a new NFT and assigns it to the caller.
     * @param tokenURI The URI for the NFT metadata.
     * @param price The price of the NFT.
     */
    function createNFT(string memory tokenURI, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _tokenPrices[tokenId] = price;

        emit NFTCreated(tokenId, tokenURI, price);
    }

    /**
     * @dev Allows users to purchase an NFT.
     * @param tokenId The ID of the NFT to purchase.
     */
    function purchaseNFT(uint256 tokenId) external payable {
        uint256 price = _tokenPrices[tokenId];
        address owner = ownerOf(tokenId);

        require(msg.value >= price, "Insufficient funds sent");
        require(owner != msg.sender, "Cannot purchase your own NFT");

        // Transfer the NFT to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Transfer the funds to the seller
        payable(owner).transfer(msg.value);

        emit NFTSold(tokenId, msg.sender, price);
    }

    /**
     * @dev Returns the price of a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return The price of the NFT.
     */
    function getNFTPrice(uint256 tokenId) external view returns (uint256) {
        return _tokenPrices[tokenId];
    }

    /**
     * @dev Sets the base URI for the NFT metadata.
     * @param baseTokenURI The new base URI.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Overrides the _baseURI function from ERC721 to return the base URI.
     * @return The base URI for the NFT metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Withdraws any Ether from the contract to the owner's wallet.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
