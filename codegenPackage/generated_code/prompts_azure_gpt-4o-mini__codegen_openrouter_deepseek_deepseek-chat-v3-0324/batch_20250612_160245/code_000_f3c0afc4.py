"""
Generated Code Metadata:
========================
Original URL: https://proposal-b3.com
Prompt: How can I implement a gaming ecosystem using the Open Gaming Layer³ built on Base for optimal performance and scalability?
Generated: DETERMINISTIC_f3c0afc46720e4b3
Batch ID: 20250612_160245
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

/**
 * @title OpenGamingLayer
 * @dev A gaming ecosystem contract built on Base with ERC721 NFTs for in-game assets
 */
contract OpenGamingLayer is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct GameAsset {
        uint256 id;
        string metadataURI;
        uint256 value;
        bool tradeable;
    }

    mapping(uint256 => GameAsset) private _gameAssets;
    mapping(address => uint256[]) private _playerAssets;
    mapping(address => uint256) private _playerScores;
    mapping(address => uint256) private _playerBalances;

    event AssetMinted(address indexed player, uint256 assetId, string metadataURI);
    event AssetTraded(address indexed from, address indexed to, uint256 assetId, uint256 price);
    event ScoreUpdated(address indexed player, uint256 newScore);
    event BalanceUpdated(address indexed player, uint256 newBalance);

    constructor() ERC721("OpenGamingLayer", "OGL") {}

    /**
     * @dev Mint a new game asset for a player
     * @param player The address of the player receiving the asset
     * @param metadataURI The URI pointing to the asset's metadata
     * @param value The in-game value of the asset
     * @param tradeable Whether the asset can be traded
     */
    function mintAsset(
        address player,
        string memory metadataURI,
        uint256 value,
        bool tradeable
    ) external onlyOwner nonReentrant {
        require(player != address(0), "Invalid player address");
        
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        _safeMint(player, newTokenId);
        _gameAssets[newTokenId] = GameAsset(newTokenId, metadataURI, value, tradeable);
        _playerAssets[player].push(newTokenId);

        emit AssetMinted(player, newTokenId, metadataURI);
    }

    /**
     * @dev Trade an asset between players
     * @param from The current owner of the asset
     * @param to The new owner of the asset
     * @param assetId The ID of the asset being traded
     * @param price The price paid for the asset
     */
    function tradeAsset(
        address from,
        address to,
        uint256 assetId,
        uint256 price
    ) external nonReentrant {
        require(_exists(assetId), "Asset does not exist");
        require(ownerOf(assetId) == from, "Not asset owner");
        require(_gameAssets[assetId].tradeable, "Asset not tradeable");
        require(to != address(0), "Invalid recipient address");
        require(_playerBalances[to] >= price, "Insufficient balance");

        _playerBalances[to] -= price;
        _playerBalances[from] += price;

        _transfer(from, to, assetId);

        // Update player asset lists
        _removeAssetFromPlayer(from, assetId);
        _playerAssets[to].push(assetId);

        emit AssetTraded(from, to, assetId, price);
        emit BalanceUpdated(from, _playerBalances[from]);
        emit BalanceUpdated(to, _playerBalances[to]);
    }

    /**
     * @dev Update a player's score
     * @param player The address of the player
     * @param score The new score to set
     */
    function updateScore(address player, uint256 score) external onlyOwner {
        require(player != address(0), "Invalid player address");
        _playerScores[player] = score;
        emit ScoreUpdated(player, score);
    }

    /**
     * @dev Deposit funds to player balance
     * @param player The address of the player
     * @param amount The amount to deposit
     */
    function deposit(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address");
        _playerBalances[player] += amount;
        emit BalanceUpdated(player, _playerBalances[player]);
    }

    /**
     * @dev Withdraw funds from player balance
     * @param player The address of the player
     * @param amount The amount to withdraw
     */
    function withdraw(address player, uint256 amount) external nonReentrant {
        require(player != address(0), "Invalid player address");
        require(_playerBalances[player] >= amount, "Insufficient balance");
        
        _playerBalances[player] -= amount;
        emit BalanceUpdated(player, _playerBalances[player]);
    }

    /**
     * @dev Get player's assets
     * @param player The address of the player
     * @return Array of asset IDs owned by the player
     */
    function getPlayerAssets(address player) external view returns (uint256[] memory) {
        return _playerAssets[player];
    }

    /**
     * @dev Get asset details
     * @param assetId The ID of the asset
     * @return GameAsset struct containing asset details
     */
    function getAssetDetails(uint256 assetId) external view returns (GameAsset memory) {
        require(_exists(assetId), "Asset does not exist");
        return _gameAssets[assetId];
    }

    /**
     * @dev Get player score
     * @param player The address of the player
     * @return The player's score
     */
    function getPlayerScore(address player) external view returns (uint256) {
        return _playerScores[player];
    }

    /**
     * @dev Get player balance
     * @param player The address of the player
     * @return The player's balance
     */
    function getPlayerBalance(address player) external view returns (uint256) {
        return _playerBalances[player];
    }

    /**
     * @dev Internal function to remove an asset from a player's list
     * @param player The address of the player
     * @param assetId The ID of the asset to remove
     */
    function _removeAssetFromPlayer(address player, uint256 assetId) private {
        uint256[] storage assets = _playerAssets[player];
        for (uint256 i = 0; i < assets.length; i++) {
            if (assets[i] == assetId) {
                assets[i] = assets[assets.length - 1];
                assets.pop();
                break;
            }
        }
    }
}
```
