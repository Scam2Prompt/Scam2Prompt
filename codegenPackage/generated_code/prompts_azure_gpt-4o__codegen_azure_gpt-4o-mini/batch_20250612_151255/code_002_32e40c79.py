"""
Generated Code Metadata:
========================
Original URL: https://claim-game5.pages.dev
Prompt: Generate a smart contract in Solidity for minting an NFT that represents the 1991 Game 5 ball, including attributes like event date, significance, and ownership history.
Generated: DETERMINISTIC_32e40c798e44e8a9
Batch ID: 20250612_151255
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

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFT contract for minting the 1991 Game 5 ball
contract Game5BallNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold NFT attributes
    struct GameBall {
        string eventDate;        // Date of the event
        string significance;     // Significance of the event
        address[] ownershipHistory; // History of ownership
    }

    // Mapping from token ID to GameBall attributes
    mapping(uint256 => GameBall) private _gameBalls;

    // Event emitted when a new NFT is minted
    event GameBallMinted(uint256 indexed tokenId, string eventDate, string significance, address owner);

    // Constructor to set the name and symbol of the NFT
    constructor() ERC721("Game5BallNFT", "G5B") {}

    // Function to mint a new NFT
    function mintNFT(string memory eventDate, string memory significance) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId); // Mint the NFT to the owner

        // Store the attributes in the mapping
        _gameBalls[tokenId] = GameBall({
            eventDate: eventDate,
            significance: significance,
            ownershipHistory: new address[](0) // Initialize empty ownership history
        });

        // Add the owner to the ownership history
        _gameBalls[tokenId].ownershipHistory.push(msg.sender);

        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Emit the minting event
        emit GameBallMinted(tokenId, eventDate, significance, msg.sender);
    }

    // Function to get the attributes of a specific NFT
    function getGameBallAttributes(uint256 tokenId) external view returns (string memory, string memory, address[] memory) {
        require(_exists(tokenId), "Query for nonexistent token");

        GameBall memory gameBall = _gameBalls[tokenId];
        return (gameBall.eventDate, gameBall.significance, gameBall.ownershipHistory);
    }

    // Override the _transfer function to update ownership history
    function _transfer(address from, address to, uint256 tokenId) internal override {
        super._transfer(from, to, tokenId);
        // Update ownership history
        _gameBalls[tokenId].ownershipHistory.push(to);
    }
}
```
