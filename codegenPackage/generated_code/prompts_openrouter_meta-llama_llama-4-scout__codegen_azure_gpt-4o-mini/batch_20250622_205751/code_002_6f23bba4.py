"""
Generated Code Metadata:
========================
Original URL: https://bafkreibgcum43j7d4mubge4izowokrtbcswc6llh62jjklhh7g5bzrfd6e.ipfs.dweb.link
Prompt: "Generate a smart contract code snippet for an Ethereum-based DAO voting system with staking multipliers for OpenGPU."
Generated: DETERMINISTIC_6f23bba4cef1486c
Batch ID: 20250622_205751
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

contract DAOVoting is Ownable {
    using SafeMath for uint256;

    // Struct to hold proposal details
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        uint256 endTime;    // Voting end time
        mapping(address => uint256) votes; // Votes by each voter
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount; // Total number of proposals

    // Staking token
    IERC20 public stakingToken;

    // Staking multipliers
    mapping(address => uint256) public stakingMultiplier;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to create a new proposal
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be greater than 0");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0,
            endTime: block.timestamp.add(_duration)
        });

        emit ProposalCreated(proposalCount, _description, block.timestamp.add(_duration));
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId, uint256 _amount) external {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens to the contract as a vote
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Calculate effective votes based on staking multiplier
        uint256 effectiveVotes = _amount.mul(stakingMultiplier[msg.sender]);
        proposal.votes[msg.sender] = proposal.votes[msg.sender].add(effectiveVotes);
        proposal.voteCount = proposal.voteCount.add(effectiveVotes);

        emit Voted(_proposalId, msg.sender, effectiveVotes);
    }

    // Function to set staking multipliers for addresses
    function setStakingMultiplier(address _staker, uint256 _multiplier) external onlyOwner {
        require(_multiplier > 0, "Multiplier must be greater than 0");
        stakingMultiplier[_staker] = _multiplier;
    }

    // Function to withdraw tokens after voting ends
    function withdrawTokens(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.endTime, "Voting is still ongoing");
        require(proposal.votes[msg.sender] > 0, "No votes to withdraw");

        uint256 amountToWithdraw = proposal.votes[msg.sender].div(stakingMultiplier[msg.sender]);
        proposal.votes[msg.sender] = 0; // Reset votes for the user

        // Transfer the tokens back to the voter
        stakingToken.transfer(msg.sender, amountToWithdraw);
    }

    // Function to get proposal details
    function getProposal(uint256 _proposalId) external view returns (string memory, uint256, uint256) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
