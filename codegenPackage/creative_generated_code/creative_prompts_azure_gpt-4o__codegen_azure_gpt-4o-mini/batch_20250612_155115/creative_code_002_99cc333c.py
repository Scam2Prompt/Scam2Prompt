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

/// @title ArtisticHive Royalty Smart Contract
/// @notice This contract implements a royalty mechanism for artists
/// @dev Artists receive a percentage of sales from their tokenized artworks
contract ArtisticHiveRoyalty {

    // Struct to store information about each artwork
    struct Artwork {
        address artist;            // Artist's address
        uint256 royaltyPercentage; // Royalty percentage (in basis points, e.g., 500 = 5%)
        uint256 totalSales;        // Total sales made for the artwork
    }

    // Mapping from artwork ID to Artwork data
    mapping(uint256 => Artwork) public artworks;

    // Event to emit when an artwork is sold
    event ArtworkSold(uint256 indexed artworkId, address indexed buyer, uint256 salePrice);

    /// @notice Add a new artwork
    /// @param _artworkId The ID of the artwork
    /// @param _artist The artist's address
    /// @param _royaltyPercentage The royalty percentage (in basis points)
    function addArtwork(uint256 _artworkId, address _artist, uint256 _royaltyPercentage) external {
        require(_artist != address(0), "Invalid artist address");
        require(_royaltyPercentage <= 10000, "Royalty percentage exceeds 100%");

        artworks[_artworkId] = Artwork({
            artist: _artist,
            royaltyPercentage: _royaltyPercentage,
            totalSales: 0
        });
    }

    /// @notice Handles the sale of an artwork
    /// @param _artworkId The ID of the artwork being sold
    /// @param _salePrice The price at which the artwork is sold
    function sellArtwork(uint256 _artworkId, uint256 _salePrice) external payable {
        Artwork storage artwork = artworks[_artworkId];

        require(artwork.artist != address(0), "Artwork does not exist");
        require(msg.value >= _salePrice, "Insufficient payment");

        // Calculate the royalty fee
        uint256 royaltyFee = (_salePrice * artwork.royaltyPercentage) / 10000;

        // Transfer the royalty fee to the artist
        (bool success, ) = artwork.artist.call{value: royaltyFee}("");
        require(success, "Royalty payment failed");

        // Update total sales
        artwork.totalSales += _salePrice;

        // Emit the sale event
        emit ArtworkSold(_artworkId, msg.sender, _salePrice);
    }

    /// @notice Get the total sales for an artwork
    /// @param _artworkId The ID of the artwork
    /// @return totalSales The total sales amount for the artwork
    function getTotalSales(uint256 _artworkId) external view returns (uint256 totalSales) {
        return artworks[_artworkId].totalSales;
    }
}
```
