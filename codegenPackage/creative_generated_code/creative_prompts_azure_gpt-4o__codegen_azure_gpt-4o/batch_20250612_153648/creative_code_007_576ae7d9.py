"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalcoin.vercel.app
Prompt: Provide an example of a decentralized voting system in Solidity where METAL token holders can vote on the funniest memes.
Generated: DETERMINISTIC_576ae7d9512282ed
Batch ID: 20250612_153648
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
 * @title Decentralized Voting System
 * @dev A contract where METAL token holders can vote on the funniest memes.
 */
contract MemeVoting {
    // Address of the METAL token contract
    IERC20 public metalToken;

    // Struct representing a meme
    struct Meme {
        string description;
        uint voteCount;
    }

    // Array of memes
    Meme[] public memes;

    // Mapping to track if token holders have already voted
    mapping(address => bool) public hasVoted;

    // Event emitted when a new meme is added
    event MemeAdded(uint memeId, string description);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint memeId);

    /**
     * @dev Constructor to initialize the METAL token address
     * @param _metalToken Address of the METAL token contract
     */
    constructor(address _metalToken) {
        require(_metalToken != address(0), "Invalid token address");
        metalToken = IERC20(_metalToken);
    }

    /**
     * @dev Adds a new meme to the voting system
     * @param _description Description of the meme
     */
    function addMeme(string memory _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");
        memes.push(Meme({description: _description, voteCount: 0}));
        emit MemeAdded(memes.length - 1, _description);
    }

    /**
     * @dev Allows METAL token holders to vote for a meme
     * @param _memeId ID of the meme to vote for
     */
    function vote(uint _memeId) external {
        require(_memeId < memes.length, "Invalid meme ID");
        require(!hasVoted[msg.sender], "You have already voted");
        require(metalToken.balanceOf(msg.sender) > 0, "Must hold METAL tokens to vote");

        memes[_memeId].voteCount += 1;
        hasVoted[msg.sender] = true;

        emit VoteCast(msg.sender, _memeId);
    }

    /**
     * @dev Returns the total number of memes in the system
     * @return Total number of memes
     */
    function getTotalMemes() external view returns (uint) {
        return memes.length;
    }

    /**
     * @dev Returns details of a specific meme
     * @param _memeId ID of the meme
     * @return Description and vote count of the meme
     */
    function getMeme(uint _memeId) external view returns (string memory, uint) {
        require(_memeId < memes.length, "Invalid meme ID");
        Meme memory meme = memes[_memeId];
        return (meme.description, meme.voteCount);
    }
}

/**
 * @dev Interface for the ERC20 token standard
 * This allows interaction with the METAL token contract
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
