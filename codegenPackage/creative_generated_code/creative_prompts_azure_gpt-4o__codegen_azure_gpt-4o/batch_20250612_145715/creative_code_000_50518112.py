"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipblockchain.pages.dev
Prompt: Write a smart contract using the Proof-of-Creativity Protocol to tokenize intellectual property on the Story Network blockchain.
Generated: DETERMINISTIC_50518112f25d051a
Batch ID: 20250612_145715
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
 * @title IntellectualPropertyToken
 * @dev Smart contract for tokenizing intellectual property using the Proof-of-Creativity Protocol.
 * This contract is deployed on the Story Network blockchain.
 */
contract IntellectualPropertyToken {
    // Token metadata structure
    struct TokenMetadata {
        string title; // Title of the intellectual property
        string creatorName; // Name of the creator
        string ipfsHash; // IPFS hash for decentralized storage of the related content
        uint256 timestamp; // Time of token creation
    }

    // Mapping to store token metadata
    mapping(uint256 => TokenMetadata) private tokens;

    // Mapping to track ownership of tokens
    mapping(uint256 => address) private tokenOwners;

    // Token counter for generating unique IDs
    uint256 private tokenIdCounter;

    // Event emitted when a new token is minted
    event TokenMinted(
        uint256 tokenId,
        string title,
        string creatorName,
        string ipfsHash,
        address owner,
        uint256 timestamp
    );

    /**
     * @dev Modifier to check if the caller owns the token.
     * @param tokenId ID of the token to check ownership for.
     */
    modifier onlyTokenOwner(uint256 tokenId) {
        require(tokenOwners[tokenId] == msg.sender, "Caller is not the token owner");
        _;
    }

    /**
     * @dev Mint a new intellectual property token.
     * @param title Title of the intellectual property.
     * @param creatorName Name of the creator.
     * @param ipfsHash IPFS hash of the content.
     */
    function mintToken(
        string calldata title,
        string calldata creatorName,
        string calldata ipfsHash
    ) external {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(creatorName).length > 0, "Creator name cannot be empty");
        require(bytes(ipfsHash).length > 0, "IPFS hash cannot be empty");

        uint256 newTokenId = tokenIdCounter;
        tokenIdCounter++;

        tokens[newTokenId] = TokenMetadata({
            title: title,
            creatorName: creatorName,
            ipfsHash: ipfsHash,
            timestamp: block.timestamp
        });

        tokenOwners[newTokenId] = msg.sender;

        emit TokenMinted(newTokenId, title, creatorName, ipfsHash, msg.sender, block.timestamp);
    }

    /**
     * @dev Get metadata of a token by its ID.
     * @param tokenId ID of the token to retrieve metadata for.
     * @return TokenMetadata structure containing token details.
     */
    function getTokenMetadata(uint256 tokenId)
        external
        view
        returns (TokenMetadata memory)
    {
        require(tokenOwners[tokenId] != address(0), "Token does not exist");
        return tokens[tokenId];
    }

    /**
     * @dev Get the owner of a token.
     * @param tokenId ID of the token to retrieve owner for.
     * @return Address of the token owner.
     */
    function getTokenOwner(uint256 tokenId) external view returns (address) {
        require(tokenOwners[tokenId] != address(0), "Token does not exist");
        return tokenOwners[tokenId];
    }

    /**
     * @dev Transfer ownership of a token to another address.
     * @param tokenId ID of the token to transfer.
     * @param newOwner Address of the new owner.
     */
    function transferToken(uint256 tokenId, address newOwner) external onlyTokenOwner(tokenId) {
        require(newOwner != address(0), "New owner address cannot be zero");
        tokenOwners[tokenId] = newOwner;
    }
}
```
