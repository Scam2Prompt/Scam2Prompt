"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-token.pages.dev
Prompt: Create a Solidity contract for an NFT marketplace where transactions contribute to a treasury, supporting token deflation and ecosystem development, as described in Galaxy Fox.
Generated: DETERMINISTIC_cd9df38924d011f2
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title GalaxyFoxNFTMarketplace
 * @dev NFT Marketplace contract with treasury contribution and token deflation support
 */
contract GalaxyFoxNFTMarketplace {
    // Struct to represent an NFT listed for sale
    struct NFTListing {
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping of NFT contract and token ID to listing details
    mapping(address => mapping(uint256 => NFTListing)) public listings;

    // Address of the treasury wallet
    address public treasury;

    // Percentage of transaction going to treasury (in basis points, i.e., 100 = 1%)
    uint256 public treasuryFeeBasisPoints;

    // Token deflation mechanism variables
    IERC20 public ecosystemToken;
    uint256 public deflationBurnPercentage;

    // Events
    event NFTListed(address indexed nftContract, uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTSold(
        address indexed nftContract,
        uint256 indexed tokenId,
        address indexed buyer,
        uint256 price,
        address seller
    );
    event NFTDelisted(address indexed nftContract, uint256 indexed tokenId, address indexed seller);

    // Modifier to restrict access to certain functions
    modifier onlySeller(address nftContract, uint256 tokenId) {
        require(listings[nftContract][tokenId].seller == msg.sender, "Only seller can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _treasury Address of the treasury wallet
     * @param _treasuryFeeBasisPoints Percentage of transaction going to treasury (in basis points)
     * @param _ecosystemToken Address of the ecosystem ERC20 token
     * @param _deflationBurnPercentage Percentage of tokens to burn per transaction
     */
    constructor(
        address _treasury,
        uint256 _treasuryFeeBasisPoints,
        IERC20 _ecosystemToken,
        uint256 _deflationBurnPercentage
    ) {
        require(_treasury != address(0), "Treasury address cannot be zero");
        require(_treasuryFeeBasisPoints <= 10000, "Treasury fee must be <= 100%");
        require(_deflationBurnPercentage <= 100, "Deflation burn percentage must be <= 100");

        treasury = _treasury;
        treasuryFeeBasisPoints = _treasuryFeeBasisPoints;
        ecosystemToken = _ecosystemToken;
        deflationBurnPercentage = _deflationBurnPercentage;
    }

    /**
     * @dev List an NFT for sale
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the token to list
     * @param price Sale price in wei
     */
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId); // Transfer NFT to the marketplace contract

        listings[nftContract][tokenId] = NFTListing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(nftContract, tokenId, msg.sender, price);
    }

    /**
     * @dev Buy an NFT from the marketplace
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the token to buy
     */
    function buyNFT(address nftContract, uint256 tokenId) external payable {
        NFTListing memory listing = listings[nftContract][tokenId];
        require(listing.isActive, "NFT is not listed for sale");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Calculate treasury contribution
        uint256 treasuryFee = (msg.value * treasuryFeeBasisPoints) / 10000;

        // Transfer funds to seller and treasury
        payable(listing.seller).transfer(msg.value - treasuryFee);
        payable(treasury).transfer(treasuryFee);

        // Transfer NFT to buyer
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        // Burn ecosystem tokens for deflation
        uint256 burnAmount = (msg.value * deflationBurnPercentage) / 100;
        ecosystemToken.burn(burnAmount);

        // Mark listing as inactive
        listings[nftContract][tokenId].isActive = false;

        emit NFTSold(nftContract, tokenId, msg.sender, listing.price, listing.seller);
    }

    /**
     * @dev Delist an NFT from the marketplace
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the token to delist
     */
    function delistNFT(address nftContract, uint256 tokenId) external onlySeller(nftContract, tokenId) {
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId); // Transfer NFT back to the seller

        listings[nftContract][tokenId].isActive = false;

        emit NFTDelisted(nftContract, tokenId, msg.sender);
    }
}

// Interface for ERC721 NFTs
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}

// Interface for ERC20 tokens with burn functionality
interface IERC20 {
    function burn(uint256 amount) external;
}
```
