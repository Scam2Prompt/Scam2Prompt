"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Design a smart contract for a Proof of Commitment DAO that allows members to stake cryptocurrency and vote on slashing non-compliant members' stakes.
Generated: DETERMINISTIC_ef5bc812db2db39e
Batch ID: 20250622_205541
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
 * @title ProofOfCommitmentDAO
 * @dev A DAO smart contract that allows members to stake cryptocurrency and vote on slashing non-compliant members' stakes.
 */
contract ProofOfCommitmentDAO {
    // Events
    event StakeDeposited(address indexed member, uint256 amount);
    event StakeSlashed(address indexed member, uint256 amount);
    event VoteCast(address indexed voter, address indexed target, bool vote);

    // Struct to represent a member's stake and voting power
    struct Member {
        uint256 stake;
        bool exists;
    }

    // Mapping of member addresses to their stake information
    mapping(address => Member) public members;

    // Minimum stake required to become a member
    uint256 public constant MINIMUM_STAKE = 1 ether;

    // Voting threshold for slashing a member's stake
    uint256 public constant SLASH_VOTE_THRESHOLD = 50; // Percentage

    // DAO treasury to hold slashed stakes
    uint256 public treasury;

    // Mapping to track votes for slashing a member
    mapping(address => mapping(address => bool)) public votes;

    // Mapping to track vote counts for slashing a member
    mapping(address => uint256) public voteCounts;

    // Modifier to ensure only members can call certain functions
    modifier onlyMember() {
        require(members[msg.sender].exists, "Not a DAO member");
        _;
    }

    /**
     * @dev Allows a user to stake cryptocurrency and become a DAO member.
     */
    function depositStake() external payable {
        require(msg.value >= MINIMUM_STAKE, "Insufficient stake amount");

        if (!members[msg.sender].exists) {
            members[msg.sender] = Member({stake: msg.value, exists: true});
        } else {
            members[msg.sender].stake += msg.value;
        }

        emit StakeDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Allows members to vote on slashing another member's stake.
     * @param target The address of the member to vote against.
     * @param vote True to vote for slashing, false to vote against.
     */
    function castVote(address target, bool vote) external onlyMember {
        require(members[target].exists, "Target is not a DAO member");
        require(votes[msg.sender][target] == false, "Already voted");

        votes[msg.sender][target] = true;

        if (vote) {
            voteCounts[target]++;
        }

        emit VoteCast(msg.sender, target, vote);

        // Check if vote count exceeds the threshold
        if (voteCounts[target] * 100 / getTotalMembers() >= SLASH_VOTE_THRESHOLD) {
            slashStake(target);
        }
    }

    /**
     * @dev Internal function to slash a member's stake and transfer it to the treasury.
     * @param target The address of the member whose stake will be slashed.
     */
    function slashStake(address target) internal {
        uint256 slashedAmount = members[target].stake;
        treasury += slashedAmount;

        delete members[target];
        delete voteCounts[target];

        emit StakeSlashed(target, slashedAmount);
    }

    /**
     * @dev Returns the total number of DAO members.
     */
    function getTotalMembers() public view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < address(this).balance; i++) {
            if (members[address(i)].exists) {
                count++;
            }
        }
        return count;
    }

    /**
     * @dev Allows the DAO treasury to withdraw funds.
     * @param amount The amount to withdraw.
     * @param to The address to send the funds to.
     */
    function withdrawTreasury(uint256 amount, address payable to) external onlyMember {
        require(amount <= treasury, "Insufficient treasury balance");
        treasury -= amount;
        to.transfer(amount);
    }
}
```
