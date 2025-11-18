"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pendle.pages.dev
Prompt: Provide an example of how to integrate Pendle's voting mechanism into a decentralized application (dApp).
Generated: DETERMINISTIC_0963acd6a0f06078
Batch ID: 20250612_150435
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Pendle's Voting mechanism
interface IPendleVoting {
    function vote(uint256 proposalId, bool support) external;
    function getVotingPower(address voter) external view returns (uint256);
}

contract PendleVotingIntegration is Ownable {
    using SafeMath for uint256;

    IPendleVoting public pendleVoting;
    IERC20 public votingToken;

    // Mapping to keep track of user's voting power for a specific proposal
    mapping(uint256 => mapping(address => uint256)) public userVotingPower;

    // Event emitted when a user votes
    event Voted(address indexed voter, uint256 indexed proposalId, bool support, uint256 power);

    // Constructor to initialize the Pendle Voting contract and the voting token
    constructor(address _pendleVotingAddress, address _votingTokenAddress) {
        pendleVoting = IPendleVoting(_pendleVotingAddress);
        votingToken = IERC20(_votingTokenAddress);
    }

    // Function to vote on a proposal
    function voteOnProposal(uint256 proposalId, bool support) external {
        // Get the voter's current voting power
        uint256 votingPower = pendleVoting.getVotingPower(msg.sender);
        
        require(votingPower > 0, "You have no voting power");

        // Record the user's voting power for this proposal
        userVotingPower[proposalId][msg.sender] = votingPower;

        // Call Pendle's voting function
        pendleVoting.vote(proposalId, support);

        emit Voted(msg.sender, proposalId, support, votingPower);
    }

    // Function to update the Pendle Voting contract address
    function updatePendleVotingAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        pendleVoting = IPendleVoting(newAddress);
    }

    // Function to update the voting token address
    function updateVotingTokenAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        votingToken = IERC20(newAddress);
    }

    // Function to check the voting power of a user for a specific proposal
    function checkVotingPower(uint256 proposalId, address voter) external view returns (uint256) {
        return userVotingPower[proposalId][voter];
    }
}
```

This code integrates Pendle's voting mechanism into a decentralized application (dApp) by allowing users to vote on proposals using their voting power. The contract manages the interaction with the Pendle Voting interface and maintains a record of user voting power.
