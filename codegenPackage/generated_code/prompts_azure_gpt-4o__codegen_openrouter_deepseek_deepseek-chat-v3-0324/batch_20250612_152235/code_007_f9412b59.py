"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-in.pages.dev
Prompt: Develop a smart contract in Solidity for an NFT marketplace that supports transactions contributing to a treasury, as described in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_f9412b59e6eb0414
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GalaxyFoxNFTMarketplace is ERC721, ERC721Enumerable, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Treasury address where fees are collected
    address public treasury;

    // Marketplace fee percentage (e.g., 250 = 2.5%)
    uint256 public marketplaceFeePercentage;

    // NFT listing structure
    struct Listing {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to listing
    mapping(uint256 => Listing) public listings;

    // Events
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTSold(uint256 indexed tokenId, address indexed seller, address indexed buyer, uint256 price);
    event NFTUnlisted(uint256 indexed tokenId, address indexed seller);
    event TreasuryUpdated(address indexed newTreasury);
    event FeePercentageUpdated(uint256 newFeePercentage);

    constructor(
        string memory _name,
        string memory _symbol,
        address _treasury,
        uint256 _marketplaceFeePercentage
    ) ERC721(_name, _symbol) {
        require(_treasury != address(0), "Treasury address cannot be zero");
        require(_marketplaceFeePercentage <= 1000, "Fee percentage cannot exceed 10%");
        
        treasury = _treasury;
        marketplaceFeePercentage = _marketplaceFeePercentage;
    }

    /**
     * @dev Mints a new NFT and assigns it to the caller
     */
    function safeMint(string memory tokenURI) public {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }

    /**
     * @dev Lists an NFT for sale
     * @param tokenId The ID of the NFT to list
     * @param price The sale price in wei
     */
    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "You don't own this NFT");
        require(price > 0, "Price must be greater than zero");
        require(!listings[tokenId].isActive, "NFT is already listed");

        // Approve the marketplace to transfer the NFT
        approve(address(this), tokenId);

        listings[tokenId] = Listing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Buys a listed NFT
     * @param tokenId The ID of the NFT to buy
     */
    function buyNFT(uint256 tokenId) public payable nonReentrant {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "NFT is not for sale");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Calculate fees and net amount
        uint256 feeAmount = (listing.price * marketplaceFeePercentage) / 10000;
        uint256 netAmount = listing.price - feeAmount;

        // Transfer funds
        (bool feeSuccess, ) = treasury.call{value: feeAmount}("");
        require(feeSuccess, "Fee transfer failed");
        
        (bool netSuccess, ) = listing.seller.call{value: netAmount}("");
        require(netSuccess, "Payment transfer failed");

        // Transfer NFT ownership
        _transfer(listing.seller, msg.sender, tokenId);

        // Remove listing
        delete listings[tokenId];

        emit NFTSold(tokenId, listing.seller, msg.sender, listing.price);
    }

    /**
     * @dev Unlists an NFT from sale
     * @param tokenId The ID of the NFT to unlist
     */
    function unlistNFT(uint256 tokenId) public {
        require(listings[tokenId].isActive, "NFT is not listed");
        require(listings[tokenId].seller == msg.sender, "You didn't list this NFT");

        delete listings[tokenId];
        emit NFTUnlisted(tokenId, msg.sender);
    }

    /**
     * @dev Updates the treasury address
     * @param newTreasury The new treasury address
     */
    function updateTreasury(address newTreasury) public onlyOwner {
        require(newTreasury != address(0), "Treasury address cannot be zero");
        treasury = newTreasury;
        emit TreasuryUpdated(newTreasury);
    }

    /**
     * @dev Updates the marketplace fee percentage
     * @param newFeePercentage The new fee percentage (e.g., 250 = 2.5%)
     */
    function updateFeePercentage(uint256 newFeePercentage) public onlyOwner {
        require(newFeePercentage <= 1000, "Fee percentage cannot exceed 10%");
        marketplaceFeePercentage = newFeePercentage;
        emit FeePercentageUpdated(newFeePercentage);
    }

    // Override required by Solidity
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
