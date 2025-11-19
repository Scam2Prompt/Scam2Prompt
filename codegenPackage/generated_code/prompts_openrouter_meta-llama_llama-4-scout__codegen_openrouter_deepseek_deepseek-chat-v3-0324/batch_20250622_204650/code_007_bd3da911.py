"""
Generated Code Metadata:
========================
Original URL: https://ondo-foundation.pages.dev
Prompt: Design a smart contract using Solidity that enables the tokenization of real-world assets (RWAs) on a blockchain, inspired by the Ondo Foundation's work.
Generated: DETERMINISTIC_bd3da9119d916700
Batch ID: 20250622_204650
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
 * @title RWAToken
 * @dev ERC20 token representing tokenized real-world assets with compliance features
 */
contract RWAToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Struct to hold asset information
    struct Asset {
        string assetId;         // Unique identifier for the real-world asset
        uint256 value;          // Value of the asset in base units
        string legalDocument;   // IPFS hash or reference to legal documentation
        bool verified;          // Whether the asset has been verified by the issuer
    }

    // Mapping from token holder to KYC status
    mapping(address => bool) private _kycVerified;

    // Mapping from asset ID to Asset struct
    mapping(string => Asset) private _assets;

    // List of all asset IDs
    string[] private _assetIds;

    // Address of the compliance officer who can verify KYC
    address private _complianceOfficer;

    // Events
    event AssetTokenized(string indexed assetId, uint256 amount);
    event AssetVerified(string indexed assetId);
    event KYCRegistered(address indexed account);
    event ComplianceOfficerChanged(address indexed newOfficer);

    /**
     * @dev Constructor that initializes the token with basic information
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param complianceOfficer_ Address of the compliance officer
     */
    constructor(
        string memory name_,
        string memory symbol_,
        address complianceOfficer_
    ) ERC20(name_, symbol_) {
        require(complianceOfficer_ != address(0), "Compliance officer cannot be zero address");
        _complianceOfficer = complianceOfficer_;
    }

    /**
     * @dev Modifier to check if caller is the compliance officer
     */
    modifier onlyComplianceOfficer() {
        require(msg.sender == _complianceOfficer, "Caller is not the compliance officer");
        _;
    }

    /**
     * @dev Modifier to check if address is KYC verified
     */
    modifier onlyKYCVerified(address account) {
        require(_kycVerified[account], "Address is not KYC verified");
        _;
    }

    /**
     * @dev Tokenize a new real-world asset by minting tokens
     * @param assetId Unique identifier for the asset
     * @param amount Number of tokens to mint representing the asset
     * @param legalDocument Reference to legal documentation
     */
    function tokenizeAsset(
        string memory assetId,
        uint256 amount,
        string memory legalDocument
    ) external onlyOwner whenNotPaused {
        require(bytes(assetId).length > 0, "Asset ID cannot be empty");
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(legalDocument).length > 0, "Legal document reference cannot be empty");
        require(_assets[assetId].value == 0, "Asset already tokenized");

        _assets[assetId] = Asset({
            assetId: assetId,
            value: amount,
            legalDocument: legalDocument,
            verified: false
        });
        _assetIds.push(assetId);

        _mint(msg.sender, amount);
        emit AssetTokenized(assetId, amount);
    }

    /**
     * @dev Verify a tokenized asset
     * @param assetId Unique identifier for the asset to verify
     */
    function verifyAsset(string memory assetId) external onlyComplianceOfficer {
        require(_assets[assetId].value > 0, "Asset not found");
        require(!_assets[assetId].verified, "Asset already verified");

        _assets[assetId].verified = true;
        emit AssetVerified(assetId);
    }

    /**
     * @dev Register an address as KYC verified
     * @param account Address to verify
     */
    function registerKYC(address account) external onlyComplianceOfficer {
        require(account != address(0), "Cannot verify zero address");
        require(!_kycVerified[account], "Address already KYC verified");

        _kycVerified[account] = true;
        emit KYCRegistered(account);
    }

    /**
     * @dev Change the compliance officer address
     * @param newOfficer New compliance officer address
     */
    function changeComplianceOfficer(address newOfficer) external onlyOwner {
        require(newOfficer != address(0), "New officer cannot be zero address");
        _complianceOfficer = newOfficer;
        emit ComplianceOfficerChanged(newOfficer);
    }

    /**
     * @dev Override ERC20 transfer to include KYC check
     */
    function transfer(address recipient, uint256 amount) 
        public 
        override 
        whenNotPaused
        onlyKYCVerified(msg.sender)
        onlyKYCVerified(recipient)
        returns (bool) 
    {
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override ERC20 transferFrom to include KYC check
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) 
        public 
        override 
        whenNotPaused
        onlyKYCVerified(sender)
        onlyKYCVerified(recipient)
        returns (bool) 
    {
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Pause all token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause all token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get asset information by ID
     * @param assetId ID of the asset to query
     * @return Asset struct containing asset details
     */
    function getAsset(string memory assetId) external view returns (Asset memory) {
        return _assets[assetId];
    }

    /**
     * @dev Get all asset IDs
     * @return Array of all asset IDs
     */
    function getAllAssetIds() external view returns (string[] memory) {
        return _assetIds;
    }

    /**
     * @dev Check if an address is KYC verified
     * @param account Address to check
     * @return Boolean indicating KYC status
     */
    function isKYCVerified(address account) external view returns (bool) {
        return _kycVerified[account];
    }

    /**
     * @dev Get current compliance officer address
     * @return Address of the compliance officer
     */
    function getComplianceOfficer() external view returns (address) {
        return _complianceOfficer;
    }
}
```
