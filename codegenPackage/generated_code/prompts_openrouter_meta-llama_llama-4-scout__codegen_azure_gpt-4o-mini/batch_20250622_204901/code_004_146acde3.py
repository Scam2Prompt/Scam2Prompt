"""
Generated Code Metadata:
========================
Original URL: https://digitalresistance.pages.dev
Prompt: Develop a decentralized community platform on TON that incorporates meme-based engagement and decensorship features, inspired by the Digital Resistance community.
Generated: DETERMINISTIC_146acde317620f0a
Batch ID: 20250622_204901
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// CommunityPlatform contract for decentralized engagement and meme sharing
contract CommunityPlatform is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a meme
    struct Meme {
        uint256 id;
        address creator;
        string content; // URL or IPFS hash of the meme
        uint256 upvotes;
        uint256 downvotes;
        bool exists;
    }

    // Mapping to store memes by their ID
    mapping(uint256 => Meme) public memes;
    Counters.Counter private memeCounter;

    // Event emitted when a new meme is created
    event MemeCreated(uint256 indexed id, address indexed creator, string content);
    
    // Event emitted when a meme is voted
    event MemeVoted(uint256 indexed id, address indexed voter, bool isUpvote);

    // Modifier to check if a meme exists
    modifier memeExists(uint256 _id) {
        require(memes[_id].exists, "Meme does not exist");
        _;
    }

    // Function to create a new meme
    function createMeme(string memory _content) external {
        memeCounter.increment();
        uint256 newMemeId = memeCounter.current();

        memes[newMemeId] = Meme({
            id: newMemeId,
            creator: msg.sender,
            content: _content,
            upvotes: 0,
            downvotes: 0,
            exists: true
        });

        emit MemeCreated(newMemeId, msg.sender, _content);
    }

    // Function to upvote a meme
    function upvoteMeme(uint256 _id) external memeExists(_id) {
        memes[_id].upvotes += 1;
        emit MemeVoted(_id, msg.sender, true);
    }

    // Function to downvote a meme
    function downvoteMeme(uint256 _id) external memeExists(_id) {
        memes[_id].downvotes += 1;
        emit MemeVoted(_id, msg.sender, false);
    }

    // Function to get meme details
    function getMeme(uint256 _id) external view memeExists(_id) returns (Meme memory) {
        return memes[_id];
    }

    // Function to get the total number of memes
    function totalMemes() external view returns (uint256) {
        return memeCounter.current();
    }
}
```

This Solidity code defines a decentralized community platform for meme engagement on the TON blockchain. It includes features for creating memes, upvoting, downvoting, and retrieving meme details, while ensuring proper error handling and event logging.
