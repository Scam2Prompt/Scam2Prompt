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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeContest
 * @dev A smart contract for managing meme-making contests using METAL tokens as entry fees.
 */
contract MemeContest is Ownable {
    // METAL token interface
    IERC20 public metalToken;

    // Contest structure
    struct Contest {
        uint256 id;
        string title;
        uint256 entryFee;
        address[] participants;
        address winner;
        bool isActive;
    }

    // Mapping to store contests
    mapping(uint256 => Contest) public contests;
    // Counter for contest IDs
    uint256 public contestCount;

    // Event emitted when a new contest is created
    event ContestCreated(uint256 indexed contestId, string title, uint256 entryFee);
    // Event emitted when a user enters a contest
    event ContestEntered(uint256 indexed contestId, address participant);
    // Event emitted when a contest is concluded
    event ContestConcluded(uint256 indexed contestId, address winner);

    /**
     * @dev Sets the METAL token address.
     * @param _metalToken Address of the METAL token contract.
     */
    constructor(address _metalToken) {
        require(_metalToken != address(0), "Invalid token address");
        metalToken = IERC20(_metalToken);
    }

    /**
     * @dev Create a new meme contest.
     * @param _title Title of the contest.
     * @param _entryFee Entry fee in METAL tokens.
     */
    function createContest(string calldata _title, uint256 _entryFee) external onlyOwner {
        require(_entryFee > 0, "Entry fee must be greater than zero");

        contestCount++;
        contests[contestCount] = Contest({
            id: contestCount,
            title: _title,
            entryFee: _entryFee,
            participants: new address[](0),
            winner: address(0),
            isActive: true
        });

        emit ContestCreated(contestCount, _title, _entryFee);
    }

    /**
     * @dev Enter a contest by paying the entry fee.
     * @param _contestId ID of the contest to enter.
     */
    function enterContest(uint256 _contestId) external {
        Contest storage contest = contests[_contestId];
        require(contest.isActive, "Contest is not active");
        require(metalToken.balanceOf(msg.sender) >= contest.entryFee, "Insufficient METAL tokens");
        require(metalToken.allowance(msg.sender, address(this)) >= contest.entryFee, "Approve tokens first");

        // Transfer the entry fee
        require(metalToken.transferFrom(msg.sender, address(this), contest.entryFee), "Transfer failed");

        // Add participant
        contest.participants.push(msg.sender);
        emit ContestEntered(_contestId, msg.sender);
    }

    /**
     * @dev Conclude a contest and declare a winner.
     * @param _contestId ID of the contest to conclude.
     * @param _winner Address of the winner.
     */
    function concludeContest(uint256 _contestId, address _winner) external onlyOwner {
        Contest storage contest = contests[_contestId];
        require(contest.isActive, "Contest already concluded");
        require(isParticipant(_contestId, _winner), "Address is not a participant");

        contest.winner = _winner;
        contest.isActive = false;

        emit ContestConcluded(_contestId, _winner);
    }

    /**
     * @dev Check if an address is a participant in the contest.
     * @param _contestId ID of the contest.
     * @param _address Address to check.
     * @return bool Whether the address is a participant.
     */
    function isParticipant(uint256 _contestId, address _address) internal view returns (bool) {
        Contest storage contest = contests[_contestId];
        for (uint256 i = 0; i < contest.participants.length; i++) {
            if (contest.participants[i] == _address) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Withdraw METAL tokens from the contract by the owner.
     * @param _amount Amount of METAL tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount <= metalToken.balanceOf(address(this)), "Insufficient balance");
        require(metalToken.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
