"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Develop a decentralized application (dApp) that allows users to submit memes for mining METAL tokens and vote on the funniest submissions.
Generated: DETERMINISTIC_5b244dd817c5aecf
Batch ID: 20250612_153648
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

// Importing OpenZeppelin's ERC20 implementation for METAL token
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeVoting contract allows users to submit memes and vote on them
contract MemeVoting is Ownable {
    // Struct to represent a meme submission
    struct Meme {
        string content; // URL or IPFS hash of the meme
        address submitter; // Address of the meme submitter
        uint256 voteCount; // Number of votes received
    }

    // Mapping to store memes by their ID
    mapping(uint256 => Meme) public memes;
    // Counter for meme IDs
    uint256 public memeCount;

    // Event emitted when a new meme is submitted
    event MemeSubmitted(uint256 memeId, string content, address indexed submitter);
    // Event emitted when a meme is voted on
    event MemeVoted(uint256 memeId, address indexed voter);

    // ERC20 token for METAL
    ERC20 public metalToken;

    // Constructor to initialize the METAL token
    constructor(address _metalTokenAddress) {
        metalToken = ERC20(_metalTokenAddress);
    }

    // Function to submit a meme
    function submitMeme(string memory _content) public {
        require(bytes(_content).length > 0, "Meme content cannot be empty");

        // Create a new meme
        memes[memeCount] = Meme({
            content: _content,
            submitter: msg.sender,
            voteCount: 0
        });

        emit MemeSubmitted(memeCount, _content, msg.sender);
        memeCount++;
    }

    // Function to vote for a meme
    function voteMeme(uint256 _memeId) public {
        require(_memeId < memeCount, "Meme does not exist");
        
        // Check if the voter has enough METAL tokens to vote
        require(metalToken.balanceOf(msg.sender) >= 1, "Insufficient METAL tokens to vote");

        // Transfer 1 METAL token from voter to the contract
        metalToken.transferFrom(msg.sender, address(this), 1);

        // Increment the vote count for the meme
        memes[_memeId].voteCount++;

        emit MemeVoted(_memeId, msg.sender);
    }

    // Function to withdraw METAL tokens from the contract
    function withdrawTokens(address _to, uint256 _amount) public onlyOwner {
        require(_amount <= metalToken.balanceOf(address(this)), "Insufficient balance in contract");
        metalToken.transfer(_to, _amount);
    }

    // Function to get the details of a meme
    function getMeme(uint256 _memeId) public view returns (string memory content, address submitter, uint256 voteCount) {
        require(_memeId < memeCount, "Meme does not exist");
        Meme memory meme = memes[_memeId];
        return (meme.content, meme.submitter, meme.voteCount);
    }
}
```

### Note:
- This code assumes that the METAL token is already deployed and its address is provided when deploying the `MemeVoting` contract.
- The contract uses OpenZeppelin's ERC20 implementation for the METAL token, which should be included in your project dependencies.
- Ensure to handle the approval of token transfers from users before they can vote.
