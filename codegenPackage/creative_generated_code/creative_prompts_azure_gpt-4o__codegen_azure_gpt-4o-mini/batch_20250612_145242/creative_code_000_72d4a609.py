"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-ae.web.app
Prompt: Write a smart contract in Solidity that enables tokenization of real-world assets like real estate or art, similar to the functionality described in the Rexas Finance ecosystem.
Generated: DETERMINISTIC_72d4a609ec3b533d
Batch ID: 20250612_145242
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title AssetToken
 * @dev This contract allows the tokenization of real-world assets.
 * Each asset can be represented as an ERC20 token.
 */
contract AssetToken is ERC20, Ownable {
    using Counters for Counters.Counter;
    
    // Counter to keep track of asset IDs
    Counters.Counter private _assetIdCounter;

    // Struct to represent an asset
    struct Asset {
        uint256 id;
        string name;
        string description;
        address owner;
        uint256 value; // in wei
        bool exists;
    }

    // Mapping from asset ID to Asset struct
    mapping(uint256 => Asset) private _assets;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(uint256 assetId, string name, address owner, uint256 value);
    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 assetId, address from, address to, uint256 tokens);

    // Modifier to check if the asset exists
    modifier assetExists(uint256 assetId) {
        require(_assets[assetId].exists, "Asset does not exist");
        _;
    }

    /**
     * @dev Constructor to initialize the ERC20 token with a name and symbol.
     * @param name Token name.
     * @param symbol Token symbol.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Tokenize a real-world asset.
     * @param name The name of the asset.
     * @param description A description of the asset.
     * @param value The value of the asset in wei.
     * @param totalTokens The total number of tokens to mint for the asset.
     */
    function tokenizeAsset(string memory name, string memory description, uint256 value, uint256 totalTokens) external onlyOwner {
        require(value > 0, "Asset value must be greater than zero");
        require(totalTokens > 0, "Total tokens must be greater than zero");

        // Increment asset ID and create new asset
        uint256 assetId = _assetIdCounter.current();
        _assetIdCounter.increment();

        _assets[assetId] = Asset({
            id: assetId,
            name: name,
            description: description,
            owner: msg.sender,
            value: value,
            exists: true
        });

        // Mint tokens to the owner
        _mint(msg.sender, totalTokens);

        emit AssetTokenized(assetId, name, msg.sender, value);
    }

    /**
     * @dev Transfer ownership of an asset to a new address.
     * @param assetId The ID of the asset to transfer.
     * @param to The address to transfer the asset to.
     * @param tokens The number of tokens to transfer.
     */
    function transferAsset(uint256 assetId, address to, uint256 tokens) external assetExists(assetId) {
        require(msg.sender == _assets[assetId].owner, "Only the asset owner can transfer");
        require(to != address(0), "Invalid address");
        require(tokens <= balanceOf(msg.sender), "Insufficient token balance");

        // Transfer tokens and update asset owner
        _transfer(msg.sender, to, tokens);
        _assets[assetId].owner = to;

        emit AssetTransferred(assetId, msg.sender, to, tokens);
    }

    /**
     * @dev Get asset details by ID.
     * @param assetId The ID of the asset.
     * @return The asset details.
     */
    function getAsset(uint256 assetId) external view assetExists(assetId) returns (Asset memory) {
        return _assets[assetId];
    }
}
```
