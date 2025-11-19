"""
Generated Code Metadata:
========================
Original URL: https://therealworldcoin.com
Prompt: Create a Solidity smart contract that enables fractional ownership of real-world assets, inspired by the TRW platform's tokenization model.
Generated: DETERMINISTIC_866ca997101b54d6
Batch ID: 20250612_151624
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
 * @title AssetFractionalizer
 * @dev A smart contract for fractional ownership of real-world assets
 */
contract AssetFractionalizer is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    struct Asset {
        string description;
        string legalDocumentHash;
        uint256 totalValue;
        uint256 totalSupply;
        address custodian;
        bool isActive;
    }

    mapping(uint256 => Asset) public assets;
    uint256 public assetCount;
    mapping(address => mapping(uint256 => uint256)) public ownerShares;

    event AssetCreated(uint256 indexed assetId, string description, uint256 totalValue);
    event SharesMinted(uint256 indexed assetId, address indexed recipient, uint256 amount);
    event SharesBurned(uint256 indexed assetId, address indexed holder, uint256 amount);
    event AssetStatusChanged(uint256 indexed assetId, bool isActive);
    event CustodianChanged(uint256 indexed assetId, address newCustodian);

    constructor() ERC20("AssetFractionalizer", "AFT") {}

    /**
     * @dev Create a new asset for fractional ownership
     * @param _description Description of the asset
     * @param _legalDocumentHash Hash of legal documentation
     * @param _totalValue Total appraised value of the asset
     * @param _initialSupply Initial number of fractional shares
     * @param _custodian Address responsible for asset custody
     */
    function createAsset(
        string memory _description,
        string memory _legalDocumentHash,
        uint256 _totalValue,
        uint256 _initialSupply,
        address _custodian
    ) external onlyOwner whenNotPaused {
        require(_totalValue > 0, "Total value must be greater than zero");
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        require(_custodian != address(0), "Invalid custodian address");

        assetCount++;
        assets[assetCount] = Asset({
            description: _description,
            legalDocumentHash: _legalDocumentHash,
            totalValue: _totalValue,
            totalSupply: _initialSupply,
            custodian: _custodian,
            isActive: true
        });

        _mint(msg.sender, _initialSupply);
        ownerShares[msg.sender][assetCount] = _initialSupply;

        emit AssetCreated(assetCount, _description, _totalValue);
    }

    /**
     * @dev Mint additional shares for an existing asset
     * @param _assetId ID of the asset
     * @param _amount Number of shares to mint
     */
    function mintShares(uint256 _assetId, uint256 _amount) external onlyOwner whenNotPaused {
        require(assets[_assetId].isActive, "Asset is not active");
        require(_amount > 0, "Amount must be greater than zero");

        assets[_assetId].totalSupply = assets[_assetId].totalSupply.add(_amount);
        _mint(msg.sender, _amount);
        ownerShares[msg.sender][_assetId] = ownerShares[msg.sender][_assetId].add(_amount);

        emit SharesMinted(_assetId, msg.sender, _amount);
    }

    /**
     * @dev Burn shares of an asset
     * @param _assetId ID of the asset
     * @param _amount Number of shares to burn
     */
    function burnShares(uint256 _assetId, uint256 _amount) external whenNotPaused {
        require(assets[_assetId].isActive, "Asset is not active");
        require(_amount > 0, "Amount must be greater than zero");
        require(ownerShares[msg.sender][_assetId] >= _amount, "Insufficient shares");

        assets[_assetId].totalSupply = assets[_assetId].totalSupply.sub(_amount);
        _burn(msg.sender, _amount);
        ownerShares[msg.sender][_assetId] = ownerShares[msg.sender][_assetId].sub(_amount);

        emit SharesBurned(_assetId, msg.sender, _amount);
    }

    /**
     * @dev Transfer shares between accounts
     * @param _assetId ID of the asset
     * @param recipient Address to receive shares
     * @param amount Number of shares to transfer
     */
    function transferShares(
        uint256 _assetId,
        address recipient,
        uint256 amount
    ) external whenNotPaused {
        require(assets[_assetId].isActive, "Asset is not active");
        require(ownerShares[msg.sender][_assetId] >= amount, "Insufficient shares");

        transfer(recipient, amount);
        ownerShares[msg.sender][_assetId] = ownerShares[msg.sender][_assetId].sub(amount);
        ownerShares[recipient][_assetId] = ownerShares[recipient][_assetId].add(amount);
    }

    /**
     * @dev Get the value per share for an asset
     * @param _assetId ID of the asset
     * @return Value per share
     */
    function getValuePerShare(uint256 _assetId) public view returns (uint256) {
        require(assets[_assetId].totalSupply > 0, "Asset has no shares");
        return assets[_assetId].totalValue.div(assets[_assetId].totalSupply);
    }

    /**
     * @dev Toggle asset active status
     * @param _assetId ID of the asset
     * @param _isActive New status
     */
    function setAssetStatus(uint256 _assetId, bool _isActive) external onlyOwner {
        require(assets[_assetId].totalSupply > 0, "Asset does not exist");
        assets[_assetId].isActive = _isActive;
        emit AssetStatusChanged(_assetId, _isActive);
    }

    /**
     * @dev Change custodian for an asset
     * @param _assetId ID of the asset
     * @param _newCustodian Address of new custodian
     */
    function changeCustodian(uint256 _assetId, address _newCustodian) external onlyOwner {
        require(_newCustodian != address(0), "Invalid custodian address");
        assets[_assetId].custodian = _newCustodian;
        emit CustodianChanged(_assetId, _newCustodian);
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
     * @dev Override ERC20 transfer to include asset-specific checks
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
