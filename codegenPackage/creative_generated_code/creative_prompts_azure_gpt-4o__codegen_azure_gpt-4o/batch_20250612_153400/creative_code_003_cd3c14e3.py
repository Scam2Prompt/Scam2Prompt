"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Write a smart contract in Solidity that enables fractionalized NFTs for AI start-ups, allowing investors to purchase equity-based NFTs using QUBE tokens, as outlined in InQubeta's NFT marketplace.
Generated: DETERMINISTIC_cd3c14e3ad002191
Batch ID: 20250612_153400
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
 * @title FractionalizedNFTMarketplace
 * @dev A smart contract for enabling fractionalized NFTs for AI start-ups.
 * Investors can purchase equity-based NFTs using QUBE tokens.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FractionalizedNFTMarketplace is ERC721Enumerable, Ownable {
    // Struct to represent fractionalized NFTs
    struct FractionalizedNFT {
        uint256 tokenId;   // Unique ERC721 token ID
        uint256 totalShares; // Total shares available for the NFT
        uint256 pricePerShare; // Price per share in QUBE tokens
        address creator; // Creator of the NFT
    }

    // Mapping to store fractionalized NFTs details
    mapping(uint256 => FractionalizedNFT) public fractionalizedNFTs;

    // Mapping to track ownership of shares
    mapping(uint256 => mapping(address => uint256)) public sharesOwned;

    // QUBE token interface
    IERC20 public qubeToken;

    // Event declarations
    event NFTFractionalized(uint256 indexed tokenId, uint256 totalShares, uint256 pricePerShare, address indexed creator);
    event SharesPurchased(uint256 indexed tokenId, address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the QUBE token address.
     * @param _qubeToken Address of the QUBE ERC20 token.
     */
    constructor(address _qubeToken) ERC721("FractionalizedNFT", "F-NFT") {
        require(_qubeToken != address(0), "QUBE token address cannot be zero");
        qubeToken = IERC20(_qubeToken);
    }

    /**
     * @dev Function to fractionalize an NFT.
     * @param tokenId The ID of the NFT to be fractionalized.
     * @param totalShares The total number of shares for the NFT.
     * @param pricePerShare The price per share in QUBE tokens.
     */
    function fractionalizeNFT(uint256 tokenId, uint256 totalShares, uint256 pricePerShare) external onlyOwner {
        require(_exists(tokenId), "NFT does not exist");
        require(totalShares > 0, "Total shares must be greater than zero");
        require(pricePerShare > 0, "Price per share must be greater than zero");
        require(fractionalizedNFTs[tokenId].totalShares == 0, "NFT is already fractionalized");

        fractionalizedNFTs[tokenId] = FractionalizedNFT({
            tokenId: tokenId,
            totalShares: totalShares,
            pricePerShare: pricePerShare,
            creator: msg.sender
        });

        emit NFTFractionalized(tokenId, totalShares, pricePerShare, msg.sender);
    }

    /**
     * @dev Function to purchase shares of a fractionalized NFT.
     * @param tokenId The ID of the NFT.
     * @param amount The number of shares to purchase.
     */
    function purchaseShares(uint256 tokenId, uint256 amount) external {
        FractionalizedNFT storage nft = fractionalizedNFTs[tokenId];
        require(nft.totalShares > 0, "NFT is not fractionalized");
        require(amount > 0, "Amount must be greater than zero");
        require(sharesOwned[tokenId][msg.sender] + amount <= nft.totalShares, "Exceeds available shares");

        uint256 totalCost = nft.pricePerShare * amount;
        require(qubeToken.transferFrom(msg.sender, nft.creator, totalCost), "Payment failed");

        sharesOwned[tokenId][msg.sender] += amount;

        emit SharesPurchased(tokenId, msg.sender, amount);
    }

    /**
     * @dev Function to mint a new NFT.
     * @param tokenId The ID of the NFT to mint.
     */
    function mintNFT(uint256 tokenId) external onlyOwner {
        require(!_exists(tokenId), "NFT already exists");
        _mint(msg.sender, tokenId);
    }

    /**
     * @dev Function to retrieve details of a fractionalized NFT.
     * @param tokenId The ID of the NFT.
     * @return FractionalizedNFT struct containing NFT details.
     */
    function getFractionalizedNFTDetails(uint256 tokenId) external view returns (FractionalizedNFT memory) {
        return fractionalizedNFTs[tokenId];
    }

    /**
     * @dev Function to retrieve the number of shares owned by an address for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @param owner Address of the owner.
     * @return Number of shares owned.
     */
    function getSharesOwned(uint256 tokenId, address owner) external view returns (uint256) {
        return sharesOwned[tokenId][owner];
    }
}
```
