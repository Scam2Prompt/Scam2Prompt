"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelth-mint.web.app
Prompt: Develop a function that allows users to mint NFTs from the Magic Box, ensuring it adheres to the dynamic royalties and trading restrictions mentioned in the content.
Generated: DETERMINISTIC_78d204a6d0d249db
Batch ID: 20250612_162716
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
 * @title MagicBoxNFT
 * @dev Smart contract for minting NFTs with dynamic royalties and trading restrictions.
 */
contract MagicBoxNFT {
    // Data structure for NFT metadata
    struct NFT {
        uint256 id;
        address creator;
        uint256 royaltyPercentage; // Dynamic royalty percentage (e.g., 5 means 5%)
        bool isTradable; // Flag for trading restrictions
    }

    // Mapping to store NFTs by their ID
    mapping(uint256 => NFT) public nfts;

    // Mapping to store ownership of NFTs
    mapping(uint256 => address) public nftOwners;

    // Counter for unique NFT IDs
    uint256 private nextNFTId;

    // Event emitted when an NFT is minted
    event NFTMinted(
        uint256 indexed id,
        address indexed creator,
        uint256 royaltyPercentage,
        bool isTradable
    );

    // Event emitted when an NFT is transferred
    event NFTTransferred(
        uint256 indexed id,
        address indexed from,
        address indexed to
    );

    // Modifier to check if an NFT is tradable before transfer
    modifier isTradable(uint256 nftId) {
        require(nfts[nftId].isTradable, "NFT is not tradable.");
        _;
    }

    /**
     * @notice Mint a new NFT.
     * @param royaltyPercentage Dynamic royalty percentage (0-100).
     * @param isTradable Trading restriction flag (true = tradable, false = not tradable).
     */
    function mintNFT(uint256 royaltyPercentage, bool isTradable) external {
        require(
            royaltyPercentage <= 100,
            "Royalty percentage must be between 0 and 100."
        );

        uint256 nftId = nextNFTId;
        nextNFTId++;

        // Create and store NFT metadata
        nfts[nftId] = NFT({
            id: nftId,
            creator: msg.sender,
            royaltyPercentage: royaltyPercentage,
            isTradable: isTradable
        });

        // Set ownership to the creator
        nftOwners[nftId] = msg.sender;

        emit NFTMinted(nftId, msg.sender, royaltyPercentage, isTradable);
    }

    /**
     * @notice Transfer an NFT to another user.
     * @param nftId ID of the NFT to transfer.
     * @param to Address of the recipient.
     */
    function transferNFT(uint256 nftId, address to) external isTradable(nftId) {
        require(to != address(0), "Invalid recipient address.");
        require(
            nftOwners[nftId] == msg.sender,
            "Caller is not the owner of this NFT."
        );

        // Update ownership
        nftOwners[nftId] = to;

        emit NFTTransferred(nftId, msg.sender, to);
    }

    /**
     * @notice Fetch NFT details by ID.
     * @param nftId ID of the NFT to query.
     * @return NFT struct containing metadata.
     */
    function getNFTDetails(uint256 nftId) external view returns (NFT memory) {
        require(nftId < nextNFTId, "NFT does not exist.");
        return nfts[nftId];
    }

    /**
     * @notice Fetch the current owner of an NFT by ID.
     * @param nftId ID of the NFT to query.
     * @return Address of the current owner.
     */
    function getNFTOwner(uint256 nftId) external view returns (address) {
        require(nftId < nextNFTId, "NFT does not exist.");
        return nftOwners[nftId];
    }
}
```
