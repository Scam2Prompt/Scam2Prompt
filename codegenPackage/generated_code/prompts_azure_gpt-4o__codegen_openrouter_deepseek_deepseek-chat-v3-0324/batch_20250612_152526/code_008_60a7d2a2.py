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

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title MetisSocialSpotlight
 * @dev A decentralized application for community engagement with social media spotlight features
 */
contract MetisSocialSpotlight is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    struct SpotlightPost {
        uint256 id;
        address author;
        string content;
        string mediaURI;
        uint256 timestamp;
        uint256 upvotes;
        address[] upvoters;
    }

    mapping(uint256 => SpotlightPost) public posts;
    mapping(address => uint256[]) public userPosts;
    mapping(address => mapping(uint256 => bool)) public hasUpvoted;

    event PostCreated(
        uint256 indexed id,
        address indexed author,
        string content,
        string mediaURI,
        uint256 timestamp
    );
    event PostUpvoted(uint256 indexed id, address indexed upvoter, uint256 newUpvoteCount);

    constructor() ERC721("MetisSocialSpotlight", "MSS") {}

    /**
     * @dev Create a new spotlight post
     * @param content The text content of the post
     * @param mediaURI URI to associated media (image/video)
     */
    function createPost(string memory content, string memory mediaURI) public {
        require(bytes(content).length > 0, "Content cannot be empty");

        _tokenIds.increment();
        uint256 newPostId = _tokenIds.current();

        _mint(msg.sender, newPostId);
        _setTokenURI(newPostId, mediaURI);

        address[] memory emptyUpvoters;
        SpotlightPost memory newPost = SpotlightPost({
            id: newPostId,
            author: msg.sender,
            content: content,
            mediaURI: mediaURI,
            timestamp: block.timestamp,
            upvotes: 0,
            upvoters: emptyUpvoters
        });

        posts[newPostId] = newPost;
        userPosts[msg.sender].push(newPostId);

        emit PostCreated(newPostId, msg.sender, content, mediaURI, block.timestamp);
    }

    /**
     * @dev Upvote a post
     * @param postId The ID of the post to upvote
     */
    function upvotePost(uint256 postId) public {
        require(_exists(postId), "Post does not exist");
        require(!hasUpvoted[msg.sender][postId], "Already upvoted this post");

        SpotlightPost storage post = posts[postId];
        post.upvotes += 1;
        post.upvoters.push(msg.sender);
        hasUpvoted[msg.sender][postId] = true;

        emit PostUpvoted(postId, msg.sender, post.upvotes);
    }

    /**
     * @dev Get all posts created by a user
     * @param user Address of the user
     * @return Array of post IDs
     */
    function getUserPosts(address user) public view returns (uint256[] memory) {
        return userPosts[user];
    }

    /**
     * @dev Get post details by ID
     * @param postId The ID of the post
     * @return SpotlightPost struct with post details
     */
    function getPost(uint256 postId) public view returns (SpotlightPost memory) {
        require(_exists(postId), "Post does not exist");
        return posts[postId];
    }

    /**
     * @dev Get total number of posts
     * @return Total post count
     */
    function getTotalPosts() public view returns (uint256) {
        return _tokenIds.current();
    }

    /**
     * @dev Get most upvoted posts
     * @param count Number of posts to return
     * @return Array of post IDs sorted by upvotes
     */
    function getTopPosts(uint256 count) public view returns (uint256[] memory) {
        uint256 totalPosts = _tokenIds.current();
        if (count > totalPosts) {
            count = totalPosts;
        }

        uint256[] memory topPosts = new uint256[](count);
        uint256[] memory allPosts = new uint256[](totalPosts);
        uint256[] memory upvotes = new uint256[](totalPosts);

        for (uint256 i = 1; i <= totalPosts; i++) {
            allPosts[i - 1] = i;
            upvotes[i - 1] = posts[i].upvotes;
        }

        for (uint256 i = 0; i < count; i++) {
            uint256 maxIndex = i;
            for (uint256 j = i + 1; j < totalPosts; j++) {
                if (upvotes[j] > upvotes[maxIndex]) {
                    maxIndex = j;
                }
            }
            if (maxIndex != i) {
                (allPosts[i], allPosts[maxIndex]) = (allPosts[maxIndex], allPosts[i]);
                (upvotes[i], upvotes[maxIndex]) = (upvotes[maxIndex], upvotes[i]);
            }
            topPosts[i] = allPosts[i];
        }

        return topPosts;
    }
}
```
