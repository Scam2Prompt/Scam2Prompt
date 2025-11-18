"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-tensorian.pages.dev
Prompt: Develop a smart contract function in Solidity to enable users to trade Tensorians collectibles securely on the Ethereum blockchain.
Generated: DETERMINISTIC_1b128e1add64a9bf
Batch ID: 20250612_153246
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

// Import the ERC721 interface for NFTs
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TensoriansMarketplace
 * @dev A smart contract for securely trading Tensorians collectibles on the Ethereum blockchain.
 */
contract TensoriansMarketplace is Ownable, ERC721Holder {
    // Event to log trades
    event Trade(address indexed seller, address indexed buyer, uint256 tokenId, uint256 price);

    // Structure to store listing details
    struct Listing {
        address seller;
        uint256 price;
        bool isSold;
    }

    // Mapping from token ID to Listing details
    mapping(uint256 => Listing) public listings;

    // Reference to the Tensorians NFT contract
    IERC721 public tensoriansNFT;

    /**
     * @dev Constructor to set the NFT contract address.
     * @param _tensoriansNFT Address of the ERC721 Tensorians contract.
     */
    constructor(address _tensoriansNFT) {
        require(_tensoriansNFT != address(0), "Invalid NFT address");
        tensoriansNFT = IERC721(_tensoriansNFT);
    }

    /**
     * @dev Allows a user to list their Tensorians collectible for sale.
     * @param tokenId The ID of the token to be listed.
     * @param price The price for which the token is listed.
     */
    function listToken(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(tensoriansNFT.ownerOf(tokenId) == msg.sender, "Caller is not the token owner");
        require(!listings[tokenId].isSold, "Token already sold");

        // Transfer the token to the contract for holding during the sale
        tensoriansNFT.safeTransferFrom(msg.sender, address(this), tokenId);

        // Create a new listing
        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price,
            isSold: false
        });
    }

    /**
     * @dev Allows a user to purchase a listed Tensorians collectible.
     * @param tokenId The ID of the token to purchase.
     */
    function purchaseToken(uint256 tokenId) external payable {
        Listing storage listing = listings[tokenId];
        require(!listing.isSold, "Token already sold");
        require(msg.value == listing.price, "Incorrect ETH amount sent");

        // Mark the token as sold
        listing.isSold = true;

        // Transfer the payment to the seller
        payable(listing.seller).transfer(msg.value);

        // Transfer the token to the buyer
        tensoriansNFT.safeTransferFrom(address(this), msg.sender, tokenId);

        // Emit a trade event
        emit Trade(listing.seller, msg.sender, tokenId, listing.price);
    }

    /**
     * @dev Allows the owner to withdraw the contract's balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Allows the seller to cancel their listing.
     * @param tokenId The ID of the token to cancel the listing for.
     */
    function cancelListing(uint256 tokenId) external {
        Listing storage listing = listings[tokenId];
        require(listing.seller == msg.sender, "Caller is not the seller");
        require(!listing.isSold, "Token already sold");

        // Transfer the token back to the seller
        tensoriansNFT.safeTransferFrom(address(this), msg.sender, tokenId);

        // Delete the listing
        delete listings[tokenId];
    }
}
```
