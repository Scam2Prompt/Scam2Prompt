"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-game5.pages.dev
Prompt: Generate a smart contract in Solidity for minting an NFT that represents the 1991 Game 5 ball, including attributes like event date, significance, and ownership history.
Generated: DETERMINISTIC_32e40c798e44e8a9
Batch ID: 20250612_151255
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
 * @title GameBallNFT
 * @dev A smart contract for minting an NFT representing the 1991 Game 5 ball
 * with attributes such as event date, significance, and ownership history.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GameBallNFT is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Struct to store the NFT metadata
    struct GameBallMetadata {
        string eventDate;
        string significance;
        string ownershipHistory;
    }

    // Mapping to associate tokenId with metadata
    mapping(uint256 => GameBallMetadata) private _gameBallMetadata;

    /**
     * @dev Constructor to initialize the ERC721 contract
     */
    constructor() ERC721("GameBallNFT", "GBNFT") {}

    /**
     * @dev Function to mint a new GameBall NFT.
     * @param to Address to receive the minted NFT.
     * @param eventDate Date of the event (e.g., "1991-06-12").
     * @param significance Significance of the game (e.g., "Historic NBA Finals moment").
     * @param ownershipHistory Ownership history of the ball (e.g., "Originally owned by PlayerX").
     * @param tokenURI URI pointing to metadata (e.g., JSON file containing additional details, image, etc.).
     */
    function mintGameBallNFT(
        address to,
        string memory eventDate,
        string memory significance,
        string memory ownershipHistory,
        string memory tokenURI
    ) external onlyOwner {
        // Increment the tokenIdCounter for the new NFT
        uint256 newTokenId = _tokenIdCounter;
        _tokenIdCounter++;

        // Mint the NFT to the recipient address
        _mint(to, newTokenId);

        // Set the token URI for metadata
        _setTokenURI(newTokenId, tokenURI);

        // Store the metadata
        _gameBallMetadata[newTokenId] = GameBallMetadata({
            eventDate: eventDate,
            significance: significance,
            ownershipHistory: ownershipHistory
        });
    }

    /**
     * @dev Function to retrieve GameBall metadata by tokenId.
     * @param tokenId ID of the token to get metadata for.
     * @return Metadata containing event date, significance, and ownership history.
     */
    function getGameBallMetadata(uint256 tokenId)
        external
        view
        returns (GameBallMetadata memory)
    {
        // Ensure the token exists
        require(_exists(tokenId), "GameBallNFT: Metadata query for nonexistent token");

        // Return the metadata
        return _gameBallMetadata[tokenId];
    }

    /**
     * @dev Function to get the current tokenId counter.
     * @return Current value of the counter (useful for tracking the number of minted tokens).
     */
    function getTokenIdCounter() external view returns (uint256) {
        return _tokenIdCounter;
    }
}
```
