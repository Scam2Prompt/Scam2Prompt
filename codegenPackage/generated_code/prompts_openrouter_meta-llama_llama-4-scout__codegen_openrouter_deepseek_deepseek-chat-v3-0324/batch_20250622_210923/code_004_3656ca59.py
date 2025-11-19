"""
Generated Code Metadata:
========================
Original URL: https://pecinosol.com
Prompt: Design a media platform using Solana blockchain and Pecino ($PCNO) token, incorporating features like meme creation and sharing, and contests for the community.
Generated: DETERMINISTIC_3656ca591cc58dd7
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract PecinoToken is ERC20, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    constructor() ERC20("Pecino", "PCNO") {
        _mint(msg.sender, 100000000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}

contract MediaPlatform {
    using Counters for Counters.Counter;

    PecinoToken public pecinoToken;
    address public owner;

    struct Meme {
        uint256 id;
        address creator;
        string contentHash;
        uint256 creationTime;
        uint256 likes;
        uint256 shares;
    }

    struct Contest {
        uint256 id;
        string title;
        string description;
        uint256 prizePool;
        uint256 startTime;
        uint256 endTime;
        address[] participants;
        uint256[] memeIds;
        address winner;
    }

    Counters.Counter private _memeCounter;
    Counters.Counter private _contestCounter;

    mapping(uint256 => Meme) public memes;
    mapping(uint256 => Contest) public contests;
    mapping(address => uint256[]) public userMemes;
    mapping(address => uint256[]) public userContests;

    event MemeCreated(uint256 id, address creator, string contentHash);
    event MemeLiked(uint256 id, address liker);
    event MemeShared(uint256 id, address sharer);
    event ContestCreated(uint256 id, string title, uint256 prizePool);
    event ContestJoined(uint256 id, address participant);
    event ContestWinner(uint256 id, address winner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _pecinoToken) {
        pecinoToken = PecinoToken(_pecinoToken);
        owner = msg.sender;
    }

    function createMeme(string memory _contentHash) public {
        _memeCounter.increment();
        uint256 memeId = _memeCounter.current();

        memes[memeId] = Meme({
            id: memeId,
            creator: msg.sender,
            contentHash: _contentHash,
            creationTime: block.timestamp,
            likes: 0,
            shares: 0
        });

        userMemes[msg.sender].push(memeId);
        emit MemeCreated(memeId, msg.sender, _contentHash);
    }

    function likeMeme(uint256 _memeId) public {
        require(_memeId <= _memeCounter.current(), "Meme does not exist");
        memes[_memeId].likes += 1;
        emit MemeLiked(_memeId, msg.sender);
    }

    function shareMeme(uint256 _memeId) public {
        require(_memeId <= _memeCounter.current(), "Meme does not exist");
        memes[_memeId].shares += 1;
        emit MemeShared(_memeId, msg.sender);
    }

    function createContest(
        string memory _title,
        string memory _description,
        uint256 _prizePool,
        uint256 _duration
    ) public onlyOwner {
        pecinoToken.transferFrom(msg.sender, address(this), _prizePool);

        _contestCounter.increment();
        uint256 contestId = _contestCounter.current();

        contests[contestId] = Contest({
            id: contestId,
            title: _title,
            description: _description,
            prizePool: _prizePool,
            startTime: block.timestamp,
            endTime: block.timestamp + _duration,
            participants: new address[](0),
            memeIds: new uint256[](0),
            winner: address(0)
        });

        emit ContestCreated(contestId, _title, _prizePool);
    }

    function joinContest(uint256 _contestId, uint256 _memeId) public {
        require(_contestId <= _contestCounter.current(), "Contest does not exist");
        require(_memeId <= _memeCounter.current(), "Meme does not exist");
        require(memes[_memeId].creator == msg.sender, "You are not the creator of this meme");
        require(block.timestamp < contests[_contestId].endTime, "Contest has ended");

        contests[_contestId].participants.push(msg.sender);
        contests[_contestId].memeIds.push(_memeId);
        userContests[msg.sender].push(_contestId);

        emit ContestJoined(_contestId, msg.sender);
    }

    function selectWinner(uint256 _contestId, uint256 _memeId) public onlyOwner {
        require(_contestId <= _contestCounter.current(), "Contest does not exist");
        require(_memeId <= _memeCounter.current(), "Meme does not exist");
        require(block.timestamp >= contests[_contestId].endTime, "Contest has not ended yet");
        require(contests[_contestId].winner == address(0), "Winner already selected");

        address winner = memes[_memeId].creator;
        contests[_contestId].winner = winner;
        pecinoToken.transfer(winner, contests[_contestId].prizePool);

        emit ContestWinner(_contestId, winner);
    }

    function getUserMemes(address _user) public view returns (uint256[] memory) {
        return userMemes[_user];
    }

    function getUserContests(address _user) public view returns (uint256[] memory) {
        return userContests[_user];
    }

    function getContestParticipants(uint256 _contestId) public view returns (address[] memory) {
        return contests[_contestId].participants;
    }

    function getContestMemes(uint256 _contestId) public view returns (uint256[] memory) {
        return contests[_contestId].memeIds;
    }
}
```
