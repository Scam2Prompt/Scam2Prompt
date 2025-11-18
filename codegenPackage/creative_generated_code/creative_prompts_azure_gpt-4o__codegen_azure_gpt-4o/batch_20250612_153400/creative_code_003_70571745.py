"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-masafinance.pages.dev
Prompt: Create a smart contract to issue Masa Soulbound Tokens (SBTs) for identity verification and rewards distribution.
Generated: DETERMINISTIC_70571745a3752727
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title Masa Soulbound Token Contract
 * @dev This contract allows issuing soulbound tokens (SBTs) for identity verification and rewards distribution.
 * Soulbound tokens are non-transferable and specific to an individual identity.
 */
contract MasaSoulboundToken {
    // Token metadata structure
    struct TokenInfo {
        uint256 tokenId; // Unique identifier for the token
        string metadata; // Metadata associated with the token
    }

    // Event emitted when a new SBT is issued
    event SBTIssued(address indexed recipient, uint256 tokenId, string metadata);

    // Event emitted when metadata of an SBT is updated
    event MetadataUpdated(uint256 indexed tokenId, string oldMetadata, string newMetadata);

    // Token counter for generating unique IDs
    uint256 private _tokenCounter;

    // Mapping of address to issued tokens
    mapping(address => TokenInfo[]) private _sbtHolders;

    // Mapping to prevent reissuance of SBT to a recipient
    mapping(address => bool) private _hasSBT;

    /**
     * @dev Modifier to prevent SBT reissuance to a recipient.
     */
    modifier noSBTAlready(address recipient) {
        require(!_hasSBT[recipient], "Recipient already has an SBT");
        _;
    }

    /**
     * @dev Issues a new soulbound token to the recipient.
     * @param recipient Address of the recipient.
     * @param metadata Metadata associated with the token.
     */
    function issueSBT(address recipient, string memory metadata) external noSBTAlready(recipient) {
        // Increment the token counter to generate a unique token ID
        _tokenCounter++;

        // Create a new token and associate it with the recipient's address
        TokenInfo memory newToken = TokenInfo({tokenId: _tokenCounter, metadata: metadata});
        _sbtHolders[recipient].push(newToken);

        // Mark recipient as having an SBT
        _hasSBT[recipient] = true;

        // Emit event for token issuance
        emit SBTIssued(recipient, _tokenCounter, metadata);
    }

    /**
     * @dev Allows a recipient to update metadata of their SBT.
     * @param tokenId ID of the token whose metadata is to be updated.
     * @param newMetadata New metadata to update.
     */
    function updateMetadata(uint256 tokenId, string memory newMetadata) external {
        // Find the token associated with the sender
        TokenInfo[] storage tokens = _sbtHolders[msg.sender];

        bool tokenFound = false;
        for (uint256 i = 0; i < tokens.length; i++) {
            if (tokens[i].tokenId == tokenId) {
                // Emit event for metadata update
                emit MetadataUpdated(tokenId, tokens[i].metadata, newMetadata);

                // Update the metadata of the token
                tokens[i].metadata = newMetadata;
                tokenFound = true;
                break;
            }
        }

        require(tokenFound, "Token not found or not owned by sender");
    }

    /**
     * @dev Fetches all tokens associated with a recipient.
     * @param recipient Address of the recipient.
     * @return TokenInfo[] Array of tokens owned by the recipient.
     */
    function getTokens(address recipient) external view returns (TokenInfo[] memory) {
        return _sbtHolders[recipient];
    }

    /**
     * @dev Checks whether a recipient has an SBT.
     * @param recipient Address of the recipient.
     * @return bool True if the recipient has an SBT, false otherwise.
     */
    function hasSBT(address recipient) external view returns (bool) {
        return _hasSBT[recipient];
    }
}
```
