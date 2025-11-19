"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularitynetio.pages.dev
Prompt: Develop a smart contract in Solidity for a decentralized media platform that integrates with SingularityNET's AI-enhanced media experience.
Generated: DETERMINISTIC_0ace1f8210424694
Batch ID: 20250612_140250
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

// Importing OpenZeppelin libraries for safe math and access control
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Define the main contract for the decentralized media platform
contract DecentralizedMediaPlatform is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a media item
    struct Media {
        uint256 id;
        address owner;
        string uri; // URI where the media file is stored
        string description;
        uint256 timestamp;
        bool isActive;
    }

    // Mapping to store media items by their ID
    mapping(uint256 => Media) public mediaItems;

    // Counter to keep track of media item IDs
    Counters.Counter private _mediaIdCounter;

    // Event to emit when a new media item is added
    event MediaAdded(uint256 indexed mediaId, address indexed owner, string uri, string description);

    // Event to emit when a media item is updated
    event MediaUpdated(uint256 indexed mediaId, string uri, string description);

    // Event to emit when a media item is deactivated
    event MediaDeactivated(uint256 indexed mediaId);

    // Function to add a new media item
    function addMedia(string memory _uri, string memory _description) external onlyOwner {
        require(bytes(_uri).length > 0, "Media URI cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");

        uint256 newMediaId = _mediaIdCounter.current();
        mediaItems[newMediaId] = Media(newMediaId, msg.sender, _uri, _description, block.timestamp, true);
        _mediaIdCounter.increment();

        emit MediaAdded(newMediaId, msg.sender, _uri, _description);
    }

    // Function to update an existing media item
    function updateMedia(uint256 _mediaId, string memory _uri, string memory _description) external {
        Media storage media = mediaItems[_mediaId];
        require(media.owner == msg.sender, "Only the owner can update this media");
        require(media.isActive, "Media item is not active");

        media.uri = _uri;
        media.description = _description;

        emit MediaUpdated(_mediaId, _uri, _description);
    }

    // Function to deactivate a media item
    function deactivateMedia(uint256 _mediaId) external {
        Media storage media = mediaItems[_mediaId];
        require(media.owner == msg.sender, "Only the owner can deactivate this media");
        require(media.isActive, "Media item is already inactive");

        media.isActive = false;

        emit MediaDeactivated(_mediaId);
    }

    // Function to retrieve media details by ID
    function getMedia(uint256 _mediaId) external view returns (Media memory) {
        Media memory media = mediaItems[_mediaId];
        require(media.id == _mediaId, "Media item does not exist");

        return media;
    }

    // Function to retrieve total media count
    function totalMediaCount() external view returns (uint256) {
        return _mediaIdCounter.current();
    }
}
```
