"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Write a smart contract in Solidity that implements a "Proof of Hilarity" mechanism, where miners submit memes and the funniest meme is rewarded with METAL tokens.
Generated: DETERMINISTIC_92a1c1c565de3802
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetalToken is ERC20, Ownable {
    constructor() ERC20("METAL", "MTL") {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}

contract ProofOfHilarity is Ownable {
    MetalToken public metalToken;
    uint256 public rewardAmount;
    uint256 public submissionFee;
    uint256 public votingPeriod;
    uint256 public currentRound;
    
    struct Meme {
        address submitter;
        string memeHash; // IPFS or similar content hash
        uint256 votes;
        bool claimed;
    }
    
    struct Round {
        uint256 startTime;
        uint256 endTime;
        uint256 winningMemeId;
        bool rewardsDistributed;
    }
    
    mapping(uint256 => Meme) public memes;
    mapping(uint256 => Round) public rounds;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    mapping(address => uint256[]) public userSubmissions;
    
    uint256 public memeCount;
    
    event MemeSubmitted(uint256 indexed memeId, address indexed submitter, string memeHash);
    event Voted(uint256 indexed memeId, address indexed voter);
    event RoundStarted(uint256 indexed roundId, uint256 startTime, uint256 endTime);
    event RewardsDistributed(uint256 indexed roundId, uint256 winningMemeId, address winner);
    
    constructor(address _metalToken, uint256 _rewardAmount, uint256 _submissionFee, uint256 _votingPeriod) {
        metalToken = MetalToken(_metalToken);
        rewardAmount = _rewardAmount;
        submissionFee = _submissionFee;
        votingPeriod = _votingPeriod;
        currentRound = 1;
        rounds[currentRound].startTime = block.timestamp;
        rounds[currentRound].endTime = block.timestamp + votingPeriod;
        emit RoundStarted(currentRound, block.timestamp, block.timestamp + votingPeriod);
    }
    
    modifier onlyActiveRound() {
        require(block.timestamp >= rounds[currentRound].startTime && block.timestamp <= rounds[currentRound].endTime, "Round not active");
        _;
    }
    
    function submitMeme(string memory _memeHash) external payable onlyActiveRound {
        require(msg.value >= submissionFee, "Insufficient submission fee");
        require(bytes(_memeHash).length > 0, "Invalid meme hash");
        
        memeCount++;
        memes[memeCount] = Meme({
            submitter: msg.sender,
            memeHash: _memeHash,
            votes: 0,
            claimed: false
        });
        
        userSubmissions[msg.sender].push(memeCount);
        emit MemeSubmitted(memeCount, msg.sender, _memeHash);
    }
    
    function vote(uint256 _memeId) external onlyActiveRound {
        require(_memeId > 0 && _memeId <= memeCount, "Invalid meme ID");
        require(!hasVoted[currentRound][msg.sender], "Already voted this round");
        
        memes[_memeId].votes++;
        hasVoted[currentRound][msg.sender] = true;
        emit Voted(_memeId, msg.sender);
    }
    
    function endRound() external onlyOwner {
        require(block.timestamp > rounds[currentRound].endTime, "Round not ended");
        require(!rounds[currentRound].rewardsDistributed, "Rewards already distributed");
        
        uint256 winningMemeId = 0;
        uint256 maxVotes = 0;
        
        for (uint256 i = 1; i <= memeCount; i++) {
            if (memes[i].votes > maxVotes) {
                maxVotes = memes[i].votes;
                winningMemeId = i;
            }
        }
        
        if (winningMemeId > 0) {
            rounds[currentRound].winningMemeId = winningMemeId;
            address winner = memes[winningMemeId].submitter;
            metalToken.mint(winner, rewardAmount);
            memes[winningMemeId].claimed = true;
            emit RewardsDistributed(currentRound, winningMemeId, winner);
        }
        
        rounds[currentRound].rewardsDistributed = true;
        
        // Start new round
        currentRound++;
        rounds[currentRound].startTime = block.timestamp;
        rounds[currentRound].endTime = block.timestamp + votingPeriod;
        emit RoundStarted(currentRound, block.timestamp, block.timestamp + votingPeriod);
    }
    
    function setRewardAmount(uint256 _rewardAmount) external onlyOwner {
        rewardAmount = _rewardAmount;
    }
    
    function setSubmissionFee(uint256 _submissionFee) external onlyOwner {
        submissionFee = _submissionFee;
    }
    
    function setVotingPeriod(uint256 _votingPeriod) external onlyOwner {
        votingPeriod = _votingPeriod;
    }
    
    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
    
    function getUserSubmissions(address _user) external view returns (uint256[] memory) {
        return userSubmissions[_user];
    }
    
    function getRoundInfo(uint256 _roundId) external view returns (Round memory) {
        return rounds[_roundId];
    }
    
    function getMemeInfo(uint256 _memeId) external view returns (Meme memory) {
        return memes[_memeId];
    }
}
```
