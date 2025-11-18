"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-sophon.xyz
Prompt: Write a smart contract for an onchain entertainment platform that allows users to register and upload creative content, referencing Sophon's mainnet features.
Generated: DETERMINISTIC_ab4c5926271e11be
Batch ID: 20250612_145455
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

contract EntertainmentPlatform {
    // Struct to represent a content item
    struct Content {
        uint256 id;              // Unique identifier for the content
        address creator;         // Address of the content creator
        string title;            // Title of the content
        string uri;              // URI for the content location
        uint256 timestamp;       // Timestamp when the content was uploaded
        bool isActive;           // Status to check if the content is active
    }

    // State variables
    address public owner;                      // Owner of the contract
    uint256 public contentCount;               // Counter for total content uploaded
    mapping(uint256 => Content) public contents; // Mapping of content ID to Content struct
    mapping(address => uint256[]) public userContentIds; // Mapping of user addresses to their content IDs

    // Events
    event ContentUploaded(uint256 indexed id, address indexed creator, string title, string uri);
    event ContentUpdated(uint256 indexed id, string newTitle, string newUri);
    event ContentDeleted(uint256 indexed id);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to upload new content
    function uploadContent(string memory _title, string memory _uri) public {
        require(bytes(_title).length > 0, "Title must not be empty");
        require(bytes(_uri).length > 0, "URI must not be empty");

        contentCount++; // Increment the content count
        contents[contentCount] = Content(contentCount, msg.sender, _title, _uri, block.timestamp, true);
        userContentIds[msg.sender].push(contentCount); // Associate content with the user

        emit ContentUploaded(contentCount, msg.sender, _title, _uri); // Emit upload event
    }

    // Function to update existing content
    function updateContent(uint256 _id, string memory _newTitle, string memory _newUri) public {
        Content storage content = contents[_id]; // Retrieve the content
        require(content.creator == msg.sender, "Only the content creator can update this content");
        require(content.isActive, "Content is not active");
        
        // Update the content details
        content.title = _newTitle;
        content.uri = _newUri;

        emit ContentUpdated(_id, _newTitle, _newUri); // Emit update event
    }

    // Function to delete content
    function deleteContent(uint256 _id) public {
        Content storage content = contents[_id]; // Retrieve the content
        require(content.creator == msg.sender, "Only the content creator can delete this content");
        require(content.isActive, "Content already deleted");

        content.isActive = false; // Mark content as inactive

        emit ContentDeleted(_id); // Emit delete event
    }

    // Function to fetch content by ID
    function getContent(uint256 _id) public view returns (Content memory) {
        require(_id > 0 && _id <= contentCount, "Content ID is invalid");
        return contents[_id]; // Return the requested content
    }

    // Function to fetch all content IDs uploaded by a user
    function getUserContentIds(address _user) public view returns (uint256[] memory) {
        return userContentIds[_user]; // Return content IDs associated with the user
    }

    // Function to retrieve the total content count
    function totalContentCount() public view returns (uint256) {
        return contentCount; // Return the total number of uploaded content
    }
}
```
