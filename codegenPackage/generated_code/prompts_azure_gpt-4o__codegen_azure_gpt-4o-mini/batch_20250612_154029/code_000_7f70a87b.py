"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Write a smart contract for tokenization of Real World Assets (RWA) using Solidity, incorporating security best practices as described by Quecko's blockchain development services.
Generated: DETERMINISTIC_7f70a87be23ae5ae
Batch ID: 20250612_154029
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title RealWorldAssetToken
 * @dev A smart contract for tokenizing real-world assets (RWA) using ERC20 standard.
 * This contract allows the owner to mint and burn tokens representing real-world assets.
 */
contract RealWorldAssetToken is ERC20, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _assetIdCounter;

    // Mapping from asset ID to asset details
    struct Asset {
        string name;
        string description;
        uint256 value; // Value in smallest currency unit (e.g., wei)
        bool exists;
    }
    
    mapping(uint256 => Asset) private _assets;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(uint256 indexed assetId, string name, uint256 value);

    // Event emitted when an asset is burned
    event AssetBurned(uint256 indexed assetId);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Tokenizes a new real-world asset by minting tokens.
     * @param assetName The name of the asset.
     * @param assetDescription A description of the asset.
     * @param assetValue The value of the asset in smallest currency unit.
     * @param amount The amount of tokens to mint.
     */
    function tokenizeAsset(string memory assetName, string memory assetDescription, uint256 assetValue, uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(assetValue > 0, "Asset value must be greater than zero");

        // Increment the asset ID counter
        uint256 assetId = _assetIdCounter.current();
        _assetIdCounter.increment();

        // Create the asset and store it
        _assets[assetId] = Asset({
            name: assetName,
            description: assetDescription,
            value: assetValue,
            exists: true
        });

        // Mint the tokens to the owner
        _mint(msg.sender, amount);

        emit AssetTokenized(assetId, assetName, assetValue);
    }

    /**
     * @dev Burns tokens representing a real-world asset.
     * @param assetId The ID of the asset to burn.
     * @param amount The amount of tokens to burn.
     */
    function burnAsset(uint256 assetId, uint256 amount) external onlyOwner nonReentrant {
        require(_assets[assetId].exists, "Asset does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);

        emit AssetBurned(assetId);
    }

    /**
     * @dev Retrieves asset details by asset ID.
     * @param assetId The ID of the asset.
     * @return name The name of the asset.
     * @return description The description of the asset.
     * @return value The value of the asset.
     */
    function getAssetDetails(uint256 assetId) external view returns (string memory name, string memory description, uint256 value) {
        require(_assets[assetId].exists, "Asset does not exist");
        Asset memory asset = _assets[assetId];
        return (asset.name, asset.description, asset.value);
    }
}
```
