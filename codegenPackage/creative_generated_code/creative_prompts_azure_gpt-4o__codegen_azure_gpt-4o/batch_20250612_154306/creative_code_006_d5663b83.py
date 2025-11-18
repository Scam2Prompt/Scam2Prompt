"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-news.com
Prompt: Create a Solidity smart contract for digital content rights management on Ethereum, leveraging the platform's potential as described in unleashing Ethereum’s potential in digital content rights management.
Generated: DETERMINISTIC_d5663b835591faed
Batch ID: 20250612_154306
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
 * @title DigitalContentRightsManagement
 * @dev A smart contract for managing digital content rights on Ethereum.
 * Allows content creators to register their work, transfer ownership, and monetize it.
 */
contract DigitalContentRightsManagement {
    // Structure to represent digital content
    struct Content {
        uint256 id;                // Unique identifier for the content
        string title;              // Title of the content
        string metadataURI;        // URI pointing to the metadata of the content
        address owner;             // Current owner of the content
        uint256 price;             // Price for transferring ownership (optional)
        bool exists;               // Existence flag for content validation
    }

    // Mapping to store contents by their ID
    mapping(uint256 => Content) public contents;

    // Event emitted when new content is registered
    event ContentRegistered(
        uint256 indexed id,
        string title,
        string metadataURI,
        address indexed owner
    );

    // Event emitted when ownership of content is transferred
    event OwnershipTransferred(
        uint256 indexed id,
        address indexed from,
        address indexed to,
        uint256 price
    );

    // Counter for assigning unique IDs to content
    uint256 private contentCounter;

    /**
     * @dev Registers new digital content.
     * @param _title Title of the content.
     * @param _metadataURI URI pointing to metadata of the content.
     * @param _price Price for transferring ownership (optional).
     */
    function registerContent(string memory _title, string memory _metadataURI, uint256 _price) external {
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_metadataURI).length > 0, "Metadata URI cannot be empty");

        // Increment content counter to generate a unique ID
        contentCounter++;

        // Create and store the content
        contents[contentCounter] = Content({
            id: contentCounter,
            title: _title,
            metadataURI: _metadataURI,
            owner: msg.sender,
            price: _price,
            exists: true
        });

        // Emit event for content registration
        emit ContentRegistered(contentCounter, _title, _metadataURI, msg.sender);
    }

    /**
     * @dev Transfers ownership of digital content to another user.
     * @param _contentId ID of the content to be transferred.
     */
    function transferOwnership(uint256 _contentId) external payable {
        require(contents[_contentId].exists, "Content does not exist");
        require(contents[_contentId].owner == msg.sender, "Caller is not the owner");
        require(msg.value >= contents[_contentId].price, "Insufficient payment");

        // Transfer ownership
        address previousOwner = contents[_contentId].owner;
        contents[_contentId].owner = msg.sender;

        // Transfer payment to the previous owner
        payable(previousOwner).transfer(msg.value);

        // Emit event for ownership transfer
        emit OwnershipTransferred(_contentId, previousOwner, msg.sender, msg.value);
    }

    /**
     * @dev Retrieves content details by ID.
     * @param _contentId ID of the content to fetch details for.
     * @return Content details.
     */
    function getContent(uint256 _contentId) external view returns (Content memory) {
        require(contents[_contentId].exists, "Content does not exist");
        return contents[_contentId];
    }
}
```
