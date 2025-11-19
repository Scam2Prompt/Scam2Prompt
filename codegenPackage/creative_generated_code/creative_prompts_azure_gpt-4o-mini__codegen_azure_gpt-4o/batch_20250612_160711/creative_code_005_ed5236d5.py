"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binaryxe.org
Prompt: Write a Solidity contract that enables players to earn rewards while playing CyberDragon, detailing the mechanics of in-game asset ownership.
Generated: DETERMINISTIC_ed5236d5f8f79a13
Batch ID: 20250612_160711
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
 * @title CyberDragonRewardSystem
 * @dev A smart contract allowing players to earn rewards and maintain in-game asset ownership while playing CyberDragon.
 */
contract CyberDragonRewardSystem {
    // Owner of the contract
    address public owner;

    // Structure representing in-game assets
    struct Asset {
        uint256 id;          // Unique asset ID
        string name;         // Asset name
        address owner;       // Address of the current owner
        uint256 value;       // In-game value of the asset
    }

    // Mapping of asset IDs to Asset structs
    mapping(uint256 => Asset) public assets;

    // Mapping of player addresses to their total reward balance
    mapping(address => uint256) public rewards;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 assetId, string assetName, address assetOwner, uint256 assetValue);

    // Event emitted when a reward is earned
    event RewardEarned(address player, uint256 amount);

    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 assetId, address from, address to);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the contract owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Creates a new in-game asset and assigns it to a player.
     * @param assetId The unique asset ID.
     * @param assetName The name of the asset.
     * @param assetOwner The address of the player who owns the asset.
     * @param assetValue The value associated with the asset.
     */
    function createAsset(
        uint256 assetId,
        string memory assetName,
        address assetOwner,
        uint256 assetValue
    ) external onlyOwner {
        require(assets[assetId].id == 0, "Asset ID already exists"); // Check if asset ID is unique

        assets[assetId] = Asset(assetId, assetName, assetOwner, assetValue);
        emit AssetCreated(assetId, assetName, assetOwner, assetValue);
    }

    /**
     * @dev Allows players to earn rewards based on gameplay.
     * @param player The address of the player earning the reward.
     * @param amount The amount of reward to be credited.
     */
    function earnReward(address player, uint256 amount) external {
        require(player != address(0), "Invalid player address"); // Prevent zero address as player
        require(amount > 0, "Reward amount must be greater than zero"); // Prevent zero reward

        rewards[player] += amount;
        emit RewardEarned(player, amount);
    }

    /**
     * @dev Transfers ownership of an in-game asset from one player to another.
     * @param assetId The ID of the asset to be transferred.
     * @param to The address of the new owner.
     */
    function transferAsset(uint256 assetId, address to) external {
        require(to != address(0), "Invalid recipient address"); // Prevent zero address as recipient
        require(assets[assetId].id != 0, "Asset does not exist"); // Ensure asset exists
        require(assets[assetId].owner == msg.sender, "Caller is not the asset owner"); // Ensure only asset owner can transfer

        address previousOwner = assets[assetId].owner;
        assets[assetId].owner = to;
        emit AssetTransferred(assetId, previousOwner, to);
    }

    /**
     * @dev Retrieves the details of an in-game asset.
     * @param assetId The ID of the asset to query.
     * @return id, name, owner, value The details of the asset.
     */
    function getAssetDetails(uint256 assetId)
        external
        view
        returns (
            uint256 id,
            string memory name,
            address owner,
            uint256 value
        )
    {
        require(assets[assetId].id != 0, "Asset does not exist"); // Ensure asset exists

        Asset memory asset = assets[assetId];
        return (asset.id, asset.name, asset.owner, asset.value);
    }

    /**
     * @dev Retrieves the reward balance of a player.
     * @param player The address of the player to query.
     * @return The reward balance of the player.
     */
    function getRewardBalance(address player) external view returns (uint256) {
        return rewards[player];
    }
}
```
