"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cosmostrader.pages.dev
Prompt: Write a code snippet that demonstrates how to use smart contracts for NFT transactions on the Ethereum blockchain as described on the Cosmos Home site.
Generated: DETERMINISTIC_f72e70125a6c4a74
Batch ID: 20250612_163338
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
 * @title NFTMarketplace
 * @dev A simple smart contract for handling NFT transactions on the Ethereum blockchain.
 *      This contract allows users to list, buy, and transfer NFTs.
 */
contract NFTMarketplace {
    // Event emitted when a new NFT is listed for sale
    event NFTListed(address indexed seller, uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(address indexed buyer, uint256 indexed tokenId, uint256 price);

    // Struct representing an NFT listing
    struct NFT {
        address seller; // Address of the seller
        uint256 price;  // Price of the NFT (in wei)
    }

    // Mapping from token ID to its corresponding NFT listing
    mapping(uint256 => NFT) public listings;

    // Address of the ERC721 contract
    address public nftContract;

    /**
     * @dev Constructor to initialize the NFT smart contract address.
     * @param _nftContract Address of the deployed ERC721 contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
    }

    /**
     * @dev Allows the owner of an NFT to list it for sale.
     * @param tokenId The ID of the token to be listed.
     * @param price The price of the NFT in wei.
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        IERC721 nft = IERC721(nftContract);
        require(nft.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(nft.isApprovedForAll(msg.sender, address(this)) || nft.getApproved(tokenId) == address(this),
                "Contract must be approved to transfer the NFT");

        // Create the listing
        listings[tokenId] = NFT(msg.sender, price);

        emit NFTListed(msg.sender, tokenId, price);
    }

    /**
     * @dev Allows a user to purchase an NFT.
     * @param tokenId The ID of the token to be purchased.
     */
    function buyNFT(uint256 tokenId) external payable {
        NFT memory nft = listings[tokenId];
        require(nft.price > 0, "NFT is not listed for sale");
        require(msg.value >= nft.price, "Insufficient payment");

        // Remove the listing
        delete listings[tokenId];

        // Transfer the NFT to the buyer
        IERC721(nftContract).safeTransferFrom(nft.seller, msg.sender, tokenId);

        // Transfer payment to the seller
        payable(nft.seller).transfer(nft.price);

        // Refund any excess payment
        if (msg.value > nft.price) {
            payable(msg.sender).transfer(msg.value - nft.price);
        }

        emit NFTPurchased(msg.sender, tokenId, nft.price);
    }

    /**
     * @dev Interface for interacting with ERC721 contracts.
     */
    interface IERC721 {
        function ownerOf(uint256 tokenId) external view returns (address);
        function approve(address to, uint256 tokenId) external;
        function getApproved(uint256 tokenId) external view returns (address);
        function isApprovedForAll(address owner, address operator) external view returns (bool);
        function safeTransferFrom(address from, address to, uint256 tokenId) external;
    }
}
```
