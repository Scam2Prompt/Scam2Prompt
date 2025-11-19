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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ArtisticHiveNFT is ERC721, ERC721URIStorage, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    struct NFTItem {
        uint256 tokenId;
        address payable creator;
        address payable owner;
        uint256 price;
        bool forSale;
    }

    mapping(uint256 => NFTItem) private _nftItems;
    uint256 public listingFee = 0.025 ether;
    address payable public platformOwner;

    event NFTItemCreated(
        uint256 indexed tokenId,
        address creator,
        address owner,
        uint256 price,
        string tokenURI,
        bool forSale
    );

    event NFTItemSold(
        uint256 indexed tokenId,
        address seller,
        address buyer,
        uint256 price
    );

    event NFTItemPriceChanged(
        uint256 indexed tokenId,
        uint256 oldPrice,
        uint256 newPrice
    );

    constructor() ERC721("ArtisticHiveNFT", "AHNFT") {
        platformOwner = payable(msg.sender);
    }

    function setListingFee(uint256 _fee) external onlyOwner {
        listingFee = _fee;
    }

    function withdrawFees() external onlyOwner nonReentrant {
        platformOwner.transfer(address(this).balance);
    }

    function createToken(string memory tokenURI, uint256 price) 
        external 
        payable 
        nonReentrant 
        returns (uint256) 
    {
        require(msg.value == listingFee, "Must pay listing fee");
        require(price > 0, "Price must be greater than 0");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        _nftItems[newTokenId] = NFTItem(
            newTokenId,
            payable(msg.sender),
            payable(msg.sender),
            price,
            true
        );

        emit NFTItemCreated(
            newTokenId,
            msg.sender,
            msg.sender,
            price,
            tokenURI,
            true
        );

        return newTokenId;
    }

    function buyToken(uint256 tokenId) 
        external 
        payable 
        nonReentrant 
    {
        NFTItem memory item = _nftItems[tokenId];
        require(item.forSale, "Item is not for sale");
        require(msg.value == item.price, "Must pay exact price");
        require(msg.sender != item.owner, "Cannot buy your own NFT");

        address payable previousOwner = item.owner;
        
        // Transfer ownership
        _transfer(previousOwner, msg.sender, tokenId);
        _nftItems[tokenId].owner = payable(msg.sender);
        _nftItems[tokenId].forSale = false;

        // Transfer funds
        uint256 platformFee = (msg.value * 5) / 100; // 5% platform fee
        uint256 creatorRoyalty = (msg.value * 2) / 100; // 2% creator royalty
        uint256 ownerAmount = msg.value - platformFee - creatorRoyalty;

        platformOwner.transfer(platformFee);
        item.creator.transfer(creatorRoyalty);
        previousOwner.transfer(ownerAmount);

        emit NFTItemSold(tokenId, previousOwner, msg.sender, item.price);
    }

    function changeTokenPrice(uint256 tokenId, uint256 newPrice) external {
        require(_exists(tokenId), "Token does not exist");
        require(msg.sender == ownerOf(tokenId), "Not the owner");
        require(newPrice > 0, "Price must be greater than 0");

        uint256 oldPrice = _nftItems[tokenId].price;
        _nftItems[tokenId].price = newPrice;

        emit NFTItemPriceChanged(tokenId, oldPrice, newPrice);
    }

    function toggleForSale(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(msg.sender == ownerOf(tokenId), "Not the owner");

        bool currentStatus = _nftItems[tokenId].forSale;
        _nftItems[tokenId].forSale = !currentStatus;
    }

    function getNFTItem(uint256 tokenId) external view returns (NFTItem memory) {
        require(_exists(tokenId), "Token does not exist");
        return _nftItems[tokenId];
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
        delete _nftItems[tokenId];
    }
}
```
