"""
Generated Code Metadata:
========================
Original URL: https://enterart.rpmltech.com
Prompt: "Write a code block in Solidity to create a smart contract for minting and trading NFTs on a platform similar to Enter Art."
Generated: DETERMINISTIC_db31d8639ca595d9
Batch ID: 20250622_205348
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

contract EnterArtNFT is ERC721, ERC721URIStorage, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    struct Listing {
        uint256 price;
        address seller;
    }

    mapping(uint256 => Listing) private _listings;
    uint256 public platformFeePercentage = 2.5 * 10; // 2.5% (multiplied by 10 for precision)
    address public platformFeeRecipient;

    event NFTMinted(uint256 tokenId, address owner, string tokenURI);
    event NFTListed(uint256 tokenId, uint256 price, address seller);
    event NFTSold(uint256 tokenId, address buyer, address seller, uint256 price);
    event NFTUnlisted(uint256 tokenId);

    constructor(address _platformFeeRecipient) ERC721("EnterArtNFT", "EANFT") {
        platformFeeRecipient = _platformFeeRecipient;
    }

    function mintNFT(string memory tokenURI) public returns (uint256) {
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        emit NFTMinted(newTokenId, msg.sender, tokenURI);
        return newTokenId;
    }

    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than 0");
        require(_listings[tokenId].seller == address(0), "Already listed");

        _listings[tokenId] = Listing(price, msg.sender);
        approve(address(this), tokenId);

        emit NFTListed(tokenId, price, msg.sender);
    }

    function buyNFT(uint256 tokenId) public payable nonReentrant {
        Listing memory listing = _listings[tokenId];
        require(listing.seller != address(0), "NFT not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds");

        uint256 platformFee = (listing.price * platformFeePercentage) / 1000;
        uint256 sellerProceeds = listing.price - platformFee;

        payable(listing.seller).transfer(sellerProceeds);
        payable(platformFeeRecipient).transfer(platformFee);

        _transfer(listing.seller, msg.sender, tokenId);
        delete _listings[tokenId];

        emit NFTSold(tokenId, msg.sender, listing.seller, listing.price);
    }

    function unlistNFT(uint256 tokenId) public {
        require(_listings[tokenId].seller == msg.sender, "Not the seller");
        delete _listings[tokenId];
        emit NFTUnlisted(tokenId);
    }

    function updatePlatformFeePercentage(uint256 newFeePercentage) public onlyOwner {
        require(newFeePercentage <= 1000, "Fee cannot exceed 100%");
        platformFeePercentage = newFeePercentage;
    }

    function updatePlatformFeeRecipient(address newRecipient) public onlyOwner {
        require(newRecipient != address(0), "Invalid address");
        platformFeeRecipient = newRecipient;
    }

    function getListing(uint256 tokenId) public view returns (Listing memory) {
        return _listings[tokenId];
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
}
```
