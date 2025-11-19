"""
Generated Code Metadata:
========================
Original URL: https://defihalal.org
Prompt: Suggest tools or frameworks for verifying halal compliance in smart contracts within a DeFi ecosystem.
Generated: DETERMINISTIC_9a556b860dedfbeb
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
 * @title HalalComplianceRegistry
 * @dev A smart contract registry to verify halal compliance of DeFi protocols
 */
contract HalalComplianceRegistry is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;
    
    struct ComplianceInfo {
        bool isHalalCertified;
        string certificationAuthority;
        uint256 certificationDate;
        string complianceDetails;
    }
    
    // Mapping from contract address to compliance info
    mapping(address => ComplianceInfo) private _complianceRecords;
    
    // Set of all halal-certified contracts
    EnumerableSet.AddressSet private _halalContracts;
    
    // Events
    event ContractCertified(address indexed contractAddress, string authority, uint256 date);
    event CertificationRevoked(address indexed contractAddress);
    
    /**
     * @dev Add or update a contract's halal certification
     * @param contractAddress The address of the contract to certify
     * @param authority The certifying authority
     * @param details Additional compliance details
     */
    function certifyContract(
        address contractAddress,
        string memory authority,
        string memory details
    ) external onlyOwner {
        require(contractAddress != address(0), "Invalid contract address");
        
        ComplianceInfo storage info = _complianceRecords[contractAddress];
        info.isHalalCertified = true;
        info.certificationAuthority = authority;
        info.certificationDate = block.timestamp;
        info.complianceDetails = details;
        
        _halalContracts.add(contractAddress);
        
        emit ContractCertified(contractAddress, authority, block.timestamp);
    }
    
    /**
     * @dev Revoke a contract's halal certification
     * @param contractAddress The address of the contract to revoke
     */
    function revokeCertification(address contractAddress) external onlyOwner {
        require(_complianceRecords[contractAddress].isHalalCertified, "Contract not certified");
        
        delete _complianceRecords[contractAddress];
        _halalContracts.remove(contractAddress);
        
        emit CertificationRevoked(contractAddress);
    }
    
    /**
     * @dev Check if a contract is halal certified
     * @param contractAddress The address to check
     * @return True if the contract is certified
     */
    function isHalalCertified(address contractAddress) external view returns (bool) {
        return _complianceRecords[contractAddress].isHalalCertified;
    }
    
    /**
     * @dev Get compliance information for a contract
     * @param contractAddress The address to query
     * @return ComplianceInfo struct containing certification details
     */
    function getComplianceInfo(address contractAddress) external view returns (ComplianceInfo memory) {
        require(_complianceRecords[contractAddress].isHalalCertified, "Contract not certified");
        return _complianceRecords[contractAddress];
    }
    
    /**
     * @dev Get all halal-certified contracts
     * @return Array of certified contract addresses
     */
    function getAllCertifiedContracts() external view returns (address[] memory) {
        return _halalContracts.values();
    }
    
    /**
     * @dev Get count of halal-certified contracts
     * @return Number of certified contracts
     */
    function getCertifiedCount() external view returns (uint256) {
        return _halalContracts.length();
    }
}
```
