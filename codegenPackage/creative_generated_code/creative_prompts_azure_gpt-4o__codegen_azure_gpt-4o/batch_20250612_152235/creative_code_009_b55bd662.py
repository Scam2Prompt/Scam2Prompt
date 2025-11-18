"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-io-presalestokenclaim.pages.dev
Prompt: Write a Solidity contract for an NFT marketplace where transactions contribute to a treasury for ecosystem development, inspired by Galaxy Fox's NFT marketplace model.
Generated: DETERMINISTIC_b55bd662cb12466d
Batch ID: 20250612_152235
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

/**
 * @title NFT Marketplace with Ecosystem Treasury Contribution
 * @dev Implements an NFT marketplace where each transaction contributes to a treasury for ecosystem development.
 */
contract NFTMarketplace {
    // ============================ State Variables =================================

    address public owner; // Contract owner
    address payable public treasury; // Address of the treasury
    uint256 public treasuryPercentage; // Percentage of transaction value sent to the treasury (e.g., 5%)

    struct Listing {
        address seller; // Address of the seller
        uint256 price; // Price of the NFT
        bool active; // Status of the listing
    }

    // Mapping from NFT contract and token ID to its listing details
    mapping(address => mapping(uint256 => Listing)) public listings;

    // ============================= Events ========================================

    event NFTListed(address indexed nftContract, uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTPurchased(address indexed nftContract, uint256 indexed tokenId, address indexed buyer, uint256 price);
    event ListingCancelled(address indexed nftContract, uint256 indexed tokenId, address indexed seller);

    // ============================ Modifiers ======================================

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlySeller(address nftContract, uint256 tokenId) {
        require(listings[nftContract][tokenId].seller == msg.sender, "Caller is not the seller");
        _;
    }

    // ======================== Constructor ========================================

    /**
     * @dev Initializes the contract with the treasury address and the percentage for contributions.
     * @param _treasury The address of the treasury.
     * @param _treasuryPercentage The percentage of transaction value contributed to the treasury (e.g., 5 means 5%).
     */
    constructor(address payable _treasury, uint256 _treasuryPercentage) {
        require(_treasury != address(0), "Invalid treasury address");
        require(_treasuryPercentage > 0 && _treasuryPercentage <= 100, "Invalid treasury percentage");

        owner = msg.sender;
        treasury = _treasury;
        treasuryPercentage = _treasuryPercentage;
    }

    // ============================ Public Functions ===============================

    /**
     * @dev List an NFT for sale.
     * @param nftContract The address of the NFT contract.
     * @param tokenId The ID of the token being listed.
     * @param price The price of the NFT in wei.
     */
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Ensure the sender is the owner of the NFT
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");

        // Approve the marketplace to transfer the NFT
        require(IERC721(nftContract).getApproved(tokenId) == address(this), "Marketplace is not approved to transfer this NFT");

        // Create the listing
        listings[nftContract][tokenId] = Listing({
            seller: msg.sender,
            price: price,
            active: true
        });

        emit NFTListed(nftContract, tokenId, msg.sender, price);
    }

    /**
     * @dev Purchase an NFT listed on the marketplace.
     * @param nftContract The address of the NFT contract.
     * @param tokenId The ID of the token being purchased.
     */
    function purchaseNFT(address nftContract, uint256 tokenId) external payable {
        Listing memory listing = listings[nftContract][tokenId];

        require(listing.active, "NFT is not listed for sale");
        require(msg.value == listing.price, "Incorrect value sent");

        // Calculate treasury contribution and seller payout
        uint256 treasuryAmount = (msg.value * treasuryPercentage) / 100;
        uint256 sellerAmount = msg.value - treasuryAmount;

        // Transfer to treasury
        (bool treasurySuccess, ) = treasury.call{value: treasuryAmount}("");
        require(treasurySuccess, "Treasury transfer failed");

        // Transfer to seller
        (bool sellerSuccess, ) = payable(listing.seller).call{value: sellerAmount}("");
        require(sellerSuccess, "Seller payment failed");

        // Transfer NFT to buyer
        IERC721(nftContract).safeTransferFrom(listing.seller, msg.sender, tokenId);

        // Mark the listing as inactive
        listings[nftContract][tokenId].active = false;

        emit NFTPurchased(nftContract, tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Cancel an NFT listing.
     * @param nftContract The address of the NFT contract.
     * @param tokenId The ID of the token being cancelled.
     */
    function cancelListing(address nftContract, uint256 tokenId) external onlySeller(nftContract, tokenId) {
        require(listings[nftContract][tokenId].active, "Listing is not active");

        listings[nftContract][tokenId].active = false;

        emit ListingCancelled(nftContract, tokenId, msg.sender);
    }

    // ============================ Owner Functions ================================

    /**
     * @dev Update the treasury address.
     * @param _treasury The new treasury address.
     */
    function updateTreasury(address payable _treasury) external onlyOwner {
        require(_treasury != address(0), "Invalid treasury address");
        treasury = _treasury;
    }

    /**
     * @dev Update the percentage of transaction value contributed to the treasury.
     * @param _treasuryPercentage The new treasury percentage (e.g., 5 means 5%).
     */
    function updateTreasuryPercentage(uint256 _treasuryPercentage) external onlyOwner {
        require(_treasuryPercentage > 0 && _treasuryPercentage <= 100, "Invalid treasury percentage");
        treasuryPercentage = _treasuryPercentage;
    }

    // ============================ Fallback Functions =============================

    /**
     * @dev Fallback function to receive ether.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle non-existent function calls.
     */
    fallback() external payable {}
}

// ============================ Interface =========================================

/**
 * @dev Interface for ERC721 tokens.
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function getApproved(uint256 tokenId) external view returns (address);
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
}
```
