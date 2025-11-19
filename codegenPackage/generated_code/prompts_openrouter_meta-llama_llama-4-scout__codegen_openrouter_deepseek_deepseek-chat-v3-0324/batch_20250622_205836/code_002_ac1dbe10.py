"""
Generated Code Metadata:
========================
Original URL: https://mintlama.pages.dev
Prompt: Generate a smart contract code for the creation and trading of NFTs on a blockchain platform, as outlined in Phase 2 of the Cyber Lama AI roadmap.
Generated: DETERMINISTIC_ac1dbe1027b01f55
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CyberLamaNFT is ERC721, ERC721URIStorage, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;
    
    // Marketplace fee in basis points (1% = 100 basis points)
    uint256 public marketplaceFee = 250; // 2.5%
    address public marketplaceWallet;

    struct Listing {
        uint256 price;
        address seller;
        bool isActive;
    }

    mapping(uint256 => Listing) public listings;

    event NFTMinted(address indexed owner, uint256 tokenId, string tokenURI);
    event NFTListed(uint256 tokenId, uint256 price, address seller);
    event NFTSold(uint256 tokenId, address buyer, address seller, uint256 price);
    event NFTUnlisted(uint256 tokenId);
    event MarketplaceFeeUpdated(uint256 newFee);
    event MarketplaceWalletUpdated(address newWallet);

    constructor(address _marketplaceWallet) ERC721("CyberLamaNFT", "CLNFT") {
        marketplaceWallet = _marketplaceWallet;
    }

    function safeMint(address to, string memory uri) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
        emit NFTMinted(to, tokenId, uri);
    }

    function listNFT(uint256 tokenId, uint256 price) public nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than 0");
        require(!listings[tokenId].isActive, "Already listed");

        listings[tokenId] = Listing({
            price: price,
            seller: msg.sender,
            isActive: true
        });

        emit NFTListed(tokenId, price, msg.sender);
    }

    function buyNFT(uint256 tokenId) public payable nonReentrant {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "NFT not for sale");
        require(msg.value >= listing.price, "Insufficient funds");

        uint256 feeAmount = listing.price.mul(marketplaceFee).div(10000);
        uint256 sellerAmount = listing.price.sub(feeAmount);

        // Transfer funds
        payable(listing.seller).transfer(sellerAmount);
        payable(marketplaceWallet).transfer(feeAmount);

        // Transfer NFT
        _transfer(listing.seller, msg.sender, tokenId);

        // Remove listing
        delete listings[tokenId];

        emit NFTSold(tokenId, msg.sender, listing.seller, listing.price);
    }

    function unlistNFT(uint256 tokenId) public nonReentrant {
        require(listings[tokenId].isActive, "NFT not listed");
        require(listings[tokenId].seller == msg.sender, "Not the seller");

        delete listings[tokenId];
        emit NFTUnlisted(tokenId);
    }

    function updateMarketplaceFee(uint256 newFee) public onlyOwner {
        require(newFee <= 1000, "Fee too high"); // Max 10%
        marketplaceFee = newFee;
        emit MarketplaceFeeUpdated(newFee);
    }

    function updateMarketplaceWallet(address newWallet) public onlyOwner {
        require(newWallet != address(0), "Invalid address");
        marketplaceWallet = newWallet;
        emit MarketplaceWalletUpdated(newWallet);
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
