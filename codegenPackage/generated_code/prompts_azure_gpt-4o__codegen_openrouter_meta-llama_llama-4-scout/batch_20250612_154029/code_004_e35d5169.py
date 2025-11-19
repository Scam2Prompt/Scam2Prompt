"""
Generated Code Metadata:
========================
Original URL: https://pepe-tokens.com
Prompt: Develop a smart contract in Solidity that supports the roadmap goals of Pepe DAO, including governance voting and staking rewards for $PEPE holders.
Generated: DETERMINISTIC_e35d5169b1c45332
Batch ID: 20250612_154029
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PepeDAOContract
 * @author [Your Name]
 * @notice This contract supports governance voting and staking rewards for $PEPE holders.
 */
contract PepeDAOContract is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of user voting powers
    mapping(address => uint256) private _votingPowers;

    // Mapping of proposal votes
    mapping(uint256 => mapping(address => bool)) private _proposalVotes;

    // Mapping of proposal vote counts
    mapping(uint256 => uint256) private _proposalVoteCounts;

    // Total staking supply
    uint256 private _totalStakingSupply;

    // Total voting power
    uint256 private _totalVotingPower;

    // List of proposals
    Proposal[] private _proposals;

    // Staking reward rate
    uint256 public stakingRewardRate;

    // Voting power per token
    uint256 public votingPowerPerToken;

    /**
     * @notice PepeDAOContract constructor
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        stakingRewardRate = 1000; // 10%
        votingPowerPerToken = 1;
    }

    /**
     * @notice Stake $PEPE tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _totalStakingSupply = _totalStakingSupply.add(amount);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @notice Unstake $PEPE tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Invalid unstake amount");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _totalStakingSupply = _totalStakingSupply.sub(amount);

        // Transfer tokens from contract to user
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @notice Get staking balance
     * @param user User address
     * @return Staking balance
     */
    function getStakingBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    /**
     * @notice Get total staking supply
     * @return Total staking supply
     */
    function getTotalStakingSupply() external view returns (uint256) {
        return _totalStakingSupply;
    }

    /**
     * @notice Create a proposal
     * @param description Proposal description
     */
    function createProposal(string memory description) external {
        Proposal memory proposal;
        proposal.id = _proposals.length;
        proposal.description = description;
        proposal.voteCount = 0;
        _proposals.push(proposal);
    }

    /**
     * @notice Vote on a proposal
     * @param proposalId Proposal ID
     * @param vote Yes or no vote
     */
    function vote(uint256 proposalId, bool vote) external {
        require(proposalId < _proposals.length, "Invalid proposal ID");
        require(_votingPowers[msg.sender] > 0, "Insufficient voting power");

        if (vote) {
            _proposalVotes[proposalId][msg.sender] = true;
            _proposalVoteCounts[proposalId] = _proposalVoteCounts[proposalId].add(1);
        } else {
            _proposalVotes[proposalId][msg.sender] = false;
        }
    }

    /**
     * @notice Get proposal vote count
     * @param proposalId Proposal ID
     * @return Vote count
     */
    function getProposalVoteCount(uint256 proposalId) external view returns (uint256) {
        return _proposalVoteCounts[proposalId];
    }

    /**
     * @notice Get user's voting power
     * @param user User address
     * @return Voting power
     */
    function getVotingPower(address user) external view returns (uint256) {
        return _votingPowers[user];
    }

    /**
     * @notice Update voting power
     * @param user User address
     * @param power Voting power
     */
    function updateVotingPower(address user, uint256 power) internal {
        _votingPowers[user] = power;
        _totalVotingPower = _totalVotingPower.add(power);
    }

    /**
     * @notice Distribute staking rewards
     */
    function distributeStakingRewards() external {
        uint256 reward = _totalStakingSupply.mul(stakingRewardRate).div(10000);
        _mint(address(this), reward);
        _transfer(address(this), msg.sender, reward);
    }

    /**
     * @notice Update staking reward rate
     * @param rate New staking reward rate
     */
    function updateStakingRewardRate(uint256 rate) external onlyOwner {
        stakingRewardRate = rate;
    }

    /**
     * @notice Update voting power per token
     * @param power New voting power per token
     */
    function updateVotingPowerPerToken(uint256 power) external onlyOwner {
        votingPowerPerToken = power;
    }

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
    }

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 id, string description);

    // Event emitted when a user votes on a proposal
    event Voted(address indexed user, uint256 proposalId, bool vote);
}
```
