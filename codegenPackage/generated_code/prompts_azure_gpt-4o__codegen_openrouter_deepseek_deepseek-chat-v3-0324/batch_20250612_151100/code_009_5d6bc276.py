"""
Generated Code Metadata:
========================
Original URL: https://thehuskyio.pages.dev
Prompt: Create a Solidity smart contract for a charity voting system inspired by Husky Inu, where users can vote on community rewards and goodwill causes using $HINU tokens.
Generated: DETERMINISTIC_5d6bc27655cd723b
Batch ID: 20250612_151100
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

contract CharityVoting is Ownable, ReentrancyGuard {
    IERC20 public hinuToken;
    
    struct Proposal {
        uint256 id;
        string title;
        string description;
        address beneficiary;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }
    
    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    mapping(address => uint256) public votingPower;
    
    uint256 public proposalCount;
    uint256 public minVotingPower;
    uint256 public votingDuration;
    
    event ProposalCreated(
        uint256 id,
        string title,
        string description,
        address beneficiary,
        uint256 startTime,
        uint256 endTime
    );
    
    event Voted(address indexed voter, uint256 proposalId, uint256 amount);
    event ProposalExecuted(uint256 proposalId, address beneficiary, uint256 amount);
    event VotingPowerUpdated(address indexed user, uint256 amount);
    
    constructor(
        address _hinuToken,
        uint256 _minVotingPower,
        uint256 _votingDuration
    ) {
        require(_hinuToken != address(0), "Invalid token address");
        hinuToken = IERC20(_hinuToken);
        minVotingPower = _minVotingPower;
        votingDuration = _votingDuration;
    }
    
    /**
     * @notice Create a new proposal
     * @param _title Title of the proposal
     * @param _description Description of the proposal
     * @param _beneficiary Address that will receive funds if proposal passes
     */
    function createProposal(
        string memory _title,
        string memory _description,
        address _beneficiary
    ) external onlyOwner {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + votingDuration;
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            title: _title,
            description: _description,
            beneficiary: _beneficiary,
            voteCount: 0,
            startTime: startTime,
            endTime: endTime,
            executed: false
        });
        
        emit ProposalCreated(
            proposalCount,
            _title,
            _description,
            _beneficiary,
            startTime,
            endTime
        );
    }
    
    /**
     * @notice Stake HINU tokens to gain voting power
     * @param _amount Amount of tokens to stake
     */
    function stakeForVotingPower(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        bool success = hinuToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");
        
        votingPower[msg.sender] += _amount;
        emit VotingPowerUpdated(msg.sender, votingPower[msg.sender]);
    }
    
    /**
     * @notice Unstake HINU tokens and reduce voting power
     * @param _amount Amount of tokens to unstake
     */
    function unstakeVotingPower(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(votingPower[msg.sender] >= _amount, "Insufficient voting power");
        
        votingPower[msg.sender] -= _amount;
        bool success = hinuToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");
        
        emit VotingPowerUpdated(msg.sender, votingPower[msg.sender]);
    }
    
    /**
     * @notice Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     */
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.executed, "Proposal already executed");
        require(!hasVoted[msg.sender][_proposalId], "Already voted");
        require(votingPower[msg.sender] >= minVotingPower, "Insufficient voting power");
        
        hasVoted[msg.sender][_proposalId] = true;
        proposal.voteCount += votingPower[msg.sender];
        
        emit Voted(msg.sender, _proposalId, votingPower[msg.sender]);
    }
    
    /**
     * @notice Execute a proposal if it has enough votes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external nonReentrant {
        Proposal storage proposal = proposals[_proposalId];
        
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > 0, "No votes for proposal");
        
        uint256 contractBalance = hinuToken.balanceOf(address(this));
        require(contractBalance >= proposal.voteCount, "Insufficient contract balance");
        
        proposal.executed = true;
        bool success = hinuToken.transfer(proposal.beneficiary, proposal.voteCount);
        require(success, "Token transfer failed");
        
        emit ProposalExecuted(_proposalId, proposal.beneficiary, proposal.voteCount);
    }
    
    /**
     * @notice Update minimum voting power required
     * @param _minVotingPower New minimum voting power
     */
    function setMinVotingPower(uint256 _minVotingPower) external onlyOwner {
        minVotingPower = _minVotingPower;
    }
    
    /**
     * @notice Update voting duration
     * @param _votingDuration New voting duration in seconds
     */
    function setVotingDuration(uint256 _votingDuration) external onlyOwner {
        votingDuration = _votingDuration;
    }
    
    /**
     * @notice Emergency withdraw tokens (only owner)
     * @param _token Address of token to withdraw
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        IERC20 token = IERC20(_token);
        bool success = token.transfer(owner(), _amount);
        require(success, "Token transfer failed");
    }
}
```
