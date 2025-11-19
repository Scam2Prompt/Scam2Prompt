"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Write a Solidity code snippet to implement a decentralized comedy ecosystem on a blockchain platform, where users can contribute and participate in meme creation and sharing.
Generated: DETERMINISTIC_abe4ae7799c220b1
Batch ID: 20250622_211009
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

/**
 * @title Decentralized Comedy Ecosystem
 * @dev This contract allows users to create, share, and vote on memes in a decentralized manner.
 */
contract ComedyEcosystem {
    // Struct to represent a meme
    struct Meme {
        uint256 id; // Unique ID for the meme
        address creator; // Address of the meme creator
        string content; // Meme content (e.g., URL or text)
        uint256 upvotes; // Number of upvotes
        uint256 downvotes; // Number of downvotes
    }

    // Mapping to store memes by their ID
    mapping(uint256 => Meme) public memes;

    // Counter to generate unique meme IDs
    uint256 private memeCounter;

    // Event emitted when a new meme is created
    event MemeCreated(uint256 id, address creator, string content);

    // Event emitted when a meme is voted on
    event MemeVoted(uint256 id, address voter, bool isUpvote);

    /**
     * @dev Create a new meme.
     * @param _content The content of the meme (e.g., URL or text).
     */
    function createMeme(string memory _content) external {
        require(bytes(_content).length > 0, "Meme content cannot be empty");

        // Increment the meme counter to generate a unique ID
        memeCounter++;

        // Create the meme and store it in the mapping
        memes[memeCounter] = Meme({
            id: memeCounter,
            creator: msg.sender,
            content: _content,
            upvotes: 0,
            downvotes: 0
        });

        // Emit the MemeCreated event
        emit MemeCreated(memeCounter, msg.sender, _content);
    }

    /**
     * @dev Vote on a meme (upvote or downvote).
     * @param _memeId The ID of the meme to vote on.
     * @param _isUpvote True for upvote, false for downvote.
     */
    function voteMeme(uint256 _memeId, bool _isUpvote) external {
        // Ensure the meme exists
        require(memes[_memeId].id != 0, "Meme does not exist");

        // Update the vote count based on the vote type
        if (_isUpvote) {
            memes[_memeId].upvotes++;
        } else {
            memes[_memeId].downvotes++;
        }

        // Emit the MemeVoted event
        emit MemeVoted(_memeId, msg.sender, _isUpvote);
    }

    /**
     * @dev Get details of a meme.
     * @param _memeId The ID of the meme to retrieve.
     * @return id The ID of the meme.
     * @return creator The address of the meme creator.
     * @return content The content of the meme.
     * @return upvotes The number of upvotes the meme has received.
     * @return downvotes The number of downvotes the meme has received.
     */
    function getMeme(uint256 _memeId)
        external
        view
        returns (
            uint256 id,
            address creator,
            string memory content,
            uint256 upvotes,
            uint256 downvotes
        )
    {
        // Ensure the meme exists
        require(memes[_memeId].id != 0, "Meme does not exist");

        // Retrieve the meme details
        Meme memory meme = memes[_memeId];
        return (meme.id, meme.creator, meme.content, meme.upvotes, meme.downvotes);
    }
}
```
