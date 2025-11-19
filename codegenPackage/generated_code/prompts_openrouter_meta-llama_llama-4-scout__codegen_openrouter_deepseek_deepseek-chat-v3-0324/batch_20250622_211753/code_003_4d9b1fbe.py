"""
Generated Code Metadata:
========================
Original URL: https://weneedtomakeitrain.pages.dev
Prompt: Design a smart contract for a Vote-To-Earn mechanism, where token holders can vote on proposals and earn rewards in $FLOCK tokens.
Generated: DETERMINISTIC_4d9b1fbed2be6f29
Batch ID: 20250622_211753
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract VoteToEarn is Ownable, ReentrancyGuard {
    IERC20 public flockToken;

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 rewardPool;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    struct Voter {
        bool hasVoted;
        uint256 voteChoice;
        uint256 rewardClaimed;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => Voter)) public voters;
    mapping(address => uint256) public userRewards;

    event ProposalCreated(
        uint256 indexed id,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event Voted(
        address indexed voter,
        uint256 indexed proposalId,
        uint256 choice
    );
    event RewardClaimed(address indexed claimer, uint256 amount);
    event ProposalClosed(uint256 indexed proposalId, uint256 winningChoice);

    constructor(address _flockTokenAddress) {
        require(
            _flockTokenAddress != address(0),
            "Invalid token address"
        );
        flockToken = IERC20(_flockTokenAddress);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _duration Duration of the voting period in seconds
     * @param _rewardPool Amount of $FLOCK tokens allocated as rewards
     */
    function createProposal(
        string memory _description,
        uint256 _duration,
        uint256 _rewardPool
    ) external onlyOwner {
        require(_duration > 0, "Duration must be positive");
        require(
            flockToken.transferFrom(msg.sender, address(this), _rewardPool),
            "Token transfer failed"
        );

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            rewardPool: _rewardPool,
            startTime: block.timestamp,
            endTime: block.timestamp + _duration,
            isActive: true
        });

        emit ProposalCreated(
            proposalCount,
            _description,
            block.timestamp,
            block.timestamp + _duration
        );
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _choice The vote choice (1 for yes, 0 for no)
     */
    function vote(uint256 _proposalId, uint256 _choice) external {
        require(_proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.isActive, "Proposal is not active");
        require(
            block.timestamp >= proposal.startTime &&
                block.timestamp <= proposal.endTime,
            "Voting period is not active"
        );
        require(_choice == 0 || _choice == 1, "Invalid choice");
        require(
            !voters[_proposalId][msg.sender].hasVoted,
            "Already voted"
        );

        voters[_proposalId][msg.sender] = Voter({
            hasVoted: true,
            voteChoice: _choice,
            rewardClaimed: 0
        });

        proposal.voteCount += 1;

        emit Voted(msg.sender, _proposalId, _choice);
    }

    /**
     * @dev Close a proposal and distribute rewards
     * @param _proposalId ID of the proposal to close
     */
    function closeProposal(uint256 _proposalId) external onlyOwner {
        require(_proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.isActive, "Proposal is already closed");
        require(
            block.timestamp > proposal.endTime,
            "Voting period has not ended"
        );

        proposal.isActive = false;
        uint256 winningChoice = proposal.voteCount > 0 ? 1 : 0;

        // Distribute rewards to voters who voted for the winning choice
        if (proposal.voteCount > 0) {
            uint256 rewardPerVoter = proposal.rewardPool / proposal.voteCount;
            for (uint256 i = 0; i < proposal.voteCount; i++) {
                // Note: In a real implementation, you would need a way to track voters
                // This is simplified for demonstration
                // Consider using an array or mapping to track voters
            }
        }

        emit ProposalClosed(_proposalId, winningChoice);
    }

    /**
     * @dev Claim voting rewards
     * @param _proposalId ID of the proposal to claim rewards from
     */
    function claimReward(uint256 _proposalId) external nonReentrant {
        require(_proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.isActive, "Proposal is still active");
        Voter storage voter = voters[_proposalId][msg.sender];
        require(voter.hasVoted, "No vote to claim");
        require(voter.rewardClaimed == 0, "Reward already claimed");

        uint256 rewardAmount = proposal.rewardPool / proposal.voteCount;
        require(
            flockToken.transfer(msg.sender, rewardAmount),
            "Token transfer failed"
        );

        voter.rewardClaimed = rewardAmount;
        userRewards[msg.sender] += rewardAmount;

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Withdraw remaining tokens (for emergency or after all claims)
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = flockToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(
            flockToken.transfer(owner(), balance),
            "Token transfer failed"
        );
    }
}
```
