"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Create a Solidity smart contract for digital content rights management on Ethereum, leveraging the platform's potential as described in unleashing Ethereum’s potential in digital content rights management.
Generated: DETERMINISTIC_d5663b835591faed
Batch ID: 20250612_154306
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

/// @title Digital Content Rights Management Contract
/// @author Your Name
/// @notice This contract manages digital content rights on the Ethereum blockchain
/// @dev This contract allows content creators to register their content and manage rights

contract DigitalContentRightsManagement {
    // Struct to represent a digital content item
    struct Content {
        uint256 id;                // Unique identifier for the content
        address creator;           // Address of the content creator
        string uri;                // URI pointing to the content
        bool isRegistered;         // Status of content registration
        uint256 rights;            // Bitmask representing rights (e.g., 1 = view, 2 = edit, etc.)
    }

    // Mapping from content ID to Content struct
    mapping(uint256 => Content) private contents;
    // Counter for content IDs
    uint256 private contentCounter;

    // Event emitted when new content is registered
    event ContentRegistered(uint256 indexed contentId, address indexed creator, string uri, uint256 rights);
    // Event emitted when rights are updated
    event RightsUpdated(uint256 indexed contentId, uint256 newRights);

    /// @notice Registers new digital content
    /// @param _uri The URI of the content
    /// @param _rights The rights associated with the content
    /// @return contentId The ID of the newly registered content
    function registerContent(string memory _uri, uint256 _rights) external returns (uint256 contentId) {
        require(bytes(_uri).length > 0, "Content URI cannot be empty");
        require(_rights > 0, "At least one right must be assigned");

        contentCounter++;
        contents[contentCounter] = Content(contentCounter, msg.sender, _uri, true, _rights);

        emit ContentRegistered(contentCounter, msg.sender, _uri, _rights);
        return contentCounter;
    }

    /// @notice Updates the rights of existing content
    /// @param _contentId The ID of the content to update
    /// @param _newRights The new rights to assign
    function updateRights(uint256 _contentId, uint256 _newRights) external {
        Content storage content = contents[_contentId];
        require(content.isRegistered, "Content not registered");
        require(content.creator == msg.sender, "Only the creator can update rights");
        require(_newRights > 0, "At least one right must be assigned");

        content.rights = _newRights;

        emit RightsUpdated(_contentId, _newRights);
    }

    /// @notice Retrieves content details by ID
    /// @param _contentId The ID of the content to retrieve
    /// @return creator The address of the content creator
    /// @return uri The URI of the content
    /// @return isRegistered The registration status of the content
    /// @return rights The rights associated with the content
    function getContent(uint256 _contentId) external view returns (address creator, string memory uri, bool isRegistered, uint256 rights) {
        Content storage content = contents[_contentId];
        require(content.isRegistered, "Content not registered");

        return (content.creator, content.uri, content.isRegistered, content.rights);
    }
}
```
