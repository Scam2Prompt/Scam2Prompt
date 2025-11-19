"""
Generated Code Metadata:
========================
Original URL: https://tfm.finance
Prompt: Create a smart contract example for enabling wallet-based access requirements in a DeFi application like TFM Finance.
Generated: DETERMINISTIC_34957f8f174afc96
Batch ID: 20250612_145117
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title WalletAccessControl
 * @dev Smart contract for managing wallet-based access requirements in DeFi applications
 */
contract WalletAccessControl is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Mapping from feature to allowed wallets
    mapping(bytes32 => EnumerableSet.AddressSet) private _featureWallets;

    // Mapping from wallet to features it can access
    mapping(address => EnumerableSet.AddressSet) private _walletFeatures;

    // Events
    event AccessGranted(bytes32 indexed feature, address indexed wallet);
    event AccessRevoked(bytes32 indexed feature, address indexed wallet);

    /**
     * @dev Grants access to a feature for a wallet
     * @param feature The feature identifier (keccak256 hash of feature name)
     * @param wallet The wallet address to grant access to
     */
    function grantAccess(bytes32 feature, address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address");
        
        _featureWallets[feature].add(wallet);
        _walletFeatures[wallet].add(address(bytes20(feature)));
        
        emit AccessGranted(feature, wallet);
    }

    /**
     * @dev Revokes access to a feature from a wallet
     * @param feature The feature identifier
     * @param wallet The wallet address to revoke access from
     */
    function revokeAccess(bytes32 feature, address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address");
        
        _featureWallets[feature].remove(wallet);
        _walletFeatures[wallet].remove(address(bytes20(feature)));
        
        emit AccessRevoked(feature, wallet);
    }

    /**
     * @dev Checks if a wallet has access to a feature
     * @param feature The feature identifier
     * @param wallet The wallet address to check
     * @return bool True if wallet has access, false otherwise
     */
    function hasAccess(bytes32 feature, address wallet) external view returns (bool) {
        return _featureWallets[feature].contains(wallet);
    }

    /**
     * @dev Gets all wallets with access to a feature
     * @param feature The feature identifier
     * @return address[] Array of wallet addresses
     */
    function getWalletsWithAccess(bytes32 feature) external view returns (address[] memory) {
        return _featureWallets[feature].values();
    }

    /**
     * @dev Gets all features accessible by a wallet
     * @param wallet The wallet address
     * @return bytes32[] Array of feature identifiers
     */
    function getFeaturesForWallet(address wallet) external view returns (bytes32[] memory) {
        address[] memory featureAddresses = _walletFeatures[wallet].values();
        bytes32[] memory features = new bytes32[](featureAddresses.length);
        
        for (uint256 i = 0; i < featureAddresses.length; i++) {
            features[i] = bytes32(bytes20(featureAddresses[i]));
        }
        
        return features;
    }

    /**
     * @dev Modifier to restrict access to specific features
     * @param feature The feature identifier
     */
    modifier onlyWithAccess(bytes32 feature) {
        require(_featureWallets[feature].contains(msg.sender), "Access denied");
        _;
    }
}
```
