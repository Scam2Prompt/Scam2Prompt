"""
Generated Code Metadata:
========================
Original URL: https://collectiblemarkethub.com
Prompt: "Generate a smart contract code for minting and trading NFTs on a platform similar to Collectible Market Hub, incorporating features like customizable templates and responsive design."
Generated: DETERMINISTIC_49cfc2cda8a48432
Batch ID: 20250622_204816
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

/**
 * @title NFTMarketplace
 * @dev A smart contract for minting and trading NFTs with customizable templates.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTMarketplace is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIds;

    // Struct to represent an NFT listing
    struct NFTListing {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isListed;
    }

    // Mapping to store NFT listings
    mapping(uint256 => NFTListing) public listings;

    // Event emitted when an NFT is minted
    event NFTMinted(uint256 tokenId, address owner, string tokenURI);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 tokenId, address seller, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 tokenId, address buyer, uint256 price);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     */
    constructor() ERC721("CollectibleMarketHub", "CMH") {}

    /**
     * @dev Mint a new NFT with a customizable template (tokenURI).
     * @param tokenURI The metadata URI for the NFT.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(string memory tokenURI) external returns (uint256) {
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the NFT and set its metadata URI
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        emit NFTMinted(newTokenId, msg.sender, tokenURI);
        return newTokenId;
    }

    /**
     * @dev List an NFT for sale.
     * @param tokenId The ID of the NFT to list.
     * @param price The sale price of the NFT (in wei).
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can list the NFT");
        require(price > 0, "Price must be greater than zero");

        listings[tokenId] = NFTListing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isListed: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Purchase a listed NFT.
     * @param tokenId The ID of the NFT to purchase.
     */
    function purchaseNFT(uint256 tokenId) external payable {
        NFTListing memory listing = listings[tokenId];
        require(listing.isListed, "NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient payment");

        // Transfer payment to the seller
        payable(listing.seller).transfer(listing.price);

        // Transfer ownership of the NFT to the buyer
        _transfer(listing.seller, msg.sender, tokenId);

        // Mark the NFT as no longer listed
        listings[tokenId].isListed = false;

        emit NFTPurchased(tokenId, msg.sender, listing.price);
    }

    /**
     * @dev Withdraw funds from the contract (if applicable).
     * Only the owner can call this function.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    receive() external payable {
        // Accept Ether transfers
    }
}
```
