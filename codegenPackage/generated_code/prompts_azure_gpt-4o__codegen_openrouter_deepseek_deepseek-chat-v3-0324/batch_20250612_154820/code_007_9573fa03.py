"""
Generated Code Metadata:
========================
Original URL: https://binaryxs.org
Prompt: Write a Solidity smart contract for managing in-game assets and consumption scenarios using BNX tokens, ensuring scalability and security.
Generated: DETERMINISTIC_9573fa03ee2117ef
Batch ID: 20250612_154820
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GameAssetManager is Ownable, ReentrancyGuard {
    // BNX token interface
    IERC20 public bnxToken;

    // Asset structure
    struct Asset {
        uint256 id;
        string name;
        uint256 price;
        uint256 maxSupply;
        uint256 totalMinted;
        bool isConsumable;
    }

    // Player's asset balance
    struct PlayerAsset {
        uint256 assetId;
        uint256 balance;
    }

    // Mapping from asset ID to Asset
    mapping(uint256 => Asset) public assets;

    // Mapping from player address to their assets
    mapping(address => PlayerAsset[]) public playerAssets;

    // Mapping from player address to asset ID to index in playerAssets array
    mapping(address => mapping(uint256 => uint256)) public playerAssetIndex;

    // Events
    event AssetCreated(uint256 indexed assetId, string name, uint256 price, uint256 maxSupply, bool isConsumable);
    event AssetPurchased(address indexed player, uint256 indexed assetId, uint256 amount);
    event AssetConsumed(address indexed player, uint256 indexed assetId, uint256 amount);

    constructor(address _bnxTokenAddress) {
        require(_bnxTokenAddress != address(0), "Invalid token address");
        bnxToken = IERC20(_bnxTokenAddress);
    }

    /**
     * @dev Create a new in-game asset
     * @param _assetId Unique ID for the asset
     * @param _name Name of the asset
     * @param _price Price in BNX tokens
     * @param _maxSupply Maximum supply (0 for unlimited)
     * @param _isConsumable Whether the asset is consumable
     */
    function createAsset(
        uint256 _assetId,
        string memory _name,
        uint256 _price,
        uint256 _maxSupply,
        bool _isConsumable
    ) external onlyOwner {
        require(assets[_assetId].id == 0, "Asset already exists");
        require(_price > 0, "Price must be greater than 0");

        assets[_assetId] = Asset({
            id: _assetId,
            name: _name,
            price: _price,
            maxSupply: _maxSupply,
            totalMinted: 0,
            isConsumable: _isConsumable
        });

        emit AssetCreated(_assetId, _name, _price, _maxSupply, _isConsumable);
    }

    /**
     * @dev Purchase an asset
     * @param _assetId ID of the asset to purchase
     * @param _amount Amount to purchase
     */
    function purchaseAsset(uint256 _assetId, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        Asset storage asset = assets[_assetId];
        require(asset.id != 0, "Asset does not exist");
        require(asset.maxSupply == 0 || asset.totalMinted + _amount <= asset.maxSupply, "Exceeds max supply");

        uint256 totalCost = asset.price * _amount;
        require(bnxToken.balanceOf(msg.sender) >= totalCost, "Insufficient BNX balance");
        require(bnxToken.allowance(msg.sender, address(this)) >= totalCost, "Insufficient allowance");

        // Transfer BNX tokens from player to contract
        bool success = bnxToken.transferFrom(msg.sender, address(this), totalCost);
        require(success, "BNX transfer failed");

        // Update asset stats
        asset.totalMinted += _amount;

        // Update player's asset balance
        _addAssetToPlayer(msg.sender, _assetId, _amount);

        emit AssetPurchased(msg.sender, _assetId, _amount);
    }

    /**
     * @dev Consume an asset (if consumable)
     * @param _assetId ID of the asset to consume
     * @param _amount Amount to consume
     */
    function consumeAsset(uint256 _assetId, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        Asset storage asset = assets[_assetId];
        require(asset.id != 0, "Asset does not exist");
        require(asset.isConsumable, "Asset is not consumable");

        uint256 playerAssetIndex = playerAssetIndex[msg.sender][_assetId];
        require(playerAssetIndex != 0, "Player does not own this asset");
        
        PlayerAsset storage playerAsset = playerAssets[msg.sender][playerAssetIndex - 1];
        require(playerAsset.balance >= _amount, "Insufficient asset balance");

        // Update player's asset balance
        playerAsset.balance -= _amount;

        // If balance reaches zero, remove from player's assets
        if (playerAsset.balance == 0) {
            _removeAssetFromPlayer(msg.sender, _assetId, playerAssetIndex - 1);
        }

        emit AssetConsumed(msg.sender, _assetId, _amount);
    }

    /**
     * @dev Get player's asset balance
     * @param _player Player address
     * @param _assetId Asset ID
     * @return Balance of the asset
     */
    function getPlayerAssetBalance(address _player, uint256 _assetId) external view returns (uint256) {
        uint256 index = playerAssetIndex[_player][_assetId];
        if (index == 0) {
            return 0;
        }
        return playerAssets[_player][index - 1].balance;
    }

    /**
     * @dev Get all assets owned by a player
     * @param _player Player address
     * @return Array of PlayerAsset structs
     */
    function getPlayerAssets(address _player) external view returns (PlayerAsset[] memory) {
        return playerAssets[_player];
    }

    /**
     * @dev Withdraw BNX tokens from contract (owner only)
     * @param _amount Amount to withdraw
     */
    function withdrawBNX(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(bnxToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        
        bool success = bnxToken.transfer(owner(), _amount);
        require(success, "BNX transfer failed");
    }

    // Internal functions

    /**
     * @dev Add asset to player's inventory
     * @param _player Player address
     * @param _assetId Asset ID
     * @param _amount Amount to add
     */
    function _addAssetToPlayer(address _player, uint256 _assetId, uint256 _amount) internal {
        uint256 index = playerAssetIndex[_player][_assetId];
        
        if (index == 0) {
            // Asset not owned by player, add new entry
            playerAssets[_player].push(PlayerAsset({
                assetId: _assetId,
                balance: _amount
            }));
            playerAssetIndex[_player][_assetId] = playerAssets[_player].length;
        } else {
            // Asset already owned by player, increase balance
            playerAssets[_player][index - 1].balance += _amount;
        }
    }

    /**
     * @dev Remove asset from player's inventory
     * @param _player Player address
     * @param _assetId Asset ID
     * @param _index Index in playerAssets array
     */
    function _removeAssetFromPlayer(address _player, uint256 _assetId, uint256 _index) internal {
        uint256 lastIndex = playerAssets[_player].length - 1;
        
        if (_index != lastIndex) {
            // Move last element to the deleted spot
            PlayerAsset memory lastAsset = playerAssets[_player][lastIndex];
            playerAssets[_player][_index] = lastAsset;
            playerAssetIndex[_player][lastAsset.assetId] = _index + 1;
        }
        
        // Remove last element
        playerAssets[_player].pop();
        delete playerAssetIndex[_player][_assetId];
    }
}
```
