"""
Generated Code Metadata:
========================
Original URL: https://landx.pages.dev
Prompt: "Design a smart contract in Solidity that enables the tokenization of farmland crops, ensuring the contract is secured by a farm audit, security deposit, and lien on the land."
Generated: DETERMINISTIC_47fff244d06d80ed
Batch ID: 20250622_205627
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
 * @title FarmlandCropTokenization
 * @author [Your Name]
 * @notice A smart contract for tokenizing farmland crops, secured by a farm audit, security deposit, and lien on the land.
 */
contract FarmlandCropTokenization is ReentrancyGuard, ERC20Burnable {
    using SafeMath for uint256;

    // Mapping of farm audits to their corresponding status
    mapping(address => FarmAudit) public farmAudits;

    // Mapping of land liens to their corresponding status
    mapping(address => LandLien) public landLiens;

    // Mapping of security deposits to their corresponding status
    mapping(address => SecurityDeposit) public securityDeposits;

    // Event emitted when a farm audit is created
    event FarmAuditCreated(address indexed farm, uint256 auditScore);

    // Event emitted when a land lien is created
    event LandLienCreated(address indexed landowner, uint256 lienAmount);

    // Event emitted when a security deposit is created
    event SecurityDepositCreated(address indexed farm, uint256 depositAmount);

    // Event emitted when a crop is tokenized
    event CropTokenized(address indexed farm, uint256 cropAmount);

    /**
     * @dev Struct representing a farm audit
     */
    struct FarmAudit {
        uint256 auditScore;
        bool isValid;
    }

    /**
     * @dev Struct representing a land lien
     */
    struct LandLien {
        uint256 lienAmount;
        bool isActive;
    }

    /**
     * @dev Struct representing a security deposit
     */
    struct SecurityDeposit {
        uint256 depositAmount;
        bool isRefunded;
    }

    /**
     * @dev Constructor for the FarmlandCropTokenization contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Creates a new farm audit
     * @param farm The address of the farm
     * @param auditScore The score of the farm audit
     */
    function createFarmAudit(address farm, uint256 auditScore) public {
        require(auditScore > 0, "Audit score must be greater than 0");
        farmAudits[farm] = FarmAudit(auditScore, true);
        emit FarmAuditCreated(farm, auditScore);
    }

    /**
     * @dev Creates a new land lien
     * @param landowner The address of the landowner
     * @param lienAmount The amount of the lien
     */
    function createLandLien(address landowner, uint256 lienAmount) public {
        require(lienAmount > 0, "Lien amount must be greater than 0");
        landLiens[landowner] = LandLien(lienAmount, true);
        emit LandLienCreated(landowner, lienAmount);
    }

    /**
     * @dev Creates a new security deposit
     * @param farm The address of the farm
     * @param depositAmount The amount of the security deposit
     */
    function createSecurityDeposit(address farm, uint256 depositAmount) public {
        require(depositAmount > 0, "Deposit amount must be greater than 0");
        securityDeposits[farm] = SecurityDeposit(depositAmount, false);
        emit SecurityDepositCreated(farm, depositAmount);
    }

    /**
     * @dev Tokenizes a crop
     * @param farm The address of the farm
     * @param cropAmount The amount of the crop to tokenize
     */
    function tokenizeCrop(address farm, uint256 cropAmount) public nonReentrant {
        require(farmAudits[farm].isValid, "Farm audit is not valid");
        require(landLiens[msg.sender].isActive, "Land lien is not active");
        require(!securityDeposits[farm].isRefunded, "Security deposit has been refunded");

        _mint(farm, cropAmount);
        emit CropTokenized(farm, cropAmount);
    }

    /**
     * @dev Refunds a security deposit
     * @param farm The address of the farm
     */
    function refundSecurityDeposit(address farm) public {
        require(msg.sender == farm, "Only the farm can refund the security deposit");
        require(!securityDeposits[farm].isRefunded, "Security deposit has already been refunded");

        securityDeposits[farm].isRefunded = true;
        payable(msg.sender).transfer(securityDeposits[farm].depositAmount);
    }

    /**
     * @dev Burns tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        require(msg.sender == owner(), "Only the owner can burn tokens");
        _burn(msg.sender, amount);
    }
}
```
