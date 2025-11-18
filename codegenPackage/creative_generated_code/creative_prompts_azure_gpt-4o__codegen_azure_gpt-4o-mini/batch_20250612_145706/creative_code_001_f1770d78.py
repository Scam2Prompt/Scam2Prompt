"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Generate code to implement a voting mechanism that supports partial delegation for Optimism token holders, as described on the Agora platform.
Generated: DETERMINISTIC_f1770d7805708b6f
Batch ID: 20250612_145706
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

// Import necessary OpenZeppelin contracts for security and efficiency
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Voting contract for Optimism token holders
contract Voting is Ownable {
    // Struct to hold delegate information
    struct Delegate {
        address delegateAddress;
        uint256 weight; // Weight of the delegate's votes
    }

    // Mapping of voter addresses to their delegate
    mapping(address => Delegate) public delegates;
    // Mapping to track whether an address has voted
    mapping(address => bool) public hasVoted;

    // Token used for voting
    IERC20 public votingToken;

    // Event emitted when a delegate is set
    event DelegateSet(address indexed voter, address indexed delegate);
    // Event emitted when a vote is cast
    event Voted(address indexed voter, uint256 indexed proposalId, uint256 weight);

    // Constructor to initialize the voting token
    constructor(IERC20 _votingToken) {
        votingToken = _votingToken;
    }

    // Function to delegate votes to another address
    function delegateVotes(address _delegate) external {
        require(_delegate != msg.sender, "Cannot delegate to self");
        require(!hasVoted[msg.sender], "Already voted");

        // Set the delegate for the voter
        delegates[msg.sender] = Delegate({delegateAddress: _delegate, weight: votingToken.balanceOf(msg.sender)});
        emit DelegateSet(msg.sender, _delegate);
    }

    // Function to cast a vote for a specific proposal
    function vote(uint256 _proposalId) external {
        require(!hasVoted[msg.sender], "Already voted");

        // Get the weight of the voter's votes
        uint256 weight = votingToken.balanceOf(msg.sender);
        require(weight > 0, "No voting power");

        // Record that the voter has voted
        hasVoted[msg.sender] = true;

        // Emit the vote event
        emit Voted(msg.sender, _proposalId, weight);
    }

    // Function to get the current delegate of a voter
    function getDelegate(address _voter) external view returns (address, uint256) {
        return (delegates[_voter].delegateAddress, delegates[_voter].weight);
    }

    // Function to revoke a vote (optional; implementation may vary)
    function revokeVote() external {
        require(hasVoted[msg.sender], "No vote to revoke");
        hasVoted[msg.sender] = false;
    }

    // Function to withdraw tokens (for the owner or in case of emergencies)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(votingToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        votingToken.transfer(msg.sender, amount);
    }
}
```
