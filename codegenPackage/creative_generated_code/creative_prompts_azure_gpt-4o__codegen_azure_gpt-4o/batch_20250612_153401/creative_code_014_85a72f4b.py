"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Develop a system for issuing and managing Masa's soulbound tokens, including ZettaKey, Blaze SBT, and opBNB Guide SBT.
Generated: DETERMINISTIC_85a72f4b5b5e36b9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an implementation in Solidity for a Soulbound Token (SBT) contract tailored for Masa's use case:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title MasaSoulboundToken
 * @dev Implementation of a Soulbound Token system for Masa, supporting ZettaKey, Blaze SBT, and opBNB Guide SBT.
 */
contract MasaSoulboundToken {
    // Token types enumeration
    enum TokenType { ZettaKey, BlazeSBT, opBNBGuideSBT }

    // Event emitted when a new token is issued
    event TokenIssued(address indexed recipient, TokenType tokenType, uint256 tokenId);

    // Event emitted when a token is revoked
    event TokenRevoked(address indexed recipient, TokenType tokenType, uint256 tokenId);

    // Struct representing a Soulbound Token
    struct SoulboundToken {
        bool exists; // Whether the token exists
        TokenType tokenType; // Type of the token
        uint256 id; // Unique identifier for the token
    }

    // Mapping of token owners to their respective tokens
    mapping(address => SoulboundToken[]) private _tokens;

    // Counter for token IDs
    uint256 private _tokenCounter;

    // Modifier to ensure a valid token type is passed
    modifier validTokenType(TokenType tokenType) {
        require(
            tokenType == TokenType.ZettaKey || tokenType == TokenType.BlazeSBT || tokenType == TokenType.opBNBGuideSBT,
            "Invalid token type"
        );
        _;
    }

    /**
     * @dev Issues a new Soulbound Token to the specified recipient.
     * @param recipient Address of the recipient.
     * @param tokenType Type of the token to issue.
     */
    function issueToken(address recipient, TokenType tokenType) external validTokenType(tokenType) {
        require(recipient != address(0), "Recipient address cannot be zero");

        // Generate a new token ID
        uint256 tokenId = ++_tokenCounter;

        // Create the token
        SoulboundToken memory newToken = SoulboundToken({
            exists: true,
            tokenType: tokenType,
            id: tokenId
        });

        // Store the token
        _tokens[recipient].push(newToken);

        // Emit event
        emit TokenIssued(recipient, tokenType, tokenId);
    }

    /**
     * @dev Revokes a Soulbound Token from the recipient.
     * @param recipient Address of the recipient.
     * @param tokenId ID of the token to revoke.
     */
    function revokeToken(address recipient, uint256 tokenId) external {
        require(recipient != address(0), "Recipient address cannot be zero");

        // Find and remove the token
        bool tokenFound = false;
        for (uint256 i = 0; i < _tokens[recipient].length; i++) {
            if (_tokens[recipient][i].id == tokenId && _tokens[recipient][i].exists) {
                tokenFound = true;
                _tokens[recipient][i].exists = false; // Mark as revoked
                emit TokenRevoked(recipient, _tokens[recipient][i].tokenType, tokenId);
                break;
            }
        }

        require(tokenFound, "Token not found or already revoked");
    }

    /**
     * @dev Retrieves all active tokens for a given recipient.
     * @param recipient Address of the recipient.
     * @return An array of active Soulbound Tokens.
     */
    function getTokens(address recipient) external view returns (SoulboundToken[] memory) {
        require(recipient != address(0), "Recipient address cannot be zero");

        uint256 activeCount = 0;

        // Count active tokens
        for (uint256 i = 0; i < _tokens[recipient].length; i++) {
            if (_tokens[recipient][i].exists) {
                activeCount++;
            }
        }

        // Create array for active tokens
        SoulboundToken[] memory activeTokens = new SoulboundToken[](activeCount);
        uint256 index = 0;

        for (uint256 i = 0; i < _tokens[recipient].length; i++) {
            if (_tokens[recipient][i].exists) {
                activeTokens[index] = _tokens[recipient][i];
                index++;
            }
        }

        return activeTokens;
    }
}
```

This code implements a smart contract to issue and manage Soulbound Tokens for Masa. It includes functionality for issuing, revoking, and querying tokens. All operations are validated, and events are emitted for transparency.
