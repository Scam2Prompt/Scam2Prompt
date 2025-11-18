"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartauthresolver.web.app
Prompt: Write a Solidity contract to manage and troubleshoot NFT creation and marketplace interactions, ensuring smooth functionality as outlined on SmartAuthResolver.
Generated: DETERMINISTIC_19f56f5b384ec410
Batch ID: 20250612_154207
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title NFTMarketplace
// @dev This contract manages the creation and trading of NFTs
contract NFTMarketplace is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to store NFT details
    struct NFT {
        uint256 id;
        string uri;
        address owner;
        uint256 price;
        bool forSale;
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) private _nfts;

    // Event emitted when an NFT is created
    event NFTCreated(uint256 indexed tokenId, string uri, address indexed owner, uint256 price);

    // Event emitted when an NFT is put up for sale
    event NFTPutOnSale(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer, address indexed seller);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("MyNFTCollection", "MNFT") {}

    // Function to create a new NFT
    function createNFT(string memory uri, uint256 price) public onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        
        _nfts[tokenId] = NFT({
            id: tokenId,
            uri: uri,
            owner: msg.sender,
            price: price,
            forSale: false
        });

        _tokenIdCounter.increment();

        emit NFTCreated(tokenId, uri, msg.sender, price);
    }

    // Function to put an NFT up for sale
    function putNFTOnSale(uint256 tokenId, uint256 price) public {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "You are not the owner");
        require(price > 0, "Price must be greater than zero");

        _nfts[tokenId].forSale = true;
        _nfts[tokenId].price = price;

        emit NFTPutOnSale(tokenId, price);
    }

    // Function to purchase an NFT
    function purchaseNFT(uint256 tokenId) public payable {
        require(_exists(tokenId), "NFT does not exist");
        require(_nfts[tokenId].forSale, "NFT is not for sale");
        require(msg.value >= _nfts[tokenId].price, "Insufficient funds");

        address seller = _nfts[tokenId].owner;

        // Transfer the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);

        // Update NFT owner and sale status
        _nfts[tokenId].owner = msg.sender;
        _nfts[tokenId].forSale = false;

        // Transfer funds to seller
        payable(seller).transfer(msg.value);

        emit NFTPurchased(tokenId, msg.sender, seller);
    }

    // Function to get NFT details
    function getNFTDetails(uint256 tokenId) public view returns (NFT memory) {
        require(_exists(tokenId), "NFT does not exist");
        return _nfts[tokenId];
    }
}
```
