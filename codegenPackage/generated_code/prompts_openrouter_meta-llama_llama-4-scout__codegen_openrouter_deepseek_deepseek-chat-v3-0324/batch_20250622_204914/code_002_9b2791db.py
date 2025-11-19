"""
Generated Code Metadata:
========================
Original URL: https://poly-market.now.sh
Prompt: Generate a simple smart contract using Solidity to create and manage NFTs on the Polygon network, similar to PolyMarket 1.0.
Generated: DETERMINISTIC_9b2791dbf6bfc40a
Batch ID: 20250622_204914
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

/**
 * @title SimpleNFTMarketplace
 * @dev A simple NFT marketplace contract for creating and managing NFTs on Polygon
 */
contract SimpleNFTMarketplace is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Struct to store NFT listing information
    struct NFTListing {
        uint256 tokenId;
        address payable seller;
        uint256 price;
        bool isListed;
    }

    // Mapping from token ID to NFT listing
    mapping(uint256 => NFTListing) private _listings;

    // Event emitted when a new NFT is created and listed
    event NFTListed(
        uint256 indexed tokenId,
        address indexed seller,
        uint256 price,
        string tokenURI
    );

    // Event emitted when an NFT is purchased
    event NFTPurchased(
        uint256 indexed tokenId,
        address indexed seller,
        address indexed buyer,
        uint256 price
    );

    // Event emitted when an NFT listing is canceled
    event NFTUnlisted(uint256 indexed tokenId);

    /**
     * @dev Initializes the contract by setting the name and symbol for the NFT collection
     */
    constructor() ERC721("SimpleNFTMarketplace", "SNFT") {}

    /**
     * @dev Creates a new NFT and lists it for sale
     * @param tokenURI The URI pointing to the NFT metadata
     * @param price The price of the NFT in MATIC
     */
    function createAndListNFT(string memory tokenURI, uint256 price) external {
        require(price > 0, "Price must be greater than 0");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        _listings[newTokenId] = NFTListing({
            tokenId: newTokenId,
            seller: payable(msg.sender),
            price: price,
            isListed: true
        });

        emit NFTListed(newTokenId, msg.sender, price, tokenURI);
    }

    /**
     * @dev Purchases an NFT that is listed for sale
     * @param tokenId The ID of the NFT to purchase
     */
    function purchaseNFT(uint256 tokenId) external payable {
        NFTListing memory listing = _listings[tokenId];
        require(listing.isListed, "NFT is not listed for sale");
        require(msg.value == listing.price, "Incorrect payment amount");
        require(msg.sender != listing.seller, "Seller cannot buy their own NFT");

        _transfer(listing.seller, msg.sender, tokenId);
        listing.seller.transfer(msg.value);

        _listings[tokenId].isListed = false;

        emit NFTPurchased(tokenId, listing.seller, msg.sender, listing.price);
    }

    /**
     * @dev Cancels an NFT listing
     * @param tokenId The ID of the NFT to unlist
     */
    function cancelListing(uint256 tokenId) external {
        require(_listings[tokenId].isListed, "NFT is not listed for sale");
        require(
            _listings[tokenId].seller == msg.sender || msg.sender == owner(),
            "Only seller or owner can cancel listing"
        );

        _listings[tokenId].isListed = false;

        emit NFTUnlisted(tokenId);
    }

    /**
     * @dev Returns the listing information for a specific NFT
     * @param tokenId The ID of the NFT
     * @return NFTListing The listing information
     */
    function getListing(uint256 tokenId) external view returns (NFTListing memory) {
        return _listings[tokenId];
    }

    /**
     * @dev Returns the total number of NFTs created
     * @return uint256 The total number of NFTs
     */
    function totalNFTs() external view returns (uint256) {
        return _tokenIds.current();
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

    /**
     * @dev Withdraws contract balance to owner (only callable by owner)
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
