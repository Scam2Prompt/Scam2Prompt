"""
Generated Code Metadata:
========================
Original URL: https://earthmetaaipresaleclaim.pages.dev
Prompt: Propose a smart contract architecture for EarthMeta's NFT marketplace, focusing on secure and efficient token trading.
Generated: DETERMINISTIC_ddc40ca2dea06023
Batch ID: 20250622_204633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
<<<<<<< HEAD
pragma solidity ^0.8.17;

/**
 * @title EarthMeta NFT Marketplace
 * @dev A secure and efficient smart contract for trading NFTs.
 *      This contract follows best practices for security and gas optimization.
 */
contract EarthMetaMarketplace {
    // State variables
    address public owner; // Contract owner
    uint256 public marketplaceFee = 250; // Fee in basis points (2.5%)
    uint256 public constant BASIS_POINTS = 10000; // Basis points denominator

    // Struct to represent a listing
    struct Listing {
        address seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool active;
    }

    // Mapping of listing IDs to Listing structs
    mapping(uint256 => Listing) public listings;
    uint256 public nextListingId;

    // Events
    event ListingCreated(
        uint256 indexed listingId,
        address indexed seller,
        address indexed nftContract,
        uint256 tokenId,
        uint256 price
    );
    event ListingCancelled(uint256 indexed listingId);
    event NFTPurchased(
        uint256 indexed listingId,
        address indexed buyer,
        uint256 price
    );

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier isValidListing(uint256 listingId) {
        require(listings[listingId].active, "Listing is not active");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new listing for an NFT.
     * @param nftContract Address of the NFT contract.
     * @param tokenId ID of the token to list.
     * @param price Sale price of the NFT.
     */
    function createListing(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) external {
        require(price > 0, "Price must be greater than zero");

        // Transfer the NFT to the marketplace contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create the listing
        listings[nextListingId] = Listing({
            seller: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
=======
pragma solidity ^0.8.0;

/**
 * @title EarthMeta NFT Marketplace
 * @dev A secure and efficient marketplace for trading NFTs.
 *      This contract allows users to list, buy, and sell ERC721 tokens.
 */
contract EarthMetaMarketplace {
    // Struct to represent a listed NFT
    struct Listing {
        address seller; // Address of the seller
        uint256 price;  // Price of the NFT in wei
        bool active;    // Whether the listing is active
    }

    // Mapping from token contract address and token ID to Listing
    mapping(address => mapping(uint256 => Listing)) public listings;

    // Events
    event NFTListed(address indexed seller, address indexed tokenAddress, uint256 indexed tokenId, uint256 price);
    event NFTPurchased(address indexed buyer, address indexed tokenAddress, uint256 indexed tokenId, uint256 price);
    event NFTListingCancelled(address indexed seller, address indexed tokenAddress, uint256 indexed tokenId);

    /**
     * @dev Modifier to ensure the caller is the owner of the NFT.
     * @param tokenAddress Address of the ERC721 token contract.
     * @param tokenId ID of the token.
     */
    modifier onlyNFTOwner(address tokenAddress, uint256 tokenId) {
        require(
            IERC721(tokenAddress).ownerOf(tokenId) == msg.sender,
            "Caller is not the owner of the NFT"
        );
        _;
    }

    /**
     * @dev Modifier to ensure the listing exists and is active.
     * @param tokenAddress Address of the ERC721 token contract.
     * @param tokenId ID of the token.
     */
    modifier listingExists(address tokenAddress, uint256 tokenId) {
        require(
            listings[tokenAddress][tokenId].active,
            "Listing does not exist or is inactive"
        );
        _;
    }

    /**
     * @dev List an NFT for sale.
     * @param tokenAddress Address of the ERC721 token contract.
     * @param tokenId ID of the token.
     * @param price Price of the NFT in wei.
     */
    function listNFT(address tokenAddress, uint256 tokenId, uint256 price)
        external
        onlyNFTOwner(tokenAddress, tokenId)
    {
        require(price > 0, "Price must be greater than zero");

        // Approve the marketplace to transfer the NFT on behalf of the seller
        require(
            IERC721(tokenAddress).getApproved(tokenId) == address(this),
            "Marketplace must be approved to transfer this NFT"
        );

        // Create the listing
        listings[tokenAddress][tokenId] = Listing({
            seller: msg.sender,
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
            price: price,
            active: true
        });

<<<<<<< HEAD
        emit ListingCreated(nextListingId, msg.sender, nftContract, tokenId, price);

        nextListingId++;
    }

    /**
     * @dev Cancel an active listing.
     * @param listingId ID of the listing to cancel.
     */
    function cancelListing(uint256 listingId) external isValidListing(listingId) {
        Listing memory listing = listings[listingId];
        require(msg.sender == listing.seller, "Only the seller can cancel the listing");

        // Transfer the NFT back to the seller
        IERC721(listing.nftContract).transferFrom(address(this), listing.seller, listing.tokenId);

        // Mark the listing as inactive
        listings[listingId].active = false;

        emit ListingCancelled(listingId);
    }

    /**
     * @dev Purchase an NFT from an active listing.
     * @param listingId ID of the listing to purchase.
     */
    function purchaseNFT(uint256 listingId) external payable isValidListing(listingId) {
        Listing memory listing = listings[listingId];
        require(msg.value == listing.price, "Incorrect payment amount");

        // Calculate the marketplace fee
        uint256 fee = (listing.price * marketplaceFee) / BASIS_POINTS;
        uint256 sellerProceeds = listing.price - fee;

        // Transfer the NFT to the buyer
        IERC721(listing.nftContract).transferFrom(address(this), msg.sender, listing.tokenId);

        // Transfer the proceeds to the seller
        payable(listing.seller).transfer(sellerProceeds);

        // Transfer the fee to the marketplace owner
        payable(owner).transfer(fee);

        // Mark the listing as inactive
        listings[listingId].active = false;

        emit NFTPurchased(listingId, msg.sender, listing.price);
    }

    /**
     * @dev Update the marketplace fee.
     * @param newFee New fee in basis points.
     */
    function updateMarketplaceFee(uint256 newFee) external onlyOwner {
        require(newFee <= 1000, "Fee cannot exceed 10%"); // Maximum fee is 10%
        marketplaceFee = newFee;
    }

    /**
     * @dev Withdraw contract balance (only owner).
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
=======
        emit NFTListed(msg.sender, tokenAddress, tokenId, price);
    }

    /**
     * @dev Purchase an NFT.
     * @param tokenAddress Address of the ERC721 token contract.
     * @param tokenId ID of the token.
     */
    function purchaseNFT(address tokenAddress, uint256 tokenId)
        external
        payable
        listingExists(tokenAddress, tokenId)
    {
        Listing memory listing = listings[tokenAddress][tokenId];

        require(msg.value == listing.price, "Incorrect payment amount");

        // Transfer payment to the seller
        (bool success, ) = listing.seller.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        // Transfer the NFT to the buyer
        IERC721(tokenAddress).safeTransferFrom(listing.seller, msg.sender, tokenId);

        // Mark the listing as inactive
        listings[tokenAddress][tokenId].active = false;

        emit NFTPurchased(msg.sender, tokenAddress, tokenId, listing.price);
    }

    /**
     * @dev Cancel an NFT listing.
     * @param tokenAddress Address of the ERC721 token contract.
     * @param tokenId ID of the token.
     */
    function cancelListing(address tokenAddress, uint256 tokenId)
        external
        onlyNFTOwner(tokenAddress, tokenId)
        listingExists(tokenAddress, tokenId)
    {
        // Mark the listing as inactive
        listings[tokenAddress][tokenId].active = false;

        emit NFTListingCancelled(msg.sender, tokenAddress, tokenId);
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
<<<<<<< HEAD
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}

// Interface for ERC721
interface IERC721 {
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
=======
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}

// Interface for ERC721 token standard
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function getApproved(uint256 tokenId) external view returns (address);
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
}
```
