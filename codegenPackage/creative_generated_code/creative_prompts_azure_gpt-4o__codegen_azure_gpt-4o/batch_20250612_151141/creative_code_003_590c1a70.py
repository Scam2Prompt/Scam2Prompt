"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layeralorg.pages.dev
Prompt: Create a smart contract in Solidity for trading Data Capsule NFTs on the KyotoX NFT Marketplace within the LayerAI ecosystem.
Generated: DETERMINISTIC_590c1a702c42cc86
Batch ID: 20250612_151141
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
 * @title DataCapsuleNFTMarketplace
 * @dev Smart contract for trading Data Capsule NFTs on KyotoX NFT Marketplace within LayerAI ecosystem.
 */
contract DataCapsuleNFTMarketplace {
    // Struct to represent a listed NFT
    struct ListedNFT {
        address seller;
        uint256 price;
        bool isListed;
    }

    // Mapping to store listed NFTs by their token ID
    mapping(uint256 => ListedNFT) public listedNFTs;

    // Address of the NFT contract
    address public nftContract;

    // Marketplace owner
    address public owner;

    // Events
    event NFTListed(address indexed seller, uint256 indexed tokenId, uint256 price);
    event NFTUnlisted(address indexed seller, uint256 indexed tokenId);
    event NFTPurchased(address indexed buyer, address indexed seller, uint256 indexed tokenId, uint256 price);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Permission denied: Only owner can call this function");
        _;
    }

    // Modifier to check if the caller is the NFT owner
    modifier isNFTOwner(uint256 tokenId) {
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Caller is not the NFT owner");
        _;
    }

    // Modifier to ensure the token is listed
    modifier isListed(uint256 tokenId) {
        require(listedNFTs[tokenId].isListed, "NFT is not listed for sale");
        _;
    }

    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
        owner = msg.sender;
    }

    /**
     * @dev List an NFT for sale on the marketplace.
     * @param tokenId The token ID of the NFT being listed.
     * @param price The price of the NFT in wei.
     */
    function listNFT(uint256 tokenId, uint256 price) external isNFTOwner(tokenId) {
        require(price > 0, "Price must be greater than zero");
        require(!listedNFTs[tokenId].isListed, "NFT is already listed");

        listedNFTs[tokenId] = ListedNFT(msg.sender, price, true);

        emit NFTListed(msg.sender, tokenId, price);
    }

    /**
     * @dev Remove an NFT from sale on the marketplace.
     * @param tokenId The token ID of the NFT being unlisted.
     */
    function unlistNFT(uint256 tokenId) external isNFTOwner(tokenId) isListed(tokenId) {
        delete listedNFTs[tokenId];

        emit NFTUnlisted(msg.sender, tokenId);
    }

    /**
     * @dev Purchase a listed NFT on the marketplace.
     * @param tokenId The token ID of the NFT being purchased.
     */
    function purchaseNFT(uint256 tokenId) external payable isListed(tokenId) {
        ListedNFT memory listedNFT = listedNFTs[tokenId];
        require(msg.value == listedNFT.price, "Incorrect payment amount");

        // Transfer payment to seller
        (bool success, ) = listedNFT.seller.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        // Transfer NFT to buyer
        IERC721(nftContract).safeTransferFrom(listedNFT.seller, msg.sender, tokenId);

        // Remove NFT from listing
        delete listedNFTs[tokenId];

        emit NFTPurchased(msg.sender, listedNFT.seller, tokenId, listedNFT.price);
    }

    /**
     * @dev Update the address of the NFT contract (owner only).
     * @param _nftContract The new NFT contract address.
     */
    function updateNFTContract(address _nftContract) external onlyOwner {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
    }

    // Fallback function to prevent accidental Ether transfers
    fallback() external payable {
        revert("Direct payments are not allowed");
    }

    receive() external payable {
        revert("Direct payments are not allowed");
    }
}

// Interface for ERC721
interface IERC721 {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
