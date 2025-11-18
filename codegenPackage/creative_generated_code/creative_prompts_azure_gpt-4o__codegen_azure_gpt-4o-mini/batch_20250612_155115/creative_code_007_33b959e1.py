"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless.firstmate.xyz
Prompt: Develop a smart contract template for trading Bankless NFTs on a decentralized marketplace, ensuring compatibility with items listed on the Bankless platform.
Generated: DETERMINISTIC_33b959e1655eaf10
Batch ID: 20250612_155115
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

// Interface for the ERC721 standard (Non-Fungible Tokens)
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
    function approve(address to, uint256 tokenId) external;
}

// Contract for trading Bankless NFTs on a decentralized marketplace
contract BanklessNFTMarketplace {
    // Structure to store an item listing
    struct Listing {
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to its listing
    mapping(uint256 => Listing) public listings;

    // Event emitted when an NFT is listed
    event Listed(uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an NFT is purchased
    event Purchased(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    // Event emitted when a listing is canceled
    event Canceled(uint256 indexed tokenId, address indexed seller);

    // Address of the Bankless NFT contract
    IERC721 public banklessNFTContract;

    // Constructor to set the NFT contract address
    constructor(address _nftContractAddress) {
        banklessNFTContract = IERC721(_nftContractAddress);
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(banklessNFTContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Approve the marketplace contract to transfer the NFT
        banklessNFTContract.approve(address(this), tokenId);

        // Create the listing
        listings[tokenId] = Listing(msg.sender, price, true);
        emit Listed(tokenId, msg.sender, price);
    }

    // Function to purchase a listed NFT
    function purchaseNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "This NFT is not for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Transfer the NFT from seller to buyer
        banklessNFTContract.transferFrom(listing.seller, msg.sender, tokenId);

        // Mark the listing as inactive
        listings[tokenId].isActive = false;

        // Transfer funds to the seller
        payable(listing.seller).transfer(listing.price);

        emit Purchased(tokenId, msg.sender, listing.seller, listing.price);
    }

    // Function to cancel a listing
    function cancelListing(uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        require(listing.seller == msg.sender, "You do not own this listing");
        require(listing.isActive, "This NFT is not listed for sale");

        // Mark the listing as inactive
        listings[tokenId].isActive = false;

        emit Canceled(tokenId, msg.sender);
    }

    // Function to withdraw ETH from the contract (for future enhancements)
    function withdraw() external {
        // This function can be used for fee withdrawal or other purposes in the future
        // Implementation to be added later
    }
}
```
