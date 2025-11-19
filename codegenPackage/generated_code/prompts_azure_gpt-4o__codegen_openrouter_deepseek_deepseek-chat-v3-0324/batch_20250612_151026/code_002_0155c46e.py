"""
Generated Code Metadata:
========================
Original URL: https://synspad.firebaseapp.com
Prompt: Generate a smart contract template for launching high-quality blockchain projects on a decentralized protocol, inspired by SynsPad's features.
Generated: DETERMINISTIC_0155c46ef2ac8ffc
Batch ID: 20250612_151026
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ProjectLaunchpad
 * @dev A smart contract for launching high-quality blockchain projects with features inspired by SynsPad
 */
contract ProjectLaunchpad is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Project details structure
    struct Project {
        address creator;
        string name;
        string description;
        string website;
        string whitepaper;
        uint256 softCap;
        uint256 hardCap;
        uint256 minContribution;
        uint256 maxContribution;
        uint256 startTime;
        uint256 endTime;
        uint256 totalRaised;
        uint256 tokenPrice;
        address paymentToken;
        bool isApproved;
        bool isActive;
        bool isCompleted;
    }

    // Investor details structure
    struct Investor {
        uint256 amountContributed;
        bool hasClaimedTokens;
    }

    // Platform fee percentage (1% = 100)
    uint256 public platformFee = 200; // 2%
    address public feeWallet;
    
    // Array of all projects
    Project[] public projects;
    
    // Mapping from project ID to investor address to Investor struct
    mapping(uint256 => mapping(address => Investor)) public projectInvestors;
    
    // Mapping from project ID to token address
    mapping(uint256 => address) public projectTokens;
    
    // Events
    event ProjectCreated(uint256 indexed projectId, address indexed creator);
    event ProjectApproved(uint256 indexed projectId);
    event ProjectActivated(uint256 indexed projectId);
    event ProjectCompleted(uint256 indexed projectId);
    event Contributed(uint256 indexed projectId, address indexed investor, uint256 amount);
    event TokensClaimed(uint256 indexed projectId, address indexed investor, uint256 amount);
    event EmergencyWithdraw(uint256 indexed projectId, address indexed investor, uint256 amount);
    event FeeWalletUpdated(address newFeeWallet);
    event PlatformFeeUpdated(uint256 newFee);

    constructor(address _feeWallet) {
        require(_feeWallet != address(0), "Invalid fee wallet address");
        feeWallet = _feeWallet;
    }

    /**
     * @dev Create a new project
     */
    function createProject(
        string memory _name,
        string memory _description,
        string memory _website,
        string memory _whitepaper,
        uint256 _softCap,
        uint256 _hardCap,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _tokenPrice,
        address _paymentToken
    ) external {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_softCap > 0, "Softcap must be greater than 0");
        require(_hardCap > _softCap, "Hardcap must be greater than softcap");
        require(_minContribution > 0, "Min contribution must be greater than 0");
        require(_maxContribution >= _minContribution, "Max contribution must be >= min");
        require(_startTime > block.timestamp, "Start time must be in future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_paymentToken != address(0), "Invalid payment token address");

        Project memory newProject = Project({
            creator: msg.sender,
            name: _name,
            description: _description,
            website: _website,
            whitepaper: _whitepaper,
            softCap: _softCap,
            hardCap: _hardCap,
            minContribution: _minContribution,
            maxContribution: _maxContribution,
            startTime: _startTime,
            endTime: _endTime,
            totalRaised: 0,
            tokenPrice: _tokenPrice,
            paymentToken: _paymentToken,
            isApproved: false,
            isActive: false,
            isCompleted: false
        });

        projects.push(newProject);
        
        emit ProjectCreated(projects.length - 1, msg.sender);
    }

    /**
     * @dev Approve a project (only owner)
     */
    function approveProject(uint256 _projectId) external onlyOwner {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        
        require(!project.isApproved, "Project already approved");
        require(!project.isActive, "Project already active");
        
        project.isApproved = true;
        
        emit ProjectApproved(_projectId);
    }

    /**
     * @dev Activate a project (only creator)
     */
    function activateProject(uint256 _projectId) external {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        
        require(project.creator == msg.sender, "Only creator can activate");
        require(project.isApproved, "Project not approved");
        require(!project.isActive, "Project already active");
        require(block.timestamp >= project.startTime, "Project not started yet");
        require(block.timestamp < project.endTime, "Project already ended");
        
        project.isActive = true;
        
        emit ProjectActivated(_projectId);
    }

    /**
     * @dev Contribute to a project
     */
    function contribute(uint256 _projectId, uint256 _amount) external nonReentrant {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        
        require(project.isActive, "Project not active");
        require(block.timestamp >= project.startTime, "Project not started yet");
        require(block.timestamp < project.endTime, "Project ended");
        require(_amount >= project.minContribution, "Amount below minimum");
        require(_amount <= project.maxContribution, "Amount exceeds maximum");
        require(project.totalRaised.add(_amount) <= project.hardCap, "Exceeds hardcap");
        
        Investor storage investor = projectInvestors[_projectId][msg.sender];
        uint256 newContribution = investor.amountContributed.add(_amount);
        require(newContribution <= project.maxContribution, "Exceeds personal cap");
        
        // Transfer funds from investor
        IERC20 paymentToken = IERC20(project.paymentToken);
        require(paymentToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        
        // Update investor and project totals
        investor.amountContributed = newContribution;
        project.totalRaised = project.totalRaised.add(_amount);
        
        emit Contributed(_projectId, msg.sender, _amount);
    }

    /**
     * @dev Claim tokens after project completion
     */
    function claimTokens(uint256 _projectId) external nonReentrant {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        
        require(project.isCompleted, "Project not completed");
        require(block.timestamp > project.endTime, "Project not ended yet");
        
        Investor storage investor = projectInvestors[_projectId][msg.sender];
        require(investor.amountContributed > 0, "No contribution");
        require(!investor.hasClaimedTokens, "Already claimed");
        
        address projectToken = projectTokens[_projectId];
        require(projectToken != address(0), "Token not set");
        
        uint256 tokenAmount = investor.amountContributed.mul(1e18).div(project.tokenPrice);
        
        // Mark as claimed
        investor.hasClaimedTokens = true;
        
        // Transfer tokens
        IERC20(projectToken).transfer(msg.sender, tokenAmount);
        
        emit TokensClaimed(_projectId, msg.sender, tokenAmount);
    }

    /**
     * @dev Complete project and distribute funds (only creator)
     */
    function completeProject(uint256 _projectId, address _tokenAddress) external nonReentrant {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        
        require(project.creator == msg.sender, "Only creator can complete");
        require(project.isActive, "Project not active");
        require(block.timestamp >= project.endTime, "Project not ended yet");
        require(!project.isCompleted, "Project already completed");
        require(_tokenAddress != address(0), "Invalid token address");
        
        project.isCompleted = true;
        project.isActive = false;
        projectTokens[_projectId] = _tokenAddress;
        
        // Calculate and transfer platform fee
        uint256 feeAmount = project.totalRaised.mul(platformFee).div(10000);
        uint256 creatorAmount = project.totalRaised.sub(feeAmount
