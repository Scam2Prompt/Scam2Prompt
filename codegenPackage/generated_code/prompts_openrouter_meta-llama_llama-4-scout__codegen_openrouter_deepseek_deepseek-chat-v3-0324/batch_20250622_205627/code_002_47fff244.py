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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FarmlandTokenization
 * @dev A smart contract for tokenizing farmland crops with security measures including farm audit, security deposit, and lien enforcement.
 */
contract FarmlandTokenization is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    struct FarmDetails {
        string location;
        uint256 size; // in acres
        string cropType;
        uint256 auditExpiry;
        bool isAuditPassed;
    }

    struct LienDetails {
        address lienHolder;
        uint256 lienAmount;
        bool isActive;
    }

    mapping(address => FarmDetails) public farmOwners;
    mapping(address => uint256) public securityDeposits;
    mapping(address => LienDetails) public liens;

    uint256 public constant MIN_SECURITY_DEPOSIT = 1 ether;
    uint256 public constant AUDIT_VALIDITY_PERIOD = 365 days;

    event FarmRegistered(address indexed owner, string location, uint256 size, string cropType);
    event AuditCompleted(address indexed owner, bool isPassed, uint256 expiry);
    event SecurityDeposited(address indexed owner, uint256 amount);
    event LienPlaced(address indexed owner, address indexed lienHolder, uint256 amount);
    event LienReleased(address indexed owner);
    event TokensMinted(address indexed owner, uint256 amount);
    event TokensBurned(address indexed owner, uint256 amount);

    /**
     * @dev Constructor initializes the token with a name and symbol.
     */
    constructor() ERC20("FarmlandToken", "FLT") {}

    /**
     * @dev Register farmland with necessary details.
     * @param _location Geographic location of the farm.
     * @param _size Size of the farm in acres.
     * @param _cropType Type of crop grown on the farm.
     */
    function registerFarm(string memory _location, uint256 _size, string memory _cropType) external whenNotPaused {
        require(bytes(_location).length > 0, "Location cannot be empty");
        require(_size > 0, "Farm size must be greater than 0");
        require(bytes(_cropType).length > 0, "Crop type cannot be empty");

        farmOwners[msg.sender] = FarmDetails({
            location: _location,
            size: _size,
            cropType: _cropType,
            auditExpiry: 0,
            isAuditPassed: false
        });

        emit FarmRegistered(msg.sender, _location, _size, _cropType);
    }

    /**
     * @dev Complete farm audit. Only callable by the contract owner.
     * @param _owner Address of the farm owner.
     * @param _isPassed Whether the audit passed or failed.
     */
    function completeAudit(address _owner, bool _isPassed) external onlyOwner {
        require(farmOwners[_owner].size > 0, "Farm not registered");

        farmOwners[_owner].isAuditPassed = _isPassed;
        farmOwners[_owner].auditExpiry = block.timestamp.add(AUDIT_VALIDITY_PERIOD);

        emit AuditCompleted(_owner, _isPassed, farmOwners[_owner].auditExpiry);
    }

    /**
     * @dev Deposit security amount. Must be at least MIN_SECURITY_DEPOSIT.
     */
    function depositSecurity() external payable whenNotPaused {
        require(msg.value >= MIN_SECURITY_DEPOSIT, "Deposit must be at least 1 ETH");
        require(farmOwners[msg.sender].size > 0, "Farm not registered");
        require(farmOwners[msg.sender].isAuditPassed, "Farm audit not passed");

        securityDeposits[msg.sender] = securityDeposits[msg.sender].add(msg.value);

        emit SecurityDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Place a lien on the farm. Only callable by the contract owner.
     * @param _owner Address of the farm owner.
     * @param _amount Amount of the lien.
     */
    function placeLien(address _owner, uint256 _amount) external onlyOwner {
        require(farmOwners[_owner].size > 0, "Farm not registered");
        require(securityDeposits[_owner] >= _amount, "Insufficient security deposit");

        liens[_owner] = LienDetails({
            lienHolder: msg.sender,
            lienAmount: _amount,
            isActive: true
        });

        emit LienPlaced(_owner, msg.sender, _amount);
    }

    /**
     * @dev Release a lien on the farm. Only callable by the lien holder.
     * @param _owner Address of the farm owner.
     */
    function releaseLien(address _owner) external {
        require(liens[_owner].isActive, "No active lien");
        require(liens[_owner].lienHolder == msg.sender, "Not the lien holder");

        liens[_owner].isActive = false;

        emit LienReleased(_owner);
    }

    /**
     * @dev Mint tokens for the farm owner. Only callable by the contract owner.
     * @param _owner Address of the farm owner.
     * @param _amount Amount of tokens to mint.
     */
    function mintTokens(address _owner, uint256 _amount) external onlyOwner {
        require(farmOwners[_owner].size > 0, "Farm not registered");
        require(farmOwners[_owner].isAuditPassed, "Farm audit not passed");
        require(block.timestamp <= farmOwners[_owner].auditExpiry, "Audit expired");
        require(!liens[_owner].isActive, "Active lien on farm");

        _mint(_owner, _amount);

        emit TokensMinted(_owner, _amount);
    }

    /**
     * @dev Burn tokens from the farm owner. Only callable by the contract owner.
     * @param _owner Address of the farm owner.
     * @param _amount Amount of tokens to burn.
     */
    function burnTokens(address _owner, uint256 _amount) external onlyOwner {
        require(balanceOf(_owner) >= _amount, "Insufficient token balance");

        _burn(_owner, _amount);

        emit TokensBurned(_owner, _amount);
    }

    /**
     * @dev Pause the contract. Only callable by the contract owner.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract. Only callable by the contract owner.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Withdraw security deposit. Only callable by the farm owner when no active lien exists.
     * @param _amount Amount to withdraw.
     */
    function withdrawSecurity(uint256 _amount) external whenNotPaused {
        require(securityDeposits[msg.sender] >= _amount, "Insufficient security deposit");
        require(!liens[msg.sender].isActive, "Active lien on farm");

        securityDeposits[msg.sender] = securityDeposits[msg.sender].sub(_amount);
        payable(msg.sender).transfer(_amount);
    }
}
```
