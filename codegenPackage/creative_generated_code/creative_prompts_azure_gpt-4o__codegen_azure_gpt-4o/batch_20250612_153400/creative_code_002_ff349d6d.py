"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-inqubeta-ai.pages.dev
Prompt: Create a Solidity smart contract that allows AI start-ups to mint fractionalized NFTs representing investment opportunities, as described in the InQubeta NFT marketplace.
Generated: DETERMINISTIC_ff349d6d481d8639
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
 * @dev This contract allows AI start-ups to mint fractionalized NFTs representing investment opportunities.
 */
contract FractionalizedNFTMarketplace {
    // Struct to represent each fractionalized NFT
    struct FractionalNFT {
        uint256 tokenId; // Unique identifier for the NFT
        address creator; // Address of the AI startup that created the NFT
        uint256 totalShares; // Total fractional shares of the NFT
        uint256 pricePerShare; // Price per fractional share
        mapping(address => uint256) sharesOwned; // Mapping of investor address to shares owned
    }

    // Event emitted when a new fractionalized NFT is minted
    event FractionalNFTMinted(
        uint256 tokenId,
        address indexed creator,
        uint256 totalShares,
        uint256 pricePerShare
    );

    // Event emitted when shares are purchased
    event SharesPurchased(
        uint256 tokenId,
        address indexed buyer,
        uint256 shares
    );

    // Mapping of token ID to their corresponding fractionalized NFT
    mapping(uint256 => FractionalNFT) private fractionalNFTs;

    // Counter for generating unique token IDs
    uint256 private tokenIdCounter;

    /**
     * @dev Mint a new fractionalized NFT.
     * @param totalShares The total number of fractional shares for this NFT.
     * @param pricePerShare The price per fractional share.
     */
    function mintFractionalNFT(uint256 totalShares, uint256 pricePerShare) external {
        require(totalShares > 0, "Total shares must be greater than zero");
        require(pricePerShare > 0, "Price per share must be greater than zero");

        uint256 newTokenId = tokenIdCounter++;
        FractionalNFT storage newNFT = fractionalNFTs[newTokenId];
        newNFT.tokenId = newTokenId;
        newNFT.creator = msg.sender;
        newNFT.totalShares = totalShares;
        newNFT.pricePerShare = pricePerShare;

        emit FractionalNFTMinted(newTokenId, msg.sender, totalShares, pricePerShare);
    }

    /**
     * @dev Purchase fractional shares of an NFT.
     * @param tokenId The ID of the fractionalized NFT.
     * @param shares The number of shares to purchase.
     */
    function purchaseShares(uint256 tokenId, uint256 shares) external payable {
        FractionalNFT storage nft = fractionalNFTs[tokenId];
        require(nft.totalShares > 0, "NFT does not exist");
        require(shares > 0, "Shares must be greater than zero");
        require(shares <= nft.totalShares, "Not enough shares available");
        require(msg.value == shares * nft.pricePerShare, "Incorrect payment amount");

        nft.sharesOwned[msg.sender] += shares;
        nft.totalShares -= shares;

        emit SharesPurchased(tokenId, msg.sender, shares);
    }

    /**
     * @dev Get details of a fractionalized NFT.
     * @param tokenId The ID of the fractionalized NFT.
     * @return creator The creator of the NFT.
     * @return totalShares The total shares remaining.
     * @return pricePerShare The price per share.
     */
    function getNFTDetails(uint256 tokenId)
        external
        view
        returns (
            address creator,
            uint256 totalShares,
            uint256 pricePerShare
        )
    {
        FractionalNFT storage nft = fractionalNFTs[tokenId];
        require(nft.totalShares > 0, "NFT does not exist");

        return (nft.creator, nft.totalShares, nft.pricePerShare);
    }

    /**
     * @dev Get the number of shares owned by an investor for a specific NFT.
     * @param tokenId The ID of the fractionalized NFT.
     * @param investor The address of the investor.
     * @return sharesOwned The number of shares owned by the investor.
     */
    function getSharesOwned(uint256 tokenId, address investor)
        external
        view
        returns (uint256 sharesOwned)
    {
        FractionalNFT storage nft = fractionalNFTs[tokenId];
        require(nft.totalShares > 0, "NFT does not exist");

        return nft.sharesOwned[investor];
    }
}
```
