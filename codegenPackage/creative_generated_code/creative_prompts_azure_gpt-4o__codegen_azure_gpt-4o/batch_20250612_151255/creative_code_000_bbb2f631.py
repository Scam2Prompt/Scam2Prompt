"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-game5.pages.dev
Prompt: Write code to tokenize a physical sports memorabilia item, such as the 1991 Game 5 ball, using a blockchain platform like Ethereum or Solana. Include metadata like historical significance and provenance.
Generated: DETERMINISTIC_bbb2f631011d99df
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title SportsMemorabiliaToken
 * @dev A smart contract for tokenizing sports memorabilia on the Ethereum blockchain.
 */
contract SportsMemorabiliaToken {
    // Token metadata structure
    struct ItemMetadata {
        string name;              // Name of the memorabilia item
        string description;       // Historical significance of the item
        string provenance;        // Provenance (ownership chain, history, etc.)
    }

    // Mapping to track token IDs to metadata
    mapping(uint256 => ItemMetadata) private tokenMetadata;

    // Mapping to track token ownership
    mapping(uint256 => address) private tokenOwner;

    // Current token ID counter
    uint256 private currentTokenId;

    // Contract owner address for administrative purposes
    address private contractOwner;

    // Events
    event TokenMinted(
        uint256 indexed tokenId,
        address indexed owner,
        string name,
        string description,
        string provenance
    );

    event OwnershipTransferred(uint256 indexed tokenId, address indexed from, address indexed to);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == contractOwner, "Caller is not the contract owner");
        _;
    }

    // Modifier to restrict access to token owner
    modifier onlyTokenOwner(uint256 tokenId) {
        require(msg.sender == tokenOwner[tokenId], "Caller is not the token owner");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        contractOwner = msg.sender;
    }

    /**
     * @dev Mint a new token representing a sports memorabilia item.
     * @param name Name of the item (e.g., "1991 Game 5 Ball").
     * @param description Historical significance of the item.
     * @param provenance Provenance details (e.g., ownership history).
     */
    function mintToken(
        string memory name,
        string memory description,
        string memory provenance
    ) public onlyOwner {
        // Increment the token ID counter
        uint256 newTokenId = currentTokenId + 1;

        // Store metadata
        tokenMetadata[newTokenId] = ItemMetadata(name, description, provenance);

        // Assign ownership to the contract owner initially
        tokenOwner[newTokenId] = msg.sender;

        // Emit the minting event
        emit TokenMinted(newTokenId, msg.sender, name, description, provenance);

        // Update the token ID counter
        currentTokenId = newTokenId;
    }

    /**
     * @dev Transfer ownership of a token to another address.
     * @param tokenId The ID of the token to transfer.
     * @param newOwner Address of the new token owner.
     */
    function transferOwnership(uint256 tokenId, address newOwner) public onlyTokenOwner(tokenId) {
        // Ensure the new owner address is valid
        require(newOwner != address(0), "New owner cannot be the zero address");

        // Perform the ownership transfer
        address previousOwner = tokenOwner[tokenId];
        tokenOwner[tokenId] = newOwner;

        // Emit the ownership transfer event
        emit OwnershipTransferred(tokenId, previousOwner, newOwner);
    }

    /**
     * @dev Get metadata of a token by its ID.
     * @param tokenId The ID of the token to query.
     * @return name, description, provenance details.
     */
    function getTokenMetadata(uint256 tokenId)
        public
        view
        returns (string memory name, string memory description, string memory provenance)
    {
        require(tokenOwner[tokenId] != address(0), "Token does not exist");
        ItemMetadata memory metadata = tokenMetadata[tokenId];
        return (metadata.name, metadata.description, metadata.provenance);
    }

    /**
     * @dev Get the owner of a token by its ID.
     * @param tokenId The ID of the token to query.
     * @return Address of the token owner.
     */
    function getTokenOwner(uint256 tokenId) public view returns (address) {
        require(tokenOwner[tokenId] != address(0), "Token does not exist");
        return tokenOwner[tokenId];
    }

    /**
     * @dev Get the total number of tokens minted.
     * @return Current number of tokens minted.
     */
    function getTotalTokens() public view returns (uint256) {
        return currentTokenId;
    }
}
```
