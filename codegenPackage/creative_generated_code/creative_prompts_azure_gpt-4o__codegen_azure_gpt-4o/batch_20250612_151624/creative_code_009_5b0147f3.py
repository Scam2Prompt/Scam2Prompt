"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cumcoin.io
Prompt: Write a Solidity smart contract that integrates a humorous feature where users can "vote" for the coin's slogan, such as "Make CUM Great Again."
Generated: DETERMINISTIC_5b0147f345c6cf3b
Batch ID: 20250612_151624
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
 * @title SloganVoting
 * @dev This smart contract allows users to vote for their favorite slogans for the coin.
 */
contract SloganVoting {
    // Owner of the contract
    address public owner;

    // Array to store slogans
    string[] public slogans;

    // Mapping to track votes for each slogan
    mapping(string => uint256) private votes;

    // Event emitted when a new slogan is added
    event SloganAdded(string slogan);

    // Event emitted when a vote is cast
    event VoteCast(string slogan, uint256 votes);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new slogan to the list. Only the contract owner can add slogans.
     * @param _slogan The slogan to add.
     */
    function addSlogan(string memory _slogan) public onlyOwner {
        require(bytes(_slogan).length > 0, "Slogan cannot be empty");

        slogans.push(_slogan);
        votes[_slogan] = 0; // Initialize votes for the new slogan to 0

        emit SloganAdded(_slogan);
    }

    /**
     * @dev Vote for a slogan. Anyone can cast a vote.
     * @param _slogan The slogan to vote for.
     */
    function voteForSlogan(string memory _slogan) public {
        require(sloganExists(_slogan), "Slogan does not exist");

        votes[_slogan] += 1;

        emit VoteCast(_slogan, votes[_slogan]);
    }

    /**
     * @dev Get the vote count for a specific slogan.
     * @param _slogan The slogan to check votes for.
     * @return The number of votes received by the slogan.
     */
    function getVoteCount(string memory _slogan) public view returns (uint256) {
        require(sloganExists(_slogan), "Slogan does not exist");

        return votes[_slogan];
    }

    /**
     * @dev Check if a slogan exists in the list.
     * @param _slogan The slogan to check.
     * @return True if the slogan exists, false otherwise.
     */
    function sloganExists(string memory _slogan) internal view returns (bool) {
        for (uint256 i = 0; i < slogans.length; i++) {
            if (keccak256(bytes(slogans[i])) == keccak256(bytes(_slogan))) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Get all slogans added to the contract.
     * @return An array of all slogans.
     */
    function getAllSlogans() public view returns (string[] memory) {
        return slogans;
    }
}
```
