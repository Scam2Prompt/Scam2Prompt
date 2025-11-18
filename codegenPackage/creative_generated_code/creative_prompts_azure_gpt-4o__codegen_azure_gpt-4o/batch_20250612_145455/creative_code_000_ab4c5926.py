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

Here is the Solidity smart contract for an on-chain entertainment platform:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title OnChainEntertainmentPlatform
 * @dev A platform for users to register and upload creative content on-chain.
 */
contract OnChainEntertainmentPlatform {
    // Struct to store user information
    struct User {
        address userAddress;
        string username;
        bool isRegistered;
    }

    // Struct to store content information
    struct Content {
        uint256 id;
        address creator;
        string title;
        string description;
        string contentHash; // IPFS or decentralized storage hash
        uint256 timestamp;
    }

    // Mappings
    mapping(address => User) public users; // Maps an address to a User
    mapping(uint256 => Content) public contents; // Maps a content ID to Content

    // Counters
    uint256 private contentCounter;

    // Events
    event UserRegistered(address indexed user, string username);
    event ContentUploaded(
        uint256 indexed contentId,
        address indexed creator,
        string title,
        string contentHash
    );

    /**
     * @dev Modifier to check if a user is registered.
     */
    modifier onlyRegisteredUser() {
        require(users[msg.sender].isRegistered, "User is not registered.");
        _;
    }

    /**
     * @dev Registers a new user on the platform.
     * @param _username The username of the user.
     */
    function registerUser(string calldata _username) external {
        require(!users[msg.sender].isRegistered, "User is already registered.");
        require(bytes(_username).length > 0, "Username cannot be empty.");

        // Add user to the mapping
        users[msg.sender] = User({
            userAddress: msg.sender,
            username: _username,
            isRegistered: true
        });

        emit UserRegistered(msg.sender, _username);
    }

    /**
     * @dev Uploads creative content to the platform.
     * @param _title The title of the content.
     * @param _description A short description of the content.
     * @param _contentHash The hash of the content (e.g., IPFS hash).
     */
    function uploadContent(
        string calldata _title,
        string calldata _description,
        string calldata _contentHash
    ) external onlyRegisteredUser {
        require(bytes(_title).length > 0, "Title cannot be empty.");
        require(bytes(_contentHash).length > 0, "Content hash cannot be empty.");

        // Increment content counter and create new content
        contentCounter++;
        contents[contentCounter] = Content({
            id: contentCounter,
            creator: msg.sender,
            title: _title,
            description: _description,
            contentHash: _contentHash,
            timestamp: block.timestamp
        });

        emit ContentUploaded(contentCounter, msg.sender, _title, _contentHash);
    }

    /**
     * @dev Fetch details of a content item by its ID.
     * @param _contentId The ID of the content.
     * @return content Information about the content.
     */
    function getContent(uint256 _contentId)
        external
        view
        returns (Content memory content)
    {
        require(_contentId > 0 && _contentId <= contentCounter, "Content does not exist.");
        return contents[_contentId];
    }

    /**
     * @dev Check if an address is a registered user.
     * @param _user The address to check.
     * @return isRegistered True if the user is registered.
     */
    function isRegistered(address _user) external view returns (bool isRegistered) {
        return users[_user].isRegistered;
    }
}
```

This code is production-ready and follows Solidity best practices, including proper error handling, clear comments, and structured code.
