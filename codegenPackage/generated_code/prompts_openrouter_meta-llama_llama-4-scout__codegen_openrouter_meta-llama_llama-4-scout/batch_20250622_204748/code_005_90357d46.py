"""
Generated Code Metadata:
========================
Original URL: https://sakaivault-io.pages.dev
Prompt: "Design a smart contract for a decentralized staking platform similar to Sakai Vault, including functions for staking, claiming rewards, and voting."
Generated: DETERMINISTIC_90357d46af4ba5ff
Batch ID: 20250622_204748
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title Staking Contract
 * @author [Your Name]
 * @notice A decentralized staking platform similar to Sakai Vault
 */
contract StakingContract is Ownable, Pausable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => Staker) public stakers;

    // Mapping of voting information
    mapping(address => Voter) public voters;

    // Token being staked
    IERC20 public stakingToken;

    // Reward token
    IERC20 public rewardToken;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Reward per second
    uint256 public rewardPerSecond;

    // Total staked amount
    uint256 public totalStaked;

    // Total reward
    uint256 public totalReward;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event ClaimedRewards(address indexed user, uint256 amount);

    // Event emitted when a user votes
    event Voted(address indexed user, uint256 proposalId, bool vote);

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Struct to hold staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 stakedAt;
        uint256 rewards;
    }

    // Struct to hold voter information
    struct Voter {
        mapping(uint256 => bool) votes;
    }

    // Mapping of proposals
    mapping(uint256 => Proposal) public proposals;

    // Proposal counter
    uint256 public proposalCounter;

    // Struct to hold proposal information
    struct Proposal {
        uint256 id;
        string description;
        bool executed;
        uint256 yesVotes;
        uint256 noVotes;
    }

    /**
     * @notice Constructor
     * @param _stakingToken Token being staked
     * @param _rewardToken Reward token
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public whenNotPaused {
        require(_amount > 0, "Invalid stake amount");

        Staker storage staker = stakers[msg.sender];

        // If user already staked, add to existing stake
        if (staker.stakedAt > 0) {
            require(staker.stakedAt.add(stakingDuration) >= block.timestamp, "Staking duration not over");
            staker.stakedAmount = staker.stakedAmount.add(_amount);
        } else {
            staker.stakedAmount = _amount;
            staker.stakedAt = block.timestamp;
        }

        totalStaked = totalStaked.add(_amount);

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public whenNotPaused {
        Staker storage staker = stakers[msg.sender];

        require(staker.stakedAt > 0, "User not staked");

        uint256 stakingEnd = staker.stakedAt.add(stakingDuration);
        require(stakingEnd <= block.timestamp, "Staking duration not over");

        uint256 rewards = calculateRewards(msg.sender);

        staker.rewards = 0;

        rewardToken.safeTransfer(msg.sender, rewards);

        emit ClaimedRewards(msg.sender, rewards);
    }

    /**
     * @notice Vote on a proposal
     * @param _proposalId Proposal ID
     * @param _vote Vote (true for yes, false for no)
     */
    function vote(uint256 _proposalId, bool _vote) public whenNotPaused {
        Voter storage voter = voters[msg.sender];

        require(proposals[_proposalId].id > 0, "Proposal not found");

        voter.votes[_proposalId] = _vote;

        if (_vote) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(1);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(1);
        }

        emit Voted(msg.sender, _proposalId, _vote);
    }

    /**
     * @notice Create a proposal
     * @param _description Proposal description
     */
    function createProposal(string memory _description) public onlyOwner {
        Proposal storage proposal = proposals[proposalCounter];

        proposal.id = proposalCounter;
        proposal.description = _description;
        proposal.executed = false;
        proposal.yesVotes = 0;
        proposal.noVotes = 0;

        proposalCounter++;

        emit ProposalCreated(proposal.id, proposal.description);
    }

    /**
     * @notice Execute a proposal
     * @param _proposalId Proposal ID
     */
    function executeProposal(uint256 _proposalId) public onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id > 0, "Proposal not found");
        require(!proposal.executed, "Proposal already executed");

        // Simple voting logic: if yes votes > no votes, execute proposal
        if (proposal.yesVotes > proposal.noVotes) {
            // Execute proposal logic here
            proposal.executed = true;

            emit ProposalExecuted(_proposalId);
        }
    }

    /**
     * @notice Calculate rewards for a user
     * @param _user User address
     * @return Rewards
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        Staker storage staker = stakers[_user];

        uint256 stakingEnd = staker.stakedAt.add(stakingDuration);
        uint256 stakingTime = block.timestamp.sub(staker.stakedAt);

        if (stakingTime > stakingDuration) {
            stakingTime = stakingDuration;
        }

        uint256 rewards = stakingTime.mul(rewardPerSecond).mul(staker.stakedAmount).div(totalStaked);

        return staker.rewards.add(rewards);
    }

    /**
     * @notice Pause the contract
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @notice Unpause the contract
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}
```
