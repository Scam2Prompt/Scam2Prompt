"""
Generated Code Metadata:
========================
Original URL: https://cyberco.pages.dev
Prompt: "Design a simple smart contract using Solidity to deploy a social application on Cyber.co's platform, utilizing its decentralized sequencer and verifier network."
Generated: DETERMINISTIC_946a4dedbcc6078c
Batch ID: 20250622_205751
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

/// @title SocialAppContract
/// @notice A simple smart contract for a social application on Cyber.co's platform
/// @dev This contract allows users to post messages and view them
contract SocialAppContract {
    // Struct to represent a post
    struct Post {
        uint256 id;            // Unique identifier for the post
        address author;        // Address of the post's author
        string content;        // Content of the post
        uint256 timestamp;     // Timestamp of when the post was created
    }

    // State variable to store posts
    Post[] private posts;

    // Event emitted when a new post is created
    event PostCreated(uint256 indexed postId, address indexed author, string content, uint256 timestamp);

    /// @notice Creates a new post
    /// @param _content The content of the post
    /// @dev Emits a PostCreated event upon successful creation
    function createPost(string calldata _content) external {
        require(bytes(_content).length > 0, "Post content cannot be empty");

        // Create a new post
        uint256 postId = posts.length;
        posts.push(Post(postId, msg.sender, _content, block.timestamp));

        // Emit the PostCreated event
        emit PostCreated(postId, msg.sender, _content, block.timestamp);
    }

    /// @notice Retrieves a post by its ID
    /// @param _postId The ID of the post to retrieve
    /// @return The post details
    /// @dev Reverts if the post ID is invalid
    function getPost(uint256 _postId) external view returns (Post memory) {
        require(_postId < posts.length, "Post does not exist");
        return posts[_postId];
    }

    /// @notice Retrieves all posts
    /// @return An array of all posts
    function getAllPosts() external view returns (Post[] memory) {
        return posts;
    }

    /// @notice Retrieves the total number of posts
    /// @return The total number of posts
    function getPostCount() external view returns (uint256) {
        return posts.length;
    }
}
```
