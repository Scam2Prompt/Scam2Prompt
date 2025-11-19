"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skillchain.io
Prompt: Provide an example of how to set up a smart contract with Skillchain for issuing immutable documents.
Generated: DETERMINISTIC_834f39d339330d8b
Batch ID: 20250612_155538
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

/**
 * @title SkillchainDocumentIssuer
 * @dev Smart contract for issuing immutable documents on Skillchain
 */
contract SkillchainDocumentIssuer {
    
    // Event emitted when a new document is issued
    event DocumentIssued(
        address indexed issuer,
        address indexed recipient,
        string documentHash,
        uint256 timestamp
    );

    // Struct to store document information
    struct Document {
        address issuer;
        address recipient;
        string documentHash;
        uint256 timestamp;
    }

    // Mapping to store issued documents by hash
    mapping(string => Document) private documents;

    /**
     * @dev Issue a new immutable document
     * @param recipient The address of the recipient
     * @param documentHash The unique hash of the document (e.g., IPFS hash or SHA-256 hash)
     */
    function issueDocument(address recipient, string memory documentHash) external {
        require(recipient != address(0), "Recipient address cannot be zero.");
        require(bytes(documentHash).length > 0, "Document hash cannot be empty.");
        require(documents[documentHash].timestamp == 0, "Document hash already issued.");

        // Record the document in the mapping
        documents[documentHash] = Document({
            issuer: msg.sender,
            recipient: recipient,
            documentHash: documentHash,
            timestamp: block.timestamp
        });

        // Emit the event for transparency
        emit DocumentIssued(msg.sender, recipient, documentHash, block.timestamp);
    }

    /**
     * @dev Verify the issuance of a document
     * @param documentHash The unique hash of the document
     * @return issuer The address of the issuer
     * @return recipient The address of the recipient
     * @return timestamp The timestamp of issuance
     */
    function verifyDocument(string memory documentHash)
        external
        view
        returns (
            address issuer,
            address recipient,
            uint256 timestamp
        )
    {
        require(bytes(documentHash).length > 0, "Document hash cannot be empty.");
        Document memory doc = documents[documentHash];
        require(doc.timestamp != 0, "Document not found.");

        return (doc.issuer, doc.recipient, doc.timestamp);
    }

    /**
     * @dev Check if a document exists
     * @param documentHash The unique hash of the document
     * @return exists True if the document exists, false otherwise
     */
    function documentExists(string memory documentHash) external view returns (bool exists) {
        require(bytes(documentHash).length > 0, "Document hash cannot be empty.");
        return documents[documentHash].timestamp != 0;
    }
}
```
