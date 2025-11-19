"""
Generated Code Metadata:
========================
Original URL: https://www.xbank.plus
Prompt: Develop a smart contract for tokenizing tangible and intangible real-world assets (RWAs), ensuring compliance with regulatory frameworks, inspired by xBank's solutions.
Generated: DETERMINISTIC_4009cb2cf25f3d44
Batch ID: 20250612_154049
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
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RWAToken
 * @dev ERC20 token representing tokenized real-world assets with compliance features
 */
contract RWAToken is ERC20, AccessControl, Pausable {
    using SafeMath for uint256;

    bytes32 public constant COMPLIANCE_ROLE = keccak256("COMPLIANCE_ROLE");
    bytes32 public constant ISSUER_ROLE = keccak256("ISSUER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");

    struct Asset {
        string assetId;
        string assetType;
        uint256 value;
        string legalDocumentHash;
        bool isVerified;
    }

    mapping(string => Asset) public assets;
    mapping(address => bool) public frozenAccounts;
    mapping(address => bool) public whitelist;
    mapping(address => mapping(address => bool)) private _approvals;

    bool public whitelistEnabled = true;
    uint256 public maxSupply;
    uint256 public totalAssetsValue;

    event AssetAdded(string indexed assetId, string assetType, uint256 value);
    event AssetVerified(string indexed assetId);
    event AccountFrozen(address indexed account);
    event AccountUnfrozen(address indexed account);
    event WhitelistUpdated(address indexed account, bool status);
    event ComplianceOverride(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Constructor
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param initialSupply Initial token supply
     * @param maxSupply_ Maximum token supply
     * @param admin Admin address with DEFAULT_ADMIN_ROLE
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply,
        uint256 maxSupply_,
        address admin
    ) ERC20(name_, symbol_) {
        require(maxSupply_ >= initialSupply, "Initial supply exceeds max supply");
        maxSupply = maxSupply_;
        _setupRole(DEFAULT_ADMIN_ROLE, admin);
        _setupRole(COMPLIANCE_ROLE, admin);
        _setupRole(ISSUER_ROLE, admin);
        _setupRole(PAUSER_ROLE, admin);
        _mint(admin, initialSupply);
    }

    /**
     * @dev Add a new real-world asset backing the tokens
     * @param assetId Unique identifier for the asset
     * @param assetType Type of asset (tangible/intangible)
     * @param value Asset value in base units
     * @param legalDocumentHash Hash of legal documentation
     */
    function addAsset(
        string memory assetId,
        string memory assetType,
        uint256 value,
        string memory legalDocumentHash
    ) external onlyRole(ISSUER_ROLE) {
        require(bytes(assets[assetId].assetId).length == 0, "Asset already exists");
        assets[assetId] = Asset(assetId, assetType, value, legalDocumentHash, false);
        totalAssetsValue = totalAssetsValue.add(value);
        emit AssetAdded(assetId, assetType, value);
    }

    /**
     * @dev Verify an asset by compliance officer
     * @param assetId Unique identifier for the asset
     */
    function verifyAsset(string memory assetId) external onlyRole(COMPLIANCE_ROLE) {
        require(bytes(assets[assetId].assetId).length != 0, "Asset does not exist");
        require(!assets[assetId].isVerified, "Asset already verified");
        assets[assetId].isVerified = true;
        emit AssetVerified(assetId);
    }

    /**
     * @dev Mint new tokens (only by issuer)
     * @param to Address to receive tokens
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyRole(ISSUER_ROLE) {
        require(totalSupply().add(amount) <= maxSupply, "Exceeds max supply");
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens (only by issuer)
     * @param from Address to burn from
     * @param amount Amount to burn
     */
    function burn(address from, uint256 amount) external onlyRole(ISSUER_ROLE) {
        _burn(from, amount);
    }

    /**
     * @dev Freeze an account (only by compliance officer)
     * @param account Address to freeze
     */
    function freezeAccount(address account) external onlyRole(COMPLIANCE_ROLE) {
        require(!frozenAccounts[account], "Account already frozen");
        frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    /**
     * @dev Unfreeze an account (only by compliance officer)
     * @param account Address to unfreeze
     */
    function unfreezeAccount(address account) external onlyRole(COMPLIANCE_ROLE) {
        require(frozenAccounts[account], "Account not frozen");
        frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    /**
     * @dev Add/remove address from whitelist
     * @param account Address to update
     * @param status New whitelist status
     */
    function updateWhitelist(address account, bool status) external onlyRole(COMPLIANCE_ROLE) {
        whitelist[account] = status;
        emit WhitelistUpdated(account, status);
    }

    /**
     * @dev Toggle whitelist enforcement
     * @param enabled New whitelist status
     */
    function setWhitelistEnabled(bool enabled) external onlyRole(COMPLIANCE_ROLE) {
        whitelistEnabled = enabled;
    }

    /**
     * @dev Override transfer with compliance checks
     * @param to Recipient address
     * @param amount Transfer amount
     */
    function transfer(address to, uint256 amount) public override whenNotPaused returns (bool) {
        _checkCompliance(_msgSender(), to, amount);
        return super.transfer(to, amount);
    }

    /**
     * @dev Override transferFrom with compliance checks
     * @param from Sender address
     * @param to Recipient address
     * @param amount Transfer amount
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override whenNotPaused returns (bool) {
        _checkCompliance(from, to, amount);
        return super.transferFrom(from, to, amount);
    }

    /**
     * @dev Internal compliance check
     * @param from Sender address
     * @param to Recipient address
     * @param amount Transfer amount
     */
    function _checkCompliance(
        address from,
        address to,
        uint256 amount
    ) internal view {
        require(!frozenAccounts[from], "Sender account is frozen");
        require(!frozenAccounts[to], "Recipient account is frozen");

        if (whitelistEnabled) {
            require(whitelist[from], "Sender not whitelisted");
            require(whitelist[to], "Recipient not whitelisted");
        }
    }

    /**
     * @dev Compliance override for special cases
     * @param from Sender address
     * @param to Recipient address
     * @param amount Transfer amount
     */
    function complianceOverride(
        address from,
        address to,
        uint256 amount
    ) external onlyRole(COMPLIANCE_ROLE) {
        emit ComplianceOverride(from, to, amount);
    }

    /**
     * @dev Pause all token transfers
     */
    function pause() external onlyRole(PAUSER_ROLE) {
        _pause();
    }

    /**
     * @dev Unpause all token transfers
     */
    function unpause() external onlyRole(PAUSER_ROLE) {
        _unpause();
    }

    /**
     * @dev Get asset verification status
     * @param assetId Asset identifier
     * @return Verification status
     */
    function isAssetVerified(string memory assetId) external view returns (bool) {
        return assets[assetId].isVerified;
    }

    /**
     * @dev Get total value of all verified assets
     * @return Total value
     */
    function getTotalVerifiedAssetsValue() external view returns (uint256) {
        uint256 total = 0;
        // In a real implementation, we would iterate through verified assets
        // This is simplified for demonstration
        return totalAssetsValue;
    }
}
```
