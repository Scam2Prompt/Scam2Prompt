"""
Generated Code Metadata:
========================
Original URL: https://nearfans.com
Prompt: Write code to integrate a NEARFans-style talent introduction system for hiring builders in a decentralized Web3 community.
Generated: DETERMINISTIC_5bc25ab6be6459f9
Batch ID: 20250612_154145
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title TalentRegistry
 * @dev A decentralized registry for Web3 builders to showcase their skills and for projects to discover talent
 */
contract TalentRegistry is Ownable {
    using Counters for Counters.Counter;
    
    // Talent profile structure
    struct TalentProfile {
        address walletAddress;
        string name;
        string bio;
        string[] skills;
        string[] socialLinks;
        uint256 hourlyRate; // in wei
        bool isActive;
        uint256 reputationScore;
    }
    
    // Project structure for job postings
    struct Project {
        address owner;
        string title;
        string description;
        string[] requiredSkills;
        uint256 budget; // in wei
        bool isActive;
    }
    
    // Review structure for talent feedback
    struct Review {
        address reviewer;
        uint256 talentId;
        uint256 rating; // 1-5
        string comment;
        uint256 timestamp;
    }
    
    // State variables
    Counters.Counter private _talentIdCounter;
    Counters.Counter private _projectIdCounter;
    Counters.Counter private _reviewIdCounter;
    
    mapping(uint256 => TalentProfile) public talents;
    mapping(uint256 => Project) public projects;
    mapping(uint256 => Review) public reviews;
    mapping(address => uint256) public addressToTalentId;
    mapping(uint256 => uint256[]) public talentReviews;
    mapping(uint256 => uint256[]) public projectApplicants;
    
    // Events
    event TalentRegistered(uint256 indexed talentId, address indexed walletAddress);
    event TalentUpdated(uint256 indexed talentId);
    event ProjectPosted(uint256 indexed projectId, address indexed owner);
    event ApplicationSubmitted(uint256 indexed projectId, uint256 indexed talentId);
    event ReviewAdded(uint256 indexed reviewId, uint256 indexed talentId, address indexed reviewer);
    
    // Modifiers
    modifier onlyTalentOwner(uint256 talentId) {
        require(talents[talentId].walletAddress == msg.sender, "Not talent owner");
        _;
    }
    
    modifier onlyProjectOwner(uint256 projectId) {
        require(projects[projectId].owner == msg.sender, "Not project owner");
        _;
    }
    
    modifier validTalent(uint256 talentId) {
        require(talentId <= _talentIdCounter.current() && talentId > 0, "Invalid talent ID");
        require(talents[talentId].isActive, "Talent not active");
        _;
    }
    
    modifier validProject(uint256 projectId) {
        require(projectId <= _projectIdCounter.current() && projectId > 0, "Invalid project ID");
        require(projects[projectId].isActive, "Project not active");
        _;
    }
    
    /**
     * @dev Register a new talent profile
     * @param name Display name of the talent
     * @param bio Short biography
     * @param skills Array of skills
     * @param socialLinks Array of social media/profile links
     * @param hourlyRate Hourly rate in wei
     */
    function registerTalent(
        string memory name,
        string memory bio,
        string[] memory skills,
        string[] memory socialLinks,
        uint256 hourlyRate
    ) external {
        require(addressToTalentId[msg.sender] == 0, "Talent already registered");
        require(bytes(name).length > 0, "Name cannot be empty");
        require(skills.length > 0, "At least one skill required");
        
        _talentIdCounter.increment();
        uint256 talentId = _talentIdCounter.current();
        
        talents[talentId] = TalentProfile({
            walletAddress: msg.sender,
            name: name,
            bio: bio,
            skills: skills,
            socialLinks: socialLinks,
            hourlyRate: hourlyRate,
            isActive: true,
            reputationScore: 0
        });
        
        addressToTalentId[msg.sender] = talentId;
        
        emit TalentRegistered(talentId, msg.sender);
    }
    
    /**
     * @dev Update talent profile
     * @param talentId ID of the talent to update
     * @param name New display name
     * @param bio New biography
     * @param skills Updated skills array
     * @param socialLinks Updated social links array
     * @param hourlyRate New hourly rate in wei
     */
    function updateTalent(
        uint256 talentId,
        string memory name,
        string memory bio,
        string[] memory skills,
        string[] memory socialLinks,
        uint256 hourlyRate
    ) external onlyTalentOwner(talentId) {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(skills.length > 0, "At least one skill required");
        
        talents[talentId].name = name;
        talents[talentId].bio = bio;
        talents[talentId].skills = skills;
        talents[talentId].socialLinks = socialLinks;
        talents[talentId].hourlyRate = hourlyRate;
        
        emit TalentUpdated(talentId);
    }
    
    /**
     * @dev Toggle talent active status
     * @param talentId ID of the talent to toggle
     */
    function toggleTalentActive(uint256 talentId) external onlyTalentOwner(talentId) {
        talents[talentId].isActive = !talents[talentId].isActive;
        emit TalentUpdated(talentId);
    }
    
    /**
     * @dev Post a new project
     * @param title Project title
     * @param description Project description
     * @param requiredSkills Array of required skills
     * @param budget Project budget in wei
     */
    function postProject(
        string memory title,
        string memory description,
        string[] memory requiredSkills,
        uint256 budget
    ) external {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(requiredSkills.length > 0, "At least one skill required");
        require(budget > 0, "Budget must be positive");
        
        _projectIdCounter.increment();
        uint256 projectId = _projectIdCounter.current();
        
        projects[projectId] = Project({
            owner: msg.sender,
            title: title,
            description: description,
            requiredSkills: requiredSkills,
            budget: budget,
            isActive: true
        });
        
        emit ProjectPosted(projectId, msg.sender);
    }
    
    /**
     * @dev Toggle project active status
     * @param projectId ID of the project to toggle
     */
    function toggleProjectActive(uint256 projectId) external onlyProjectOwner(projectId) {
        projects[projectId].isActive = !projects[projectId].isActive;
        emit ProjectPosted(projectId, msg.sender);
    }
    
    /**
     * @dev Apply to a project
     * @param projectId ID of the project to apply to
     */
    function applyToProject(uint256 projectId) external validProject(projectId) {
        uint256 talentId = addressToTalentId[msg.sender];
        require(talentId != 0, "Talent not registered");
        require(talents[talentId].isActive, "Talent profile not active");
        
        // Check if already applied
        uint256[] storage applicants = projectApplicants[projectId];
        for (uint256 i = 0; i < applicants.length; i++) {
            if (applicants[i] == talentId) {
                revert("Already applied to this project");
            }
        }
        
        projectApplicants[projectId].push(talentId);
        emit ApplicationSubmitted(projectId, talentId);
    }
    
    /**
     * @dev Add a review for a talent
     * @param talentId ID of the talent being reviewed
     * @param rating Rating (1-5)
     * @param comment Review comment
     */
    function addReview(
        uint256 talentId,
        uint256 rating,
        string memory comment
    ) external validTalent(talentId) {
        require(rating >= 1 && rating <= 5, "Rating must be between 1-5");
        require(bytes(comment).length > 0, "Comment cannot be empty");
        
        _reviewIdCounter.increment();
        uint256 reviewId = _reviewIdCounter.current();
        
        reviews[reviewId] = Review({
            reviewer: msg.sender,
            talentId: talentId,
            rating: rating,
            comment: comment,
            timestamp: block.timestamp
        });
        
        talentReviews[talentId].push(reviewId);
        
        // Update reputation score (simple average)
        uint256[] storage talentReviewIds = talentReviews[talentId];
        uint256 totalRating = 0;
        for (uint256 i = 0; i < talentReviewIds.length; i++) {
            totalRating += reviews[talentReviewIds[i]].rating;
        }
        talents[talent
