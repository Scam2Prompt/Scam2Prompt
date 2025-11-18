"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Write a Solidity-based implementation of a tamper-proof academic credential system using Mazze's blockchain, leveraging its ZK Proofs for privacy.
Generated: DETERMINISTIC_5dcf514e42c68fd7
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

// Interface for interacting with the Mazze blockchain's ZK Proofs
interface IMazzeZKProofs {
    function generateProof(bytes32 dataHash) external returns (bytes memory);
    function verifyProof(bytes memory proof, bytes32 dataHash) external returns (bool);
}

// AcademicCredential contract to manage tamper-proof credentials
contract AcademicCredential is Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Structure to represent an academic credential
    struct Credential {
        uint256 id;
        string studentName;
        string degree;
        uint256 year;
        bytes32 dataHash; // Hash of the credential data for ZK proof
    }

    // Events for credential issuance and verification
    event CredentialIssued(uint256 id, string studentName, string degree, uint256 year);
    event CredentialVerified(uint256 id, bool isValid);

    // State variables
    Counters.Counter private _credentialIdCounter;
    mapping(uint256 => Credential) private _credentials; // Mapping from credential ID to Credential struct
    IMazzeZKProofs private _zkProofsContract; // Instance of the Mazze ZK Proofs contract

    // Constructor to initialize the ZK Proofs contract address
    constructor(address zkProofsContractAddress) {
        require(zkProofsContractAddress != address(0), "Invalid ZK Proofs contract address");
        _zkProofsContract = IMazzeZKProofs(zkProofsContractAddress);
    }

    // Function to issue a new academic credential
    function issueCredential(
        string memory studentName,
        string memory degree,
        uint256 year
    ) external onlyOwner {
        // Increment the credential ID counter
        _credentialIdCounter.increment();
        uint256 newCredentialId = _credentialIdCounter.current();

        // Create the credential with a hash of its data
        bytes32 dataHash = keccak256(abi.encodePacked(studentName, degree, year));
        _credentials[newCredentialId] = Credential(newCredentialId, studentName, degree, year, dataHash);

        // Emit credential issued event
        emit CredentialIssued(newCredentialId, studentName, degree, year);
    }

    // Function to verify the academic credential using ZK Proofs
    function verifyCredential(uint256 credentialId, bytes memory proof) external {
        require(credentialId > 0 && credentialId <= _credentialIdCounter.current(), "Invalid credential ID");
        
        // Retrieve the credential
        Credential memory credential = _credentials[credentialId];
        
        // Verify the ZK proof
        bool isValid = _zkProofsContract.verifyProof(proof, credential.dataHash);
        
        // Emit credential verified event
        emit CredentialVerified(credentialId, isValid);
    }

    // Function to get credential information (for transparency)
    function getCredential(uint256 credentialId) external view returns (string memory, string memory, uint256) {
        require(credentialId > 0 && credentialId <= _credentialIdCounter.current(), "Invalid credential ID");

        Credential memory credential = _credentials[credentialId];
        return (credential.studentName, credential.degree, credential.year);
    }
}
```
