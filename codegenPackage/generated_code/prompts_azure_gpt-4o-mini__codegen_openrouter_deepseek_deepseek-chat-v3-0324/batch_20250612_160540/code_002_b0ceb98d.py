"""
Generated Code Metadata:
========================
Original URL: https://safemoonmeme.com
Prompt: Create a Solidity smart contract that allows community members to submit and vote on memes for the SafeMoon Meme project.
Generated: DETERMINISTIC_b0ceb98df4a84851
Batch ID: 20250612_160540
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
 * @title SafeMoonMemeVoting
 * @dev A smart contract for submitting and voting on memes in the SafeMoon community
 */
contract SafeMoonMemeVoting {
    // Struct to represent a meme submission
    struct Meme {
        uint256 id;
        address submitter;
        string memeUrl;
        uint256 voteCount;
        uint256 submissionTime;
        bool isActive;
    }

    // Struct to track user votes
    struct Vote {
        bool hasVoted;
        uint256 memeId;
    }

    // State variables
    address public owner;
    uint256 public memeCount;
    uint256 public votingPeriod; // in seconds
    uint256 public submissionFee; // in wei

    // Mappings
    mapping(uint256 => Meme) public memes;
    mapping(address => Vote) public votes;
    mapping(address => bool) public bannedUsers;

    // Events
    event MemeSubmitted(uint256 indexed memeId, address indexed submitter, string memeUrl);
    event Voted(uint256 indexed memeId, address indexed voter);
    event MemeRemoved(uint256 indexed memeId, address indexed remover);
    event UserBanned(address indexed user);
    event UserUnbanned(address indexed user);
    event VotingPeriodUpdated(uint256 newPeriod);
    event SubmissionFeeUpdated(uint256 newFee);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier notBanned() {
        require(!bannedUsers[msg.sender], "You are banned from submitting/voting");
        _;
    }

    modifier validMemeId(uint256 _memeId) {
        require(_memeId > 0 && _memeId <= memeCount, "Invalid meme ID");
        _;
    }

    /**
     * @dev Constructor function
     * @param _votingPeriod Duration of voting period in seconds
     * @param _submissionFee Fee required to submit a meme in wei
     */
    constructor(uint256 _votingPeriod, uint256 _submissionFee) {
        owner = msg.sender;
        votingPeriod = _votingPeriod;
        submissionFee = _submissionFee;
        memeCount = 0;
    }

    /**
     * @dev Submit a new meme
     * @param _memeUrl URL of the meme image
     */
    function submitMeme(string memory _memeUrl) external payable notBanned {
        require(msg.value >= submissionFee, "Insufficient submission fee");
        require(bytes(_memeUrl).length > 0, "Meme URL cannot be empty");

        memeCount++;
        memes[memeCount] = Meme({
            id: memeCount,
            submitter: msg.sender,
            memeUrl: _memeUrl,
            voteCount: 0,
            submissionTime: block.timestamp,
            isActive: true
        });

        emit MemeSubmitted(memeCount, msg.sender, _memeUrl);
    }

    /**
     * @dev Vote for a meme
     * @param _memeId ID of the meme to vote for
     */
    function vote(uint256 _memeId) external validMemeId(_memeId) notBanned {
        Meme storage meme = memes[_memeId];
        require(meme.isActive, "Meme is no longer active");
        require(block.timestamp <= meme.submissionTime + votingPeriod, "Voting period has ended");
        require(!votes[msg.sender].hasVoted, "You have already voted");

        votes[msg.sender] = Vote({
            hasVoted: true,
            memeId: _memeId
        });

        meme.voteCount++;
        emit Voted(_memeId, msg.sender);
    }

    /**
     * @dev Get meme details by ID
     * @param _memeId ID of the meme
     * @return Meme details
     */
    function getMeme(uint256 _memeId) external view validMemeId(_memeId) returns (
        uint256 id,
        address submitter,
        string memory memeUrl,
        uint256 voteCount,
        uint256 submissionTime,
        bool isActive
    ) {
        Meme memory meme = memes[_memeId];
        return (
            meme.id,
            meme.submitter,
            meme.memeUrl,
            meme.voteCount,
            meme.submissionTime,
            meme.isActive
        );
    }

    /**
     * @dev Get top memes by vote count
     * @param _count Number of top memes to return
     * @return Array of meme IDs
     */
    function getTopMemes(uint256 _count) external view returns (uint256[] memory) {
        require(_count > 0 && _count <= memeCount, "Invalid count");

        uint256[] memory topMemeIds = new uint256[](_count);
        uint256[] memory voteCounts = new uint256[](_count);

        for (uint256 i = 1; i <= memeCount; i++) {
            if (!memes[i].isActive) continue;

            uint256 currentVotes = memes[i].voteCount;
            for (uint256 j = 0; j < _count; j++) {
                if (currentVotes > voteCounts[j]) {
                    // Shift elements
                    for (uint256 k = _count - 1; k > j; k--) {
                        topMemeIds[k] = topMemeIds[k - 1];
                        voteCounts[k] = voteCounts[k - 1];
                    }
                    // Insert new element
                    topMemeIds[j] = i;
                    voteCounts[j] = currentVotes;
                    break;
                }
            }
        }

        return topMemeIds;
    }

    /**
     * @dev Remove a meme (owner only)
     * @param _memeId ID of the meme to remove
     */
    function removeMeme(uint256 _memeId) external onlyOwner validMemeId(_memeId) {
        memes[_memeId].isActive = false;
        emit MemeRemoved(_memeId, msg.sender);
    }

    /**
     * @dev Ban a user from submitting/voting (owner only)
     * @param _user Address of the user to ban
     */
    function banUser(address _user) external onlyOwner {
        require(!bannedUsers[_user], "User is already banned");
        bannedUsers[_user] = true;
        emit UserBanned(_user);
    }

    /**
     * @dev Unban a user (owner only)
     * @param _user Address of the user to unban
     */
    function unbanUser(address _user) external onlyOwner {
        require(bannedUsers[_user], "User is not banned");
        bannedUsers[_user] = false;
        emit UserUnbanned(_user);
    }

    /**
     * @dev Update voting period (owner only)
     * @param _newPeriod New voting period in seconds
     */
    function updateVotingPeriod(uint256 _newPeriod) external onlyOwner {
        require(_newPeriod > 0, "Voting period must be positive");
        votingPeriod = _newPeriod;
        emit VotingPeriodUpdated(_newPeriod);
    }

    /**
     * @dev Update submission fee (owner only)
     * @param _newFee New submission fee in wei
     */
    function updateSubmissionFee(uint256 _newFee) external onlyOwner {
        submissionFee = _newFee;
        emit SubmissionFeeUpdated(_newFee);
    }

    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Check if voting is active for a meme
     * @param _memeId ID of the meme to check
     * @return True if voting is still active
     */
    function isVotingActive(uint256 _memeId) external view validMemeId(_memeId) returns (bool) {
        Meme memory meme = memes[_memeId];
        return meme.isActive && block.timestamp <= meme.submissionTime + votingPeriod;
    }
}
```
