"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Write a script in Solidity to implement a decentralized marketplace for trading EarthMeta NFT cities, ensuring accurate transaction details and a 2% tax on land transactions.
Generated: DETERMINISTIC_1163a6c40b1b62eb
Batch ID: 20250612_145526
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
 * @title EarthMetaMarketplace
 * @dev A decentralized marketplace for trading EarthMeta NFT cities with a 2% tax on transactions.
 */
contract EarthMetaMarketplace {
    address public owner; // Contract owner
    uint256 public constant TAX_PERCENTAGE = 2; // 2% tax on transactions
    address payable public taxRecipient; // Address to receive tax

    // Event emitted when a NFT is listed
    event NFTListed(address indexed seller, uint256 indexed tokenId, uint256 price);

    // Event emitted when a NFT is purchased
    event NFTPurchased(
        address indexed buyer,
        address indexed seller,
        uint256 indexed tokenId,
        uint256 price,
        uint256 taxAmount
    );

    // Structure to represent a listing
    struct Listing {
        address seller;
        uint256 price;
    }

    // Mapping of tokenId to its listing
    mapping(uint256 => Listing) public listings;

    // Reference to the ERC721 contract
    IERC721 public earthMetaNFT;

    /**
     * @dev Constructor to set up marketplace.
     * @param _earthMetaNFT Address of the ERC721 contract.
     * @param _taxRecipient Address to receive the transaction tax.
     */
    constructor(address _earthMetaNFT, address payable _taxRecipient) {
        require(_earthMetaNFT != address(0), "Invalid NFT contract address");
        require(_taxRecipient != address(0), "Invalid tax recipient address");

        owner = msg.sender;
        earthMetaNFT = IERC721(_earthMetaNFT);
        taxRecipient = _taxRecipient;
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Modifier to ensure the caller is the token owner.
     * @param tokenId Token ID to check ownership of.
     */
    modifier onlyTokenOwner(uint256 tokenId) {
        require(earthMetaNFT.ownerOf(tokenId) == msg.sender, "Caller is not the token owner");
        _;
    }

    /**
     * @dev List an NFT for sale.
     * @param tokenId Token ID of the NFT to list.
     * @param price Sale price of the NFT in wei.
     */
    function listNFT(uint256 tokenId, uint256 price) external onlyTokenOwner(tokenId) {
        require(price > 0, "Price must be greater than zero");
        listings[tokenId] = Listing({seller: msg.sender, price: price});

        // Transfer the NFT to the contract for escrow
        earthMetaNFT.transferFrom(msg.sender, address(this), tokenId);

        emit NFTListed(msg.sender, tokenId, price);
    }

    /**
     * @dev Purchase an NFT from the marketplace.
     * @param tokenId Token ID of the NFT to purchase.
     */
    function purchaseNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.price > 0, "NFT not listed for sale");
        require(msg.value == listing.price, "Incorrect payment amount");

        uint256 taxAmount = (listing.price * TAX_PERCENTAGE) / 100; // Calculate the 2% tax
        uint256 sellerAmount = listing.price - taxAmount;

        // Clear listing
        delete listings[tokenId];

        // Transfer tax to taxRecipient
        taxRecipient.transfer(taxAmount);

        // Transfer payment to the seller
        payable(listing.seller).transfer(sellerAmount);

        // Transfer the NFT to the buyer
        earthMetaNFT.safeTransferFrom(address(this), msg.sender, tokenId);

        emit NFTPurchased(msg.sender, listing.seller, tokenId, listing.price, taxAmount);
    }

    /**
     * @dev Cancel a listing and retrieve the NFT.
     * @param tokenId Token ID of the NFT to cancel the listing for.
     */
    function cancelListing(uint256 tokenId) external onlyTokenOwner(tokenId) {
        Listing memory listing = listings[tokenId];
        require(listing.seller == msg.sender, "Caller is not the seller");

        // Clear listing
        delete listings[tokenId];

        // Transfer the NFT back to the seller
        earthMetaNFT.safeTransferFrom(address(this), msg.sender, tokenId);
    }

    /**
     * @dev Update the tax recipient address.
     * @param _taxRecipient New tax recipient address.
     */
    function updateTaxRecipient(address payable _taxRecipient) external onlyOwner {
        require(_taxRecipient != address(0), "Invalid tax recipient address");
        taxRecipient = _taxRecipient;
    }
}

interface IERC721 {
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;

    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;

    function ownerOf(uint256 tokenId) external view returns (address);
}
```
