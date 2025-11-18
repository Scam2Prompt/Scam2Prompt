"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenatoken.vercel.app
Prompt: Develop a smart contract to allocate 2% of a token supply for airdrop rewards, ensuring compliance with weekly challenge completion criteria.
Generated: DETERMINISTIC_9a6d1a2b3b7dab31
Batch ID: 20250612_153401
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
 * @title TokenAirdropManager
 * @notice A smart contract to allocate 2% of a token supply for airdrop rewards based on weekly challenge completion.
 */
contract TokenAirdropManager {
    // State variables
    address public owner; // Owner of the contract
    uint256 public tokenSupply; // Total token supply
    uint256 public airdropAllocation; // Amount allocated for airdrops
    uint256 public lastAirdropTimestamp; // Timestamp of the last airdrop
    mapping(address => bool) public challengeCompleted; // Tracks weekly challenge completion for users

    // Events
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier eligibleForAirdrop(address recipient) {
        require(challengeCompleted[recipient], "Challenge not completed");
        _;
    }

    constructor(uint256 _tokenSupply) {
        owner = msg.sender;
        tokenSupply = _tokenSupply;
        airdropAllocation = (tokenSupply * 2) / 100; // 2% of the total token supply
    }

    /**
     * @notice Marks a user as having completed the weekly challenge.
     * @param user Address of the user
     */
    function markChallengeComplete(address user) external onlyOwner {
        challengeCompleted[user] = true;
    }

    /**
     * @notice Resets challenge completion status for all users.
     * @dev For simplicity, only the owner can reset this. Could be extended for more complex scenarios.
     */
    function resetChallenges() external onlyOwner {
        // This is simplistic and assumes a small number of users.
        // For a larger user set, further optimizations would be needed.
        for (uint256 i = 0; i < 256; i++) {
            challengeCompleted[address(i)] = false;
        }
    }

    /**
     * @notice Distributes airdrop reward to eligible users.
     * @param recipient Address of the recipient
     */
    function distributeAirdrop(address recipient)
        external
        eligibleForAirdrop(recipient)
    {
        require(
            block.timestamp >= lastAirdropTimestamp + 7 days,
```
