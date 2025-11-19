"""
Generated Code Metadata:
========================
Original URL: https://metisdap.pages.dev
Prompt: Develop a decentralized application (dApp) for the Metis ecosystem that incorporates social media spotlight features for community engagement, as described in the CVP program.
Generated: DETERMINISTIC_60a7d2a2c4f181ce
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for the dApp
contract SocialMediaSpotlight is Ownable {
    // Struct to represent a spotlight post
    struct SpotlightPost {
        uint256 id;
        address creator;
        string content;
        uint256 timestamp;
        bool isActive;
    }

    // Mapping to store spotlight posts by ID
    mapping(uint256 => SpotlightPost) public spotlightPosts;
    // Counter for the number of posts
    uint256 public postCount;

    // Event emitted when a new post is created
    event PostCreated(uint256 indexed postId, address indexed creator, string content, uint256 timestamp);
    // Event emitted when a post is updated
    event PostUpdated(uint256 indexed postId, string content);
    // Event emitted when a post is deleted
    event PostDeleted(uint256 indexed postId);

    // Function to create a new spotlight post
    function createPost(string memory _content) external {
        require(bytes(_content).length > 0, "Content cannot be empty");

        postCount++;
        spotlightPosts[postCount] = SpotlightPost(postCount, msg.sender, _content, block.timestamp, true);

        emit PostCreated(postCount, msg.sender, _content, block.timestamp);
    }

    // Function to update an existing spotlight post
    function updatePost(uint256 _postId, string memory _content) external {
        SpotlightPost storage post = spotlightPosts[_postId];
        require(post.creator == msg.sender, "Only the creator can update the post");
        require(post.isActive, "Post is not active");
        require(bytes(_content).length > 0, "Content cannot be empty");

        post.content = _content;

        emit PostUpdated(_postId, _content);
    }

    // Function to delete a spotlight post
    function deletePost(uint256 _postId) external {
        SpotlightPost storage post = spotlightPosts[_postId];
        require(post.creator == msg.sender, "Only the creator can delete the post");
        require(post.isActive, "Post is already inactive");

        post.isActive = false;

        emit PostDeleted(_postId);
    }

    // Function to retrieve a spotlight post by ID
    function getPost(uint256 _postId) external view returns (SpotlightPost memory) {
        SpotlightPost memory post = spotlightPosts[_postId];
        require(post.isActive, "Post is not active");
        return post;
    }

    // Function to retrieve all active posts
    function getAllActivePosts() external view returns (SpotlightPost[] memory) {
        uint256 activeCount = 0;
        for (uint256 i = 1; i <= postCount; i++) {
            if (spotlightPosts[i].isActive) {
                activeCount++;
            }
        }

        SpotlightPost[] memory activePosts = new SpotlightPost[](activeCount);
        uint256 index = 0;
        for (uint256 i = 1; i <= postCount; i++) {
            if (spotlightPosts[i].isActive) {
                activePosts[index] = spotlightPosts[i];
                index++;
            }
        }
        return activePosts;
    }
}
```
