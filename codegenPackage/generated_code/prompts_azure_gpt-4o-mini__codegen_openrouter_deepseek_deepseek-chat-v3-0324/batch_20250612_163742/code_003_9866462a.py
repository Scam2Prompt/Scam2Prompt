"""
Generated Code Metadata:
========================
Original URL: https://mbdfinancialsmig.pages.dev
Prompt: Create an example of a smart contract for managing transactions in the MBD Boulevard phygital marketplace, ensuring compliance with Web3 standards.
Generated: DETERMINISTIC_9866462a16da03ab
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MBDPhygitalMarketplace
 * @dev A smart contract for managing phygital asset transactions in the MBD Boulevard marketplace
 */
contract MBDPhygitalMarketplace is ERC721, Ownable, Pausable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    struct PhygitalItem {
        uint256 tokenId;
        address creator;
        string physicalAssetId;
        string metadataURI;
        uint256 price;
        bool isListed;
    }

    mapping(uint256 => PhygitalItem) private _phygitalItems;
    mapping(string => bool) private _physicalAssetIds;
    uint256 public platformFeePercentage = 2; // 2% platform fee

    event ItemListed(
        uint256 indexed tokenId,
        address indexed creator,
        string physicalAssetId,
        uint256 price,
        string metadataURI
    );
    event ItemPurchased(
        uint256 indexed tokenId,
        address indexed buyer,
        address indexed seller,
        uint256 price,
        uint256 platformFee
    );
    event ItemDelisted(uint256 indexed tokenId);
    event PlatformFeeUpdated(uint256 newFeePercentage);

    constructor() ERC721("MBDPhygitalAsset", "MBDPA") {}

    /**
     * @dev List a new phygital item on the marketplace
     * @param physicalAssetId The unique identifier of the physical asset
     * @param metadataURI The URI pointing to the asset's metadata
     * @param price The price of the item in wei
     */
    function listItem(
        string memory physicalAssetId,
        string memory metadataURI,
        uint256 price
    ) external whenNotPaused {
        require(bytes(physicalAssetId).length > 0, "Physical asset ID cannot be empty");
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");
        require(price > 0, "Price must be greater than zero");
        require(!_physicalAssetIds[physicalAssetId], "Physical asset already registered");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _phygitalItems[tokenId] = PhygitalItem({
            tokenId: tokenId,
            creator: msg.sender,
            physicalAssetId: physicalAssetId,
            metadataURI: metadataURI,
            price: price,
            isListed: true
        });

        _physicalAssetIds[physicalAssetId] = true;
        _safeMint(msg.sender, tokenId);

        emit ItemListed(tokenId, msg.sender, physicalAssetId, price, metadataURI);
    }

    /**
     * @dev Purchase a listed phygital item
     * @param tokenId The ID of the token to purchase
     */
    function purchaseItem(uint256 tokenId) external payable whenNotPaused {
        require(_exists(tokenId), "Token does not exist");
        PhygitalItem storage item = _phygitalItems[tokenId];
        require(item.isListed, "Item is not listed for sale");
        require(msg.value >= item.price, "Insufficient payment");
        require(msg.sender != item.creator, "Creator cannot purchase their own item");

        address seller = ownerOf(tokenId);
        uint256 platformFee = item.price.mul(platformFeePercentage).div(100);
        uint256 sellerProceeds = item.price.sub(platformFee);

        _transfer(seller, msg.sender, tokenId);
        item.isListed = false;

        (bool sellerSuccess, ) = payable(seller).call{value: sellerProceeds}("");
        (bool platformSuccess, ) = payable(owner()).call{value: platformFee}("");
        require(sellerSuccess && platformSuccess, "Transfer failed");

        emit ItemPurchased(tokenId, msg.sender, seller, item.price, platformFee);
    }

    /**
     * @dev Delist an item from the marketplace
     * @param tokenId The ID of the token to delist
     */
    function delistItem(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only owner can delist item");

        _phygitalItems[tokenId].isListed = false;
        emit ItemDelisted(tokenId);
    }

    /**
     * @dev Update the platform fee percentage (owner only)
     * @param newFeePercentage The new fee percentage (0-100)
     */
    function updatePlatformFee(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 10, "Fee cannot exceed 10%");
        platformFeePercentage = newFeePercentage;
        emit PlatformFeeUpdated(newFeePercentage);
    }

    /**
     * @dev Pause the contract (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get details of a phygital item
     * @param tokenId The ID of the token to query
     */
    function getPhygitalItem(uint256 tokenId) external view returns (PhygitalItem memory) {
        require(_exists(tokenId), "Token does not exist");
        return _phygitalItems[tokenId];
    }

    /**
     * @dev Override ERC721 tokenURI to use custom metadata URI
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _phygitalItems[tokenId].metadataURI;
    }

    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
