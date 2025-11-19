"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: Create a governance contract for a DAO with veNFT-based voting, boosting, and staking reward mechanisms, similar to iZUMi Finance's governance model.
Generated: DETERMINISTIC_c32d651506712888
Batch ID: 20250612_153424
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title Governance Contract for DAO with veNFT-based Voting, Boosting, and Staking Reward Mechanisms
 */
contract GovernanceContract {
    using SafeMath for uint256;

    // Mapping of user to their veNFT balance
    mapping(address => uint256) public veNFTBalances;

    // Mapping of proposal ID to proposal details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user to their voting power
    mapping(address => uint256) public votingPowers;

    // veNFT contract address
    address public veNFTContractAddress;

    // Reward token contract address
    address public rewardTokenContractAddress;

    // Proposal count
    uint256 public proposalCount;

    // Voting power threshold for proposal creation
    uint256 public votingPowerThreshold;

    // Boosting factor for staked veNFTs
    uint256 public boostingFactor;

    // Staking reward rate
    uint256 public stakingRewardRate;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 proposalId, address creator, string description);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 proposalId, address voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Event emitted when a user stakes veNFTs
    event veNFTStaked(address user, uint256 amount);

    // Event emitted when a user unstakes veNFTs
    event veNFTUnstaked(address user, uint256 amount);

    // Event emitted when staking rewards are distributed
    event StakingRewardsDistributed(address user, uint256 amount);

    /**
     * @notice Constructor for GovernanceContract
     * @param _veNFTContractAddress veNFT contract address
     * @param _rewardTokenContractAddress Reward token contract address
     * @param _votingPowerThreshold Voting power threshold for proposal creation
     * @param _boostingFactor Boosting factor for staked veNFTs
     * @param _stakingRewardRate Staking reward rate
     */
    constructor(
        address _veNFTContractAddress,
        address _rewardTokenContractAddress,
        uint256 _votingPowerThreshold,
        uint256 _boostingFactor,
        uint256 _stakingRewardRate
    ) public {
        veNFTContractAddress = _veNFTContractAddress;
        rewardTokenContractAddress = _rewardTokenContractAddress;
        votingPowerThreshold = _votingPowerThreshold;
        boostingFactor = _boostingFactor;
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @notice Create a new proposal
     * @param _description Proposal description
     */
    function createProposal(string memory _description) public {
        require(votingPowers[msg.sender] >= votingPowerThreshold, "Insufficient voting power");

        proposalCount++;
        proposals[proposalCount] = Proposal(
            proposalCount,
            msg.sender,
            _description,
            0,
            0,
            false
        );

        emit NewProposal(proposalCount, msg.sender, _description);
    }

    /**
     * @notice Vote on a proposal
     * @param _proposalId Proposal ID
     * @param _support Whether to support the proposal
     */
    function vote(uint256 _proposalId, bool _support) public {
        require(proposals[_proposalId].exists, "Proposal does not exist");

        uint256 votingPower = votingPowers[msg.sender];
        require(votingPower > 0, "Insufficient voting power");

        if (_support) {
            proposals[_proposalId].yesVotes = proposals[_proposalId].yesVotes.add(votingPower);
        } else {
            proposals[_proposalId].noVotes = proposals[_proposalId].noVotes.add(votingPower);
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @notice Execute a proposal
     * @param _proposalId Proposal ID
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(proposals[_proposalId].yesVotes > proposals[_proposalId].noVotes, "Proposal not passed");

        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @notice Stake veNFTs
     * @param _amount Amount of veNFTs to stake
     */
    function stakeveNFTs(uint256 _amount) public {
        require(IERC721(veNFTContractAddress).balanceOf(msg.sender) >= _amount, "Insufficient veNFTs");

        veNFTBalances[msg.sender] = veNFTBalances[msg.sender].add(_amount);
        votingPowers[msg.sender] = votingPowers[msg.sender].add(_amount.mul(boostingFactor));

        emit veNFTStaked(msg.sender, _amount);
    }

    /**
     * @notice Unstake veNFTs
     * @param _amount Amount of veNFTs to unstake
     */
    function unstakeveNFTs(uint256 _amount) public {
        require(veNFTBalances[msg.sender] >= _amount, "Insufficient staked veNFTs");

        veNFTBalances[msg.sender] = veNFTBalances[msg.sender].sub(_amount);
        votingPowers[msg.sender] = votingPowers[msg.sender].sub(_amount.mul(boostingFactor));

        emit veNFTUnstaked(msg.sender, _amount);
    }

    /**
     * @notice Distribute staking rewards
     */
    function distributeStakingRewards() public {
        uint256 rewardAmount = IERC20(rewardTokenContractAddress).balanceOf(address(this)).mul(stakingRewardRate);
        IERC20(rewardTokenContractAddress).transfer(msg.sender, rewardAmount);

        emit StakingRewardsDistributed(msg.sender, rewardAmount);
    }

    /**
     * @notice Proposal struct
     */
    struct Proposal {
        uint256 id;
        address creator;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        bool exists;
    }
}
```
