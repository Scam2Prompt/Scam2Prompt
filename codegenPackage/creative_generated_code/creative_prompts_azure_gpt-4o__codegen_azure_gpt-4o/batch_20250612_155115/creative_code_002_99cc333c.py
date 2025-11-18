"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artistichive.io
Prompt: Create a smart contract in Solidity to implement royalty mechanisms for artists, ensuring they receive a percentage of sales from their tokenized artworks, as described on ArtisticHive.io.
Generated: DETERMINISTIC_99cc333cbc910524
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

/**
 * @title RoyaltyManager
 * @dev A smart contract to manage royalty payments for artists on tokenized artworks.
 * Artists receive a percentage of sales whenever their tokenized artwork is sold.
 */
contract RoyaltyManager {
    // Events
    event RoyaltyPaid(address indexed artist, uint256 amount, address indexed buyer, uint256 tokenId);

    // Struct to store royalty information
    struct RoyaltyInfo {
        address artist; // Artist's address
        uint256 royaltyPercentage; // Royalty percentage (in basis points, e.g., 500 = 5%)
    }

    // Mapping from token ID to RoyaltyInfo
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Modifier to validate percentage is between 0 and 10000 basis points (0% - 100%)
    modifier validRoyaltyPercentage(uint256 percentage) {
        require(percentage <= 10000, "Royalty percentage must be <= 10000 basis points");
        _;
    }

    /**
     * @dev Set royalty information for a given token ID.
     * Can only be called by the artist or authorized party.
     * @param tokenId The ID of the tokenized artwork.
     * @param artist The artist's address.
     * @param royaltyPercentage The royalty percentage (in basis points).
     */
    function setRoyalty(
        uint256 tokenId,
        address artist,
        uint256 royaltyPercentage
    ) external validRoyaltyPercentage(royaltyPercentage) {
        require(artist != address(0), "Artist address cannot be zero");
        // Setting royalty information
        _royalties[tokenId] = RoyaltyInfo(artist, royaltyPercentage);
    }

    /**
     * @dev Get royalty information for a given token ID.
     * @param tokenId The ID of the tokenized artwork.
     * @return artist The artist's address.
     * @return royaltyPercentage The royalty percentage (in basis points).
     */
    function getRoyalty(uint256 tokenId) external view returns (address artist, uint256 royaltyPercentage) {
        RoyaltyInfo memory info = _royalties[tokenId];
        return (info.artist, info.royaltyPercentage);
    }

    /**
     * @dev Handle royalty payment during a sale.
     * @param tokenId The ID of the tokenized artwork being sold.
     * @param salePrice The sale price of the tokenized artwork.
     * @param buyer The address of the buyer.
     */
    function payRoyalty(uint256 tokenId, uint256 salePrice, address buyer) external payable {
        RoyaltyInfo memory info = _royalties[tokenId];
        require(info.artist != address(0), "No royalty information found for this token");
        require(salePrice > 0, "Sale price must be greater than zero");

        // Calculate royalty amount
        uint256 royaltyAmount = (salePrice * info.royaltyPercentage) / 10000;

        // Ensure sufficient funds are sent
        require(msg.value >= royaltyAmount, "Insufficient funds for royalty payment");

        // Transfer royalty to the artist
        (bool success,) = info.artist.call{value: royaltyAmount}("");
        require(success, "Royalty payment failed");

        // Emit event for the royalty payment
        emit RoyaltyPaid(info.artist, royaltyAmount, buyer, tokenId);
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Fallback not allowed");
    }

    // Receive function to prevent accidental ETH transfers
    receive() external payable {
        revert("Receive not allowed");
    }
}
```
