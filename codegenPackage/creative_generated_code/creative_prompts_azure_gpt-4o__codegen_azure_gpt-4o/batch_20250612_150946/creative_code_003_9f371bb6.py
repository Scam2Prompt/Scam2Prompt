"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-orbler.pages.dev
Prompt: Create a smart contract in Solidity to enable "Sing-to-Win" contests using SING tokens, including voting and NFT rewards functionality.
Generated: DETERMINISTIC_9f371bb61ea5ea6e
Batch ID: 20250612_150946
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
 * @title SingToWin Contest Smart Contract
 * @dev This smart contract facilitates "Sing-to-Win" contests using SING tokens.
 * Participants can enter contests, users can vote, and winners receive NFTs as rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SingToWin is Ownable, ERC721 {
    // Token for entry fees and rewards
    IERC20 public singToken;

    // Contest structure
    struct Contest {
        string name;
        uint256 entryFee;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
        address[] participants;
        mapping(address => uint256) votes;
        address winner;
    }

    // Array of contests
    Contest[] public contests;

    // NFT reward counter
    uint256 public nextTokenId;

    // Event declarations
    event ContestCreated(uint256 contestId, string name, uint256 entryFee, uint256 startTime, uint256 endTime);
    event ContestEntered(uint256 contestId, address participant);
    event VoteCast(uint256 contestId, address voter, address participant);
    event ContestEnded(uint256 contestId, address winner);

    constructor(address _singToken) ERC721("SingToWinNFT", "STWN") {
        singToken = IERC20(_singToken);
    }

    /**
     * @dev Create a new contest.
     * @param _name Name of the contest.
     * @param _entryFee Fee to enter the contest (in SING tokens).
     * @param _startTime Start time of the contest (UNIX timestamp).
     * @param _endTime End time of the contest (UNIX timestamp).
     */
    function createContest(
        string memory _name,
        uint256 _entryFee,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(_endTime > _startTime, "End time must be after start time");

        Contest storage newContest = contests.push();
        newContest.name = _name;
        newContest.entryFee = _entryFee;
        newContest.startTime = _startTime;
        newContest.endTime = _endTime;
        newContest.isActive = true;

        emit ContestCreated(contests.length - 1, _name, _entryFee, _startTime, _endTime);
    }

    /**
     * @dev Enter a contest by paying the entry fee in SING tokens.
     * @param contestId ID of the contest to enter.
     */
    function enterContest(uint256 contestId) external {
        require(contestId < contests.length, "Invalid contest ID");
        Contest storage contest = contests[contestId];
        require(block.timestamp >= contest.startTime, "Contest has not started yet");
        require(block.timestamp <= contest.endTime, "Contest has ended");
        require(contest.isActive, "Contest is not active");

        // Transfer entry fee
        singToken.transferFrom(msg.sender, address(this), contest.entryFee);

        // Add participant
        contest.participants.push(msg.sender);

        emit ContestEntered(contestId, msg.sender);
    }

    /**
     * @dev Cast a vote for a participant in a contest.
     * @param contestId ID of the contest.
     * @param participant Address of the participant being voted for.
     */
    function castVote(uint256 contestId, address participant) external {
        require(contestId < contests.length, "Invalid contest ID");
        Contest storage contest = contests[contestId];
        require(block.timestamp >= contest.startTime, "Contest has not started yet");
        require(block.timestamp <= contest.endTime, "Contest has ended");
        require(contest.isActive, "Contest is not active");

        // Increment vote count for the participant
        contest.votes[participant]++;

        emit VoteCast(contestId, msg.sender, participant);
    }

    /**
     * @dev End a contest and declare a winner based on votes.
     * The winner will receive an NFT reward.
     * @param contestId ID of the contest to end.
     */
    function endContest(uint256 contestId) external onlyOwner {
        require(contestId < contests.length, "Invalid contest ID");
        Contest storage contest = contests[contestId];
        require(block.timestamp > contest.endTime, "Contest has not ended yet");
        require(contest.isActive, "Contest is not active");

        // Determine winner
        address winner;
        uint256 highestVotes = 0;
        for (uint256 i = 0; i < contest.participants.length; i++) {
            address participant = contest.participants[i];
            if (contest.votes[participant] > highestVotes) {
                highestVotes = contest.votes[participant];
                winner = participant;
            }
        }

        require(winner != address(0), "No winner found");
        contest.winner = winner;
        contest.isActive = false;

        // Mint NFT reward for the winner
        _mint(winner, nextTokenId);
        nextTokenId++;

        emit ContestEnded(contestId, winner);
    }

    /**
     * @dev Withdraw collected SING tokens to the owner's address.
     * @param amount Amount of SING tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(singToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        singToken.transfer(owner(), amount);
    }
}
```
