"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genopets.eu
Prompt: Create a smart contract in Solidity for managing in-game assets and rewards in a blockchain-based game like Genopets.
Generated: DETERMINISTIC_7f7a39d15469140f
Batch ID: 20250612_151513
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

/// @title In-Game Asset Management Smart Contract
/// @author Your Name
/// @notice This contract manages in-game assets and rewards for a blockchain-based game.
/// @dev Uses ERC721 standard for NFT assets and allows for reward distribution.

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GameAssets is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Events for tracking asset creation and rewards
    event AssetCreated(uint256 indexed tokenId, address indexed owner);
    event RewardDistributed(address indexed to, uint256 amount);

    // Counter for generating unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping of token IDs to asset details
    struct Asset {
        string name;
        string assetType;
    }
    mapping(uint256 => Asset) public assets;

    // Mapping for user rewards
    mapping(address => uint256) public rewards;

    /// @notice Constructor to set the name and symbol of the NFT
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Create a new in-game asset
    /// @param to The address to receive the new asset
    /// @param name The name of the asset
    /// @param assetType The type of the asset
    function createAsset(address to, string memory name, string memory assetType) external onlyOwner {
        require(to != address(0), "Invalid address");
        
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the new asset
        _mint(to, tokenId);

        // Store asset details
        assets[tokenId] = Asset(name, assetType);

        emit AssetCreated(tokenId, to);
    }

    /// @notice Distribute rewards to a user
    /// @param to The address to receive the rewards
    /// @param amount The amount of rewards to distribute
    function distributeReward(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update user's rewards
        rewards[to] += amount;

        emit RewardDistributed(to, amount);
    }

    /// @notice Retrieve the details of an asset by token ID
    /// @param tokenId The token ID of the asset
    /// @return name The name of the asset
    /// @return assetType The type of the asset
    function getAssetDetails(uint256 tokenId) external view returns (string memory name, string memory assetType) {
        require(_exists(tokenId), "Asset does not exist");

        Asset storage asset = assets[tokenId];
        return (asset.name, asset.assetType);
    }

    /// @notice Get the total rewards of a user
    /// @param user The address of the user
    /// @return totalRewards The total rewards of the user
    function getUserRewards(address user) external view returns (uint256 totalRewards) {
        return rewards[user];
    }
}
```
