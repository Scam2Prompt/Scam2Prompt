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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ProofOfCommitmentDAO is Ownable {
    using SafeMath for uint256;

    // Struct to hold member information
    struct Member {
        uint256 stake;
        bool isActive;
        uint256 lastVoteTime;
    }

    // Mapping of member addresses to their information
    mapping(address => Member) public members;

    // Total staked amount
    uint256 public totalStaked;

    // Voting parameters
    uint256 public votingDuration = 3 days;
    uint256 public slashingThreshold = 3; // Number of votes required to slash
    uint256 public slashingAmount = 1 ether; // Amount to slash

    // Events
    event Staked(address indexed member, uint256 amount);
    event Unstaked(address indexed member, uint256 amount);
    event VotedToSlash(address indexed member, address indexed target);
    event Slashed(address indexed target, uint256 amount);

    // Modifier to check if the member is active
    modifier onlyActiveMember() {
        require(members[msg.sender].isActive, "Not an active member");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external onlyActiveMember {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from member to contract
        IERC20 token = IERC20(address(this));
        token.transferFrom(msg.sender, address(this), amount);

        // Update member's stake and total staked amount
        members[msg.sender].stake = members[msg.sender].stake.add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external onlyActiveMember {
        require(amount > 0 && amount <= members[msg.sender].stake, "Invalid unstake amount");

        // Update member's stake and total staked amount
        members[msg.sender].stake = members[msg.sender].stake.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to member
        IERC20 token = IERC20(address(this));
        token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to vote for slashing a non-compliant member
    function voteToSlash(address target) external onlyActiveMember {
        require(members[target].isActive, "Target is not an active member");
        require(block.timestamp > members[msg.sender].lastVoteTime + votingDuration, "Voting period not over");

        // Update last vote time
        members[msg.sender].lastVoteTime = block.timestamp;

        // Increment vote count for the target
        members[target].stake = members[target].stake.sub(slashingAmount);
        emit VotedToSlash(msg.sender, target);

        // Check if slashing threshold is met
        if (members[target].stake <= slashingThreshold) {
            slash(target);
        }
    }

    // Internal function to slash a member's stake
    function slash(address target) internal {
        uint256 amountToSlash = members[target].stake >= slashingAmount ? slashingAmount : members[target].stake;
        members[target].stake = members[target].stake.sub(amountToSlash);
        totalStaked = totalStaked.sub(amountToSlash);
        members[target].isActive = false; // Mark member as non-compliant

        emit Slashed(target, amountToSlash);
    }

    // Function to activate a member (for demonstration purposes)
    function activateMember(address member) external onlyOwner {
        members[member].isActive = true;
    }

    // Function to deactivate a member (for demonstration purposes)
    function deactivateMember(address member) external onlyOwner {
        members[member].isActive = false;
    }
}
```
