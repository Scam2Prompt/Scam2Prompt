"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a smart contract to manage the Galaxy Fox NFT marketplace, allowing users to buy, sell, and trade NFTs while contributing a percentage of transactions to the treasury.
Generated: DETERMINISTIC_2cd9bbe7b7820f87
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a smart contract written in Solidity to manage the Galaxy Fox NFT marketplace:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title GalaxyFoxNFTMarketplace
 * @dev A simple NFT marketplace for buying, selling, and trading NFTs.
 * Includes a mechanism to contribute a percentage of transaction fees to the treasury.
 */
contract GalaxyFoxNFTMarketplace {
    // State variables
    address public owner; // Contract owner
    address public treasury; // Treasury address to receive fees
    uint256 public treasuryFeePercentage; // Fee percentage for treasury (e.g., 2% = 200)
    
    struct Listing {
        address seller;
        uint256 price;
    }

    // Mapping from NFT contract address and token ID to listing details
    mapping(address => mapping(uint256 => Listing)) public listings;

    // Events
    event NFTListed(address indexed nftContract, uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTSold(address indexed nftContract, uint256 indexed tokenId, address indexed buyer, uint256 price);
    event NFTDelisted(address indexed nftContract, uint256 indexed tokenId);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier isListed(address nftContract, uint256 tokenId) {
        require(listings[nftContract][tokenId].seller != address(0), "NFT is not listed");
        _;
    }

    modifier isNotListed(address nftContract, uint256 tokenId) {
        require(listings[nftContract][tokenId].seller == address(0), "NFT is already listed");
        _;
    }

    modifier isSeller(address nftContract, uint256 tokenId) {
        require(listings[nftContract][tokenId].seller == msg.sender, "You are not the seller");
        _;
    }

    // Constructor
    constructor(address _treasury, uint256 _treasuryFeePercentage) {
        require(_treasury != address(0), "Treasury address cannot be zero");
        require(_treasuryFeePercentage <= 10000, "Fee percentage cannot exceed 100%");
        
        owner = msg.sender;
        treasury = _treasury;
        treasuryFeePercentage = _treasuryFeePercentage;
    }

    // Function to list an NFT for sale
    function listNFT(address nftContract, uint256 tokenId, uint256 price)
        external
        isNotListed(nftContract, tokenId)
    {
        require(price > 0, "Price must be greater than zero");

        // Transfer the NFT to the contract to escrow it
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create listing
        listings[nftContract][tokenId] = Listing({
            seller: msg.sender,
            price: price
        });

        emit NFTListed(nftContract, tokenId, msg.sender, price);
    }

    // Function to buy a listed NFT
    function buyNFT(address nftContract, uint256 tokenId)
        external
        payable
        isListed(nftContract, tokenId)
    {
        Listing memory listing = listings[nftContract][tokenId];

        require(msg.value == listing.price, "Incorrect payment amount");

        // Calculate treasury fee
        uint256 treasuryFee = (listing.price * treasuryFeePercentage) / 10000;
        uint256 sellerAmount = listing.price - treasuryFee;

        // Transfer funds
        payable(treasury).transfer(treasuryFee);
        payable(listing.seller).transfer(sellerAmount);

        // Transfer NFT to buyer
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        // Clear listing
        delete listings[nftContract][tokenId];

        emit NFTSold(nftContract, tokenId, msg.sender, listing.price);
    }

    // Function to delist an NFT
    function delistNFT(address nftContract, uint256 tokenId)
        external
        isListed(nftContract, tokenId)
        isSeller(nftContract, tokenId)
    {
        // Transfer NFT back to seller
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        // Clear listing
        delete listings[nftContract][tokenId];

        emit NFTDelisted(nftContract, tokenId);
    }

    // Function to update treasury address
    function updateTreasury(address _treasury) external onlyOwner {
        require(_treasury != address(0), "Treasury address cannot be zero");
        treasury = _treasury;
    }

    // Function to update treasury fee percentage
    function updateTreasuryFeePercentage(uint256 _treasuryFeePercentage) external onlyOwner {
        require(_treasuryFeePercentage <= 10000, "Fee percentage cannot exceed 100%");
        treasuryFeePercentage = _treasuryFeePercentage;
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Direct ether transfers not allowed");
    }
}

// Interface for ERC721 tokens
interface IERC721 {
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
}
```

This code defines a clean and production-ready NFT marketplace smart contract. It includes error handling, supports listing, buying, and delisting NFTs, and ensures a percentage of transactions goes to the treasury.
