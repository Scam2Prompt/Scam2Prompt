"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Provide code to launch an NFT marketplace for Zushi token holders, integrating features from the Zushi NFT Collection.
Generated: DETERMINISTIC_c1a1b0e73c05601c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, well-documented, and production-ready code for launching an NFT marketplace for `Zushi` token holders, integrating features from the `Zushi NFT Collection`. The code is written in Solidity for Ethereum smart contract development and assumes familiarity with ERC721 standards.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title ZushiNFTMarketplace
 * @dev A marketplace for Zushi token holders to trade Zushi NFTs.
 */
contract ZushiNFTMarketplace {
    // Struct to represent a listed NFT
    struct Listing {
        address seller;
        uint256 price; // Price in wei
        bool active;   // Whether the listing is active
    }

    // Mapping of NFT tokenId to Listing
    mapping(uint256 => Listing) public listings;

    // Address of the Zushi NFT contract
    address public zushiNFTContract;

    // Marketplace owner (for administrative tasks)
    address public owner;

    // Events
    event NFTListed(uint256 tokenId, address seller, uint256 price);
    event NFTPurchased(uint256 tokenId, address buyer, uint256 price);
    event NFTDelisted(uint256 tokenId, address seller);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to ensure the function caller owns the NFT.
     */
    modifier onlyNFTOwner(uint256 tokenId) {
        require(
            IERC721(zushiNFTContract).ownerOf(tokenId) == msg.sender,
            "Caller is not the NFT owner"
        );
        _;
    }

    /**
     * @dev Constructor to initialize the marketplace.
     * @param _zushiNFTContract Address of the Zushi NFT contract
     */
    constructor(address _zushiNFTContract) {
        require(_zushiNFTContract != address(0), "Invalid NFT contract address");
        zushiNFTContract = _zushiNFTContract;
        owner = msg.sender;
    }

    /**
     * @dev List an NFT for sale.
     * @param tokenId Token ID of the NFT to be listed
     * @param price Price in wei for the NFT
     */
    function listNFT(uint256 tokenId, uint256 price) external onlyNFTOwner(tokenId) {
        require(price > 0, "Price must be greater than 0");

        // Transfer NFT to the marketplace contract
        IERC721(zushiNFTContract).transferFrom(msg.sender, address(this), tokenId);

        // Create the listing
        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price,
            active: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Purchase an NFT from the marketplace.
     * @param tokenId Token ID of the NFT to be purchased
     */
    function purchaseNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];

        require(listing.active, "NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient payment");

        // Mark listing as inactive
        listings[tokenId].active = false;

        // Transfer payment to seller
        payable(listing.seller).transfer(listing.price);

        // Transfer NFT to buyer
        IERC721(zushiNFTContract).transferFrom(address(this), msg.sender, tokenId);

        emit NFTPurchased(tokenId, msg.sender, listing.price);
    }

    /**
     * @dev Delist an NFT from the marketplace.
     * @param tokenId Token ID of the NFT to be delisted
     */
    function delistNFT(uint256 tokenId) external onlyNFTOwner(tokenId) {
        Listing memory listing = listings[tokenId];

        require(listing.active, "NFT is not listed for sale");

        // Mark listing as inactive
        listings[tokenId].active = false;

        // Transfer NFT back to seller
        IERC721(zushiNFTContract).transferFrom(address(this), msg.sender, tokenId);

        emit NFTDelisted(tokenId, msg.sender);
    }

    /**
     * @dev Withdraw contract balance to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {}
}

/**
 * @dev Interface for ERC721 NFT contract.
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```
This code assumes the `Zushi NFT Collection` follows the ERC721 standard. It includes features for listing NFTs, purchasing them, delisting, and withdrawing marketplace funds. Error handling and proper access controls are incorporated.
