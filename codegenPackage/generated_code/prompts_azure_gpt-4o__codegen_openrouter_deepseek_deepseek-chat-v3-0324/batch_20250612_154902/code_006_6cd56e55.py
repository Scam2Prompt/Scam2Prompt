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
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title RWAToken
 * @dev Tokenized Real World Asset (RWA) contract with KYC/AML compliance
 */
contract RWAToken is ERC20, AccessControl, Pausable {
    bytes32 public constant KYC_VERIFIED_ROLE = keccak256("KYC_VERIFIED_ROLE");
    bytes32 public constant COMPLIANCE_OFFICER_ROLE = keccak256("COMPLIANCE_OFFICER_ROLE");
    bytes32 public constant ASSET_MANAGER_ROLE = keccak256("ASSET_MANAGER_ROLE");

    struct Asset {
        string assetId;
        string description;
        uint256 valuation;
        bool isActive;
    }

    mapping(string => Asset) public assets;
    mapping(address => bool) public frozenAccounts;
    mapping(address => string) public investorCountries;

    event AssetAdded(string indexed assetId, string description, uint256 valuation);
    event AssetUpdated(string indexed assetId, uint256 newValuation);
    event AssetDeactivated(string indexed assetId);
    event AccountFrozen(address indexed account);
    event AccountUnfrozen(address indexed account);
    event KYCVerified(address indexed account, string country);
    event KYCRemoved(address indexed account);

    /**
     * @dev Initializes the contract
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param admin_ Address of the admin
     */
    constructor(
        string memory name_,
        string memory symbol_,
        address admin_
    ) ERC20(name_, symbol_) {
        _setupRole(DEFAULT_ADMIN_ROLE, admin_);
        _setupRole(COMPLIANCE_OFFICER_ROLE, admin_);
        _setupRole(ASSET_MANAGER_ROLE, admin_);
    }

    modifier onlyKYCVerified(address account) {
        require(hasRole(KYC_VERIFIED_ROLE, account), "RWAToken: account not KYC verified");
        _;
    }

    modifier onlyComplianceOfficer() {
        require(hasRole(COMPLIANCE_OFFICER_ROLE, msg.sender), "RWAToken: must have compliance officer role");
        _;
    }

    modifier onlyAssetManager() {
        require(hasRole(ASSET_MANAGER_ROLE, msg.sender), "RWAToken: must have asset manager role");
        _;
    }

    modifier notFrozen(address account) {
        require(!frozenAccounts[account], "RWAToken: account is frozen");
        _;
    }

    /**
     * @dev Adds a new asset
     * @param assetId Unique identifier for the asset
     * @param description Description of the asset
     * @param valuation Valuation of the asset in base units
     */
    function addAsset(
        string memory assetId,
        string memory description,
        uint256 valuation
    ) external onlyAssetManager {
        require(bytes(assetId).length > 0, "RWAToken: assetId cannot be empty");
        require(bytes(description).length > 0, "RWAToken: description cannot be empty");
        require(valuation > 0, "RWAToken: valuation must be positive");

        assets[assetId] = Asset(assetId, description, valuation, true);
        emit AssetAdded(assetId, description, valuation);
    }

    /**
     * @dev Updates asset valuation
     * @param assetId Asset identifier
     * @param newValuation New valuation amount
     */
    function updateAssetValuation(string memory assetId, uint256 newValuation) external onlyAssetManager {
        require(bytes(assetId).length > 0, "RWAToken: assetId cannot be empty");
        require(newValuation > 0, "RWAToken: valuation must be positive");
        require(assets[assetId].isActive, "RWAToken: asset is not active");

        assets[assetId].valuation = newValuation;
        emit AssetUpdated(assetId, newValuation);
    }

    /**
     * @dev Deactivates an asset
     * @param assetId Asset identifier
     */
    function deactivateAsset(string memory assetId) external onlyAssetManager {
        require(bytes(assetId).length > 0, "RWAToken: assetId cannot be empty");
        require(assets[assetId].isActive, "RWAToken: asset already inactive");

        assets[assetId].isActive = false;
        emit AssetDeactivated(assetId);
    }

    /**
     * @dev Mints new tokens for an asset
     * @param assetId Asset identifier
     * @param to Address to receive the tokens
     * @param amount Amount to mint
     */
    function mint(
        string memory assetId,
        address to,
        uint256 amount
    ) external onlyAssetManager onlyKYCVerified(to) notFrozen(to) {
        require(bytes(assetId).length > 0, "RWAToken: assetId cannot be empty");
        require(assets[assetId].isActive, "RWAToken: asset is not active");
        require(amount > 0, "RWAToken: amount must be positive");

        _mint(to, amount);
    }

    /**
     * @dev Burns tokens
     * @param from Address to burn from
     * @param amount Amount to burn
     */
    function burn(address from, uint256 amount) external onlyAssetManager notFrozen(from) {
        require(amount > 0, "RWAToken: amount must be positive");
        _burn(from, amount);
    }

    /**
     * @dev Freezes an account
     * @param account Address to freeze
     */
    function freezeAccount(address account) external onlyComplianceOfficer {
        require(!frozenAccounts[account], "RWAToken: account already frozen");
        frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    /**
     * @dev Unfreezes an account
     * @param account Address to unfreeze
     */
    function unfreezeAccount(address account) external onlyComplianceOfficer {
        require(frozenAccounts[account], "RWAToken: account not frozen");
        frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    /**
     * @dev Verifies KYC for an account
     * @param account Address to verify
     * @param country Country of residence
     */
    function verifyKYC(address account, string memory country) external onlyComplianceOfficer {
        require(bytes(country).length > 0, "RWAToken: country cannot be empty");
        _grantRole(KYC_VERIFIED_ROLE, account);
        investorCountries[account] = country;
        emit KYCVerified(account, country);
    }

    /**
     * @dev Removes KYC verification
     * @param account Address to remove verification from
     */
    function removeKYC(address account) external onlyComplianceOfficer {
        _revokeRole(KYC_VERIFIED_ROLE, account);
        delete investorCountries[account];
        emit KYCRemoved(account);
    }

    /**
     * @dev Pauses all token transfers
     */
    function pause() external onlyComplianceOfficer {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers
     */
    function unpause() external onlyComplianceOfficer {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        require(!frozenAccounts[from], "RWAToken: sender account is frozen");
        require(!frozenAccounts[to], "RWAToken: recipient account is frozen");

        if (from != address(0)) {
            require(hasRole(KYC_VERIFIED_ROLE, from), "RWAToken: sender not KYC verified");
        }
        if (to != address(0)) {
            require(hasRole(KYC_VERIFIED_ROLE, to), "RWAToken: recipient not KYC verified");
        }

        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Returns the country of an investor
     * @param account Address of the investor
     * @return Country code
     */
    function getInvestorCountry(address account) external view returns (string memory) {
        return investorCountries[account];
    }

    /**
     * @dev Returns asset details
     * @param assetId Asset identifier
     * @return description Asset description
     * @return valuation Asset valuation
     * @return isActive Asset status
     */
    function getAssetDetails(string memory assetId)
        external
        view
        returns (
            string memory description,
            uint256 valuation,
            bool isActive
        )
    {
        Asset storage asset = assets[
