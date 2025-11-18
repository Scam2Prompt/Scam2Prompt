"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allianceblock-ahz.pages.dev
Prompt: Write a smart contract that enables tokenized financing of art, cars, and collectibles through on-chain options, inspired by Arkefi AG's platform on AllianceBlock.
Generated: DETERMINISTIC_aa3e9cf3d1494ca1
Batch ID: 20250612_152739
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
 * @title Tokenized Financing Contract
 * @dev A smart contract that enables tokenized financing of art, cars, and collectibles through on-chain options.
 * Inspired by Arkefi AG's platform on AllianceBlock.
 */
contract TokenizedFinancing {
    // Structure to represent an asset
    struct Asset {
        uint256 id; // Unique identifier for the asset
        string name; // Name of the asset
        string category; // Category of the asset (e.g., "Art", "Car", "Collectible")
        address owner; // Owner of the asset
        uint256 price; // Price of the asset (in wei)
        uint256 optionPremium; // Premium for the option (in wei)
        uint256 optionExpiration; // Expiration timestamp for the option
        bool isOptionActive; // Whether the option is active
    }

    // Mapping to store all assets by their ID
    mapping(uint256 => Asset) private assets;

    // Counter for asset IDs
    uint256 private assetCounter;

    // Events
    event AssetCreated(uint256 indexed id, string name, string category, address indexed owner, uint256 price);
    event OptionPurchased(uint256 indexed assetId, address indexed purchaser);
    event OptionExecuted(uint256 indexed assetId, address indexed executor);
    event OptionExpired(uint256 indexed assetId);

    // Modifier to ensure the caller is the owner of the asset
    modifier onlyOwner(uint256 assetId) {
        require(assets[assetId].owner == msg.sender, "Caller is not the owner of the asset");
        _;
    }

    // Modifier to ensure the asset exists
    modifier assetExists(uint256 assetId) {
        require(assets[assetId].owner != address(0), "Asset does not exist");
        _;
    }

    /**
     * @dev Create a new asset for tokenized financing.
     * @param name Name of the asset.
     * @param category Category of the asset.
     * @param price Price of the asset (in wei).
     * @param optionPremium Premium for the option (in wei).
     * @param optionExpiration Expiration timestamp for the option.
     */
    function createAsset(
        string memory name,
        string memory category,
        uint256 price,
        uint256 optionPremium,
        uint256 optionExpiration
    ) external {
        require(price > 0, "Price must be greater than zero");
        require(optionPremium > 0, "Option premium must be greater than zero");
        require(optionExpiration > block.timestamp, "Option expiration must be in the future");

        assetCounter++;
        assets[assetCounter] = Asset({
            id: assetCounter,
            name: name,
            category: category,
            owner: msg.sender,
            price: price,
            optionPremium: optionPremium,
            optionExpiration: optionExpiration,
            isOptionActive: false
        });

        emit AssetCreated(assetCounter, name, category, msg.sender, price);
    }

    /**
     * @dev Purchase an option for a specific asset.
     * @param assetId ID of the asset.
     */
    function purchaseOption(uint256 assetId) external payable assetExists(assetId) {
        Asset storage asset = assets[assetId];
        require(!asset.isOptionActive, "Option is already active");
        require(msg.value == asset.optionPremium, "Incorrect premium sent");

        asset.isOptionActive = true;

        emit OptionPurchased(assetId, msg.sender);
    }

    /**
     * @dev Execute the option to transfer ownership of the asset.
     * @param assetId ID of the asset.
     */
    function executeOption(uint256 assetId) external payable assetExists(assetId) {
        Asset storage asset = assets[assetId];
        require(asset.isOptionActive, "Option is not active");
        require(block.timestamp <= asset.optionExpiration, "Option has expired");
        require(msg.value == asset.price, "Incorrect price sent");

        // Transfer ownership
        address previousOwner = asset.owner;
        asset.owner = msg.sender;
        asset.isOptionActive = false;

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit OptionExecuted(assetId, msg.sender);
    }

    /**
     * @dev Expire the option if the expiration timestamp has passed.
     * @param assetId ID of the asset.
     */
    function expireOption(uint256 assetId) external assetExists(assetId) {
        Asset storage asset = assets[assetId];
        require(asset.isOptionActive, "Option is not active");
        require(block.timestamp > asset.optionExpiration, "Option has not expired yet");

        asset.isOptionActive = false;

        emit OptionExpired(assetId);
    }

    /**
     * @dev Retrieve details of an asset.
     * @param assetId ID of the asset.
     * @return Asset details.
     */
    function getAsset(uint256 assetId)
        external
        view
        assetExists(assetId)
        returns (
            uint256 id,
            string memory name,
            string memory category,
            address owner,
            uint256 price,
            uint256 optionPremium,
            uint256 optionExpiration,
            bool isOptionActive
        )
    {
        Asset memory asset = assets[assetId];
        return (
            asset.id,
            asset.name,
            asset.category,
            asset.owner,
            asset.price,
            asset.optionPremium,
            asset.optionExpiration,
            asset.isOptionActive
        );
    }
}
```
