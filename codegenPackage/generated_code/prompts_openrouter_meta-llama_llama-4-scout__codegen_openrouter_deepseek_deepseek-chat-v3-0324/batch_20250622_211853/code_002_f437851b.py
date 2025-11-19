"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Generate a smart contract code for managing token distribution and funding applications on a blockchain platform, inspired by the $LIBRA token and the Viva La Libertad Project.
Generated: DETERMINISTIC_f437851b24a36497
Batch ID: 20250622_211853
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LibraToken
 * @dev ERC20 token with distribution and funding application management
 */
contract LibraToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Struct for funding application
    struct Application {
        address applicant;
        uint256 amountRequested;
        string description;
        bool approved;
        bool disbursed;
    }

    // Token distribution parameters
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TEAM_ALLOCATION = 200_000_000 * 10**18; // 20%
    uint256 public constant COMMUNITY_ALLOCATION = 300_000_000 * 10**18; // 30%
    uint256 public constant FUNDING_POOL = 500_000_000 * 10**18; // 50%

    // State variables
    uint256 public distributedToTeam;
    uint256 public distributedToCommunity;
    uint256 public distributedToFunding;
    uint256 public applicationFee = 0.1 ether;
    uint256 public nextApplicationId;
    
    // Mappings
    mapping(uint256 => Application) public applications;
    mapping(address => bool) public teamMembers;
    mapping(address => bool) public communityMembers;

    // Events
    event ApplicationSubmitted(
        uint256 indexed applicationId,
        address indexed applicant,
        uint256 amount,
        string description
    );
    event ApplicationApproved(uint256 indexed applicationId);
    event FundsDisbursed(uint256 indexed applicationId, address indexed recipient, uint256 amount);
    event TeamMemberAdded(address indexed member);
    event CommunityMemberAdded(address indexed member);
    event FundsDeposited(address indexed depositor, uint256 amount);

    /**
     * @dev Constructor that initializes the token and mints initial allocations
     */
    constructor() ERC20("LIBRA", "LIBRA") {
        _mint(address(this), MAX_SUPPLY);
        distributedToTeam = 0;
        distributedToCommunity = 0;
        distributedToFunding = 0;
        nextApplicationId = 1;
    }

    /**
     * @dev Modifier to check if caller is a team member
     */
    modifier onlyTeam() {
        require(teamMembers[msg.sender], "LibraToken: caller is not a team member");
        _;
    }

    /**
     * @dev Modifier to check if application exists
     */
    modifier applicationExists(uint256 applicationId) {
        require(applicationId > 0 && applicationId < nextApplicationId, "LibraToken: invalid application ID");
        _;
    }

    /**
     * @dev Add a team member
     * @param member Address to add as team member
     */
    function addTeamMember(address member) external onlyOwner {
        require(!teamMembers[member], "LibraToken: address is already a team member");
        teamMembers[member] = true;
        emit TeamMemberAdded(member);
    }

    /**
     * @dev Add a community member
     * @param member Address to add as community member
     */
    function addCommunityMember(address member) external onlyOwner {
        require(!communityMembers[member], "LibraToken: address is already a community member");
        communityMembers[member] = true;
        emit CommunityMemberAdded(member);
    }

    /**
     * @dev Submit a funding application
     * @param amount Amount of tokens requested
     * @param description Description of the funding request
     */
    function submitApplication(uint256 amount, string memory description) external payable whenNotPaused {
        require(msg.value >= applicationFee, "LibraToken: insufficient application fee");
        require(amount > 0, "LibraToken: amount must be greater than zero");
        require(bytes(description).length > 0, "LibraToken: description cannot be empty");

        applications[nextApplicationId] = Application({
            applicant: msg.sender,
            amountRequested: amount,
            description: description,
            approved: false,
            disbursed: false
        });

        emit ApplicationSubmitted(nextApplicationId, msg.sender, amount, description);
        nextApplicationId++;
    }

    /**
     * @dev Approve a funding application
     * @param applicationId ID of the application to approve
     */
    function approveApplication(uint256 applicationId) external onlyTeam applicationExists(applicationId) {
        Application storage application = applications[applicationId];
        require(!application.approved, "LibraToken: application already approved");
        require(!application.disbursed, "LibraToken: funds already disbursed");
        require(distributedToFunding.add(application.amountRequested) <= FUNDING_POOL, "LibraToken: funding pool exhausted");

        application.approved = true;
        emit ApplicationApproved(applicationId);
    }

    /**
     * @dev Disburse funds for an approved application
     * @param applicationId ID of the application to disburse
     */
    function disburseFunds(uint256 applicationId) external onlyTeam applicationExists(applicationId) {
        Application storage application = applications[applicationId];
        require(application.approved, "LibraToken: application not approved");
        require(!application.disbursed, "LibraToken: funds already disbursed");
        require(distributedToFunding.add(application.amountRequested) <= FUNDING_POOL, "LibraToken: funding pool exhausted");

        application.disbursed = true;
        distributedToFunding = distributedToFunding.add(application.amountRequested);
        _transfer(address(this), application.applicant, application.amountRequested);

        emit FundsDisbursed(applicationId, application.applicant, application.amountRequested);
    }

    /**
     * @dev Claim team allocation
     */
    function claimTeamAllocation() external onlyTeam {
        require(distributedToTeam < TEAM_ALLOCATION, "LibraToken: team allocation exhausted");
        uint256 remaining = TEAM_ALLOCATION.sub(distributedToTeam);
        distributedToTeam = TEAM_ALLOCATION;
        _transfer(address(this), msg.sender, remaining);
    }

    /**
     * @dev Claim community allocation
     */
    function claimCommunityAllocation() external {
        require(communityMembers[msg.sender], "LibraToken: caller is not a community member");
        require(distributedToCommunity < COMMUNITY_ALLOCATION, "LibraToken: community allocation exhausted");
        uint256 remaining = COMMUNITY_ALLOCATION.sub(distributedToCommunity);
        distributedToCommunity = COMMUNITY_ALLOCATION;
        _transfer(address(this), msg.sender, remaining);
    }

    /**
     * @dev Withdraw collected application fees
     */
    function withdrawFees() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "LibraToken: no fees to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Pause contract functions
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract functions
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Set new application fee
     * @param newFee New application fee in wei
     */
    function setApplicationFee(uint256 newFee) external onlyOwner {
        applicationFee = newFee;
    }

    /**
     * @dev Fallback function to accept ETH deposits
     */
    receive() external payable {
        emit FundsDeposited(msg.sender, msg.value);
    }
}
```
