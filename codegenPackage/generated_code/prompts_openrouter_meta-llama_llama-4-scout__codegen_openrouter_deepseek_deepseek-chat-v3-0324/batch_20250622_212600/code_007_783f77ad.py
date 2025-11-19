"""
Generated Code Metadata:
========================
Original URL: https://alphaspherearts.com
Prompt: Develop a smart contract using Solidity to create, buy, and sell NFTs on a platform like Alpha Sphere Arts.
Generated: DETERMINISTIC_783f77ad8e05085b
Batch ID: 20250622_212600
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

contract AlphaSphereArts is ERC721, ERC721URIStorage, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Listing {
        uint256 price;
        address seller;
    }

    mapping(uint256 => Listing) private _listings;
    uint256 private _platformFeePercentage; // Percentage fee (e.g., 100 = 1%)
    address private _platformFeeRecipient;

    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTUnlisted(uint256 indexed tokenId, address indexed owner);
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    constructor(
        string memory name,
        string memory symbol,
        uint256 platformFeePercentage,
        address platformFeeRecipient
    ) ERC721(name, symbol) {
        require(platformFeePercentage <= 10000, "Fee cannot exceed 100%");
        _platformFeePercentage = platformFeePercentage;
        _platformFeeRecipient = platformFeeRecipient;
    }

    function safeMint(address to, string memory uri) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than 0");
        require(_listings[tokenId].seller == address(0), "Already listed");

        _listings[tokenId] = Listing(price, msg.sender);
        emit NFTListed(tokenId, msg.sender, price);
    }

    function unlistNFT(uint256 tokenId) public {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(_listings[tokenId].seller != address(0), "Not listed");

        delete _listings[tokenId];
        emit NFTUnlisted(tokenId, msg.sender);
    }

    function buyNFT(uint256 tokenId) public payable nonReentrant {
        Listing memory listing = _listings[tokenId];
        require(listing.seller != address(0), "NFT not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds");

        uint256 platformFee = (listing.price * _platformFeePercentage) / 10000;
        uint256 sellerProceeds = listing.price - platformFee;

        address seller = listing.seller;
        delete _listings[tokenId];

        _transfer(seller, msg.sender, tokenId);
        payable(seller).transfer(sellerProceeds);
        payable(_platformFeeRecipient).transfer(platformFee);

        emit NFTSold(tokenId, msg.sender, seller, listing.price);
    }

    function updatePlatformFee(uint256 newFeePercentage) public onlyOwner {
        require(newFeePercentage <= 10000, "Fee cannot exceed 100%");
        _platformFeePercentage = newFeePercentage;
    }

    function updatePlatformFeeRecipient(address newRecipient) public onlyOwner {
        require(newRecipient != address(0), "Invalid address");
        _platformFeeRecipient = newRecipient;
    }

    function getListing(uint256 tokenId) public view returns (Listing memory) {
        return _listings[tokenId];
    }

    function getPlatformFee() public view returns (uint256) {
        return _platformFeePercentage;
    }

    function getPlatformFeeRecipient() public view returns (address) {
        return _platformFeeRecipient;
    }

    // The following functions are overrides required by Solidity.
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

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
