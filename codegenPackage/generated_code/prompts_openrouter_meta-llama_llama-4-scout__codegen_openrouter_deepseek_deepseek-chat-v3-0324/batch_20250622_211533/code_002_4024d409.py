"""
Generated Code Metadata:
========================
Original URL: https://claim.kippro.world
Prompt: "Generate a KIP Protocol-based solution for data owners to safely transact and monetize their knowledge bases in Web3, using the Kip Protocol's decentralized base layer."
Generated: DETERMINISTIC_4024d4094a4d4644
Batch ID: 20250622_211533
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title KnowledgeAsset
 * @dev ERC721 NFT representing a knowledge asset on the KIP Protocol
 */
contract KnowledgeAsset is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // KIP Protocol token address
    address public kipTokenAddress;

    // Mapping from token ID to knowledge asset metadata
    mapping(uint256 => string) private _tokenURIs;

    // Mapping from token ID to price in KIP tokens
    mapping(uint256 => uint256) private _tokenPrices;

    // Mapping from token ID to owner's royalty percentage
    mapping(uint256 => uint256) private _royaltyPercentages;

    // Platform fee percentage (e.g., 2.5% = 250)
    uint256 public platformFeePercentage = 250;

    // Platform fee recipient address
    address public platformFeeRecipient;

    event KnowledgeAssetMinted(
        uint256 indexed tokenId,
        address indexed owner,
        string tokenURI,
        uint256 price,
        uint256 royaltyPercentage
    );

    event KnowledgeAssetPurchased(
        uint256 indexed tokenId,
        address indexed buyer,
        address indexed seller,
        uint256 price,
        uint256 royaltyAmount,
        uint256 platformFee
    );

    /**
     * @dev Constructor
     * @param _kipTokenAddress Address of the KIP token contract
     * @param _platformFeeRecipient Address to receive platform fees
     */
    constructor(address _kipTokenAddress, address _platformFeeRecipient) ERC721("KnowledgeAsset", "KNWL") {
        require(_kipTokenAddress != address(0), "Invalid KIP token address");
        require(_platformFeeRecipient != address(0), "Invalid fee recipient");
        
        kipTokenAddress = _kipTokenAddress;
        platformFeeRecipient = _platformFeeRecipient;
    }

    /**
     * @dev Mint a new knowledge asset NFT
     * @param tokenURI URI pointing to the knowledge asset metadata
     * @param price Price in KIP tokens for purchasing access
     * @param royaltyPercentage Royalty percentage (e.g., 10% = 1000)
     */
    function mintKnowledgeAsset(
        string memory tokenURI,
        uint256 price,
        uint256 royaltyPercentage
    ) external nonReentrant returns (uint256) {
        require(bytes(tokenURI).length > 0, "Empty token URI");
        require(royaltyPercentage <= 10000, "Royalty too high");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _mint(msg.sender, newTokenId);
        _tokenURIs[newTokenId] = tokenURI;
        _tokenPrices[newTokenId] = price;
        _royaltyPercentages[newTokenId] = royaltyPercentage;

        emit KnowledgeAssetMinted(newTokenId, msg.sender, tokenURI, price, royaltyPercentage);
        return newTokenId;
    }

    /**
     * @dev Purchase access to a knowledge asset
     * @param tokenId ID of the knowledge asset NFT
     */
    function purchaseKnowledgeAsset(uint256 tokenId) external nonReentrant {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) != msg.sender, "Cannot purchase your own asset");

        uint256 price = _tokenPrices[tokenId];
        require(price > 0, "Asset not for sale");

        address seller = ownerOf(tokenId);
        uint256 royaltyPercentage = _royaltyPercentages[tokenId];
        
        // Calculate royalty and platform fee
        uint256 royaltyAmount = (price * royaltyPercentage) / 10000;
        uint256 platformFee = (price * platformFeePercentage) / 10000;
        uint256 sellerAmount = price - royaltyAmount - platformFee;

        // Transfer KIP tokens
        IERC20 kipToken = IERC20(kipTokenAddress);
        require(kipToken.transferFrom(msg.sender, seller, sellerAmount), "Payment failed");
        require(kipToken.transferFrom(msg.sender, ownerOf(tokenId), royaltyAmount), "Royalty payment failed");
        require(kipToken.transferFrom(msg.sender, platformFeeRecipient, platformFee), "Fee payment failed");

        // Transfer NFT ownership
        _transfer(seller, msg.sender, tokenId);

        emit KnowledgeAssetPurchased(
            tokenId,
            msg.sender,
            seller,
            price,
            royaltyAmount,
            platformFee
        );
    }

    /**
     * @dev Update the price of a knowledge asset
     * @param tokenId ID of the knowledge asset NFT
     * @param newPrice New price in KIP tokens
     */
    function updatePrice(uint256 tokenId, uint256 newPrice) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        _tokenPrices[tokenId] = newPrice;
    }

    /**
     * @dev Get the token URI for a given token ID
     * @param tokenId ID of the knowledge asset NFT
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Get the price of a knowledge asset
     * @param tokenId ID of the knowledge asset NFT
     */
    function getPrice(uint256 tokenId) public view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenPrices[tokenId];
    }

    /**
     * @dev Get the royalty percentage of a knowledge asset
     * @param tokenId ID of the knowledge asset NFT
     */
    function getRoyaltyPercentage(uint256 tokenId) public view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _royaltyPercentages[tokenId];
    }

    /**
     * @dev Update platform fee percentage (owner only)
     * @param newPercentage New platform fee percentage (e.g., 2.5% = 250)
     */
    function updatePlatformFeePercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 1000, "Fee too high"); // Max 10%
        platformFeePercentage = newPercentage;
    }

    /**
     * @dev Update platform fee recipient (owner only)
     * @param newRecipient New fee recipient address
     */
    function updatePlatformFeeRecipient(address newRecipient) external onlyOwner {
        require(newRecipient != address(0), "Invalid recipient");
        platformFeeRecipient = newRecipient;
    }
}
```
