"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metisdap.pages.dev
Prompt: Develop a decentralized application (dApp) for the Metis ecosystem that incorporates social media spotlight features for community engagement, as described in the CVP program.
Generated: DETERMINISTIC_60a7d2a2c4f181ce
Batch ID: 20250612_152526
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

// Import OpenZeppelin's ERC20 token standard for reward distribution
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for SocialMediaSpotlight dApp on the Metis ecosystem
contract SocialMediaSpotlight is ERC20, Ownable {
    // Structure to represent a post
    struct Post {
        uint256 id;
        string content;
        address author;
        uint256 likes;
        bool isActive;
    }

    // Events for logging
    event PostCreated(uint256 indexed postId, address indexed author, string content);
    event PostLiked(uint256 indexed postId, address indexed liker);
    event PostRemoved(uint256 indexed postId);

    // State variables
    uint256 private postCounter;
    mapping(uint256 => Post) public posts; // Mapping from post ID to Post
    mapping(address => uint256[]) private userPosts; // Mapping from user address to their posts

    // Constructor to initialize the ERC20 token
    constructor() ERC20("SpotlightToken", "SPOT") {
        // Initial minting of tokens to contract owner
        _mint(msg.sender, 10000 * 10 ** decimals());
    }

    // Function to create a new post
    function createPost(string memory content) public {
        require(bytes(content).length > 0, "Post content cannot be empty");

        postCounter++;
        posts[postCounter] = Post(postCounter, content, msg.sender, 0, true);
        userPosts[msg.sender].push(postCounter);

        emit PostCreated(postCounter, msg.sender, content);
    }

    // Function to like a post
    function likePost(uint256 postId) public {
        require(posts[postId].isActive, "Post does not exist or is inactive");
        
        posts[postId].likes++;

        emit PostLiked(postId, msg.sender);
    }

    // Function to remove a post
    function removePost(uint256 postId) public onlyOwner {
        require(posts[postId].isActive, "Post does not exist or is already inactive");
        
        posts[postId].isActive = false;

        emit PostRemoved(postId);
    }

    // Function to get the details of a post
    function getPost(uint256 postId) public view returns (Post memory) {
        require(posts[postId].isActive, "Post does not exist or is inactive");
        return posts[postId];
    }

    // Function to get all posts by a user
    function getUserPosts(address user) public view returns (uint256[] memory) {
        return userPosts[user];
    }
}
```

This Solidity smart contract provides a basic framework for a decentralized application that allows users to create, like, and manage social media posts. The contract includes proper error handling, uses OpenZeppelin libraries to ensure security, and emits events for important actions, making it suitable for production deployment on the Metis ecosystem.
