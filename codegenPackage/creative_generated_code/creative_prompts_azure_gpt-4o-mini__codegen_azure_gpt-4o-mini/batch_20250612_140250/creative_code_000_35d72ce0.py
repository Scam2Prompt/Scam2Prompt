"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Write a code snippet to implement zero-knowledge proofs for selective data disclosure in a DApp using the Data Ownership Protocol on Ethereum.
Generated: DETERMINISTIC_35d72ce05547d8b2
Batch ID: 20250612_140250
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

// Importing necessary libraries and contracts for the zero-knowledge proof implementation
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title ZeroKnowledgeProofDApp
 * @dev A DApp implementing zero-knowledge proofs for selective data disclosure using the Data Ownership Protocol
 */
contract ZeroKnowledgeProofDApp is Ownable {
    using Counters for Counters.Counter;
    
    // Counter for generating unique proof IDs
    Counters.Counter private proofIdCounter;

    // Struct to hold proof data
    struct Proof {
        uint256 id;
        address creator;
        string dataHash; // Hash of the data being proved
        bytes32 proof; // The actual zero-knowledge proof
        bool isValid; // Status of the proof
    }

    // Mapping from proof ID to Proof object
    mapping(uint256 => Proof) private proofs;

    // Event emitted when a new proof is created
    event ProofCreated(uint256 indexed proofId, address indexed creator, string dataHash);
    
    // Event emitted when a proof's validity is updated
    event ProofValidityUpdated(uint256 indexed proofId, bool isValid);

    /**
     * @dev Creates a new zero-knowledge proof.
     * @param _dataHash The hash of the data for which the proof is created.
     * @param _proof The zero-knowledge proof itself.
     */
    function createProof(string memory _dataHash, bytes32 _proof) external onlyOwner {
        require(bytes(_dataHash).length > 0, "Data hash cannot be empty");
        require(_proof != bytes32(0), "Proof cannot be empty");

        proofIdCounter.increment();
        uint256 newProofId = proofIdCounter.current();

        // Create a new proof
        proofs[newProofId] = Proof({
            id: newProofId,
            creator: msg.sender,
            dataHash: _dataHash,
            proof: _proof,
            isValid: true
        });

        emit ProofCreated(newProofId, msg.sender, _dataHash);
    }

    /**
     * @dev Validates the proof.
     * @param _proofId The ID of the proof to validate.
     * @param _isValid The validity status to set.
     */
    function validateProof(uint256 _proofId, bool _isValid) external onlyOwner {
        Proof storage proofToUpdate = proofs[_proofId];
        require(proofToUpdate.creator != address(0), "Proof does not exist");

        proofToUpdate.isValid = _isValid;

        emit ProofValidityUpdated(_proofId, _isValid);
    }

    /**
     * @dev Fetches the details of a proof by its ID.
     * @param _proofId The ID of the proof to fetch.
     * @return The Proof object containing all relevant details.
     */
    function getProof(uint256 _proofId) external view returns (Proof memory) {
        Proof memory proof = proofs[_proofId];
        require(proof.creator != address(0), "Proof does not exist");
        return proof;
    }
}
```
