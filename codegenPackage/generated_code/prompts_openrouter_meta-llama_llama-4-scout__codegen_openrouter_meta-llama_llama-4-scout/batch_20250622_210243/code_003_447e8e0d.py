"""
Generated Code Metadata:
========================
Original URL: https://realio-bridge.web.app
Prompt: "Develop a smart contract for creating and managing digitally native real-world assets (RWAs) on the Realio Network."
Generated: DETERMINISTIC_447e8e0da743397a
Batch ID: 20250622_210243
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Realio RWA Contract
 * @author [Your Name]
 * @notice A smart contract for creating and managing digitally native real-world assets (RWAs) on the Realio Network.
 */
contract RealioRWA is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of asset metadata
    mapping (address => AssetMetadata) public assetMetadata;

    // Mapping of asset owners
    mapping (address => mapping (address => uint256)) public assetOwners;

    // Event emitted when a new asset is created
    event NewAsset(address indexed asset, string name, string symbol);

    // Event emitted when an asset is transferred
    event TransferAsset(address indexed from, address indexed to, uint256 amount);

    // Event emitted when an asset is burned
    event BurnAsset(address indexed from, uint256 amount);

    /**
     * @dev Struct for asset metadata
     */
    struct AssetMetadata {
        string name;
        string symbol;
        uint256 totalSupply;
    }

    /**
     * @dev Constructor for Realio RWA contract
     * @param name_ Name of the asset
     * @param symbol_ Symbol of the asset
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {
        // Initialize asset metadata
        assetMetadata[msg.sender] = AssetMetadata(name_, symbol_, 0);
    }

    /**
     * @dev Creates a new asset
     * @param name_ Name of the asset
     * @param symbol_ Symbol of the asset
     * @param amount_ Initial supply of the asset
     */
    function createAsset(string memory name_, string memory symbol_, uint256 amount_) public {
        // Check if asset already exists
        require(assetMetadata[msg.sender].totalSupply == 0, "Asset already exists");

        // Initialize asset metadata
        assetMetadata[msg.sender] = AssetMetadata(name_, symbol_, amount_);

        // Mint initial supply
        _mint(msg.sender, amount_);

        // Emit event
        emit NewAsset(msg.sender, name_, symbol_);
    }

    /**
     * @dev Transfers asset ownership
     * @param to Address of the new owner
     * @param amount Amount of asset to transfer
     */
    function transferAsset(address to, uint256 amount) public {
        // Check if sender is the owner
        require(assetOwners[msg.sender][to] == 0, "Sender is not the owner");

        // Transfer asset
        assetOwners[msg.sender][to] = amount;

        // Emit event
        emit TransferAsset(msg.sender, to, amount);
    }

    /**
     * @dev Burns asset
     * @param amount Amount of asset to burn
     */
    function burnAsset(uint256 amount) public {
        // Check if sender has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn asset
        _burn(msg.sender, amount);

        // Emit event
        emit BurnAsset(msg.sender, amount);
    }

    /**
     * @dev Gets asset metadata
     * @param asset Address of the asset
     * @return Asset metadata
     */
    function getAssetMetadata(address asset) public view returns (string memory, string memory, uint256) {
        // Check if asset exists
        require(assetMetadata[asset].totalSupply > 0, "Asset does not exist");

        // Return asset metadata
        return (assetMetadata[asset].name, assetMetadata[asset].symbol, assetMetadata[asset].totalSupply);
    }

    /**
     * @dev Gets asset balance
     * @param owner Address of the owner
     * @return Asset balance
     */
    function getAssetBalance(address owner) public view returns (uint256) {
        // Return asset balance
        return balanceOf(owner);
    }

    /**
     * @dev Overrides transfer function to ensure asset ownership
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        // Check if sender is the owner
        require(assetOwners[msg.sender][recipient] == 0, "Sender is not the owner");

        // Transfer asset
        _transfer(msg.sender, recipient, amount);

        // Emit event
        emit TransferAsset(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @dev Overrides transferFrom function to ensure asset ownership
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override nonReentrant returns (bool) {
        // Check if sender is the owner
        require(assetOwners[sender][recipient] == 0, "Sender is not the owner");

        // Transfer asset
        _transfer(sender, recipient, amount);

        // Emit event
        emit TransferAsset(sender, recipient, amount);

        return true;
    }
}
```
