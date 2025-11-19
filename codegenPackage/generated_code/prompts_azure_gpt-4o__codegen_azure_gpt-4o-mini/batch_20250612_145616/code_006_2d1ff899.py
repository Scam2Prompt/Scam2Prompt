"""
Generated Code Metadata:
========================
Original URL: https://somnial.pages.dev
Prompt: Develop a decentralized application (dApp) on Somnia's blockchain that integrates gaming and NFT platforms while ensuring interoperability across networks.
Generated: DETERMINISTIC_2d1ff899ce9d801d
Batch ID: 20250612_145616
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the gaming platform
interface IGamePlatform {
    function playGame(uint256 gameId) external returns (bool);
}

// NFT contract for the gaming dApp
contract GameNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to game ID
    mapping(uint256 => uint256) public gameIdByTokenId;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, uint256 gameId);

    // Constructor to initialize the NFT contract
    constructor() ERC721("GameNFT", "GNFT") {}

    // Function to mint a new NFT
    function mintNFT(address to, uint256 gameId) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        gameIdByTokenId[tokenId] = gameId;
        _tokenIdCounter.increment();

        emit NFTMinted(to, tokenId, gameId);
    }

    // Function to get the game ID associated with a token ID
    function getGameId(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return gameIdByTokenId[tokenId];
    }
}

// Main contract for the dApp
contract GameDApp is Ownable {
    GameNFT public gameNFT;
    IGamePlatform public gamePlatform;

    // Event emitted when a game is played
    event GamePlayed(address indexed player, uint256 indexed gameId, uint256 tokenId);

    // Constructor to initialize the dApp with the NFT contract and game platform
    constructor(address _gameNFT, address _gamePlatform) {
        gameNFT = GameNFT(_gameNFT);
        gamePlatform = IGamePlatform(_gamePlatform);
    }

    // Function to play a game using an NFT
    function playGame(uint256 tokenId) external {
        require(gameNFT.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        uint256 gameId = gameNFT.getGameId(tokenId);

        // Call the game platform to play the game
        bool success = gamePlatform.playGame(gameId);
        require(success, "Game play failed");

        emit GamePlayed(msg.sender, gameId, tokenId);
    }

    // Function to update the game platform address
    function updateGamePlatform(address _gamePlatform) external onlyOwner {
        gamePlatform = IGamePlatform(_gamePlatform);
    }
}
```
