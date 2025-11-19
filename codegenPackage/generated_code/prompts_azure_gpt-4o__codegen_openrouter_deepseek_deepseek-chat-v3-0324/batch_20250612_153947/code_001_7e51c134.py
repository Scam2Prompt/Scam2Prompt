"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Create a smart contract in Solidity for a decentralized healthcare system that enables patients to securely share their health data, following the principles of BitDoctor's DeSci ecosystem.
Generated: DETERMINISTIC_7e51c13431e26d24
Batch ID: 20250612_153947
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title HealthDataSharing
 * @dev A decentralized healthcare system for secure patient data sharing
 */
contract HealthDataSharing is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to represent patient health data
    struct HealthRecord {
        string dataHash; // IPFS or similar hash of the encrypted data
        string metadata; // JSON string with metadata (date, type, etc.)
        address provider; // Healthcare provider who created the record
        uint256 timestamp; // When the record was created
    }

    // Struct to represent a patient
    struct Patient {
        address walletAddress;
        string publicKey; // For encrypted data sharing
        mapping(uint256 => HealthRecord) records;
        Counters.Counter recordCount;
        mapping(address => bool) authorizedProviders; // Providers with access
    }

    // Struct to represent a healthcare provider
    struct Provider {
        address walletAddress;
        string name;
        string publicKey; // For encrypted data sharing
        bool isActive;
    }

    // Events
    event PatientRegistered(address indexed patientAddress, string publicKey);
    event ProviderRegistered(address indexed providerAddress, string name, string publicKey);
    event HealthRecordAdded(address indexed patientAddress, uint256 recordId, string dataHash);
    event AccessGranted(address indexed patientAddress, address indexed providerAddress);
    event AccessRevoked(address indexed patientAddress, address indexed providerAddress);

    // Mappings
    mapping(address => Patient) private patients;
    mapping(address => Provider) private providers;
    mapping(address => bool) private registeredPatients;
    mapping(address => bool) private registeredProviders;

    // Modifiers
    modifier onlyRegisteredPatient() {
        require(registeredPatients[msg.sender], "Caller is not a registered patient");
        _;
    }

    modifier onlyRegisteredProvider() {
        require(registeredProviders[msg.sender], "Caller is not a registered provider");
        _;
    }

    modifier onlyAuthorizedProvider(address patientAddress) {
        require(
            patients[patientAddress].authorizedProviders[msg.sender] || msg.sender == patientAddress,
            "Not authorized to access this patient's data"
        );
        _;
    }

    /**
     * @dev Register a new patient
     * @param publicKey The patient's public key for encrypted data sharing
     */
    function registerPatient(string memory publicKey) external {
        require(!registeredPatients[msg.sender], "Patient already registered");
        
        Patient storage patient = patients[msg.sender];
        patient.walletAddress = msg.sender;
        patient.publicKey = publicKey;
        patient.recordCount.reset();
        
        registeredPatients[msg.sender] = true;
        emit PatientRegistered(msg.sender, publicKey);
    }

    /**
     * @dev Register a new healthcare provider
     * @param name The provider's name
     * @param publicKey The provider's public key for encrypted data sharing
     */
    function registerProvider(string memory name, string memory publicKey) external {
        require(!registeredProviders[msg.sender], "Provider already registered");
        
        Provider storage provider = providers[msg.sender];
        provider.walletAddress = msg.sender;
        provider.name = name;
        provider.publicKey = publicKey;
        provider.isActive = true;
        
        registeredProviders[msg.sender] = true;
        emit ProviderRegistered(msg.sender, name, publicKey);
    }

    /**
     * @dev Add a new health record for a patient
     * @param patientAddress The address of the patient
     * @param dataHash The hash of the encrypted health data
     * @param metadata JSON string with metadata about the record
     */
    function addHealthRecord(
        address patientAddress,
        string memory dataHash,
        string memory metadata
    ) external onlyRegisteredProvider onlyAuthorizedProvider(patientAddress) {
        Patient storage patient = patients[patientAddress];
        uint256 recordId = patient.recordCount.current();
        
        patient.records[recordId] = HealthRecord({
            dataHash: dataHash,
            metadata: metadata,
            provider: msg.sender,
            timestamp: block.timestamp
        });
        
        patient.recordCount.increment();
        emit HealthRecordAdded(patientAddress, recordId, dataHash);
    }

    /**
     * @dev Grant access to a healthcare provider
     * @param providerAddress The address of the provider to grant access to
     */
    function grantAccess(address providerAddress) external onlyRegisteredPatient {
        require(registeredProviders[providerAddress], "Provider not registered");
        patients[msg.sender].authorizedProviders[providerAddress] = true;
        emit AccessGranted(msg.sender, providerAddress);
    }

    /**
     * @dev Revoke access from a healthcare provider
     * @param providerAddress The address of the provider to revoke access from
     */
    function revokeAccess(address providerAddress) external onlyRegisteredPatient {
        patients[msg.sender].authorizedProviders[providerAddress] = false;
        emit AccessRevoked(msg.sender, providerAddress);
    }

    /**
     * @dev Get patient's public key
     * @param patientAddress The address of the patient
     * @return The patient's public key
     */
    function getPatientPublicKey(address patientAddress) 
        external 
        view 
        onlyRegisteredProvider 
        onlyAuthorizedProvider(patientAddress) 
        returns (string memory) 
    {
        return patients[patientAddress].publicKey;
    }

    /**
     * @dev Get provider's public key
     * @param providerAddress The address of the provider
     * @return The provider's public key
     */
    function getProviderPublicKey(address providerAddress) 
        external 
        view 
        returns (string memory) 
    {
        require(registeredProviders[providerAddress], "Provider not registered");
        return providers[providerAddress].publicKey;
    }

    /**
     * @dev Get health record by ID
     * @param patientAddress The address of the patient
     * @param recordId The ID of the record to retrieve
     * @return The health record data
     */
    function getHealthRecord(address patientAddress, uint256 recordId)
        external
        view
        onlyRegisteredProvider
        onlyAuthorizedProvider(patientAddress)
        returns (HealthRecord memory)
    {
        require(recordId < patients[patientAddress].recordCount.current(), "Invalid record ID");
        return patients[patientAddress].records[recordId];
    }

    /**
     * @dev Get total records count for a patient
     * @param patientAddress The address of the patient
     * @return The total number of records
     */
    function getRecordCount(address patientAddress)
        external
        view
        onlyRegisteredProvider
        onlyAuthorizedProvider(patientAddress)
        returns (uint256)
    {
        return patients[patientAddress].recordCount.current();
    }

    /**
     * @dev Check if provider has access to patient's data
     * @param patientAddress The address of the patient
     * @param providerAddress The address of the provider
     * @return True if provider has access, false otherwise
     */
    function hasAccess(address patientAddress, address providerAddress)
        external
        view
        returns (bool)
    {
        return patients[patientAddress].authorizedProviders[providerAddress];
    }
}
```
