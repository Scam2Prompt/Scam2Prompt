"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Design a high-level architecture for an Ethereum-based digital content rights management system, leveraging the potential of blockchain technology for secure and reliable identity verification.
Generated: DETERMINISTIC_83f41e44cbf5700c
Batch ID: 20250622_211548
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
 * @title DigitalContentRightsManagement
 * @dev A smart contract for managing digital content rights using Ethereum blockchain.
 *      This contract allows creators to register content, verify ownership, and transfer rights securely.
 */
contract DigitalContentRightsManagement {
    // Struct to represent a piece of digital content
    struct Content {
        uint256 id; // Unique identifier for the content
        string title; // Title of the content
        string metadataURI; // URI pointing to metadata (e.g., IPFS link)
        address creator; // Address of the content creator
        address currentOwner; // Address of the current rights owner
        bool exists; // Flag to check if the content exists
    }

    // Mapping to store content by ID
    mapping(uint256 => Content) private contents;

    // Event emitted when new content is registered
    event ContentRegistered(
        uint256 indexed id,
        string title,
        string metadataURI,
        address indexed creator
    );

    // Event emitted when content rights are transferred
    event RightsTransferred(
        uint256 indexed id,
        address indexed from,
        address indexed to
    );

    // Counter for generating unique content IDs
    uint256 private contentCounter;

    /**
     * @dev Registers new digital content on the blockchain.
     * @param _title Title of the content.
     * @param _metadataURI URI pointing to the content's metadata.
     */
    function registerContent(string memory _title, string memory _metadataURI) external {
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_metadataURI).length > 0, "Metadata URI cannot be empty");

        contentCounter++; // Increment the content counter
        uint256 newContentId = contentCounter;

        // Create a new content entry
        contents[newContentId] = Content({
            id: newContentId,
            title: _title,
            metadataURI: _metadataURI,
            creator: msg.sender,
            currentOwner: msg.sender,
            exists: true
        });

        // Emit the ContentRegistered event
        emit ContentRegistered(newContentId, _title, _metadataURI, msg.sender);
    }

    /**
     * @dev Transfers ownership of content rights to another address.
     * @param _contentId ID of the content to transfer.
     * @param _newOwner Address of the new owner.
     */
    function transferRights(uint256 _contentId, address _newOwner) external {
        require(_newOwner != address(0), "New owner address cannot be zero");
        require(contents[_contentId].exists, "Content does not exist");
        require(contents[_contentId].currentOwner == msg.sender, "Only the current owner can transfer rights");

        // Update the current owner
        address previousOwner = contents[_contentId].currentOwner;
        contents[_contentId].currentOwner = _newOwner;

        // Emit the RightsTransferred event
        emit RightsTransferred(_contentId, previousOwner, _newOwner);
    }

    /**
     * @dev Retrieves details of a specific content by ID.
     * @param _contentId ID of the content to retrieve.
     * @return Content details including ID, title, metadata URI, creator, and current owner.
     */
    function getContent(uint256 _contentId) external view returns (Content memory) {
        require(contents[_contentId].exists, "Content does not exist");
        return contents[_contentId];
    }

    /**
     * @dev Checks if a specific address is the current owner of a content.
     * @param _contentId ID of the content to check.
     * @param _address Address to verify ownership.
     * @return True if the address is the current owner, false otherwise.
     */
    function isOwner(uint256 _contentId, address _address) external view returns (bool) {
        require(contents[_contentId].exists, "Content does not exist");
        return contents[_contentId].currentOwner == _address;
    }
}
```
