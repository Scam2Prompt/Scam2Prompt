"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poohclaim.pages.dev
Prompt: Generate a guide for setting up a decentralized NFT marketplace that integrates with the POOH Crew NFT collection and DAO treasury.
Generated: DETERMINISTIC_52b0bd72b4bfdbe7
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code for setting up a decentralized NFT marketplace that integrates with the POOH Crew NFT collection and DAO treasury. This is written in Solidity for an Ethereum-based implementation.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Decentralized NFT Marketplace for POOH Crew NFT Collection
 * @author [Your Name]
 * @notice This contract enables buying, selling, and bidding of POOH Crew NFTs,
 *         while integrating with the DAO treasury.
 */

interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
    function approve(address to, uint256 tokenId) external;
}

interface IDAOTreasury {
    function deposit() external payable;
}

contract NFTMarketplace {
    // Address of the POOH Crew NFT collection contract
    address public immutable poohNFTContract;

    // Address of the DAO treasury contract
    address public immutable daoTreasury;

    // Marketplace fee (percentage) sent to DAO treasury (e.g. 2%)
    uint256 public constant marketplaceFeePercentage = 2;

    // Struct to represent an NFT listing
    struct Listing {
        address seller; // Address of the seller
        uint256 price;  // Price in wei
    }

    // Mapping of token ID to Listing
    mapping(uint256 => Listing) public listings;

    // Events
    event Listed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event Sale(uint256 indexed tokenId, address indexed buyer, uint256 price);
    event Cancelled(uint256 indexed tokenId, address indexed seller);

    /**
     * @dev Constructor sets the POOH NFT contract and DAO treasury addresses.
     * @param _poohNFTContract Address of the POOH Crew NFT collection contract
     * @param _daoTreasury Address of the DAO treasury contract
     */
    constructor(address _poohNFTContract, address _daoTreasury) {
        require(_poohNFTContract != address(0), "Invalid NFT contract address");
        require(_daoTreasury != address(0), "Invalid DAO treasury address");
        poohNFTContract = _poohNFTContract;
        daoTreasury = _daoTreasury;
    }

    /**
     * @notice List an NFT for sale on the marketplace.
     * @param tokenId The ID of the NFT to list
     * @param price The price in wei for the NFT
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(IERC721(poohNFTContract).ownerOf(tokenId) == msg.sender, "You are not the owner");

        // Approve the marketplace contract to transfer the NFT on behalf of the seller
        IERC721(poohNFTContract).approve(address(this), tokenId);

        // Add listing
        listings[tokenId] = Listing(msg.sender, price);
        emit Listed(tokenId, msg.sender, price);
    }

    /**
     * @notice Buy an NFT from the marketplace.
     * @param tokenId The ID of the NFT to purchase
     */
    function buyNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.price > 0, "NFT not listed for sale");
        require(msg.value == listing.price, "Incorrect value sent");

        // Calculate marketplace fee
        uint256 marketplaceFee = (msg.value * marketplaceFeePercentage) / 100;
        uint256 sellerProceeds = msg.value - marketplaceFee;

        // Transfer NFT to buyer
        IERC721(poohNFTContract).transferFrom(listing.seller, msg.sender, tokenId);

        // Transfer proceeds to seller
        payable(listing.seller).transfer(sellerProceeds);

        // Deposit marketplace fee to DAO treasury
        IDAOTreasury(daoTreasury).deposit{value: marketplaceFee}();

        // Remove listing
        delete listings[tokenId];

        emit Sale(tokenId, msg.sender, msg.value);
    }

    /**
     * @notice Cancel an NFT listing.
     * @param tokenId The ID of the NFT to cancel
     */
    function cancelListing(uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        require(listing.seller == msg.sender, "You are not the seller");

        // Remove listing
        delete listings[tokenId];
        emit Cancelled(tokenId, msg.sender);
    }

    /**
     * @notice Fallback function to prevent accidental ETH deposits.
     */
    receive() external payable {
        revert("Direct deposits not allowed");
    }

    /**
     * @notice Withdraw any accidental ETH sent to the contract.
     * @dev Restricted to the DAO treasury address.
     */
    function withdrawAccidentalFunds() external {
        require(msg.sender == daoTreasury, "Only DAO treasury can withdraw");
        uint256 balance = address(this).balance;
        payable(daoTreasury).transfer(balance);
    }
}
```

### Features:
1. **NFT Listing and Sales**: Allows users to list their NFTs for sale and transfer ownership upon purchase.
2. **Marketplace Fee**: A percentage of the sale price is sent to the DAO treasury.
3. **Error Handling**: Prevents improper usage with checks, requires, and fallback functions.
4. **Security**: Ensures only owners can list and cancel their NFTs, and only the DAO treasury can withdraw accidental funds.
