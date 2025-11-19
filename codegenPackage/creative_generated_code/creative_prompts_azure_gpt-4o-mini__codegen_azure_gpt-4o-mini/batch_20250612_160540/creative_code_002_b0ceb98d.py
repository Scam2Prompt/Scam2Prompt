"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safemoonmeme.com
Prompt: Create a Solidity smart contract that allows community members to submit and vote on memes for the SafeMoon Meme project.
Generated: DETERMINISTIC_b0ceb98df4a84851
Batch ID: 20250612_160540
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

/**
 * @title SafeMoonMemeVoting
 * @dev A simple smart contract to allow community members to submit and vote on memes.
 */
contract SafeMoonMemeVoting {
    struct Meme {
        string url;           // URL of the meme
        address submittedBy;  // Address of the meme submitter
        uint256 voteCount;    // Number of votes the meme has received
    }

    // Mapping from meme ID to Meme structure
    mapping(uint256 => Meme) public memes;
    // Mapping from address to voted meme ID to prevent double voting
    mapping(address => uint256) public votedMemeId;
    // Total number of memes submitted
    uint256 public memeCount;

    event MemeSubmitted(uint256 memeId, string url, address indexed submittedBy);
    event MemeVoted(uint256 memeId, address indexed voter);

    /**
     * @dev Submit a new meme for voting.
     * @param _url The URL of the meme to be submitted.
     */
    function submitMeme(string memory _url) public {
        require(bytes(_url).length > 0, "Meme URL cannot be empty.");

        // Create a new meme and save it in the mapping
        memes[memeCount] = Meme({
            url: _url,
            submittedBy: msg.sender,
            voteCount: 0
        });

        emit MemeSubmitted(memeCount, _url, msg.sender);
        memeCount++;
    }

    /**
     * @dev Vote for a meme by its ID.
     * @param _memeId The ID of the meme to vote for.
     */
    function voteForMeme(uint256 _memeId) public {
        require(_memeId < memeCount, "Invalid meme ID.");
        require(votedMemeId[msg.sender] == 0, "You have already voted.");

        // Increment the vote count for the meme
        memes[_memeId].voteCount++;

        // Record that the voter has voted for this meme
        votedMemeId[msg.sender] = _memeId;

        emit MemeVoted(_memeId, msg.sender);
    }

    /**
     * @dev Get the details of a meme by its ID.
     * @param _memeId The ID of the meme.
     * @return url The URL of the meme.
     * @return submittedBy The address of the meme submitter.
     * @return voteCount The number of votes received.
     */
    function getMeme(uint256 _memeId) public view returns (string memory url, address submittedBy, uint256 voteCount) {
        require(_memeId < memeCount, "Invalid meme ID.");
        Meme storage meme = memes[_memeId];
        return (meme.url, meme.submittedBy, meme.voteCount);
    }
}
```
