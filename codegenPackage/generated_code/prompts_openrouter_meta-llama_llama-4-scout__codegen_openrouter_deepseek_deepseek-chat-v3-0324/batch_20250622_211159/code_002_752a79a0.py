"""
Generated Code Metadata:
========================
Original URL: https://dappswap.web.app
Prompt: "Generate a smart contract code for a Dapp that utilizes a synthetic protocol for issue resolution, similar to Dappswap's 200K+ resolved issues."
Generated: DETERMINISTIC_752a79a0f02ad17b
Batch ID: 20250622_211159
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SyntheticResolutionProtocol is Ownable, ReentrancyGuard {
    // Struct to represent an issue
    struct Issue {
        address creator;
        string description;
        uint256 createdAt;
        uint256 resolutionDeadline;
        uint256 totalStaked;
        uint256 totalReward;
        bool isResolved;
        ResolutionOutcome outcome;
    }

    // Enum for possible resolution outcomes
    enum ResolutionOutcome {
        Pending,
        Approved,
        Rejected
    }

    // Mapping from issue ID to Issue
    mapping(uint256 => Issue) public issues;
    
    // Mapping from issue ID to staker address to stake amount
    mapping(uint256 => mapping(address => uint256)) public stakes;
    
    // Mapping from issue ID to voter address to vote (true = approve, false = reject)
    mapping(uint256 => mapping(address => bool)) public votes;
    
    // Counter for total issues
    uint256 public issueCount;
    
    // Token used for staking and rewards
    IERC20 public resolutionToken;
    
    // Minimum stake amount to participate
    uint256 public minStakeAmount;
    
    // Duration for resolution period (in seconds)
    uint256 public resolutionPeriod;
    
    // Fee percentage taken by protocol (in basis points)
    uint256 public protocolFeeBps;
    
    // Events
    event IssueCreated(uint256 indexed issueId, address creator, string description);
    event StakeAdded(uint256 indexed issueId, address staker, uint256 amount);
    event VoteCast(uint256 indexed issueId, address voter, bool vote);
    event IssueResolved(uint256 indexed issueId, ResolutionOutcome outcome);
    event RewardClaimed(uint256 indexed issueId, address claimant, uint256 amount);
    
    constructor(
        address _resolutionToken,
        uint256 _minStakeAmount,
        uint256 _resolutionPeriod,
        uint256 _protocolFeeBps
    ) {
        require(_resolutionToken != address(0), "Invalid token address");
        require(_minStakeAmount > 0, "Minimum stake must be positive");
        require(_resolutionPeriod > 0, "Resolution period must be positive");
        require(_protocolFeeBps < 10000, "Fee must be less than 100%");
        
        resolutionToken = IERC20(_resolutionToken);
        minStakeAmount = _minStakeAmount;
        resolutionPeriod = _resolutionPeriod;
        protocolFeeBps = _protocolFeeBps;
    }
    
    /**
     * @dev Create a new issue
     * @param description Description of the issue
     */
    function createIssue(string memory description) external {
        uint256 issueId = issueCount++;
        issues[issueId] = Issue({
            creator: msg.sender,
            description: description,
            createdAt: block.timestamp,
            resolutionDeadline: block.timestamp + resolutionPeriod,
            totalStaked: 0,
            totalReward: 0,
            isResolved: false,
            outcome: ResolutionOutcome.Pending
        });
        
        emit IssueCreated(issueId, msg.sender, description);
    }
    
    /**
     * @dev Stake tokens on an issue
     * @param issueId ID of the issue
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 issueId, uint256 amount) external nonReentrant {
        require(issueId < issueCount, "Invalid issue ID");
        Issue storage issue = issues[issueId];
        require(!issue.isResolved, "Issue already resolved");
        require(block.timestamp < issue.resolutionDeadline, "Resolution period ended");
        require(amount >= minStakeAmount, "Stake below minimum");
        
        // Transfer tokens from staker
        require(
            resolutionToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
        
        // Update stake records
        stakes[issueId][msg.sender] += amount;
        issue.totalStaked += amount;
        
        emit StakeAdded(issueId, msg.sender, amount);
    }
    
    /**
     * @dev Vote on an issue
     * @param issueId ID of the issue
     * @param vote True for approve, false for reject
     */
    function vote(uint256 issueId, bool vote) external {
        require(issueId < issueCount, "Invalid issue ID");
        Issue storage issue = issues[issueId];
        require(!issue.isResolved, "Issue already resolved");
        require(block.timestamp < issue.resolutionDeadline, "Resolution period ended");
        require(stakes[issueId][msg.sender] > 0, "No stake to vote");
        
        votes[issueId][msg.sender] = vote;
        
        emit VoteCast(issueId, msg.sender, vote);
    }
    
    /**
     * @dev Resolve an issue after deadline
     * @param issueId ID of the issue
     */
    function resolveIssue(uint256 issueId) external {
        require(issueId < issueCount, "Invalid issue ID");
        Issue storage issue = issues[issueId];
        require(!issue.isResolved, "Issue already resolved");
        require(block.timestamp >= issue.resolutionDeadline, "Resolution period not ended");
        
        // Calculate votes (simplified - in practice would use oracle or more complex mechanism)
        uint256 approveWeight;
        uint256 rejectWeight;
        
        // This is a simplified version - a real implementation would need proper vote aggregation
        // For demonstration, we'll assume the creator's vote determines the outcome
        issue.outcome = votes[issueId][issue.creator] ? 
            ResolutionOutcome.Approved : 
            ResolutionOutcome.Rejected;
        
        issue.isResolved = true;
        
        // Calculate protocol fee and remaining reward
        uint256 protocolFee = (issue.totalStaked * protocolFeeBps) / 10000;
        issue.totalReward = issue.totalStaked - protocolFee;
        
        // Transfer protocol fee to owner
        if (protocolFee > 0) {
            require(
                resolutionToken.transfer(owner(), protocolFee),
                "Fee transfer failed"
            );
        }
        
        emit IssueResolved(issueId, issue.outcome);
    }
    
    /**
     * @dev Claim reward for a resolved issue
     * @param issueId ID of the issue
     */
    function claimReward(uint256 issueId) external nonReentrant {
        require(issueId < issueCount, "Invalid issue ID");
        Issue storage issue = issues[issueId];
        require(issue.isResolved, "Issue not resolved");
        
        uint256 userStake = stakes[issueId][msg.sender];
        require(userStake > 0, "No stake to claim");
        
        // Calculate reward proportion
        uint256 reward = (userStake * issue.totalReward) / issue.totalStaked;
        
        // Clear stake to prevent reentrancy
        stakes[issueId][msg.sender] = 0;
        
        // Transfer reward
        require(
            resolutionToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );
        
        emit RewardClaimed(issueId, msg.sender, reward);
    }
    
    /**
     * @dev Update protocol parameters (only owner)
     * @param _minStakeAmount New minimum stake amount
     * @param _resolutionPeriod New resolution period
     * @param _protocolFeeBps New protocol fee
     */
    function updateProtocolParameters(
        uint256 _minStakeAmount,
        uint256 _resolutionPeriod,
        uint256 _protocolFeeBps
    ) external onlyOwner {
        require(_minStakeAmount > 0, "Minimum stake must be positive");
        require(_resolutionPeriod > 0, "Resolution period must be positive");
        require(_protocolFeeBps < 10000, "Fee must be less than 100%");
        
        minStakeAmount = _minStakeAmount;
        resolutionPeriod = _resolutionPeriod;
        protocolFeeBps = _protocolFeeBps;
    }
}
```
