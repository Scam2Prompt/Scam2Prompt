"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Develop a smart contract using Ethereum's Solidity language to facilitate the buying and selling of NFTs, including features like royalty payments to artists.
Generated: DETERMINISTIC_0fe65bcfca46cb97
Batch ID: 20250622_212427
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTMarketplace is ERC721URIStorage, Ownable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    struct RoyaltyInfo {
        address recipient;
        uint256 percentage; // Basis points (e.g., 1000 = 10%)
    }

    struct Listing {
        uint256 price;
        address seller;
        bool isListed;
    }

    mapping(uint256 => RoyaltyInfo) private _royalties;
    mapping(uint256 => Listing) private _listings;

    event NFTListed(uint256 indexed tokenId, uint256 price, address seller);
    event NFTSold(uint256 indexed tokenId, address buyer, address seller, uint256 price);
    event NFTRoyaltyPaid(uint256 indexed tokenId, address recipient, uint256 amount);

    constructor() ERC721("NFT Marketplace", "NFTM") {}

    function mintNFT(address recipient, string memory tokenURI, address royaltyRecipient, uint256 royaltyPercentage) public returns (uint256) {
        require(royaltyPercentage <= 10000, "Royalty percentage cannot exceed 100%");
        
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _mint(recipient, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        if (royaltyRecipient != address(0) && royaltyPercentage > 0) {
            _royalties[newTokenId] = RoyaltyInfo(royaltyRecipient, royaltyPercentage);
        }

        return newTokenId;
    }

    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "Only owner can list NFT");
        require(price > 0, "Price must be greater than 0");
        
        _listings[tokenId] = Listing(price, msg.sender, true);
        emit NFTListed(tokenId, price, msg.sender);
    }

    function buyNFT(uint256 tokenId) public payable {
        Listing memory listing = _listings[tokenId];
        require(listing.isListed, "NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient payment");

        address seller = listing.seller;
        uint256 salePrice = listing.price;
        uint256 royaltyAmount = 0;
        address royaltyRecipient = address(0);

        // Calculate and transfer royalty if applicable
        if (_royalties[tokenId].recipient != address(0)) {
            RoyaltyInfo memory royalty = _royalties[tokenId];
            royaltyAmount = salePrice.mul(royalty.percentage).div(10000);
            royaltyRecipient = royalty.recipient;
            
            if (royaltyAmount > 0) {
                payable(royaltyRecipient).transfer(royaltyAmount);
                emit NFTRoyaltyPaid(tokenId, royaltyRecipient, royaltyAmount);
            }
        }

        // Transfer remaining amount to seller
        uint256 sellerAmount = salePrice.sub(royaltyAmount);
        payable(seller).transfer(sellerAmount);

        // Transfer NFT ownership
        _transfer(seller, msg.sender, tokenId);

        // Remove listing
        delete _listings[tokenId];

        emit NFTSold(tokenId, msg.sender, seller, salePrice);
    }

    function cancelListing(uint256 tokenId) public {
        require(_listings[tokenId].seller == msg.sender, "Only seller can cancel listing");
        delete _listings[tokenId];
    }

    function getListing(uint256 tokenId) public view returns (Listing memory) {
        return _listings[tokenId];
    }

    function getRoyaltyInfo(uint256 tokenId) public view returns (RoyaltyInfo memory) {
        return _royalties[tokenId];
    }

    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
