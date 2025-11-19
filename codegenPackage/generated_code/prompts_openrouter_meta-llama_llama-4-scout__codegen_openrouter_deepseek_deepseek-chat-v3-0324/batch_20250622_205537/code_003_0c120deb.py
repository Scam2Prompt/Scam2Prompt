"""
Generated Code Metadata:
========================
Original URL: https://ethershares.blogspot.nl
Prompt: How can I use ethers to create a decentralized blog, and what are the advantages and limitations?
Generated: DETERMINISTIC_0c120debafb89701
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

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DecentralizedBlog is Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _postIds;

    struct Post {
        uint256 id;
        address author;
        string title;
        string content;
        uint256 timestamp;
    }

    mapping(uint256 => Post) private _posts;
    mapping(address => uint256[]) private _userPosts;

    event PostCreated(uint256 id, address author, string title);
    event PostUpdated(uint256 id, string title);
    event PostDeleted(uint256 id);

    modifier onlyPostAuthor(uint256 postId) {
        require(_posts[postId].author == msg.sender, "Not the post author");
        _;
    }

    function createPost(string memory title, string memory content) external {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(content).length > 0, "Content cannot be empty");

        _postIds.increment();
        uint256 newPostId = _postIds.current();

        Post memory newPost = Post({
            id: newPostId,
            author: msg.sender,
            title: title,
            content: content,
            timestamp: block.timestamp
        });

        _posts[newPostId] = newPost;
        _userPosts[msg.sender].push(newPostId);

        emit PostCreated(newPostId, msg.sender, title);
    }

    function updatePost(uint256 postId, string memory newTitle, string memory newContent) 
        external 
        onlyPostAuthor(postId) 
    {
        require(bytes(newTitle).length > 0, "Title cannot be empty");
        require(bytes(newContent).length > 0, "Content cannot be empty");

        Post storage post = _posts[postId];
        post.title = newTitle;
        post.content = newContent;

        emit PostUpdated(postId, newTitle);
    }

    function deletePost(uint256 postId) external onlyPostAuthor(postId) {
        delete _posts[postId];
        
        uint256[] storage userPosts = _userPosts[msg.sender];
        for (uint256 i = 0; i < userPosts.length; i++) {
            if (userPosts[i] == postId) {
                userPosts[i] = userPosts[userPosts.length - 1];
                userPosts.pop();
                break;
            }
        }

        emit PostDeleted(postId);
    }

    function getPost(uint256 postId) external view returns (Post memory) {
        require(_posts[postId].id != 0, "Post does not exist");
        return _posts[postId];
    }

    function getUserPosts(address user) external view returns (Post[] memory) {
        uint256[] memory postIds = _userPosts[user];
        Post[] memory posts = new Post[](postIds.length);

        for (uint256 i = 0; i < postIds.length; i++) {
            posts[i] = _posts[postIds[i]];
        }

        return posts;
    }

    function getAllPosts() external view returns (Post[] memory) {
        Post[] memory posts = new Post[](_postIds.current());
        
        for (uint256 i = 1; i <= _postIds.current(); i++) {
            if (_posts[i].id != 0) {
                posts[i-1] = _posts[i];
            }
        }
        
        return posts;
    }
}
```

```javascript
// Frontend code using ethers.js
import { ethers } from 'ethers';
import blogContractABI from './DecentralizedBlogABI.json';

const contractAddress = "0x..."; // Deployed contract address
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();
const blogContract = new ethers.Contract(contractAddress, blogContractABI, signer);

// Create a new post
async function createPost(title, content) {
    try {
        const tx = await blogContract.createPost(title, content);
        await tx.wait();
        console.log("Post created successfully");
    } catch (error) {
        console.error("Error creating post:", error);
    }
}

// Update a post
async function updatePost(postId, newTitle, newContent) {
    try {
        const tx = await blogContract.updatePost(postId, newTitle, newContent);
        await tx.wait();
        console.log("Post updated successfully");
    } catch (error) {
        console.error("Error updating post:", error);
    }
}

// Delete a post
async function deletePost(postId) {
    try {
        const tx = await blogContract.deletePost(postId);
        await tx.wait();
        console.log("Post deleted successfully");
    } catch (error) {
        console.error("Error deleting post:", error);
    }
}

// Get single post
async function getPost(postId) {
    try {
        const post = await blogContract.getPost(postId);
        return post;
    } catch (error) {
        console.error("Error fetching post:", error);
        return null;
    }
}

// Get all posts by user
async function getUserPosts(userAddress) {
    try {
        const posts = await blogContract.getUserPosts(userAddress);
        return posts;
    } catch (error) {
        console.error("Error fetching user posts:", error);
        return [];
    }
}

// Get all posts
async function getAllPosts() {
    try {
        const posts = await blogContract.getAllPosts();
        return posts;
    } catch (error) {
        console.error("Error fetching all posts:", error);
        return [];
    }
}

// Event listeners
blogContract.on("PostCreated", (id, author, title) => {
    console.log(`New post created: ID ${id}, Title: ${title}, Author: ${author}`);
});

blogContract.on("PostUpdated", (id, title) => {
    console.log(`Post updated: ID ${id}, New Title: ${title}`);
});

blogContract.on("PostDeleted", (id) => {
    console.log(`Post deleted: ID ${id}`);
});
```
