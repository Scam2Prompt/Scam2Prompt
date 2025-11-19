"""
Generated Code Metadata:
========================
Original URL: https://app-whiterock.web.app
Prompt: Create a Solidity contract for tokenized real-world assets (RWA) trading, ensuring compliance with KYC and AML requirements, inspired by WhiteRock's legal framework.
Generated: DETERMINISTIC_6cd56e5522dc3088
Batch ID: 20250612_154902
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for KYC and AML compliance
interface IKYC {
    function isVerified(address user) external view returns (bool);
}

// Tokenized Real-World Asset (RWA) contract
contract RWAToken is ERC20, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _assetIdCounter;

    // Struct to represent an asset
    struct Asset {
        uint256 id;
        string name;
        string description;
        address owner;
        uint256 value; // in wei
        bool isActive;
    }

    // Mapping from asset ID to Asset details
    mapping(uint256 => Asset) public assets;

    // KYC contract address
    IKYC public kycContract;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 indexed assetId, string name, address indexed owner, uint256 value);
    
    // Event emitted when an asset is traded
    event AssetTraded(uint256 indexed assetId, address indexed from, address indexed to, uint256 value);

    // Modifier to check KYC compliance
    modifier onlyVerified() {
        require(kycContract.isVerified(msg.sender), "User is not KYC verified");
        _;
    }

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, address _kycContract) ERC20(name, symbol) {
        kycContract = IKYC(_kycContract);
    }

    // Function to create a new asset
    function createAsset(string memory name, string memory description, uint256 value) external onlyOwner {
        require(value > 0, "Asset value must be greater than zero");

        _assetIdCounter.increment();
        uint256 newAssetId = _assetIdCounter.current();

        assets[newAssetId] = Asset({
            id: newAssetId,
            name: name,
            description: description,
            owner: msg.sender,
            value: value,
            isActive: true
        });

        emit AssetCreated(newAssetId, name, msg.sender, value);
    }

    // Function to trade an asset
    function tradeAsset(uint256 assetId, address to) external onlyVerified {
        Asset storage asset = assets[assetId];
        require(asset.isActive, "Asset is not active");
        require(asset.owner == msg.sender, "Only the owner can trade this asset");

        // Transfer ownership
        asset.owner = to;

        emit AssetTraded(assetId, msg.sender, to, asset.value);
    }

    // Function to deactivate an asset
    function deactivateAsset(uint256 assetId) external onlyOwner {
        Asset storage asset = assets[assetId];
        require(asset.isActive, "Asset is already inactive");

        asset.isActive = false;
    }

    // Function to set a new KYC contract
    function setKYCContract(address _kycContract) external onlyOwner {
        kycContract = IKYC(_kycContract);
    }
}
```
