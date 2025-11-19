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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract ComedyEcosystem is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    struct Meme {
        uint256 id;
        string contentHash;
        address creator;
        uint256 creationTimestamp;
        uint256 upvotes;
        uint256 downvotes;
    }

    mapping(uint256 => Meme) public memes;
    mapping(address => uint256[]) public userMemes;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    uint256 public constant MIN_CONTRIBUTION = 0.01 ether;
    uint256 public constant VOTING_PERIOD = 7 days;

    event MemeCreated(uint256 indexed id, address indexed creator, string contentHash);
    event Voted(uint256 indexed memeId, address indexed voter, bool isUpvote);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    constructor() ERC721("ComedyMeme", "CMEME") {}

    function createMeme(string memory _contentHash) external payable {
        require(msg.value >= MIN_CONTRIBUTION, "Insufficient contribution");
        require(bytes(_contentHash).length > 0, "Content hash cannot be empty");

        _tokenIdCounter.increment();
        uint256 newMemeId = _tokenIdCounter.current();

        memes[newMemeId] = Meme({
            id: newMemeId,
            contentHash: _contentHash,
            creator: msg.sender,
            creationTimestamp: block.timestamp,
            upvotes: 0,
            downvotes: 0
        });

        userMemes[msg.sender].push(newMemeId);
        _safeMint(msg.sender, newMemeId);

        emit MemeCreated(newMemeId, msg.sender, _contentHash);
    }

    function vote(uint256 _memeId, bool _isUpvote) external {
        require(_exists(_memeId), "Meme does not exist");
        require(block.timestamp <= memes[_memeId].creationTimestamp + VOTING_PERIOD, "Voting period ended");
        require(!hasVoted[_memeId][msg.sender], "Already voted");

        if (_isUpvote) {
            memes[_memeId].upvotes += 1;
        } else {
            memes[_memeId].downvotes += 1;
        }

        hasVoted[_memeId][msg.sender] = true;
        emit Voted(_memeId, msg.sender, _isUpvote);
    }

    function getMeme(uint256 _memeId) external view returns (Meme memory) {
        require(_exists(_memeId), "Meme does not exist");
        return memes[_memeId];
    }

    function getUserMemes(address _user) external view returns (uint256[] memory) {
        return userMemes[_user];
    }

    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
        
        emit FundsWithdrawn(owner(), balance);
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return string(abi.encodePacked(baseURI(), tokenId.toString()));
    }

    function baseURI() internal pure returns (string memory) {
        return "ipfs://";
    }

    function _exists(uint256 tokenId) internal view returns (bool) {
        return tokenId > 0 && tokenId <= _tokenIdCounter.current();
    }
}
```
