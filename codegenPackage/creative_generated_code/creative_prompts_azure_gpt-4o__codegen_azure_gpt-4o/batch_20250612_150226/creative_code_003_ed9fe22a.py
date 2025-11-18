"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Write a smart contract in Solidity to manage the creation and trading of Hero NFTs in the R-Planet Conquest game.
Generated: DETERMINISTIC_ed9fe22a7a4579c3
Batch ID: 20250612_150226
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title HeroNFT - A smart contract to manage Hero NFTs for R-Planet Conquest game.
/// @dev This contract uses OpenZeppelin libraries for ERC721, access control, and counters.
contract HeroNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    /// @notice Event emitted when a new Hero NFT is created.
    /// @param tokenId The unique ID of the minted Hero NFT.
    /// @param owner The address of the owner of the minted Hero NFT.
    event HeroCreated(uint256 tokenId, address owner);

    /// @notice Event emitted when an NFT is put up for trade.
    /// @param tokenId The unique ID of the Hero NFT.
    /// @param price The price in wei for which the NFT is listed.
    event HeroListedForTrade(uint256 tokenId, uint256 price);

    /// @notice Event emitted when an NFT is successfully traded.
    /// @param tokenId The unique ID of the Hero NFT.
    /// @param seller The address of the seller.
    /// @param buyer The address of the buyer.
    /// @param price The price in wei for which the NFT was bought.
    event HeroTraded(uint256 tokenId, address seller, address buyer, uint256 price);

    // Struct to keep track of NFTs listed for trading
    struct Listing {
        uint256 price;
        address seller;
    }

    // Mapping to store active listings for NFTs
    mapping(uint256 => Listing) public listings;

    constructor() ERC721("HeroNFT", "HERO") {}

    /// @notice Mint a new Hero NFT.
    /// @param recipient The address of the NFT recipient.
    /// @param tokenURI The metadata URI of the NFT.
    /// @return tokenId The unique ID of the minted Hero NFT.
    function createHero(address recipient, string memory tokenURI) external onlyOwner returns (uint256 tokenId) {
        _tokenIds.increment();
        tokenId = _tokenIds.current();

        _mint(recipient, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit HeroCreated(tokenId, recipient);
        return tokenId;
    }

    /// @notice List a Hero NFT for trading.
    /// @param tokenId The unique ID of the NFT to list.
    /// @param price The price in wei at which the NFT is listed.
    function listHeroForTrade(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(ownerOf(tokenId) == msg.sender, "Only the owner can list the NFT");
        require(listings[tokenId].price == 0, "NFT is already listed");

        listings[tokenId] = Listing(price, msg.sender);
        emit HeroListedForTrade(tokenId, price);
    }

    /// @notice Buy a listed Hero NFT.
    /// @param tokenId The unique ID of the NFT to buy.
    function buyHero(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.price > 0, "NFT is not listed for trade");
        require(msg.value == listing.price, "Incorrect value sent for purchase");

        address seller = listing.seller;

        // Transfer the NFT from seller to buyer
        _transfer(seller, msg.sender, tokenId);

        // Transfer payment to the seller
        payable(seller).transfer(msg.value);

        // Remove the listing
        delete listings[tokenId];

        emit HeroTraded(tokenId, seller, msg.sender, listing.price);
    }

    /// @notice Delist an NFT from trading.
    /// @param tokenId The unique ID of the NFT to delist.
    function delistHero(uint256 tokenId) external {
        require(listings[tokenId].price > 0, "NFT is not listed for trade");
        require(listings[tokenId].seller == msg.sender, "Only the seller can delist the NFT");

        delete listings[tokenId];
    }

    /// @notice Get the details of an NFT listing.
    /// @param tokenId The unique ID of the NFT.
    /// @return price The price in wei.
    /// @return seller The address of the seller.
    function getListing(uint256 tokenId) external view returns (uint256 price, address seller) {
        Listing memory listing = listings[tokenId];
        require(listing.price > 0, "NFT is not listed for trade");
        return (listing.price, listing.seller);
    }
}
```
