"""
Generated Code Metadata:
========================
Original URL: https://launchpad.seedify.de
Prompt: "Generate a smart contract code in Solidity for creating and managing NFT sales on a platform like Seedify."
Generated: DETERMINISTIC_42cac36c8d826a17
Batch ID: 20250622_205529
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title NFTMarketplace
 * @dev A smart contract for creating and managing NFT sales on a platform like Seedify.
 */
contract NFTMarketplace is ERC721, ERC721Enumerable, Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    struct Listing {
        uint256 price;
        address seller;
        bool isActive;
    }

    mapping(uint256 => Listing) private _listings;
    uint256 public listingFee = 0.01 ether; // Fee for listing an NFT

    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);
    event ListingCancelled(uint256 indexed tokenId, address indexed seller);

    constructor() ERC721("SeedifyNFT", "SNFT") {}

    /**
     * @dev Mints a new NFT and assigns it to the caller.
     * @param tokenURI The URI for the token metadata.
     */
    function mintNFT(string memory tokenURI) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }

    /**
     * @dev Lists an NFT for sale.
     * @param tokenId The ID of the NFT to list.
     * @param price The price in wei for the NFT.
     */
    function listNFT(uint256 tokenId, uint256 price) public payable nonReentrant {
        require(msg.value == listingFee, "Incorrect listing fee");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than 0");
        require(!_listings[tokenId].isActive, "NFT already listed");

        _listings[tokenId] = Listing({
            price: price,
            seller: msg.sender,
            isActive: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Buys an NFT that is listed for sale.
     * @param tokenId The ID of the NFT to buy.
     */
    function buyNFT(uint256 tokenId) public payable nonReentrant {
        Listing memory listing = _listings[tokenId];
        require(listing.isActive, "NFT not listed");
        require(msg.value == listing.price, "Incorrect payment amount");

        address seller = listing.seller;
        _transfer(seller, msg.sender, tokenId);

        payable(seller).transfer(msg.value);
        delete _listings[tokenId];

        emit NFTSold(tokenId, msg.sender, seller, msg.value);
    }

    /**
     * @dev Cancels an active listing.
     * @param tokenId The ID of the NFT to delist.
     */
    function cancelListing(uint256 tokenId) public nonReentrant {
        Listing memory listing = _listings[tokenId];
        require(listing.isActive, "NFT not listed");
        require(listing.seller == msg.sender, "Not the seller");

        delete _listings[tokenId];
        emit ListingCancelled(tokenId, msg.sender);
    }

    /**
     * @dev Returns the listing details for a given NFT.
     * @param tokenId The ID of the NFT.
     * @return price The price of the NFT.
     * @return seller The seller's address.
     * @return isActive Whether the listing is active.
     */
    function getListing(uint256 tokenId) public view returns (uint256 price, address seller, bool isActive) {
        Listing memory listing = _listings[tokenId];
        return (listing.price, listing.seller, listing.isActive);
    }

    /**
     * @dev Withdraws the contract's balance to the owner.
     */
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Override required by Solidity for ERC721Enumerable
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    // Override required by Solidity for ERC721Enumerable
    function supportsInterface(bytes4 interfaceId) public view override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
