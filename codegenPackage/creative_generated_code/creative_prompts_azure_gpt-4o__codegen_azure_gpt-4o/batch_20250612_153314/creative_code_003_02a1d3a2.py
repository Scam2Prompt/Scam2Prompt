"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnfts.com
Prompt: Write a smart contract in Solidity for managing the sale and ownership of Cornucopias NFTs, ensuring that assets like land plots and vehicles can be traded securely within the game economy.
Generated: DETERMINISTIC_02a1d3a25926ee72
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title CornucopiasNFTMarketplace
 * @dev Smart contract for managing the sale and ownership of Cornucopias NFTs.
 *      This contract allows users to securely trade assets such as land plots and vehicles.
 */
contract CornucopiasNFTMarketplace {
    // ----------------------------------------
    // Struct Definitions
    // ----------------------------------------

    struct NFT {
        uint256 id; // Unique identifier for the NFT
        address owner; // Current owner of the NFT
        uint256 price; // Price for selling the NFT (0 if not listed)
        bool forSale; // Flag indicating whether the NFT is listed for sale
    }

    // ----------------------------------------
    // State Variables
    // ----------------------------------------

    uint256 private nextNFTId = 1; // Tracks the next NFT ID to be assigned
    address public admin; // Address of the contract administrator
    mapping(uint256 => NFT) public nfts; // Mapping from NFT ID to its details
    mapping(address => uint256[]) public ownerToNFTs; // Mapping from owner to array of owned NFT IDs

    // ----------------------------------------
    // Events
    // ----------------------------------------

    event NFTCreated(uint256 indexed nftId, address indexed owner);
    event NFTListedForSale(uint256 indexed nftId, uint256 price);
    event NFTRemovedFromSale(uint256 indexed nftId);
    event NFTPurchased(uint256 indexed nftId, address indexed buyer, uint256 price);

    // ----------------------------------------
    // Modifiers
    // ----------------------------------------

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can execute this.");
        _;
    }

    modifier onlyOwner(uint256 nftId) {
        require(nfts[nftId].owner == msg.sender, "Only NFT owner can execute this.");
        _;
    }

    modifier nftExists(uint256 nftId) {
        require(nfts[nftId].owner != address(0), "NFT does not exist.");
        _;
    }

    // ----------------------------------------
    // Constructor
    // ----------------------------------------

    constructor() {
        admin = msg.sender; // Set contract deployer as admin
    }

    // ----------------------------------------
    // Functions
    // ----------------------------------------

    /**
     * @notice Create a new NFT.
     * @dev Admin function to create a new NFT and assign it to an owner.
     * @param owner Address of the NFT's initial owner.
     */
    function createNFT(address owner) external onlyAdmin {
        require(owner != address(0), "Invalid owner address.");

        uint256 nftId = nextNFTId++;
        nfts[nftId] = NFT(nftId, owner, 0, false);
        ownerToNFTs[owner].push(nftId);

        emit NFTCreated(nftId, owner);
    }

    /**
     * @notice List an NFT for sale.
     * @dev Set the price and mark the NFT as "for sale".
     * @param nftId ID of the NFT to be listed.
     * @param price Sale price of the NFT.
     */
    function listNFTForSale(uint256 nftId, uint256 price) external nftExists(nftId) onlyOwner(nftId) {
        require(price > 0, "Price must be greater than zero.");

        nfts[nftId].price = price;
        nfts[nftId].forSale = true;

        emit NFTListedForSale(nftId, price);
    }

    /**
     * @notice Remove an NFT from sale.
     * @dev Unlist the NFT by setting its forSale flag to false.
     * @param nftId ID of the NFT to be removed from sale.
     */
    function removeNFTFromSale(uint256 nftId) external nftExists(nftId) onlyOwner(nftId) {
        nfts[nftId].forSale = false;
        nfts[nftId].price = 0;

        emit NFTRemovedFromSale(nftId);
    }

    /**
     * @notice Purchase an NFT.
     * @dev Transfer ownership of the NFT to the buyer and handle payment securely.
     * @param nftId ID of the NFT to be purchased.
     */
    function purchaseNFT(uint256 nftId) external payable nftExists(nftId) {
        NFT storage nft = nfts[nftId];
        require(nft.forSale, "NFT is not for sale.");
        require(msg.value == nft.price, "Incorrect payment amount.");

        // Transfer payment to the current owner
        payable(nft.owner).transfer(msg.value);

        // Transfer ownership
        _transferOwnership(nftId, nft.owner, msg.sender);

        nft.forSale = false;
        nft.price = 0;

        emit NFTPurchased(nftId, msg.sender, msg.value);
    }

    /**
     * @notice Internal function to handle NFT ownership transfer.
     * @dev Updates mappings and transfers the NFT to the new owner.
     * @param nftId ID of the NFT being transferred.
     * @param from Current owner of the NFT.
     * @param to New owner of the NFT.
     */
    function _transferOwnership(uint256 nftId, address from, address to) internal {
        require(to != address(0), "Invalid new owner address.");
        
        // Update NFT owner
        nfts[nftId].owner = to;

        // Remove NFT from current owner's list
        uint256[] storage fromNFTs = ownerToNFTs[from];
        for (uint256 i = 0; i < fromNFTs.length; i++) {
            if (fromNFTs[i] == nftId) {
                fromNFTs[i] = fromNFTs[fromNFTs.length - 1];
                fromNFTs.pop();
                break;
            }
        }

        // Add NFT to new owner's list
        ownerToNFTs[to].push(nftId);
    }

    /**
     * @notice Get all NFTs owned by a specific address.
     * @param owner Address to query for owned NFTs.
     * @return Array of NFT IDs owned by the address.
     */
    function getNFTsByOwner(address owner) external view returns (uint256[] memory) {
        return ownerToNFTs[owner];
    }
}
```
