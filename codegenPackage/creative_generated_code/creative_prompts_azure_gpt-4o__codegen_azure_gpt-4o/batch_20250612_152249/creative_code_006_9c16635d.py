"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitamadapp.pages.dev
Prompt: Develop a smart contract in Solidity for an NFT marketplace like FANG, allowing users to create, trade, and pay for NFTs using Saitama tokens.
Generated: DETERMINISTIC_9c16635d957a0aec
Batch ID: 20250612_152249
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

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function safeMint(address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract NFTMarketplace {
    // Address of the Saitama token contract
    IERC20 public saitamaToken;

    // Address of the NFT contract
    IERC721 public nftContract;

    // Structure to represent an NFT listed for sale
    struct Listing {
        address seller;
        uint256 price; // Price in Saitama tokens
    }

    // Mapping from token ID to its listing
    mapping(uint256 => Listing) public listings;

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 tokenId, address seller, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 tokenId, address buyer, uint256 price);

    // Event emitted when an NFT listing is canceled
    event NFTListingCanceled(uint256 tokenId);

    /**
     * @dev Constructor to initialize the NFT and Saitama token contracts
     * @param _saitamaToken Address of the Saitama token contract
     * @param _nftContract Address of the NFT contract
     */
    constructor(IERC20 _saitamaToken, IERC721 _nftContract) {
        saitamaToken = _saitamaToken;
        nftContract = _nftContract;
    }

    /**
     * @dev Function to list an NFT for sale
     * @param tokenId ID of the NFT to list
     * @param price Price in Saitama tokens
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Transfer the NFT to the marketplace contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Create a new listing
        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price
        });

        // Emit the event
        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Function to purchase an NFT
     * @param tokenId ID of the NFT to purchase
     */
    function purchaseNFT(uint256 tokenId) external {
        Listing memory listing = listings[tokenId];

        require(listing.price > 0, "NFT is not listed for sale");

        // Transfer Saitama tokens from buyer to seller
        require(
            saitamaToken.transferFrom(msg.sender, listing.seller, listing.price),
            "Payment failed"
        );

        // Transfer the NFT to the buyer
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        // Remove the listing
        delete listings[tokenId];

        // Emit the event
        emit NFTPurchased(tokenId, msg.sender, listing.price);
    }

    /**
     * @dev Function to cancel an NFT listing
     * @param tokenId ID of the NFT to cancel
     */
    function cancelListing(uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        
        require(listing.seller == msg.sender, "You are not the seller");

        // Transfer the NFT back to the seller
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        // Remove the listing
        delete listings[tokenId];

        // Emit the event
        emit NFTListingCanceled(tokenId);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    receive() external payable {
        revert("Ether not accepted");
    }

    /**
     * @dev Function to withdraw accidentally sent ERC20 tokens
     * @param token Address of the ERC20 token
     * @param recipient Address to send the tokens to
     * @param amount Amount of tokens to withdraw
     */
    function withdrawERC20(IERC20 token, address recipient, uint256 amount) external {
        require(recipient != address(0), "Invalid recipient address");
        require(token.transfer(recipient, amount), "Transfer failed");
    }
}
```
