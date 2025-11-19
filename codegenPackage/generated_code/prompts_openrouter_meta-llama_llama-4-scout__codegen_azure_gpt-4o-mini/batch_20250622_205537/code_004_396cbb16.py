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

/// @title ContentOwnership
/// @dev A smart contract for managing content ownership on a blogging platform
contract ContentOwnership {
    // Struct to represent a blog post
    struct BlogPost {
        uint256 id;                // Unique identifier for the blog post
        address owner;             // Address of the content owner
        string title;              // Title of the blog post
        string content;            // Content of the blog post
        uint256 timestamp;         // Timestamp of when the post was created
    }

    // Mapping from post ID to BlogPost
    mapping(uint256 => BlogPost) private posts;
    // Counter for post IDs
    uint256 private postIdCounter;

    // Event emitted when a new blog post is created
    event BlogPostCreated(uint256 indexed postId, address indexed owner, string title);

    // Modifier to check if the caller is the owner of the post
    modifier onlyOwner(uint256 postId) {
        require(posts[postId].owner == msg.sender, "Not the owner of this post");
        _;
    }

    /// @dev Creates a new blog post
    /// @param title The title of the blog post
    /// @param content The content of the blog post
    /// @return postId The ID of the newly created blog post
    function createBlogPost(string calldata title, string calldata content) external returns (uint256 postId) {
        postIdCounter++;
        postId = postIdCounter;

        // Create a new blog post
        posts[postId] = BlogPost({
            id: postId,
            owner: msg.sender,
            title: title,
            content: content,
            timestamp: block.timestamp
        });

        emit BlogPostCreated(postId, msg.sender, title);
    }

    /// @dev Retrieves a blog post by its ID
    /// @param postId The ID of the blog post
    /// @return owner The owner of the blog post
    /// @return title The title of the blog post
    /// @return content The content of the blog post
    /// @return timestamp The timestamp of when the post was created
    function getBlogPost(uint256 postId) external view returns (address owner, string memory title, string memory content, uint256 timestamp) {
        BlogPost storage post = posts[postId];
        require(post.owner != address(0), "Post does not exist");

        return (post.owner, post.title, post.content, post.timestamp);
    }

    /// @dev Updates the content of an existing blog post
    /// @param postId The ID of the blog post to update
    /// @param newContent The new content for the blog post
    function updateBlogPost(uint256 postId, string calldata newContent) external onlyOwner(postId) {
        require(bytes(newContent).length > 0, "Content cannot be empty");
        posts[postId].content = newContent;
    }

    /// @dev Deletes a blog post
    /// @param postId The ID of the blog post to delete
    function deleteBlogPost(uint256 postId) external onlyOwner(postId) {
        delete posts[postId];
    }
}
```
