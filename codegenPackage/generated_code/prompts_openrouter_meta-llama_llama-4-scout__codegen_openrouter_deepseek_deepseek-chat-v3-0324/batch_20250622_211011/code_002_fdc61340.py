"""
Generated Code Metadata:
========================
Original URL: https://grand-baseio.pages.dev
Prompt: "Generate a smart contract code for minting and managing gAssets (synthetic RWAs) on the Base blockchain, inspired by Grand Base's implementation."
Generated: DETERMINISTIC_fdc613409cac2aa0
Batch ID: 20250622_211011
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title gAsset - Synthetic Real World Asset Token
 * @dev ERC20 token representing synthetic RWAs with minting/burning functionality
 */
contract gAsset is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of authorized minters
    mapping(address => bool) private _minters;

    // Asset details
    string private _assetName;
    string private _assetSymbol;
    string private _underlyingAsset;
    string private _assetDetailsURI;

    // Supply cap (0 means unlimited)
    uint256 private _maxSupply;

    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);
    event MinterAdded(address indexed account);
    event MinterRemoved(address indexed account);
    event AssetDetailsUpdated(string newDetailsURI);

    /**
     * @dev Constructor
     * @param name_ Name of the gAsset
     * @param symbol_ Symbol of the gAsset
     * @param underlyingAsset_ Description of underlying RWA
     * @param detailsURI_ URI containing asset details/metadata
     * @param maxSupply_ Maximum supply cap (0 for unlimited)
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory underlyingAsset_,
        string memory detailsURI_,
        uint256 maxSupply_
    ) ERC20(name_, symbol_) {
        _assetName = name_;
        _assetSymbol = symbol_;
        _underlyingAsset = underlyingAsset_;
        _assetDetailsURI = detailsURI_;
        _maxSupply = maxSupply_;
    }

    modifier onlyMinter() {
        require(_minters[msg.sender], "gAsset: caller is not a minter");
        _;
    }

    /**
     * @dev Mint new tokens
     * @param to Address to receive the minted tokens
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyMinter whenNotPaused {
        require(to != address(0), "gAsset: mint to the zero address");
        require(amount > 0, "gAsset: mint amount must be positive");

        if (_maxSupply > 0) {
            require(totalSupply().add(amount) <= _maxSupply, "gAsset: exceeds max supply");
        }

        _mint(to, amount);
        emit Mint(to, amount);
    }

    /**
     * @dev Burn tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) external whenNotPaused {
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Add a minter address
     * @param account Address to be added as minter
     */
    function addMinter(address account) external onlyOwner {
        require(account != address(0), "gAsset: zero address cannot be minter");
        _minters[account] = true;
        emit MinterAdded(account);
    }

    /**
     * @dev Remove a minter address
     * @param account Address to be removed from minters
     */
    function removeMinter(address account) external onlyOwner {
        _minters[account] = false;
        emit MinterRemoved(account);
    }

    /**
     * @dev Check if address is minter
     * @param account Address to check
     * @return bool True if address is minter
     */
    function isMinter(address account) external view returns (bool) {
        return _minters[account];
    }

    /**
     * @dev Update asset details URI
     * @param newDetailsURI New URI containing asset details
     */
    function updateAssetDetails(string memory newDetailsURI) external onlyOwner {
        _assetDetailsURI = newDetailsURI;
        emit AssetDetailsUpdated(newDetailsURI);
    }

    /**
     * @dev Pause token operations
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token operations
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get underlying asset description
     * @return string Underlying asset description
     */
    function underlyingAsset() external view returns (string memory) {
        return _underlyingAsset;
    }

    /**
     * @dev Get asset details URI
     * @return string URI containing asset details
     */
    function assetDetailsURI() external view returns (string memory) {
        return _assetDetailsURI;
    }

    /**
     * @dev Get max supply
     * @return uint256 Maximum token supply (0 means unlimited)
     */
    function maxSupply() external view returns (uint256) {
        return _maxSupply;
    }
}

/**
 * @title gAssetFactory - Factory for deploying gAsset contracts
 * @dev Creates new gAsset instances
 */
contract gAssetFactory is Ownable {
    event gAssetCreated(address indexed tokenAddress, string name, string symbol);

    /**
     * @dev Create a new gAsset
     * @param name Name of the gAsset
     * @param symbol Symbol of the gAsset
     * @param underlyingAsset Description of underlying RWA
     * @param detailsURI URI containing asset details/metadata
     * @param maxSupply Maximum supply cap (0 for unlimited)
     * @return address Address of the deployed gAsset
     */
    function createGAsset(
        string memory name,
        string memory symbol,
        string memory underlyingAsset,
        string memory detailsURI,
        uint256 maxSupply
    ) external onlyOwner returns (address) {
        gAsset newToken = new gAsset(
            name,
            symbol,
            underlyingAsset,
            detailsURI,
            maxSupply
        );
        newToken.transferOwnership(msg.sender);
        
        emit gAssetCreated(address(newToken), name, symbol);
        return address(newToken);
    }
}
```
