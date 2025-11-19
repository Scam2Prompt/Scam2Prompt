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

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for issuing immutable documents
contract ImmutableDocument is ERC721Enumerable, Ownable {
    
    // Struct to hold document details
    struct Document {
        string uri; // URI to access the document data
        uint256 issueDate; // Timestamp of document issuance
    }

    // Mapping from token ID to document details
    mapping(uint256 => Document) private documents;

    // Event emitted when a document is issued
    event DocumentIssued(uint256 indexed tokenId, string uri, uint256 issueDate);

    // Constructor to initialize the smart contract
    constructor() ERC721("ImmutableDocument", "IDOC") {}

    // Function to issue a new document
    function issueDocument(string memory _uri) external onlyOwner returns (uint256) {
        // Validate the URI input
        require(bytes(_uri).length > 0, "Document URI cannot be empty");

        // Mint a new token for the document
        uint256 tokenId = totalSupply() + 1;
        _mint(msg.sender, tokenId);

        // Store document details
        documents[tokenId] = Document({
            uri: _uri,
            issueDate: block.timestamp
        });

        // Emit the document issued event
        emit DocumentIssued(tokenId, _uri, block.timestamp);

        return tokenId;
    }

    // Function to retrieve document details by token ID
    function getDocument(uint256 _tokenId) external view returns (string memory uri, uint256 issueDate) {
        // Ensure the token exists
        require(_exists(_tokenId), "Document does not exist");

        Document memory doc = documents[_tokenId];
        return (doc.uri, doc.issueDate);
    }
}
```
