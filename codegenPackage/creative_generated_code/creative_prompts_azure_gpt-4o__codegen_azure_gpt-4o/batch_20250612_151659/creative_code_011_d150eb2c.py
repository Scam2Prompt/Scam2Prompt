"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Write a function in Solidity to equip NFTs with utilities for games, movies, and Metaverse meet-ups, inspired by Prime Ape Planet's features.
Generated: DETERMINISTIC_d150eb2cce790609
Batch ID: 20250612_151659
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
 * @title NFTUtilityManager
 * @dev A contract to equip NFTs with utilities for games, movies, and Metaverse meet-ups.
 */
contract NFTUtilityManager {
    // Mapping to store utilities for each NFT token
    mapping(uint256 => NFTUtilities) private nftUtilities;

    // Structure to define utilities
    struct NFTUtilities {
        bool gameAccess;        // Access to games
        bool movieAccess;       // Access to movies
        bool metaverseAccess;   // Access to Metaverse meet-ups
    }

    // Event to log updates to NFT utilities
    event NFTUtilitiesUpdated(
        uint256 indexed tokenId,
        bool gameAccess,
        bool movieAccess,
        bool metaverseAccess
    );

    // Modifier to ensure valid token ID
    modifier validTokenId(uint256 tokenId) {
        require(tokenId > 0, "Invalid token ID");
        _;
    }

    /**
     * @dev Sets utilities for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @param gameAccess Whether the NFT grants access to games.
     * @param movieAccess Whether the NFT grants access to movies.
     * @param metaverseAccess Whether the NFT grants access to Metaverse meet-ups.
     */
    function setUtilities(
        uint256 tokenId,
        bool gameAccess,
        bool movieAccess,
        bool metaverseAccess
    ) external validTokenId(tokenId) {
        // Update the utilities for the given tokenId
        nftUtilities[tokenId] = NFTUtilities({
            gameAccess: gameAccess,
            movieAccess: movieAccess,
            metaverseAccess: metaverseAccess
        });

        // Emit event to log the changes
        emit NFTUtilitiesUpdated(tokenId, gameAccess, movieAccess, metaverseAccess);
    }

    /**
     * @dev Gets the utilities for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return gameAccess Whether the NFT grants access to games.
     * @return movieAccess Whether the NFT grants access to movies.
     * @return metaverseAccess Whether the NFT grants access to Metaverse meet-ups.
     */
    function getUtilities(uint256 tokenId)
        external
        view
        validTokenId(tokenId)
        returns (
            bool gameAccess,
            bool movieAccess,
            bool metaverseAccess
        )
    {
        // Fetch utilities for the given tokenId
        NFTUtilities memory utilities = nftUtilities[tokenId];
        return (utilities.gameAccess, utilities.movieAccess, utilities.metaverseAccess);
    }
}
```
