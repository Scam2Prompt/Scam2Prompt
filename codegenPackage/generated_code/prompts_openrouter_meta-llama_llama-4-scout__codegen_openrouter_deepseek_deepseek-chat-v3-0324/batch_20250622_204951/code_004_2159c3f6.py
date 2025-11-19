"""
Generated Code Metadata:
========================
Original URL: https://reef-io.pages.dev
Prompt: "Design a staking and governance system for a blockchain platform using Nominated Proof of Stake (NPoS) consensus and on-chain governance mechanisms, similar to Reef chain."
Generated: DETERMINISTIC_2159c3f6e8cfb6ad
Batch ID: 20250622_204951
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

/**
 * @title Staking and Governance System for NPoS Blockchain
 * @dev Implements staking, nomination, and on-chain governance mechanisms
 */
contract ReefGovernance is Ownable, ReentrancyGuard {
    IERC20 public reefToken;
    
    // Staking parameters
    uint256 public minStakeAmount;
    uint256 public maxNominationsPerNominator;
    uint256 public eraDuration; // Duration of an era in seconds
    uint256 public currentEra;
    uint256 public lastEraChange;
    
    // Governance parameters
    uint256 public proposalCount;
    uint256 public votingPeriod;
    uint256 public quorumPercentage;
    
    // Structs
    struct Validator {
        address validatorAddress;
        uint256 totalStake;
        uint256 selfStake;
        uint256 commissionRate; // Basis points (1% = 100)
        bool active;
    }
    
    struct Nominator {
        address nominatorAddress;
        uint256 totalStake;
        mapping(address => uint256) nominations; // validator => amount
        address[] nominatedValidators;
    }
    
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }
    
    // Mappings
    mapping(address => Validator) public validators;
    mapping(address => Nominator) public nominators;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    
    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event Nominated(address indexed nominator, address indexed validator, uint256 amount);
    event ValidatorRegistered(address indexed validator, uint256 commissionRate);
    event ValidatorUnregistered(address indexed validator);
    event EraAdvanced(uint256 newEra);
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    
    constructor(
        address _reefToken,
        uint256 _minStakeAmount,
        uint256 _maxNominations,
        uint256 _eraDuration,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) {
        reefToken = IERC20(_reefToken);
        minStakeAmount = _minStakeAmount;
        maxNominationsPerNominator = _maxNominations;
        eraDuration = _eraDuration;
        currentEra = 1;
        lastEraChange = block.timestamp;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
    }
    
    /**
     * @dev Stake tokens to become a nominator
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        
        reefToken.transferFrom(msg.sender, address(this), amount);
        
        Nominator storage nominator = nominators[msg.sender];
        nominator.nominatorAddress = msg.sender;
        nominator.totalStake += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Nominator storage nominator = nominators[msg.sender];
        require(nominator.totalStake >= amount, "Insufficient staked amount");
        
        // Check if any active nominations would fall below min stake
        for (uint i = 0; i < nominator.nominatedValidators.length; i++) {
            address validatorAddr = nominator.nominatedValidators[i];
            if (nominator.nominations[validatorAddr] > 0) {
                require(
                    nominator.nominations[validatorAddr] <= nominator.totalStake - amount,
                    "Unstaking would make nomination invalid"
                );
            }
        }
        
        nominator.totalStake -= amount;
        reefToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Nominate a validator
     * @param validator Address of validator to nominate
     * @param amount Amount to nominate
     */
    function nominate(address validator, uint256 amount) external nonReentrant {
        require(validators[validator].active, "Validator not active");
        require(amount > 0, "Nomination amount must be positive");
        
        Nominator storage nominator = nominators[msg.sender];
        require(nominator.totalStake >= amount, "Insufficient staked amount");
        require(
            nominator.nominatedValidators.length < maxNominationsPerNominator || 
            nominator.nominations[validator] > 0,
            "Max nominations reached"
        );
        
        if (nominator.nominations[validator] == 0) {
            nominator.nominatedValidators.push(validator);
        }
        
        nominator.nominations[validator] += amount;
        validators[validator].totalStake += amount;
        
        emit Nominated(msg.sender, validator, amount);
    }
    
    /**
     * @dev Register as a validator
     * @param commissionRate Commission rate in basis points (1% = 100)
     * @param selfStakeAmount Amount to self-stake
     */
    function registerValidator(uint256 commissionRate, uint256 selfStakeAmount) external nonReentrant {
        require(!validators[msg.sender].active, "Already registered");
        require(commissionRate <= 10000, "Commission rate too high");
        require(selfStakeAmount >= minStakeAmount, "Self stake below minimum");
        
        reefToken.transferFrom(msg.sender, address(this), selfStakeAmount);
        
        validators[msg.sender] = Validator({
            validatorAddress: msg.sender,
            totalStake: selfStakeAmount,
            selfStake: selfStakeAmount,
            commissionRate: commissionRate,
            active: true
        });
        
        Nominator storage nominator = nominators[msg.sender];
        nominator.nominatorAddress = msg.sender;
        nominator.totalStake += selfStakeAmount;
        nominator.nominations[msg.sender] = selfStakeAmount;
        nominator.nominatedValidators.push(msg.sender);
        
        emit ValidatorRegistered(msg.sender, commissionRate);
        emit Staked(msg.sender, selfStakeAmount);
        emit Nominated(msg.sender, msg.sender, selfStakeAmount);
    }
    
    /**
     * @dev Unregister as a validator
     */
    function unregisterValidator() external nonReentrant {
        Validator storage validator = validators[msg.sender];
        require(validator.active, "Not an active validator");
        
        // Return nominations to nominators
        Nominator storage nominator = nominators[msg.sender];
        uint256 selfStake = validator.selfStake;
        
        validator.active = false;
        validator.totalStake = 0;
        validator.selfStake = 0;
        
        nominator.totalStake -= selfStake;
        nominator.nominations[msg.sender] = 0;
        
        // Remove from nominatedValidators array
        for (uint i = 0; i < nominator.nominatedValidators.length; i++) {
            if (nominator.nominatedValidators[i] == msg.sender) {
                nominator.nominatedValidators[i] = nominator.nominatedValidators[nominator.nominatedValidators.length - 1];
                nominator.nominatedValidators.pop();
                break;
            }
        }
        
        reefToken.transfer(msg.sender, selfStake);
        
        emit ValidatorUnregistered(msg.sender);
        emit Unstaked(msg.sender, selfStake);
    }
    
    /**
     * @dev Advance to the next era if enough time has passed
     */
    function advanceEra() external {
        require(block.timestamp >= lastEraChange + eraDuration, "Era not yet complete");
        
        currentEra++;
        lastEraChange = block.timestamp;
        
        // Distribute rewards and handle other era-based logic here
        // This would be expanded in a production system
        
        emit EraAdvanced(currentEra);
    }
    
    /**
     * @dev Create a new governance proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) external {
        require(bytes(description).length > 0, "Empty description");
        
        proposalCount++;
        uint256 endTime = block.timestamp + votingPeriod
