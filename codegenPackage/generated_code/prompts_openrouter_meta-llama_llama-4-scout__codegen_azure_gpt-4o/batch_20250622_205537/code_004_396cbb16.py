"""
Generated Code Metadata:
========================
Original URL: https://ethershares.blogspot.nl
Prompt: Design a basic smart contract for content ownership on a blogging platform.
Generated: DETERMINISTIC_396cbb165099684a
Batch ID: 20250622_205537
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

/**
 * @title ContentOwnership
 * @dev A smart contract for managing content ownership on a blogging platform.
 */
contract ContentOwnership {
    // Struct to represent a piece of content
    struct Content {
        uint256 id; // Unique identifier for the content
        string title; // Title of the content
        string ipfsHash; // IPFS hash for storing content off-chain
        address owner; // Address of the content owner
        uint256 timestamp; // Timestamp of when the content was created
    }

    // Mapping to store content by ID
    mapping(uint256 => Content) private contents;

    // Counter for generating unique content IDs
    uint256 private contentCounter;

    // Event emitted when new content is created
    event ContentCreated(
        uint256 indexed id,
        string title,
        string ipfsHash,
        address indexed owner,
        uint256 timestamp
    );

    // Modifier to check if the caller is the owner of the content
    modifier onlyOwner(uint256 contentId) {
        require(contents[contentId].owner == msg.sender, "Caller is not the owner");
        _;
    }

    /**
     * @dev Create new content and assign ownership to the caller.
     * @param title The title of the content.
     * @param ipfsHash The IPFS hash of the content.
     */
    function createContent(string memory title, string memory ipfsHash) external {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(ipfsHash).length > 0, "IPFS hash cannot be empty");

        contentCounter++; // Increment the content ID counter
        uint256 newContentId = contentCounter;

        // Create the content and store it in the mapping
        contents[newContentId] = Content({
            id: newContentId,
            title: title,
            ipfsHash: ipfsHash,
            owner: msg.sender,
            timestamp: block.timestamp
        });

        // Emit the ContentCreated event
        emit ContentCreated(newContentId, title, ipfsHash, msg.sender, block.timestamp);
    }

    /**
     * @dev Retrieve content details by ID.
     * @param contentId The ID of the content to retrieve.
     * @return id, title, ipfsHash, owner, timestamp
     */
    function getContent(uint256 contentId)
        external
        view
        returns (
            uint256 id,
            string memory title,
            string memory ipfsHash,
            address owner,
            uint256 timestamp
        )
    {
        require(contents[contentId].id != 0, "Content does not exist");

        Content memory content = contents[contentId];
        return (content.id, content.title, content.ipfsHash, content.owner, content.timestamp);
    }

    /**
     * @dev Transfer ownership of content to another address.
     * @param contentId The ID of the content to transfer.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(uint256 contentId, address newOwner) external onlyOwner(contentId) {
        require(newOwner != address(0), "New owner cannot be the zero address");

        contents[contentId].owner = newOwner;
    }
}
```
