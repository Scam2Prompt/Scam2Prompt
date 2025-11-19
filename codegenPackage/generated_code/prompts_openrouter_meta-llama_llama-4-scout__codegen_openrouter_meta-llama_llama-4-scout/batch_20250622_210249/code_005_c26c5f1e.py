"""
Generated Code Metadata:
========================
Original URL: https://pre-mpeppe-live.pages.dev
Prompt: Design a basic NFT marketplace using Solidity and OpenZeppelin libraries, similar to the Player Card NFTs on the Mpeppe platform.
Generated: DETERMINISTIC_c26c5f1e7977dc08
Batch ID: 20250622_210249
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMarketplace is ERC721URIStorage, ReentrancyGuard, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Mapping of token ID to its current price
    mapping(uint256 => uint256) public tokenPrices;

    // Mapping of token ID to its current seller
    mapping(uint256 => address) public tokenSellers;

    // Mapping of token ID to its current status (listed or not)
    mapping(uint256 => bool) public tokenStatuses;

    // Event emitted when a new NFT is created
    event NewNFT(address indexed owner, uint256 tokenId);

    // Event emitted when an NFT is listed for sale
    event NFTListed(address indexed seller, uint256 tokenId, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(address indexed buyer, uint256 tokenId);

    // Event emitted when an NFT is delisted
    event NFTDelisted(address indexed seller, uint256 tokenId);

    constructor() ERC721("NFTMarketplace", "NFTM") {}

    // Function to create a new NFT
    function createNFT(string memory tokenURI) public returns (uint256) {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);

        emit NewNFT(msg.sender, newItemId);

        return newItemId;
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        require(!tokenStatuses[tokenId], "This NFT is already listed");

        tokenPrices[tokenId] = price;
        tokenSellers[tokenId] = msg.sender;
        tokenStatuses[tokenId] = true;

        emit NFTListed(msg.sender, tokenId, price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) public payable {
        require(tokenStatuses[tokenId], "This NFT is not listed");
        require(msg.value >= tokenPrices[tokenId], "You must pay at least the listed price");

        address seller = tokenSellers[tokenId];
        require(seller != msg.sender, "You cannot buy your own NFT");

        // Transfer ownership and clear listing
        _transfer(seller, msg.sender, tokenId);
        tokenStatuses[tokenId] = false;
        tokenSellers[tokenId] = address(0);

        payable(seller).transfer(msg.value);

        emit NFTSold(msg.sender, tokenId);
    }

    // Function to delist an NFT
    function delistNFT(uint256 tokenId) public {
        require(tokenSellers[tokenId] == msg.sender, "You are not the seller of this NFT");
        require(tokenStatuses[tokenId], "This NFT is not listed");

        tokenStatuses[tokenId] = false;
        tokenSellers[tokenId] = address(0);

        emit NFTDelisted(msg.sender, tokenId);
    }

    // Function to withdraw funds
    function withdraw() public onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
