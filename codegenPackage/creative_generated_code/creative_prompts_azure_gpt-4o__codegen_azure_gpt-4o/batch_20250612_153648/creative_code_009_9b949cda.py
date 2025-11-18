"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalcoin.vercel.app
Prompt: Develop a smart contract in Solidity that enables users to participate in meme-making contests using METAL tokens as entry fees.
Generated: DETERMINISTIC_9b949cda911e2a5e
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
 * @title MemeContest
 * @dev A smart contract to facilitate meme-making contests where users pay an entry fee in METAL tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MemeContest {
    // Address of the METAL token contract
    IERC20 public metalToken;

    // Struct representing a meme submission
    struct Meme {
        uint256 id;
        address creator;
        string memeUrl;
        uint256 votes;
    }

    // State variables
    uint256 public contestId = 0; // Unique ID for contests
    uint256 public entryFee; // Entry fee in METAL tokens
    mapping(uint256 => Meme[]) public contests; // Mapping contest ID to memes
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Mapping to track votes
    address public owner; // Contract owner

    // Events
    event MemeSubmitted(uint256 contestId, uint256 memeId, address creator, string memeUrl);
    event VoteCast(uint256 contestId, uint256 memeId, address voter);
    event ContestStarted(uint256 contestId);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize METAL token address and entry fee
    constructor(address _metalToken, uint256 _entryFee) {
        require(_metalToken != address(0), "Invalid METAL token address");
        require(_entryFee > 0, "Entry fee must be greater than zero");

        metalToken = IERC20(_metalToken);
        entryFee = _entryFee;
        owner = msg.sender;
    }

    /**
     * @dev Starts a new contest. Only the owner can call this function.
     */
    function startContest() external onlyOwner {
        contestId++;
        emit ContestStarted(contestId);
    }

    /**
     * @dev Submit a meme to the current contest by paying the entry fee.
     * @param memeUrl URL of the meme being submitted.
     */
    function submitMeme(string memory memeUrl) external {
        require(bytes(memeUrl).length > 0, "Meme URL cannot be empty");
        require(metalToken.transferFrom(msg.sender, address(this), entryFee), "Entry fee transfer failed");

        uint256 memeId = contests[contestId].length;
        contests[contestId].push(Meme(memeId, msg.sender, memeUrl, 0));

        emit MemeSubmitted(contestId, memeId, msg.sender, memeUrl);
    }

    /**
     * @dev Vote for a meme in the current contest.
     * @param memeId ID of the meme being voted for.
     */
    function vote(uint256 memeId) external {
        require(!hasVoted[contestId][msg.sender], "You have already voted in this contest");
        require(memeId < contests[contestId].length, "Invalid meme ID");

        contests[contestId][memeId].votes++;
        hasVoted[contestId][msg.sender] = true;

        emit VoteCast(contestId, memeId, msg.sender);
    }

    /**
     * @dev Get the winner of a contest (the meme with the highest votes).
     * @param _contestId ID of the contest to get the winner for.
     * @return winnerMeme The winning meme details.
     */
    function getWinner(uint256 _contestId) external view returns (Meme memory winnerMeme) {
        require(_contestId > 0 && _contestId <= contestId, "Invalid contest ID");
        require(contests[_contestId].length > 0, "No memes submitted for this contest");

        uint256 highestVotes = 0;
        uint256 winnerIndex = 0;

        for (uint256 i = 0; i < contests[_contestId].length; i++) {
            if (contests[_contestId][i].votes > highestVotes) {
                highestVotes = contests[_contestId][i].votes;
                winnerIndex = i;
            }
        }

        winnerMeme = contests[_contestId][winnerIndex];
    }

    /**
     * @dev Withdraw accumulated METAL tokens from the contract. Only the owner can call this function.
     * @param amount Amount of METAL tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(metalToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        require(metalToken.transfer(owner, amount), "Withdrawal failed");
    }
}
```
