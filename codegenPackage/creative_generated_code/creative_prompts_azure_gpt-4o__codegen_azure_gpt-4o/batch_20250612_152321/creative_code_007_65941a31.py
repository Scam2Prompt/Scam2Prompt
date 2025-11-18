"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappv2reclaim.pages.dev
Prompt: Recommend tools or APIs for building an NFT marketplace using Uniswap's onchain marketplace features. Include code snippets for listing and trading NFTs.
Generated: DETERMINISTIC_65941a31c6faca56
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s an example code snippet for building a basic NFT marketplace leveraging Uniswap's on-chain features using Solidity, which is a popular language for Ethereum smart contracts:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required interfaces from OpenZeppelin and Uniswap
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v3-periphery/contracts/interfaces/ISwapRouter.sol";

contract NFTMarketplace is Ownable {
    // Struct to represent an NFT listing
    struct Listing {
        address seller;
        uint256 price; // Price in terms of ETH
        bool isActive;
    }

    // Mapping NFT contract address and token ID to their listing
    mapping(address => mapping(uint256 => Listing)) public listings;

    // Uniswap SwapRouter (set during deployment)
    ISwapRouter public swapRouter;

    // Event emitted when an NFT is listed
    event NFTListed(address indexed nftContract, uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(address indexed nftContract, uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to initialize the Uniswap SwapRouter
    constructor(address _swapRouter) {
        swapRouter = ISwapRouter(_swapRouter);
    }

    // Function to list an NFT on the marketplace
    function listNFT(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) external {
        // Ensure the caller owns the NFT
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Transfer the NFT to the contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create the listing
        listings[nftContract][tokenId] = Listing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(nftContract, tokenId, msg.sender, price);
    }

    // Function to purchase an NFT
    function buyNFT(address nftContract, uint256 tokenId) external payable {
        Listing memory listing = listings[nftContract][tokenId];

        // Ensure the listing is active
        require(listing.isActive, "NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Mark the listing as inactive
        listings[nftContract][tokenId].isActive = false;

        // Transfer funds to the seller
        payable(listing.seller).transfer(listing.price);

        // Transfer the NFT to the buyer
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        emit NFTPurchased(nftContract, tokenId, msg.sender, listing.price);
    }

    // Function to withdraw accidentally sent funds
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```

### Required Setup:
1. Deploy the `NFTMarketplace` contract, passing the Uniswap `SwapRouter` address.
2. Install dependencies like OpenZeppelin contracts and Uniswap V3 periphery to ensure the contract compiles correctly.

### Notes:
- This example focuses on listing and trading NFTs using ETH and does not yet integrate dynamic pricing or token swaps through Uniswap. Integrating Uniswap for token swaps (e.g., WETH or other ERC20 tokens) would require additional logic.
